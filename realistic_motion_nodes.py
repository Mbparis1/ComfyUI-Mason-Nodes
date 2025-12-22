"""
Mason's Realistic Motion Nodes for ComfyUI
Human-like motion with anatomical accuracy - SD 1.5 optimized
"""

import math


class RealisticWalkCycle:
    """Anatomically correct walking animation"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "cycle_frames": ("INT", {"default": 8, "min": 4, "max": 16}),
                "walk_style": (["casual", "confident", "seductive", "runway", "hurried"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("walk_prompt",)
    FUNCTION = "animate"
    CATEGORY = "Mason's Nodes/Realistic Motion"

    def animate(self, prompt, frame_number, cycle_frames, walk_style):
        phase = (frame_number % cycle_frames) / cycle_frames
        
        # Realistic walking phases
        if phase < 0.125:
            pose = "right foot forward, left foot back, weight shifting, arms naturally swinging"
        elif phase < 0.25:
            pose = "mid-stride, both feet close together, transitioning weight"
        elif phase < 0.375:
            pose = "left foot forward, right foot back, natural arm swing"
        elif phase < 0.5:
            pose = "left foot planted, pushing off, natural walking motion"
        elif phase < 0.625:
            pose = "weight on left foot, right leg swinging forward"
        elif phase < 0.75:
            pose = "both feet close, transitioning, balanced stance"
        elif phase < 0.875:
            pose = "right foot forward, weight shifting naturally"
        else:
            pose = "completing stride, natural walking cycle"
        
        style_mods = {
            "casual": "relaxed walk, natural gait",
            "confident": "confident stride, powerful walk, head high",
            "seductive": "seductive walk, swaying hips, alluring stride",
            "runway": "runway walk, model strut, deliberate steps",
            "hurried": "fast walk, purposeful stride, quick pace",
        }
        
        style = style_mods.get(walk_style, "")
        
        return (f"{prompt}, walking, {pose}, {style}, anatomically correct posture",)


class RealisticDanceMotion:
    """Human-like dance movements"""
    
    DANCE_MOVES = {
        "sway": ["hips swaying left", "centered stance", "hips swaying right", "centered stance"],
        "spin": ["beginning to turn", "quarter turn, profile view", "half turn, back visible", "three-quarter turn", "completing full turn"],
        "body_roll": ["chest forward, hips back", "wave moving down body", "hips forward, chest back", "neutral stance"],
        "arm_wave": ["arms down", "arms rising gracefully", "arms extended above", "arms flowing down"],
        "hip_circle": ["hips thrust forward", "hips to right side", "hips back", "hips to left side"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "dance_move": (list(cls.DANCE_MOVES.keys()),),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "total_frames": ("INT", {"default": 4, "min": 2, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("dance_prompt",)
    FUNCTION = "dance"
    CATEGORY = "Mason's Nodes/Realistic Motion"

    def dance(self, prompt, dance_move, frame_number, total_frames):
        moves = self.DANCE_MOVES.get(dance_move, ["dancing"])
        idx = frame_number % len(moves)
        move_desc = moves[idx]
        
        return (f"{prompt}, dancing, {move_desc}, graceful movement, natural body motion, anatomically correct",)


class NaturalHeadMovement:
    """Realistic head turns and tilts"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "movement_type": (["turn_left_right", "nod", "tilt", "look_around"],),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "cycle_frames": ("INT", {"default": 5, "min": 3, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("head_prompt",)
    FUNCTION = "move_head"
    CATEGORY = "Mason's Nodes/Realistic Motion"

    def move_head(self, prompt, movement_type, frame_number, cycle_frames):
        phase = (frame_number % cycle_frames) / cycle_frames
        
        movements = {
            "turn_left_right": [
                "looking left, head turned left, profile approaching",
                "head turning, transitioning to center",
                "looking forward, head centered, facing camera",
                "head turning right, transitioning",
                "looking right, head turned right, opposite profile",
            ],
            "nod": [
                "head neutral, looking forward",
                "head tilting down, chin lowering, nodding",
                "head at lowest point, looking down slightly",
                "head rising, returning to neutral",
                "head neutral, completed nod",
            ],
            "tilt": [
                "head straight, neutral position",
                "head tilting right, curious expression",
                "head at full tilt, playful angle",
                "head returning to center",
                "head tilting left, opposite side",
            ],
            "look_around": [
                "looking straight ahead, alert",
                "eyes and head moving right, scanning",
                "looking right side, attentive",
                "head moving back to center",
                "looking left, completing scan",
            ],
        }
        
        move_list = movements.get(movement_type, movements["turn_left_right"])
        idx = int(phase * len(move_list)) % len(move_list)
        
        return (f"{prompt}, {move_list[idx]}, natural head position, realistic neck movement",)


