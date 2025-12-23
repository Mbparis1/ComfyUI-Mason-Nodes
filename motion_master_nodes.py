"""
Mason's Motion Master Nodes for ComfyUI
Enhanced batch animation and motion helpers - SD 1.5 optimized
"""

import os
import json
from datetime import datetime


class BatchAnimationBuilder:
    """Create frame-by-frame animation prompts with interpolated motion"""
    
    MOTION_TYPES = {
        "static": ("", ""),  # No motion
        "head_turn_left": ("head facing forward", "head turned left, looking left"),
        "head_turn_right": ("head facing forward", "head turned right, looking right"),
        "look_down": ("looking forward", "looking down, eyes down"),
        "look_up": ("looking forward", "looking up, eyes up"),
        "smile": ("neutral expression", "smiling, happy expression"),
        "blink": ("eyes open", "eyes closed, blinking"),
        "hair_blow": ("hair still", "hair blowing in wind, flowing hair"),
        "breathing": ("normal posture", "chest expanded, deep breath"),
        "lean_forward": ("standing straight", "leaning forward"),
        "lean_back": ("standing straight", "leaning back"),
        "arm_raise": ("arms down", "arms raised"),
        "walk_step": ("standing still", "mid-stride, walking"),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
                "motion_type": (list(cls.MOTION_TYPES.keys()),),
                "total_frames": ("INT", {"default": 8, "min": 2, "max": 60}),
                "current_frame": ("INT", {"default": 0, "min": 0, "max": 59}),
                "loop_motion": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("frame_prompt", "frame_info")
    FUNCTION = "build_frame"
    CATEGORY = "Mason's Nodes/Motion Master"

    def build_frame(self, base_prompt, motion_type, total_frames, current_frame, loop_motion):
        start_state, end_state = self.MOTION_TYPES.get(motion_type, ("", ""))
        
        if motion_type == "static":
            return (base_prompt, f"Frame {current_frame + 1}/{total_frames} - Static")
        
        # Calculate interpolation
        if loop_motion:
            # Go forward then backward for seamless loop
            half = total_frames // 2
            if current_frame < half:
                progress = current_frame / half
            else:
                progress = 1.0 - ((current_frame - half) / half)
        else:
            progress = current_frame / (total_frames - 1)
        
        # Blend states based on progress
        if progress < 0.5:
            motion_desc = f"{start_state}, transitioning to {end_state}"
        else:
            motion_desc = f"{end_state}, transitioning from {start_state}"
        
        frame_prompt = f"{base_prompt}, {motion_desc}"
        frame_info = f"Frame {current_frame + 1}/{total_frames} - Progress: {progress:.1%}"
        
        return (frame_prompt, frame_info)


class FrameSequenceGenerator:
    """Generate a sequence of seeds for consistent batch frames"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_seed": ("INT", {"default": 42, "min": 0, "max": 0xffffffffffffffff}),
                "total_frames": ("INT", {"default": 8, "min": 1, "max": 120}),
                "current_frame": ("INT", {"default": 0, "min": 0, "max": 119}),
                "seed_variation": ("FLOAT", {"default": 0.1, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("frame_seed", "denoise_strength")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Motion Master"

    def generate(self, base_seed, total_frames, current_frame, seed_variation):
        # Keep seed consistent for coherent animation
        if seed_variation == 0:
            frame_seed = base_seed
        else:
            # Small seed variations for subtle differences
            frame_seed = base_seed + int(current_frame * seed_variation * 100)
        
        # Denoise strength - higher for first frame, lower for subsequent
        if current_frame == 0:
            denoise = 1.0
        else:
            denoise = max(0.3, 1.0 - (seed_variation * current_frame * 0.5))
        
        return (frame_seed, denoise)


class ConsistentSubjectLock:
    """Lock subject description across frames for consistency"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject_description": ("STRING", {"default": "", "multiline": True}),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 999}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("locked_subject",)
    FUNCTION = "lock"
    CATEGORY = "Mason's Nodes/Motion Master"

    def lock(self, subject_description, frame_number):
        # Add consistency-enforcing keywords
        consistency = "same person, consistent features, consistent face, consistent body, consistent outfit"
        if frame_number > 0:
            consistency += ", maintaining previous appearance"
        return (f"{subject_description}, {consistency}",)


