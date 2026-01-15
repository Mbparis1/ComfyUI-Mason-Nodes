"""
Quick Prompt Builder Nodes - Simple dropdowns to build prompts fast
No typing needed - just select options from menus
"""

class QuickPersonBuilder:
    """Build a person prompt with simple dropdowns - no typing needed"""
    
    GENDERS = ["woman", "man", "female", "male", "girl", "boy", "person"]
    AGES = ["young", "20s", "30s", "40s", "mature", "elderly", "teen", "adult"]
    ETHNICITIES = ["caucasian", "asian", "african", "latina", "indian", "middle eastern", "mixed", ""]
    BODY_TYPES = ["slim", "athletic", "curvy", "petite", "average", "muscular", "thick", "fit", ""]
    HAIR_COLORS = ["blonde", "brunette", "black hair", "red hair", "auburn", "silver", "platinum blonde", "dark brown", ""]
    HAIR_STYLES = ["long hair", "short hair", "ponytail", "bun", "braids", "wavy hair", "straight hair", "curly hair", "messy hair", ""]
    EYE_COLORS = ["blue eyes", "green eyes", "brown eyes", "hazel eyes", "dark eyes", ""]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "gender": (cls.GENDERS,),
                "age": (cls.AGES,),
            },
            "optional": {
                "ethnicity": (cls.ETHNICITIES,),
                "body_type": (cls.BODY_TYPES,),
                "hair_color": (cls.HAIR_COLORS,),
                "hair_style": (cls.HAIR_STYLES,),
                "eye_color": (cls.EYE_COLORS,),
                "extra_details": ("STRING", {"default": "", "multiline": False}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("person_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason/Quick Builders"

    def build(self, gender, age, ethnicity="", body_type="", hair_color="", hair_style="", eye_color="", extra_details=""):
        parts = [f"{age} {ethnicity} {gender}".strip()]
        if body_type: parts.append(body_type)
        if hair_color: parts.append(hair_color)
        if hair_style: parts.append(hair_style)
        if eye_color: parts.append(eye_color)
        if extra_details: parts.append(extra_details)
        return (", ".join(parts),)


class QuickOutfitBuilder:
    """Build outfit prompts with dropdowns"""
    
    OUTFIT_TYPES = ["casual", "formal", "lingerie", "swimwear", "athletic", "business", "evening dress", "nude", "topless", "underwear", "bikini", ""]
    COLORS = ["black", "white", "red", "blue", "pink", "purple", "green", "gold", "silver", "nude colored", ""]
    MATERIALS = ["silk", "lace", "cotton", "leather", "satin", "sheer", "mesh", "velvet", "denim", ""]
    FIT = ["tight", "loose", "fitted", "revealing", "conservative", "elegant", ""]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "outfit_type": (cls.OUTFIT_TYPES,),
            },
            "optional": {
                "color": (cls.COLORS,),
                "material": (cls.MATERIALS,),
                "fit": (cls.FIT,),
                "extra": ("STRING", {"default": "", "multiline": False}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("outfit_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason/Quick Builders"

    def build(self, outfit_type, color="", material="", fit="", extra=""):
        parts = []
        if fit: parts.append(fit)
        if color: parts.append(color)
        if material: parts.append(material)
        if outfit_type: parts.append(outfit_type)
        if extra: parts.append(extra)
        return (", ".join(parts) if parts else "",)


class QuickSceneBuilder:
    """Build scene/background prompts with dropdowns"""
    
    LOCATIONS = ["bedroom", "living room", "bathroom", "kitchen", "office", "studio", "outdoor", "beach", "forest", "city street", "hotel room", "pool", "garden", "rooftop", ""]
    LIGHTING = ["natural light", "soft lighting", "dramatic lighting", "golden hour", "sunset", "studio lighting", "dim lighting", "candlelight", "neon", ""]
    MOOD = ["romantic", "sensual", "professional", "casual", "intimate", "artistic", "cinematic", "moody", "bright", ""]
    TIME = ["daytime", "night", "morning", "evening", "sunset", ""]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "location": (cls.LOCATIONS,),
            },
            "optional": {
                "lighting": (cls.LIGHTING,),
                "mood": (cls.MOOD,),
                "time_of_day": (cls.TIME,),
                "extra": ("STRING", {"default": "", "multiline": False}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason/Quick Builders"

    def build(self, location, lighting="", mood="", time_of_day="", extra=""):
        parts = []
        if mood: parts.append(mood)
        if location: parts.append(location)
        if lighting: parts.append(lighting)
        if time_of_day: parts.append(time_of_day)
        if extra: parts.append(extra)
        return (", ".join(parts) if parts else "",)


class QuickPoseBuilder:
    """Build pose prompts with dropdowns"""
    
    POSES = ["standing", "sitting", "lying down", "kneeling", "leaning", "walking", "dancing", "stretching", "bending over", "on all fours", "side lying", ""]
    POSITIONS = ["front view", "side view", "back view", "three quarter view", "from above", "from below", "close up", "full body", "upper body", ""]
    EXPRESSIONS = ["smiling", "serious", "seductive", "laughing", "neutral", "playful", "sultry", "confident", "shy", ""]
    ACTIONS = ["looking at camera", "looking away", "eyes closed", "touching hair", "hands on hips", "arms crossed", "relaxed", ""]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pose": (cls.POSES,),
            },
            "optional": {
                "camera_position": (cls.POSITIONS,),
                "expression": (cls.EXPRESSIONS,),
                "action": (cls.ACTIONS,),
                "extra": ("STRING", {"default": "", "multiline": False}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason/Quick Builders"

    def build(self, pose, camera_position="", expression="", action="", extra=""):
        parts = []
        if pose: parts.append(pose)
        if camera_position: parts.append(camera_position)
        if expression: parts.append(expression)
        if action: parts.append(action)
        if extra: parts.append(extra)
        return (", ".join(parts) if parts else "",)


class QuickQualityBuilder:
    """Add quality tags with one click"""
    
    QUALITY_PRESETS = [
        "ultra realistic, photorealistic, 8k, highly detailed",
        "masterpiece, best quality, highly detailed",
        "professional photo, sharp focus, detailed",
        "cinematic, film grain, dramatic",
        "soft focus, artistic, ethereal",
        "raw photo, natural, unedited look",
        "studio photo, professional lighting",
        ""
    ]
    
    CAMERA_PRESETS = [
        "shot on Canon EOS R5, 85mm lens",
        "shot on Sony A7III, portrait lens",
        "shot on Nikon D850, natural light",
        "DSLR, bokeh, shallow depth of field",
        "professional photography",
        ""
    ]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "quality_preset": (cls.QUALITY_PRESETS,),
            },
            "optional": {
                "camera_preset": (cls.CAMERA_PRESETS,),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("quality_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason/Quick Builders"

    def build(self, quality_preset, camera_preset=""):
        parts = [p for p in [quality_preset, camera_preset] if p]
        return (", ".join(parts),)


class PromptCombiner:
    """Combine all the quick builders into one final prompt"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "person": ("STRING", {"forceInput": True}),
                "outfit": ("STRING", {"forceInput": True}),
                "pose": ("STRING", {"forceInput": True}),
                "scene": ("STRING", {"forceInput": True}),
                "quality": ("STRING", {"forceInput": True}),
                "extra": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("final_prompt",)
    FUNCTION = "combine"
    CATEGORY = "Mason/Quick Builders"

    def combine(self, person="", outfit="", pose="", scene="", quality="", extra=""):
        parts = [p for p in [person, outfit, pose, scene, quality, extra] if p and p.strip()]
        return (", ".join(parts),)


class QuickNegativeBuilder:
    """Pre-built negative prompts"""
    
    PRESETS = {
        "Standard": "ugly, deformed, noisy, blurry, low contrast, bad anatomy, bad hands, missing fingers, extra limbs, disfigured, poorly drawn face, mutation, mutated",
        "Photorealistic": "cartoon, anime, illustration, painting, drawing, art, sketch, cgi, 3d, render, bad anatomy, bad hands, missing fingers, extra limbs, deformed, blurry, noisy",
        "Portrait": "bad eyes, asymmetric eyes, bad teeth, ugly, deformed, noisy, blurry, bad anatomy, bad hands, missing fingers, disfigured, poorly drawn face",
        "Full Body": "bad anatomy, bad proportions, extra limbs, missing limbs, deformed body, twisted body, bad hands, missing fingers, extra fingers, poorly drawn, disfigured",
        "NSFW Clean": "ugly, deformed, bad anatomy, bad hands, missing fingers, extra limbs, disfigured, mutation, gross, disturbing",
        "Minimal": "ugly, deformed, blurry, bad quality",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PRESETS.keys()),),
            },
            "optional": {
                "add_extra": ("STRING", {"default": "", "multiline": False}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason/Quick Builders"

    def build(self, preset, add_extra=""):
        neg = self.PRESETS.get(preset, "")
        if add_extra:
            neg = f"{neg}, {add_extra}"
        return (neg,)


# Register nodes
NODE_CLASS_MAPPINGS = {
    "QuickPersonBuilder": QuickPersonBuilder,
    "QuickOutfitBuilder": QuickOutfitBuilder,
    "QuickSceneBuilder": QuickSceneBuilder,
    "QuickPoseBuilder": QuickPoseBuilder,
    "QuickQualityBuilder": QuickQualityBuilder,
    "QuickNegativeBuilder": QuickNegativeBuilder,
    "PromptCombiner": PromptCombiner,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QuickPersonBuilder": "👤 Quick Person",
    "QuickOutfitBuilder": "👗 Quick Outfit",
    "QuickSceneBuilder": "🏠 Quick Scene",
    "QuickPoseBuilder": "🎭 Quick Pose",
    "QuickQualityBuilder": "⭐ Quick Quality",
    "QuickNegativeBuilder": "❌ Quick Negative",
    "PromptCombiner": "🔗 Prompt Combiner",
}
