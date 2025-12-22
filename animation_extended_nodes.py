"""
Mason's Extended Animation Nodes for ComfyUI
Blink, lip sync, cloth simulation - SD 1.5 optimized
"""

import math


class BlinkController:
    """Natural eye blink timing for animation frames"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "blink_every_n_frames": ("INT", {"default": 30, "min": 10, "max": 60}),
                "blink_duration_frames": ("INT", {"default": 3, "min": 2, "max": 5}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("blink_prompt",)
    FUNCTION = "blink"
    CATEGORY = "Mason's Nodes/Animation Extended"

    def blink(self, prompt, frame_number, blink_every_n_frames, blink_duration_frames):
        # Determine if we're in a blink cycle
        cycle_pos = frame_number % blink_every_n_frames
        
        if cycle_pos == 0:
            eye_state = "eyes beginning to close, eyelids lowering"
        elif cycle_pos <= blink_duration_frames // 2:
            eye_state = "eyes closed, blinking, closed eyelids"
        elif cycle_pos <= blink_duration_frames:
            eye_state = "eyes opening, eyelids rising"
        else:
            eye_state = "eyes open, alert eyes, natural gaze"
        
        return (f"{prompt}, {eye_state}",)


class LipSyncHints:
    """Mouth positions for speech animation"""
    
    PHONEMES = {
        "closed": "mouth closed, lips together, neutral mouth",
        "slightly_open": "mouth slightly open, relaxed lips",
        "open": "mouth open, jaw slightly dropped",
        "wide_open": "mouth wide open, jaw dropped, open wide",
        "smile": "smiling, corners of mouth up, happy expression",
        "pucker": "lips puckered, kiss shape, pursed lips",
        "teeth_showing": "teeth visible, showing teeth, open smile",
        "tongue_out": "tongue visible, tongue sticking out slightly",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "mouth_position": (list(cls.PHONEMES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lipsync_prompt",)
    FUNCTION = "sync"
    CATEGORY = "Mason's Nodes/Animation Extended"

    def sync(self, prompt, mouth_position):
        mouth_desc = self.PHONEMES.get(mouth_position, "")
        return (f"{prompt}, {mouth_desc}",)


class ClothSimulationHints:
    """Realistic fabric motion keywords for animation"""
    
    CLOTH_STATES = {
        "still": "fabric at rest, still clothing, no movement",
        "slight_sway": "fabric slightly moving, gentle sway, subtle cloth motion",
        "flowing": "flowing fabric, fabric in motion, dynamic cloth",
        "billowing": "billowing fabric, fabric caught in wind, dramatic cloth movement",
        "clinging": "fabric clinging to body, wet look, form-fitting",
        "falling": "fabric falling, gravity on cloth, dropping material",
        "rising": "fabric rising, lifted by air, floating material",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "cloth_state": (list(cls.CLOTH_STATES.keys()),),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "motion_cycle": ("INT", {"default": 10, "min": 4, "max": 20}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("cloth_prompt",)
    FUNCTION = "simulate"
    CATEGORY = "Mason's Nodes/Animation Extended"

    def simulate(self, prompt, cloth_state, frame_number, motion_cycle):
        # For animation, we can cycle through states
        cloth_desc = self.CLOTH_STATES.get(cloth_state, "")
        phase = (frame_number % motion_cycle) / motion_cycle
        
        # Add subtle variation based on phase
        if phase < 0.5:
            variation = "cloth moving forward"
        else:
            variation = "cloth moving back"
        
        return (f"{prompt}, {cloth_desc}, {variation}",)


class HairPhysics:
    """Realistic hair motion for animation - SD 1.5"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "motion_type": (["still", "slight_movement", "flowing", "windblown", "underwater", "jumping"],),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "cycle_frames": ("INT", {"default": 8, "min": 4, "max": 16}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("hair_physics_prompt",)
    FUNCTION = "animate"
    CATEGORY = "Mason's Nodes/Animation Extended"

    def animate(self, prompt, motion_type, frame_number, cycle_frames):
        phase = (frame_number % cycle_frames) / cycle_frames
        
        motion_descriptions = {
            "still": "hair at rest, still hair, settled hair",
            "slight_movement": f"hair slightly moving, gentle hair motion, {'hair swaying left' if phase < 0.5 else 'hair swaying right'}",
            "flowing": f"flowing hair, hair in motion, {'hair flowing up' if phase < 0.5 else 'hair flowing down'}",
            "windblown": "windblown hair, hair caught in wind, dramatic hair movement, wild hair",
            "underwater": "hair floating, underwater hair physics, weightless hair, spread hair",
            "jumping": f"hair {'rising up' if phase < 0.5 else 'falling down'}, dynamic hair, motion hair",
        }
        
        hair_desc = motion_descriptions.get(motion_type, "")
        return (f"{prompt}, {hair_desc}",)


NODE_CLASS_MAPPINGS = {
    "BlinkController": BlinkController,
    "LipSyncHints": LipSyncHints,
    "ClothSimulationHints": ClothSimulationHints,
    "HairPhysics": HairPhysics,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BlinkController": "👁️ Blink Controller",
    "LipSyncHints": "👄 Lip Sync Hints",
    "ClothSimulationHints": "👗 Cloth Simulation",
    "HairPhysics": "💇 Hair Physics",
}
