"""
Mason's Interaction Nodes for ComfyUI
Pose interactions and reactions - SD 1.5 optimized
"""


class TwoPersonInteraction:
    """Define poses for two people interacting"""
    
    INTERACTIONS = {
        "embracing": "two people embracing, hugging, arms around each other, intimate embrace",
        "kissing": "two people kissing, lips touching, romantic kiss, intimate",
        "dancing": "two people dancing, dance partners, close dancing, romantic dance",
        "holding_hands": "two people holding hands, hand in hand, fingers intertwined",
        "back_to_back": "two people back to back, leaning on each other",
        "face_to_face": "two people face to face, looking at each other, eye contact",
        "spooning": "two people spooning, cuddling, lying together, intimate position",
        "piggyback": "piggyback ride, one person carrying another, playful",
        "leaning_on": "one person leaning on another, resting head on shoulder",
        "wrestling": "two people wrestling, playful struggle, tangled",
    }
    
    RELATIONSHIP = {
        "romantic": "romantic couple, lovers, intimate relationship, passion",
        "playful": "playful interaction, fun, lighthearted, teasing",
        "sensual": "sensual interaction, seductive, intimate, passionate",
        "tender": "tender moment, gentle, caring, soft interaction",
        "intense": "intense interaction, passionate, powerful, dramatic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "interaction": (list(cls.INTERACTIONS.keys()),),
                "relationship": (list(cls.RELATIONSHIP.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("interaction_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Interactions"

    def build(self, prompt, interaction, relationship):
        inter = self.INTERACTIONS.get(interaction, "")
        rel = self.RELATIONSHIP.get(relationship, "")
        return (f"{prompt}, {inter}, {rel}",)


class ObjectInteraction:
    """Define interaction with objects/props"""
    
    OBJECTS = {
        "phone": "holding phone, looking at smartphone, texting, selfie",
        "drink": "holding drink, cocktail glass, wine glass, beverage",
        "mirror": "looking in mirror, reflection, self-admiring, vanity",
        "camera": "posing for camera, being photographed, model pose",
        "book": "holding book, reading, intellectual, relaxed",
        "flower": "holding flower, smelling flower, romantic prop",
        "cigarette": "holding cigarette, smoking, moody, noir",
        "fan": "holding fan, fanning self, elegant, mysterious",
        "umbrella": "holding umbrella, parasol, stylish accessory",
        "hat": "holding hat, adjusting hat, playful with hat",
        "sunglasses": "wearing sunglasses, adjusting glasses, cool",
        "towel": "holding towel, wrapped in towel, post-shower",
        "pillow": "holding pillow, hugging pillow, cozy",
    }
    
    ACTION = {
        "holding": "holding, grasping, carrying",
        "using": "actively using, interacting with",
        "playing_with": "playing with, fiddling with, toying with",
        "admiring": "admiring, looking at, examining",
        "putting_down": "putting down, setting aside, releasing",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "object": (list(cls.OBJECTS.keys()),),
                "action": (list(cls.ACTION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("object_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Interactions"

    def build(self, prompt, object, action):
        obj = self.OBJECTS.get(object, "")
        act = self.ACTION.get(action, "")
        return (f"{prompt}, {obj}, {act}",)


class LookingAtCamera:
    """Control eye contact and camera awareness"""
    
    GAZE_TYPES = {
        "direct": "looking directly at camera, direct eye contact, engaging viewer",
        "seductive": "seductive gaze at camera, bedroom eyes, alluring look",
        "shy": "shy glance at camera, coy look, bashful, looking away slightly",
        "confident": "confident stare, strong eye contact, powerful gaze",
        "dreamy": "dreamy look, soft gaze, distant eyes, wistful",
        "playful": "playful look at camera, mischievous eyes, teasing glance",
        "intense": "intense stare, piercing eyes, dramatic eye contact",
        "candid": "candid moment, caught off guard, natural unposed look",
        "looking_away": "looking away from camera, profile view, not engaging",
        "eyes_closed": "eyes closed, peaceful expression, serene",
        "over_shoulder": "looking over shoulder at camera, glancing back",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "gaze": (list(cls.GAZE_TYPES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("gaze_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Interactions"

    def build(self, prompt, gaze):
        g = self.GAZE_TYPES.get(gaze, "")
        return (f"{prompt}, {g}",)


class ReactionPoses:
    """Define reaction expressions and poses"""
    
    REACTIONS = {
        "surprised": "surprised expression, wide eyes, open mouth, shocked, startled",
        "laughing": "laughing, genuine laughter, happy, joyful expression, smiling wide",
        "shy": "shy expression, blushing, looking down, bashful, demure",
        "confident": "confident expression, self-assured, powerful stance, proud",
        "flirty": "flirty expression, teasing smile, playful wink, coquettish",
        "serious": "serious expression, stern, focused, intense, no smile",
        "curious": "curious expression, interested, head tilted, questioning look",
        "sleepy": "sleepy expression, drowsy, tired eyes, yawning, relaxed",
        "excited": "excited expression, enthusiastic, energetic, animated",
        "thoughtful": "thoughtful expression, contemplative, pensive, thinking",
        "embarrassed": "embarrassed expression, blushing, covering face, flustered",
        "pleased": "pleased expression, satisfied smile, content, happy",
    }
    
    INTENSITY = {
        "subtle": "subtle expression, slight, understated, natural",
        "moderate": "moderate expression, clear, visible, natural intensity",
        "exaggerated": "exaggerated expression, dramatic, over the top, theatrical",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "reaction": (list(cls.REACTIONS.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("reaction_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Interactions"

    def build(self, prompt, reaction, intensity):
        react = self.REACTIONS.get(reaction, "")
        intense = self.INTENSITY.get(intensity, "")
        return (f"{prompt}, {react}, {intense}",)


NODE_CLASS_MAPPINGS = {
    "TwoPersonInteraction": TwoPersonInteraction,
    "ObjectInteraction": ObjectInteraction,
    "LookingAtCamera": LookingAtCamera,
    "ReactionPoses": ReactionPoses,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TwoPersonInteraction": "👫 Two Person Interaction",
    "ObjectInteraction": "🎁 Object Interaction",
    "LookingAtCamera": "👁️ Looking At Camera",
    "ReactionPoses": "😮 Reaction Poses",
}