class AnimationFrameSaver:
    """Save frames with proper naming for video compilation"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "output_folder": ("STRING", {"default": "animation_output"}),
                "project_name": ("STRING", {"default": "anim"}),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 9999}),
                "total_frames": ("INT", {"default": 8, "min": 1, "max": 9999}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("filename", "save_path")
    FUNCTION = "generate_path"
    CATEGORY = "Mason's Nodes/Motion Master"

    def generate_path(self, output_folder, project_name, frame_number, total_frames):
        # Zero-pad frame numbers for proper sorting
        padding = len(str(total_frames))
        filename = f"{project_name}_{str(frame_number).zfill(padding)}.png"
        save_path = os.path.join(output_folder, filename)
        return (filename, save_path)


class MotionStrengthController:
    """Control how much motion/change between frames"""
    
    STRENGTHS = {
        "minimal": {"desc": "minimal movement, very subtle changes", "denoise": 0.25},
        "subtle": {"desc": "subtle movement, slight changes", "denoise": 0.35},
        "moderate": {"desc": "moderate movement, noticeable changes", "denoise": 0.50},
        "dynamic": {"desc": "dynamic movement, significant changes", "denoise": 0.65},
        "dramatic": {"desc": "dramatic movement, major changes", "denoise": 0.80},
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "motion_strength": (list(cls.STRENGTHS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "FLOAT")
    RETURN_NAMES = ("motion_prompt", "suggested_denoise")
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Motion Master"

    def apply(self, prompt, motion_strength):
        strength = self.STRENGTHS.get(motion_strength, {})
        desc = strength.get("desc", "")
        denoise = strength.get("denoise", 0.5)
        return (f"{prompt}, {desc}", denoise)


class VideoCompileHelper:
    """Generate ffmpeg command for compiling frames to video"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_folder": ("STRING", {"default": "animation_output"}),
                "project_name": ("STRING", {"default": "anim"}),
                "output_filename": ("STRING", {"default": "output.mp4"}),
                "fps": ("INT", {"default": 12, "min": 1, "max": 60}),
                "loop_count": ("INT", {"default": 1, "min": 1, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("ffmpeg_command", "gif_command")
    FUNCTION = "generate_commands"
    CATEGORY = "Mason's Nodes/Motion Master"

    def generate_commands(self, input_folder, project_name, output_filename, fps, loop_count):
        # MP4 command
        mp4_cmd = f"ffmpeg -framerate {fps} -i {input_folder}/{project_name}_%04d.png -c:v libx264 -pix_fmt yuv420p {output_filename}"
        
        # GIF command
        gif_name = output_filename.replace('.mp4', '.gif')
        gif_cmd = f"ffmpeg -framerate {fps} -i {input_folder}/{project_name}_%04d.png -vf \"fps={fps},scale=512:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse\" -loop {loop_count - 1} {gif_name}"
        
        return (mp4_cmd, gif_cmd)


class PoseTransitionBuilder:
    """Build smooth pose transitions for animation"""
    
    TRANSITIONS = {
        "stand_to_sit": ["standing", "beginning to sit", "lowering body", "sitting down", "seated"],
        "sit_to_stand": ["seated", "beginning to stand", "rising up", "almost standing", "standing"],
        "stand_to_lie": ["standing", "bending down", "lowering to ground", "lying down"],
        "turn_around": ["facing forward", "turning body", "side view", "turning more", "back view"],
        "wave_hello": ["arm down", "arm raising", "arm up waving", "arm lowering", "arm down"],
        "blow_kiss": ["neutral", "hand raising to lips", "kissing hand", "blowing kiss", "hand lowering"],
        "hair_flip": ["hair down", "hand in hair", "flipping hair", "hair mid-flip", "hair settled"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
                "transition": (list(cls.TRANSITIONS.keys()),),
                "current_frame": ("INT", {"default": 0, "min": 0, "max": 59}),
                "total_frames": ("INT", {"default": 5, "min": 2, "max": 60}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("transition_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Motion Master"

    def build(self, base_prompt, transition, current_frame, total_frames):
        stages = self.TRANSITIONS.get(transition, [""])
        num_stages = len(stages)
        
        # Map frame to stage
        stage_index = int((current_frame / total_frames) * num_stages)
        stage_index = min(stage_index, num_stages - 1)
        
        stage_desc = stages[stage_index]
        return (f"{base_prompt}, {stage_desc}",)


class WorkflowAnalyzer:
    """Analyze workflow and provide guidance on node order and usage"""
    
    NODE_CATEGORIES = {
        "character": ["CompleteCharacterBuilder", "BodyTypeSelector", "EthnicitySelector"],
        "face": ["FacialStructureController", "EyeDetailMaster", "LipController", "EyeMakeupController"],
        "body": ["MuscleDefinitionController", "BodyProportionEnhancer", "SkinShineController"],
        "pose": ["UltimatePoseMaster", "PoseDirector", "PoseTransitionBuilder"],
        "outfit": ["LingerieSelector", "SwimwearSelector", "DressSelector", "ClothingFitController"],
        "lighting": ["ThreePointLightingSetup", "ShadowController", "ColorTemperatureController"],
        "composition": ["RuleOfThirdsPositioner", "FramingController", "BackgroundComplexityController"],
        "quality": ["QualityMasterNode", "PhotorealismBooster", "DetailLevelController"],
        "style": ["RenderStyleController", "ColorPaletteController", "FilmStockController"],
        "motion": ["BatchAnimationBuilder", "PoseTransitionBuilder", "MotionStrengthController"],
    }
    
    RECOMMENDED_ORDER = [
        "1. CHARACTER: Build base subject (gender, ethnicity, body type)",
        "2. FACE: Add facial details (structure, eyes, lips, makeup)",
        "3. BODY: Add body details (skin, muscle, proportions)",
        "4. OUTFIT: Dress the character (clothing type, fit, state)",
        "5. POSE: Set the pose (position, action, expression)",
        "6. COMPOSITION: Frame the shot (camera angle, framing, placement)",
        "7. LIGHTING: Set the lighting (type, shadows, color temp)",
        "8. STYLE: Apply style (render type, color palette, effects)",
        "9. QUALITY: Enhance quality (photorealism, detail, sharpness)",
        "10. MOTION: Add motion (if animating - frame builder, transitions)",
    ]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "current_prompt": ("STRING", {"default": "", "multiline": True}),
                "content_type": (["portrait", "full_body", "nsfw", "artistic", "animation"],),
            },
            "optional": {
                "show_all_recommendations": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("workflow_guide", "checklist")
    FUNCTION = "analyze"
    CATEGORY = "Mason's Nodes/Workflow Helper"

    def analyze(self, current_prompt, content_type, show_all_recommendations=True):
        guide_lines = ["=== WORKFLOW GUIDE ===", ""]
        guide_lines.append(f"Content Type: {content_type.upper()}")
        guide_lines.append("")
        guide_lines.append("RECOMMENDED NODE ORDER:")
        guide_lines.extend(self.RECOMMENDED_ORDER)
        guide_lines.append("")
        
        # Content-specific tips
        if content_type == "portrait":
            guide_lines.append("PORTRAIT TIPS:")
            guide_lines.append("- Focus on Face Detail nodes")
            guide_lines.append("- Use close-up framing")
            guide_lines.append("- Emphasize lighting and eyes")
        elif content_type == "full_body":
            guide_lines.append("FULL BODY TIPS:")
            guide_lines.append("- Use Body Detail nodes")
            guide_lines.append("- Include pose nodes")
            guide_lines.append("- Consider outfit nodes")
        elif content_type == "nsfw":
            guide_lines.append("NSFW TIPS:")
            guide_lines.append("- Start with CompleteCharacterBuilder")
            guide_lines.append("- Use BodyTypeSelector for proportions")
            guide_lines.append("- Add outfit/underwear nodes")
            guide_lines.append("- Use pose nodes for positioning")
            guide_lines.append("- Consider SkinShineController for effects")
        elif content_type == "animation":
            guide_lines.append("ANIMATION TIPS:")
            guide_lines.append("- Use BatchAnimationBuilder")
            guide_lines.append("- Keep subject consistent with ConsistentSubjectLock")
            guide_lines.append("- Use FrameSequenceGenerator for seeds")
            guide_lines.append("- Use PoseTransitionBuilder for motion")
            guide_lines.append("- Save with AnimationFrameSaver")
        
        # Checklist
        checklist = [
            "[ ] Base subject defined",
            "[ ] Facial features set",
            "[ ] Body type configured",
            "[ ] Pose selected",
            "[ ] Outfit/clothing added",
            "[ ] Lighting configured",
            "[ ] Composition set",
            "[ ] Quality enhanced",
            "[ ] Negative prompt added",
        ]
        
        if content_type == "animation":
            checklist.extend([
                "[ ] Frame count set",
                "[ ] Motion type selected",
                "[ ] Seeds configured",
                "[ ] Output path ready",
            ])
        
        return ("\n".join(guide_lines), "\n".join(checklist))


NODE_CLASS_MAPPINGS = {
    "BatchAnimationBuilder": BatchAnimationBuilder,
    "FrameSequenceGenerator": FrameSequenceGenerator,
    "ConsistentSubjectLock": ConsistentSubjectLock,
    "AnimationFrameSaver": AnimationFrameSaver,
    "MotionStrengthController": MotionStrengthController,
    "VideoCompileHelper": VideoCompileHelper,
    "PoseTransitionBuilder": PoseTransitionBuilder,
    "WorkflowAnalyzer": WorkflowAnalyzer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BatchAnimationBuilder": "🎬 Batch Animation Builder",
    "FrameSequenceGenerator": "🔢 Frame Sequence Generator",
    "ConsistentSubjectLock": "🔒 Consistent Subject Lock",
    "AnimationFrameSaver": "💾 Animation Frame Saver",
    "MotionStrengthController": "💨 Motion Strength Controller",
    "VideoCompileHelper": "🎥 Video Compile Helper",
    "PoseTransitionBuilder": "🚶 Pose Transition Builder",
    "WorkflowAnalyzer": "📋 Workflow Analyzer",
}
