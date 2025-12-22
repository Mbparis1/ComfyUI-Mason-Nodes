"""
Mason's Advanced Motion Nodes for ComfyUI
Keyframe, camera, and animation enhancement tools
"""

import random
import math


class KeyframeInterpolator:
    """Define start/end prompts, auto-generate in-between frames"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start_prompt": ("STRING", {"default": "woman standing, arms at sides", "multiline": True}),
                "end_prompt": ("STRING", {"default": "woman posing seductively, arms raised", "multiline": True}),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 20}),
                "total_frames": ("INT", {"default": 5, "min": 2, "max": 20}),
                "base_subject": ("STRING", {"default": "beautiful woman", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "FLOAT")
    RETURN_NAMES = ("interpolated_prompt", "progress")
    FUNCTION = "interpolate"
    CATEGORY = "Mason's Nodes/Motion Advanced"

    def interpolate(self, start_prompt, end_prompt, frame_number, total_frames, base_subject):
        progress = frame_number / max(total_frames - 1, 1)
        
        # At 0%, use start; at 100%, use end; in between, blend descriptions
        if progress <= 0.25:
            pose_desc = start_prompt
        elif progress <= 0.5:
            pose_desc = f"transitioning from {start_prompt} towards {end_prompt}"
        elif progress <= 0.75:
            pose_desc = f"mostly in {end_prompt}, remnants of {start_prompt}"
        else:
            pose_desc = end_prompt
        
        prompt = f"{base_subject}, {pose_desc}"
        return (prompt, progress)


class CameraMovementSimulator:
    """Simulate camera movements via prompt modification"""
    
    MOVEMENTS = {
        "zoom_in": ["wide shot", "medium shot", "medium close-up", "close-up", "extreme close-up"],
        "zoom_out": ["extreme close-up", "close-up", "medium close-up", "medium shot", "wide shot"],
        "pan_left": ["subject on right of frame", "subject slightly right", "subject centered", "subject slightly left", "subject on left of frame"],
        "pan_right": ["subject on left of frame", "subject slightly left", "subject centered", "subject slightly right", "subject on right of frame"],
        "dolly_forward": ["distant view", "approaching", "mid-distance", "close", "intimate distance"],
        "orbit_around": ["front view", "three-quarter front view", "side view", "three-quarter back view", "back view"],
        "tilt_up": ["low angle shot", "slight low angle", "eye level", "slight high angle", "high angle shot"],
        "crane_up": ["ground level", "waist level", "eye level", "above eye level", "overhead view"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "movement": (list(cls.MOVEMENTS.keys()),),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 10}),
                "total_frames": ("INT", {"default": 5, "min": 2, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("camera_prompt",)
    FUNCTION = "simulate"
    CATEGORY = "Mason's Nodes/Motion Advanced"

    def simulate(self, prompt, movement, frame_number, total_frames):
        stages = self.MOVEMENTS.get(movement, [""])
        idx = min(int(frame_number * len(stages) / total_frames), len(stages) - 1)
        camera_desc = stages[idx]
        return (f"{prompt}, {camera_desc}",)


class PhysicsAwarePoses:
    """Add realistic physics effects to poses"""
    
    PHYSICS_EFFECTS = {
        "hair_gravity": "hair falling naturally with gravity, realistic hair physics",
        "cloth_drape": "clothing draping naturally, realistic fabric physics, natural cloth folds",
        "body_weight": "realistic weight distribution, natural stance, balanced posture",
        "momentum": "motion blur suggestion, dynamic movement, kinetic energy",
        "wind_effect": "wind-blown hair and clothing, fabric billowing, dynamic air movement",
        "water_physics": "water droplets, wet skin, realistic water interaction",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "effects": (list(cls.PHYSICS_EFFECTS.keys()),),
                "intensity": (["subtle", "moderate", "strong"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("physics_prompt",)
    FUNCTION = "add_physics"
    CATEGORY = "Mason's Nodes/Motion Advanced"

    def add_physics(self, prompt, effects, intensity):
        effect_desc = self.PHYSICS_EFFECTS.get(effects, "")
        intensity_mod = {"subtle": "hint of", "moderate": "", "strong": "dramatic"}
        mod = intensity_mod[intensity]
        
        if mod:
            effect_desc = f"{mod} {effect_desc}"
        
        return (f"{prompt}, {effect_desc}",)


class EmotionTimeline:
    """Progress through emotions across frames"""
    
    EMOTION_PROGRESSIONS = {
        "warming_up": ["shy, nervous", "warming up, slight smile", "comfortable, genuine smile", "confident, radiant", "ecstatic, beaming"],
        "seduction": ["innocent look", "curious expression", "flirty smile", "seductive gaze", "intense desire"],
        "surprise_joy": ["neutral", "surprised", "delighted surprise", "joyful", "overjoyed"],
        "playful": ["serious", "hint of smile", "playful grin", "laughing", "giggling with joy"],
        "intense": ["calm", "focused", "determined", "intense", "passionate"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "emotion_arc": (list(cls.EMOTION_PROGRESSIONS.keys()),),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 10}),
                "total_frames": ("INT", {"default": 5, "min": 2, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("emotional_prompt",)
    FUNCTION = "progress_emotion"
    CATEGORY = "Mason's Nodes/Motion Advanced"

    def progress_emotion(self, prompt, emotion_arc, frame_number, total_frames):
        stages = self.EMOTION_PROGRESSIONS.get(emotion_arc, ["neutral"])
        idx = min(int(frame_number * len(stages) / total_frames), len(stages) - 1)
        emotion = stages[idx]
        return (f"{prompt}, {emotion}",)


class ActionSequenceBuilder:
    """Pre-built action sequences"""
    
    SEQUENCES = {
        "walking_toward": ["walking in distance", "walking closer", "approaching", "arriving", "standing close"],
        "dancing": ["standing ready", "arms moving", "hips swaying", "full body movement", "striking pose"],
        "turning_around": ["facing camera", "turning slightly", "profile view", "turning away", "back to camera"],
        "hair_flip": ["head neutral", "tilting head", "hair beginning to move", "hair mid-flip", "hair settling"],
        "sitting_down": ["standing", "beginning to sit", "lowering body", "almost seated", "fully seated"],
        "stretching": ["relaxed pose", "beginning stretch", "full extension", "holding stretch", "releasing"],
        "undressing_top": ["fully clothed", "hands on clothes", "loosening garment", "garment sliding", "revealing"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject": ("STRING", {"default": "beautiful woman", "multiline": True}),
                "action": (list(cls.SEQUENCES.keys()),),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 10}),
                "total_frames": ("INT", {"default": 5, "min": 2, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("action_prompt",)
    FUNCTION = "build_action"
    CATEGORY = "Mason's Nodes/Motion Advanced"

    def build_action(self, subject, action, frame_number, total_frames):
        stages = self.SEQUENCES.get(action, ["neutral"])
        idx = min(int(frame_number * len(stages) / total_frames), len(stages) - 1)
        action_desc = stages[idx]
        return (f"{subject}, {action_desc}",)


class LoopCreator:
    """Ensure smooth loop by matching first and last frames"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "total_frames": ("INT", {"default": 8, "min": 4, "max": 20}),
                "loop_type": (["pingpong", "circular"],),
            }
        }

    RETURN_TYPES = ("STRING", "INT", "FLOAT")
    RETURN_NAMES = ("looped_prompt", "effective_frame", "loop_progress")
    FUNCTION = "create_loop"
    CATEGORY = "Mason's Nodes/Motion Advanced"

    def create_loop(self, prompt, frame_number, total_frames, loop_type):
        if loop_type == "pingpong":
            # Go forward then backward
            cycle = frame_number % (total_frames * 2 - 2)
            if cycle >= total_frames:
                effective_frame = (total_frames * 2 - 2) - cycle
            else:
                effective_frame = cycle
        else:  # circular
            effective_frame = frame_number % total_frames
        
        progress = effective_frame / (total_frames - 1)
        loop_note = f"seamless loop, frame {effective_frame + 1} of {total_frames}"
        
        return (f"{prompt}, {loop_note}", effective_frame, progress)


