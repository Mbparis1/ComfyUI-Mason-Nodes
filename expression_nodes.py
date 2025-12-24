"""
Mason's Micro-Expression Master Nodes
Extreme focus on facial reactions to intensity - SD 1.5 optimized
"""

class PleasureExpressionPro:
    """Detailed facial expressions for intense pleasure"""
    
    EXPRESSIONS = {
        "eye_roll": "eyes rolling back, whites of eyes showing, ecstatic gaze",
        "lip_bite": "biting lower lip, sensual lip bite, looking down",
        "open_mouth_gasp": "mouth open in a gasp, heavy breathing, catching breath",
        "clenched_teeth": "teeth clenched, grit teeth, intense pleasure expression",
        "flushed_ecstasy": "heavily flushed face, red cheeks, face contorted in pleasure",
        "dazed_look": "dazed expression, unfocused eyes, lost in the moment",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "expression": (list(cls.EXPRESSIONS.keys()),),
                "intensity": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0, "step": 0.1}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("expression_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Expressions"

    def apply(self, prompt, expression, intensity):
        e = self.EXPRESSIONS.get(expression, "")
        if intensity > 1.5:
            e = f"extreme {e}, intense expression"
        elif intensity < 0.5:
            e = f"subtle {e}, slight expression"
        return (f"{prompt}, {e}",)

class EyeStateController:
    """Fine control over eye appearance and gaze"""
    
    STATES = {
        "dilated_pupils": "dilated pupils, large pupils, blown out pupils, wide-eyed gaze",
        "sultry_lids": "heavy eyelids, bedroom eyes, half-closed eyes, seductive gaze",
        "watery_eyes": "watery eyes, glistening eyes, tears of pleasure, moist gaze",
        "tightly_closed": "eyes tightly shut, scrunching eyes, intense focus",
        "upward_gaze": "looking up, eyes directed upwards, rolling eyes back",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "state": (list(cls.STATES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("eye_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Expressions"

    def apply(self, prompt, state):
        s = self.STATES.get(state, "")
        return (f"{prompt}, {s}",)

class ArousalVisuals:
    """Subtle visual cues for arousal and intensity"""
    
    CUES = {
        "sweat_beads": "sweat beads on forehead, perspiration on skin, glistening sweat",
        "trembling_lips": "trembling lips, quivering mouth, catch in breath",
        "heavy_flushing": "heavy flushing on chest and neck, skin turning red, heat on skin",
        "flared_nostrils": "flared nostrils, heavy breathing, quick breaths",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "cue": (list(cls.CUES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("visual_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Expressions"

    def apply(self, prompt, cue):
        c = self.CUES.get(cue, "")
        return (f"{prompt}, {c}",)

NODE_CLASS_MAPPINGS = {
    "PleasureExpressionPro": PleasureExpressionPro,
    "EyeStateController": EyeStateController,
    "ArousalVisuals": ArousalVisuals,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PleasureExpressionPro": "😫 Pleasure Expression Pro",
    "EyeStateController": "👀 Eye State Controller",
    "ArousalVisuals": "🔥 Arousal Visuals",
}
