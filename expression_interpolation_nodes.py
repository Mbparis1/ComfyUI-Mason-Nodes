"""
Mason's Expression Interpolation Nodes for ComfyUI
Precise emotional and facial expression control - SD 1.5 optimized
"""

import random


class GazeDirector:
    """Control exactly where eyes are looking"""
    
    GAZE_DIRECTIONS = {
        "at_viewer": "looking at viewer, direct eye contact, staring at camera, eyes locked on viewer",
        "away_left": "looking away to the left, gazing left, eyes directed left",
        "away_right": "looking away to the right, gazing right, eyes directed right",
        "upward": "looking upward, eyes gazing up, looking at sky, heavenward gaze",
        "downward": "looking down, downcast eyes, looking at ground, lowered gaze",
        "over_shoulder": "looking over shoulder, glancing back, sideways glance",
        "distant": "distant gaze, looking into distance, far-away look, dreamy eyes",
        "closed": "eyes closed, closed eyes, eyes shut, peaceful expression"
    }
    
    GAZE_INTENSITY = {
        "soft": "soft gaze, gentle eyes, warm look",
        "intense": "intense gaze, piercing eyes, focused stare, powerful look",
        "seductive": "seductive gaze, bedroom eyes, come-hither look, alluring eyes",
        "playful": "playful gaze, mischievous eyes, teasing look, sparkling eyes",
        "innocent": "innocent gaze, wide eyes, doe eyes, naive look"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "direction": (list(cls.GAZE_DIRECTIONS.keys()),),
                "intensity": (list(cls.GAZE_INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("gaze_prompt",)
    FUNCTION = "direct_gaze"
    CATEGORY = "Mason's Nodes/Expression Control"

    def direct_gaze(self, prompt, direction, intensity):
        gaze_dir = self.GAZE_DIRECTIONS.get(direction, "")
        gaze_int = self.GAZE_INTENSITY.get(intensity, "")
        return (f"{prompt}, {gaze_dir}, {gaze_int}",)


class EyebrowController:
    """Fine-tune eyebrow positions for expression nuance"""
    
    EYEBROW_POSITIONS = {
        "neutral": "neutral eyebrows, relaxed brow",
        "raised": "raised eyebrows, surprised brow, lifted eyebrows",
        "slightly_raised": "slightly raised eyebrows, curious expression, subtle lift",
        "furrowed": "furrowed brow, knitted eyebrows, concerned expression, worried brow",
        "angry_brow": "angry brow, deeply furrowed, scowling, intimidating brow",
        "one_raised": "one eyebrow raised, skeptical expression, questioning look",
        "relaxed_low": "relaxed low brows, sultry expression, heavy-lidded look"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "eyebrow_position": (list(cls.EYEBROW_POSITIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("eyebrow_prompt",)
    FUNCTION = "set_eyebrows"
    CATEGORY = "Mason's Nodes/Expression Control"

    def set_eyebrows(self, prompt, eyebrow_position):
        eyebrow_desc = self.EYEBROW_POSITIONS.get(eyebrow_position, "")
        return (f"{prompt}, {eyebrow_desc}",)


class MouthShapeController:
    """Control mouth and lip positions precisely"""
    
    MOUTH_SHAPES = {
        "closed_neutral": "mouth closed, neutral lips, lips together",
        "slight_smile": "slight smile, lips curved up, small grin, subtle smile",
        "wide_smile": "wide smile, big grin, beaming, showing teeth, happy smile",
        "smirk": "smirk, asymmetrical smile, knowing grin, one side up",
        "open_smile": "open mouth smile, laughing, joyful, teeth showing",
        "parted_lips": "parted lips, slightly open mouth, soft expression",
        "pouty": "pouty lips, full pout, sultry lips, duck lips",
        "o_shape": "o-shaped mouth, surprised expression, open mouth",
        "biting_lip": "biting lower lip, coy expression, seductive, playful",
        "tongue_out": "tongue out, playful, silly expression, tongue visible"
    }
    
    TEETH_VISIBILITY = {
        "hidden": "teeth hidden, lips covering teeth",
        "slight_show": "slight teeth visible, just showing teeth",
        "prominent": "teeth prominent, white teeth visible, dental detail"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "mouth_shape": (list(cls.MOUTH_SHAPES.keys()),),
                "teeth": (list(cls.TEETH_VISIBILITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("mouth_prompt",)
    FUNCTION = "set_mouth"
    CATEGORY = "Mason's Nodes/Expression Control"

    def set_mouth(self, prompt, mouth_shape, teeth):
        mouth_desc = self.MOUTH_SHAPES.get(mouth_shape, "")
        teeth_desc = self.TEETH_VISIBILITY.get(teeth, "")
        return (f"{prompt}, {mouth_desc}, {teeth_desc}",)


class EmotionMixer:
    """Blend multiple emotions for complex expressions"""
    
    EMOTIONS = {
        "happy": "happy, joyful, cheerful, positive mood",
        "seductive": "seductive, alluring, sensual, provocative, enticing",
        "confident": "confident, self-assured, powerful, commanding",
        "shy": "shy, bashful, coy, demure, modest",
        "playful": "playful, mischievous, teasing, fun",
        "serious": "serious, stoic, intense, focused",
        "dreamy": "dreamy, romantic, wistful, lost in thought",
        "fierce": "fierce, powerful, intense, strong",
        "vulnerable": "vulnerable, soft, delicate, open",
        "mysterious": "mysterious, enigmatic, intriguing, secretive"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "primary_emotion": (list(cls.EMOTIONS.keys()),),
                "primary_weight": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 1.0, "step": 0.1}),
                "secondary_emotion": (list(cls.EMOTIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("mixed_emotion_prompt",)
    FUNCTION = "mix_emotions"
    CATEGORY = "Mason's Nodes/Expression Control"

    def mix_emotions(self, prompt, primary_emotion, primary_weight, secondary_emotion):
        primary = self.EMOTIONS.get(primary_emotion, "")
        secondary = self.EMOTIONS.get(secondary_emotion, "")
        
        # Use prompt weighting syntax for SD 1.5
        if primary_weight >= 0.8:
            # Primarily first emotion with hint of second
            result = f"{prompt}, {primary}, hint of {secondary_emotion}"
        elif primary_weight >= 0.5:
            # Balanced blend
            result = f"{prompt}, ({primary}:{primary_weight:.1f}), ({secondary}:{1-primary_weight:.1f})"
        else:
            # Secondary is dominant
            result = f"{prompt}, {secondary}, hint of {primary_emotion}"
        
        return (result,)


class MicroExpressionAdder:
    """Add subtle micro-expressions for realism"""
    
    MICRO_EXPRESSIONS = {
        "none": "",
        "eye_crinkle": "subtle eye crinkles, genuine smile indicators, crow's feet",
        "nose_scrunch": "slight nose scrunch, playful micro-expression",
        "lip_twitch": "subtle lip twitch, suppressed emotion, almost-smile",
        "brow_flash": "brief eyebrow raise, recognition expression",
        "dimples": "dimples showing, cheek indentations, smile dimples",
        "nostril_flare": "subtle nostril flare, intensity tell, emotional depth",
        "jaw_tension": "slight jaw tension, determination, holding back emotion",
        "cheek_flush": "slight cheek flush, subtle blush, color in cheeks"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "micro_expression": (list(cls.MICRO_EXPRESSIONS.keys()),),
                "add_realism_tags": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("micro_expression_prompt",)
    FUNCTION = "add_micro"
    CATEGORY = "Mason's Nodes/Expression Control"

    def add_micro(self, prompt, micro_expression, add_realism_tags):
        micro_desc = self.MICRO_EXPRESSIONS.get(micro_expression, "")
        
        if add_realism_tags:
            realism = "realistic expression, natural facial movement, believable emotion"
            if micro_desc:
                return (f"{prompt}, {micro_desc}, {realism}",)
            return (f"{prompt}, {realism}",)
        
        if micro_desc:
            return (f"{prompt}, {micro_desc}",)
        return (prompt,)


NODE_CLASS_MAPPINGS = {
    "GazeDirector": GazeDirector,
    "EyebrowController": EyebrowController,
    "MouthShapeController": MouthShapeController,
    "EmotionMixer": EmotionMixer,
    "MicroExpressionAdder": MicroExpressionAdder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GazeDirector": "👁️ Gaze Director",
    "EyebrowController": "🤨 Eyebrow Controller",
    "MouthShapeController": "👄 Mouth Shape Controller",
    "EmotionMixer": "🎭 Emotion Mixer",
    "MicroExpressionAdder": "✨ Micro Expression Adder",
}