class SpeedRampController:
    """Control animation speed (slow-mo / fast sections)"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "total_frames": ("INT", {"default": 10, "min": 2}),
                "ramp_type": (["ease_in", "ease_out", "ease_in_out", "slow_middle", "fast_middle"],),
            }
        }

    RETURN_TYPES = ("FLOAT", "INT", "STRING")
    RETURN_NAMES = ("adjusted_progress", "suggested_step_multiplier", "info")
    FUNCTION = "ramp"
    CATEGORY = "Mason's Nodes/Motion Advanced"

    def ramp(self, frame_number, total_frames, ramp_type):
        linear = frame_number / max(total_frames - 1, 1)
        
        if ramp_type == "ease_in":
            progress = linear * linear
        elif ramp_type == "ease_out":
            progress = 1 - (1 - linear) ** 2
        elif ramp_type == "ease_in_out":
            progress = linear * linear * (3 - 2 * linear)
        elif ramp_type == "slow_middle":
            progress = linear  # Could add more frames in middle
        else:  # fast_middle
            progress = linear
        
        # Suggest more steps for slow-mo sections
        step_mult = 1 if progress > 0.3 and progress < 0.7 else 1
        info = f"Linear: {linear:.2f} → Adjusted: {progress:.2f}"
        
        return (progress, step_mult, info)


NODE_CLASS_MAPPINGS = {
    "KeyframeInterpolator": KeyframeInterpolator,
    "CameraMovementSimulator": CameraMovementSimulator,
    "PhysicsAwarePoses": PhysicsAwarePoses,
    "EmotionTimeline": EmotionTimeline,
    "ActionSequenceBuilder": ActionSequenceBuilder,
    "LoopCreator": LoopCreator,
    "SpeedRampController": SpeedRampController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KeyframeInterpolator": "🔑 Keyframe Interpolator",
    "CameraMovementSimulator": "📹 Camera Movement",
    "PhysicsAwarePoses": "⚡ Physics-Aware Poses",
    "EmotionTimeline": "💫 Emotion Timeline",
    "ActionSequenceBuilder": "🎭 Action Sequence",
    "LoopCreator": "🔄 Loop Creator",
    "SpeedRampController": "⏩ Speed Ramp",
}