class AnatomicalBreathing:
    """Highly realistic breathing animation"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "breath_rate": (["slow_relaxed", "normal", "elevated", "heavy"],),
                "cycle_frames": ("INT", {"default": 12, "min": 6, "max": 20}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("breathing_prompt",)
    FUNCTION = "breathe"
    CATEGORY = "Mason's Nodes/Realistic Motion"

    def breathe(self, prompt, frame_number, breath_rate, cycle_frames):
        phase = (frame_number % cycle_frames) / cycle_frames
        
        # Breathing is ~40% inhale, ~60% exhale for realism
        if phase < 0.1:
            state = "beginning to inhale, chest starting to rise"
        elif phase < 0.2:
            state = "inhaling, chest expanding, shoulders slightly rising"
        elif phase < 0.3:
            state = "deep inhale, chest fully expanded, lungs full"
        elif phase < 0.4:
            state = "holding breath briefly, chest expanded"
        elif phase < 0.5:
            state = "beginning to exhale, chest starting to lower"
        elif phase < 0.65:
            state = "exhaling, chest relaxing, natural release"
        elif phase < 0.8:
            state = "continuing exhale, chest lowering"
        elif phase < 0.9:
            state = "exhale complete, chest at rest"
        else:
            state = "brief pause between breaths, relaxed"
        
        rate_mods = {
            "slow_relaxed": "slow peaceful breathing, deeply relaxed",
            "normal": "natural breathing rhythm, relaxed",
            "elevated": "slightly faster breathing, alert",
            "heavy": "heavy breathing, chest heaving, intense",
        }
        
        rate_desc = rate_mods.get(breath_rate, "")
        
        return (f"{prompt}, {state}, {rate_desc}, anatomically correct chest movement",)


class RealisticArmMovement:
    """Natural arm gestures and movements"""
    
    MOVEMENTS = {
        "raise_above": ["arms at sides", "arms beginning to rise", "arms at shoulder level", "arms above head, extended", "arms fully raised above head"],
        "reach_forward": ["arms at rest", "arms moving forward", "arms extended forward, reaching", "arms fully extended"],
        "cross_arms": ["arms at sides", "arms moving inward", "arms crossed over chest", "arms hugging self"],
        "hands_on_hips": ["arms relaxed", "arms bending at elbows", "hands moving to hips", "hands on hips, confident pose"],
        "wave": ["arm at side", "arm raising", "arm raised, waving", "waving motion", "arm lowering"],
        "touch_hair": ["arm at side", "hand rising toward head", "fingers in hair, playing with hair", "touching hair sensually"],
        "stretch": ["arms at sides, relaxed", "arms spreading outward", "full stretch, arms wide", "stretching fully extended"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "arm_movement": (list(cls.MOVEMENTS.keys()),),
                "frame_number": ("INT", {"default": 0, "min": 0}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("arm_prompt",)
    FUNCTION = "move_arms"
    CATEGORY = "Mason's Nodes/Realistic Motion"

    def move_arms(self, prompt, arm_movement, frame_number):
        stages = self.MOVEMENTS.get(arm_movement, ["arms at sides"])
        idx = frame_number % len(stages)
        arm_desc = stages[idx]
        
        return (f"{prompt}, {arm_desc}, natural arm position, anatomically correct arms and hands",)


class WeightShiftMotion:
    """Realistic weight distribution shifts"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "shift_type": (["hip_sway", "lean_forward", "lean_back", "side_to_side", "s_curve"],),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "cycle_frames": ("INT", {"default": 6, "min": 3, "max": 12}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weight_prompt",)
    FUNCTION = "shift"
    CATEGORY = "Mason's Nodes/Realistic Motion"

    def shift(self, prompt, shift_type, frame_number, cycle_frames):
        phase = (frame_number % cycle_frames) / cycle_frames
        
        shifts = {
            "hip_sway": [
                "weight on left leg, hip jutting left, relaxed right leg",
                "weight centered, hips level, balanced stance",
                "weight on right leg, hip jutting right, relaxed left leg",
                "weight centered, transitioning",
            ],
            "lean_forward": [
                "standing straight, neutral posture",
                "leaning slightly forward, curious pose",
                "leaning forward, engaged posture",
                "returning to upright position",
            ],
            "lean_back": [
                "standing upright, neutral",
                "leaning back slightly, relaxed",
                "leaning back more, casual pose",
                "returning forward, straightening",
            ],
            "side_to_side": [
                "leaning right, weight shifted right",
                "center, balanced",
                "leaning left, weight shifted left",
                "center, balanced",
            ],
            "s_curve": [
                "subtle S-curve pose, hips right, shoulders left",
                "transitioning, straightening",
                "S-curve opposite direction, hips left, shoulders right",
                "transitioning back",
            ],
        }
        
        shift_list = shifts.get(shift_type, shifts["hip_sway"])
        idx = int(phase * len(shift_list)) % len(shift_list)
        
        return (f"{prompt}, {shift_list[idx]}, natural weight distribution, realistic body posture",)


NODE_CLASS_MAPPINGS = {
    "RealisticWalkCycle": RealisticWalkCycle,
    "RealisticDanceMotion": RealisticDanceMotion,
    "NaturalHeadMovement": NaturalHeadMovement,
    "AnatomicalBreathing": AnatomicalBreathing,
    "RealisticArmMovement": RealisticArmMovement,
    "WeightShiftMotion": WeightShiftMotion,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RealisticWalkCycle": "🚶 Realistic Walk Cycle",
    "RealisticDanceMotion": "💃 Realistic Dance Motion",
    "NaturalHeadMovement": "🗣️ Natural Head Movement",
    "AnatomicalBreathing": "🫁 Anatomical Breathing",
    "RealisticArmMovement": "💪 Realistic Arm Movement",
    "WeightShiftMotion": "⚖️ Weight Shift Motion",
}
