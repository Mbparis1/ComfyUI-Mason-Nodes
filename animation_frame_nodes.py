"""
Animation Frame Sequence Nodes - Generate frames for motion animations
Creates sequences of images with small movements for compiling into video/GIF
"""


class FrameSequenceGenerator:
    """Generate a sequence of frame prompts with incremental changes"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
                "total_frames": ("INT", {"default": 8, "min": 2, "max": 30}),
                "current_frame": ("INT", {"default": 0, "min": 0, "max": 29}),
            }
        }
    
    RETURN_TYPES = ("STRING", "INT", "FLOAT",)
    RETURN_NAMES = ("frame_prompt", "frame_number", "progress",)
    FUNCTION = "generate"
    CATEGORY = "Mason/Animation Frames"

    def generate(self, base_prompt, total_frames, current_frame):
        progress = current_frame / max(total_frames - 1, 1)
        return (base_prompt, current_frame, progress,)


class MotionInterpolator:
    """Interpolate between two poses/positions for smooth motion"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start_pose": ("STRING", {"default": "arms at sides, relaxed stance", "multiline": True}),
                "end_pose": ("STRING", {"default": "arms raised above head, stretching", "multiline": True}),
                "progress": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.05}),
            },
            "optional": {
                "easing": (["linear", "ease_in", "ease_out", "ease_in_out"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("interpolated_pose",)
    FUNCTION = "interpolate"
    CATEGORY = "Mason/Animation Frames"

    def interpolate(self, start_pose, end_pose, progress, easing="linear"):
        # Apply easing
        if easing == "ease_in":
            progress = progress ** 2
        elif easing == "ease_out":
            progress = 1 - (1 - progress) ** 2
        elif easing == "ease_in_out":
            if progress < 0.5:
                progress = 2 * progress ** 2
            else:
                progress = 1 - (-2 * progress + 2) ** 2 / 2
        
        # Create interpolated description
        if progress <= 0.1:
            return (start_pose,)
        elif progress >= 0.9:
            return (end_pose,)
        else:
            pct = int(progress * 100)
            return (f"transitioning from ({start_pose}) to ({end_pose}), {pct}% through motion",)


class HeadTurnSequence:
    """Generate head turn animation frames"""
    
    DIRECTIONS = ["left to center", "center to right", "right to center", 
                  "center to left", "left to right", "right to left"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "direction": (cls.DIRECTIONS,),
                "progress": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.05}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("head_pose",)
    FUNCTION = "generate"
    CATEGORY = "Mason/Animation Frames"

    def generate(self, direction, progress):
        positions = {
            "left to center": ["looking left", "looking slightly left", "looking forward"],
            "center to right": ["looking forward", "looking slightly right", "looking right"],
            "right to center": ["looking right", "looking slightly right", "looking forward"],
            "center to left": ["looking forward", "looking slightly left", "looking left"],
            "left to right": ["looking left", "looking slightly left", "looking forward", "looking slightly right", "looking right"],
            "right to left": ["looking right", "looking slightly right", "looking forward", "looking slightly left", "looking left"],
        }
        
        poses = positions.get(direction, ["looking forward"])
        idx = int(progress * (len(poses) - 1))
        idx = min(idx, len(poses) - 1)
        
        return (poses[idx],)


class BreathingMotion:
    """Generate subtle breathing motion for more lifelike images"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "breath_phase": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.05}),
                "intensity": (["subtle", "normal", "deep"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("breathing_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason/Animation Frames"

    def generate(self, breath_phase, intensity):
        # 0.0-0.5 = inhale, 0.5-1.0 = exhale
        if breath_phase < 0.25:
            phase = "beginning to inhale"
        elif breath_phase < 0.5:
            phase = "chest expanded, full inhale"
        elif breath_phase < 0.75:
            phase = "beginning to exhale"
        else:
            phase = "relaxed exhale"
        
        intensity_desc = {
            "subtle": "subtle breathing motion",
            "normal": "natural breathing",
            "deep": "deep breathing, noticeable chest movement",
        }
        
        return (f"{intensity_desc.get(intensity, 'breathing')}, {phase}",)


class BlinkSequence:
    """Generate eye blink animation frames"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "blink_progress": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.1}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("eye_state",)
    FUNCTION = "generate"
    CATEGORY = "Mason/Animation Frames"

    def generate(self, blink_progress):
        if blink_progress < 0.2:
            return ("eyes open",)
        elif blink_progress < 0.4:
            return ("eyes half closed, beginning to blink",)
        elif blink_progress < 0.6:
            return ("eyes closed, mid-blink",)
        elif blink_progress < 0.8:
            return ("eyes half open, opening from blink",)
        else:
            return ("eyes open",)


class ExpressionTransition:
    """Transition between facial expressions"""
    
    EXPRESSIONS = ["neutral", "smile", "laugh", "serious", "surprised", 
                   "seductive", "shy", "playful", "dreamy", "focused"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start_expression": (cls.EXPRESSIONS,),
                "end_expression": (cls.EXPRESSIONS,),
                "progress": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.05}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("expression",)
    FUNCTION = "transition"
    CATEGORY = "Mason/Animation Frames"

    def transition(self, start_expression, end_expression, progress):
        if progress <= 0.15:
            return (f"{start_expression} expression",)
        elif progress >= 0.85:
            return (f"{end_expression} expression",)
        else:
            return (f"expression transitioning from {start_expression} to {end_expression}",)


class BodySwayMotion:
    """Generate subtle body sway for natural standing poses"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "sway_progress": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.05}),
                "sway_type": (["side to side", "forward back", "circular", "weight shift"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("sway_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason/Animation Frames"

    def generate(self, sway_progress, sway_type):
        if sway_type == "side to side":
            if sway_progress < 0.25:
                return ("weight slightly on left foot",)
            elif sway_progress < 0.5:
                return ("centered stance",)
            elif sway_progress < 0.75:
                return ("weight slightly on right foot",)
            else:
                return ("centered stance",)
        
        elif sway_type == "weight shift":
            if sway_progress < 0.5:
                return ("weight on left leg, relaxed right leg",)
            else:
                return ("weight on right leg, relaxed left leg",)
        
        elif sway_type == "forward back":
            if sway_progress < 0.5:
                return ("leaning slightly forward",)
            else:
                return ("leaning slightly back",)
        
        else:  # circular
            if sway_progress < 0.25:
                return ("leaning forward slightly",)
            elif sway_progress < 0.5:
                return ("leaning right slightly",)
            elif sway_progress < 0.75:
                return ("leaning back slightly",)
            else:
                return ("leaning left slightly",)


class HairMotion:
    """Generate hair movement for animation"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "motion_type": (["wind blow", "head turn", "bounce", "settle"],),
                "progress": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.05}),
                "intensity": (["subtle", "moderate", "dramatic"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("hair_motion",)
    FUNCTION = "generate"
    CATEGORY = "Mason/Animation Frames"

    def generate(self, motion_type, progress, intensity):
        if motion_type == "wind blow":
            if progress < 0.3:
                return (f"hair beginning to move in {intensity} wind",)
            elif progress < 0.7:
                return (f"hair flowing in {intensity} wind, dynamic hair movement",)
            else:
                return (f"hair settling from wind",)
        
        elif motion_type == "head turn":
            if progress < 0.5:
                return ("hair swinging with head movement",)
            else:
                return ("hair settling after movement",)
        
        elif motion_type == "bounce":
            if progress < 0.3:
                return ("hair lifting with motion",)
            elif progress < 0.6:
                return ("hair at peak of bounce",)
            else:
                return ("hair falling back down",)
        
        else:  # settle
            return (f"hair gently settling, {intensity} movement",)


class AnimationSeedManager:
    """Manage seeds for consistent character across animation frames"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 999}),
                "seed_mode": (["fixed", "increment", "small_variation"],),
            }
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("frame_seed",)
    FUNCTION = "compute"
    CATEGORY = "Mason/Animation Frames"

    def compute(self, base_seed, frame_number, seed_mode):
        if seed_mode == "fixed":
            return (base_seed,)
        elif seed_mode == "increment":
            return (base_seed + frame_number,)
        else:  # small_variation
            # Use same base but add small noise based on frame
            return (base_seed + (frame_number * 7) % 100,)


class FrameBatcher:
    """Combine prompts from motion nodes into final frame prompt"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
            },
            "optional": {
                "pose_motion": ("STRING", {"forceInput": True}),
                "head_pose": ("STRING", {"forceInput": True}),
                "expression": ("STRING", {"forceInput": True}),
                "eye_state": ("STRING", {"forceInput": True}),
                "breathing": ("STRING", {"forceInput": True}),
                "body_sway": ("STRING", {"forceInput": True}),
                "hair_motion": ("STRING", {"forceInput": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("final_frame_prompt",)
    FUNCTION = "batch"
    CATEGORY = "Mason/Animation Frames"

    def batch(self, base_prompt, pose_motion="", head_pose="", expression="", 
              eye_state="", breathing="", body_sway="", hair_motion=""):
        parts = [base_prompt]
        
        for motion in [pose_motion, head_pose, expression, eye_state, breathing, body_sway, hair_motion]:
            if motion and motion.strip():
                parts.append(motion)
        
        return (", ".join(parts),)


# Node registration
NODE_CLASS_MAPPINGS = {
    "FrameSequenceGenerator": FrameSequenceGenerator,
    "MotionInterpolator": MotionInterpolator,
    "HeadTurnSequence": HeadTurnSequence,
    "BreathingMotion": BreathingMotion,
    "BlinkSequence": BlinkSequence,
    "ExpressionTransition": ExpressionTransition,
    "BodySwayMotion": BodySwayMotion,
    "HairMotion": HairMotion,
    "AnimationSeedManager": AnimationSeedManager,
    "FrameBatcher": FrameBatcher,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrameSequenceGenerator": "🎬 Frame Sequence Generator",
    "MotionInterpolator": "🔄 Motion Interpolator",
    "HeadTurnSequence": "↔️ Head Turn Sequence",
    "BreathingMotion": "💨 Breathing Motion",
    "BlinkSequence": "👁️ Blink Sequence",
    "ExpressionTransition": "😊 Expression Transition",
    "BodySwayMotion": "🚶 Body Sway Motion",
    "HairMotion": "💇 Hair Motion",
    "AnimationSeedManager": "🎲 Animation Seed Manager",
    "FrameBatcher": "📦 Frame Batcher",
}
