"""
Mason's Micro-Expressions Nodes for ComfyUI
Advanced control over subtle facial cues, eye contact, and emotional signaling.
"""

class MicroExpressionPro:
    """Subtle Facial Cues and Signals"""
    
    EXPRESSION = {
        "lip_bite": "biting lip, nervous lip bite, seductive lip bite, teeth on lip",
        "dilated_pupils": "dilated pupils, blown out pupils, arousal, chemical eyes",
        "half_lidded": "half lidded eyes, sleepy eyes, bedroom eyes, heavy lids",
        "flared_nostrils": "flared nostrils, heavy breathing, panting, aroused breathing",
        "eyebrow_raise": "raised eyebrow, questioning look, skeptical, one eyebrow up",
        "jaw_clench": "clenched jaw, tight jawline, tense expression",
        "swallowing": "gulping, throat bulge, visible swallow, nervous gulp",
    }
    
    INTENSITY = {
        "subtle": "subtle expression, barely visible, micro expression",
        "noticeable": "clear expression, visible emotion",
        "intense": "exaggerated expression, intense emotion, extreme face",
        "twitching": "twitching muscle, involuntary movement, spasm",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "expression": (list(cls.EXPRESSION.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Micro-Expressions"

    def generate(self, prompt, expression, intensity):
        e = self.EXPRESSION.get(expression, "")
        i = self.INTENSITY.get(intensity, "")
        
        positive = f"{prompt}, {e}, {i}"
        negative = "bad face, distorted face, uncanny valley"
        
        return (positive, negative)


class EyeContactPro:
    """Direction and Quality of Gaze"""
    
    DIRECTION = {
        "at_viewer": "looking at viewer, eye contact, breaking fourth wall, staring at camera",
        "looking_up": "looking up, ahegao eyes, eyes rolled back, upward gaze",
        "looking_down": "looking down, shy, ashamed, submissive gaze, checking body",
        "looking_away": "looking away, avoiding eye contact, distracted",
        "side_eye": "side eye, glancing sideways, suspicious, checking surroundings",
        "crossed": "crossed eyes, ahegao, silly face, confused",
    }
    
    QUALITY = {
        "intense": "intense stare, piercing gaze, unwavering",
        "glassy": "glassy eyes, wet eyes, crying eyes, stoned eyes",
        "dead": "dead eyes, thousand yard stare, empty eyes, mind break",
        "loving": "loving gaze, soft eyes, adoring look, romantic eyes",
        "lustful": "lustful gaze, hungry eyes, predatory look, bedroom eyes",
        "teary": "teary eyes, tears welling up, crying, emotional",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "direction": (list(cls.DIRECTION.keys()),),
                "quality": (list(cls.QUALITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Micro-Expressions"

    def generate(self, prompt, direction, quality):
        d = self.DIRECTION.get(direction, "")
        q = self.QUALITY.get(quality, "")
        
        positive = f"{prompt}, {d}, {q}"
        negative = "strabismus, lazy eye, bad eyes"
        
        return (positive, negative)


class LipReaderPro:
    """Mouth Shapes and Actions"""
    
    SHAPE = {
        "parted": "parted lips, slightly open mouth, breathing through mouth",
        "o_face": "o-face, gasping, surprised mouth, moaning mouth",
        "pout": "pout, duck face, kissing face, pursed lips",
        "smile": "smile, happy, grinning, showing teeth",
        "frown": "frown, sad, corners down, unhappy",
        "snarl": "snarl, showing teeth, aggressive, lip curl",
    }
    
    ACTION = {
        "licking": "licking lips, tongue out, tasting",
        "drooling": "drooling, saliva string, mess",
        "biting": "biting lip, suppressed moan",
        "sucking": "sucking in breath, vacuum seal",
        "gasping": "gasping for air, sharp intake",
    }
    
    STATE = {
        "wet": "wet lips, glossy lips, lip gloss",
        "chapped": "dry lips, chapped lips, textured",
        "lipstick": "lipstick, makeup, painted lips",
        "natural": "natural lips, nude lips, no makeup",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "shape": (list(cls.SHAPE.keys()),),
                "action": (list(cls.ACTION.keys()),),
                "state": (list(cls.STATE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Micro-Expressions"

    def generate(self, prompt, shape, action, state):
        s = self.SHAPE.get(shape, "")
        a = self.ACTION.get(action, "")
        st = self.STATE.get(state, "")
        
        positive = f"{prompt}, {s}, {a}, {st}"
        negative = "bad mouth, bad teeth, missing teeth, extra teeth"
        
        return (positive, negative)


class BlushMaster:
    """Dynamic Blood Flow and Skin Reaction"""
    
    LOCATION = {
        "cheeks": "blushing cheeks, rosy cheeks, apple of cheeks",
        "full_face": "full face blush, red face, tomato face",
        "ears": "blushing ears, red ears, hot ears",
        "chest": "chest flush, red chest, sex flush, hives",
        "nose": "red nose, cold nose, drunk nose",
        "body": "full body flush, pink skin, aroused skin",
    }
    
    INTENSITY = {
        "slight": "slight blush, hint of pink, cute",
        "moderate": "blushing, embarrassed, shy",
        "heavy": "heavy blush, deep red, feverish, hot",
        "extreme": "extreme blush, burning up, overheated",
    }
    
    CAUSE = {
        "arousal": "aroused blush, sex flush, hot and bothered",
        "embarrassment": "embarrassed, shy, ashamed, mortified",
        "exertion": "sweaty flush, workout flush, tired",
        "drunk": "drunk flush, asian glow, alcohol flush",
        "fever": "fever, sick, temperature, hot",
        "crying": "crying flush, puffy face, emotional",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "location": (list(cls.LOCATION.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
                "cause": (list(cls.CAUSE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Micro-Expressions"

    def generate(self, prompt, location, intensity, cause):
        l = self.LOCATION.get(location, "")
        i = self.INTENSITY.get(intensity, "")
        c = self.CAUSE.get(cause, "")
        
        positive = f"{prompt}, {l}, {i}, {c}"
        negative = "sunburn, rash, disease"
        
        return (positive, negative)


NODE_CLASS_MAPPINGS = {
    "MicroExpressionPro": MicroExpressionPro,
    "EyeContactPro": EyeContactPro,
    "LipReaderPro": LipReaderPro,
    "BlushMaster": BlushMaster,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MicroExpressionPro": "🥺 Micro Expression Pro",
    "EyeContactPro": "👁️ Eye Contact Pro",
    "LipReaderPro": "👄 Lip Reader Pro",
    "BlushMaster": "😳 Blush Master",
}
