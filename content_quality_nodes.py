"""
Mason's Content Quality Nodes for ComfyUI
Anatomy, consistency, and quality enhancement tools
"""

import random


class AnatomyValidator:
    """Add keywords to enforce correct proportions"""
    
    ANATOMY_FIXES = {
        "hands": "correct hand anatomy, five fingers per hand, proper finger proportions, natural hand pose",
        "face": "symmetrical face, correct facial proportions, natural features, proper eye spacing",
        "body": "correct body proportions, anatomically correct, natural body shape, proper limb lengths",
        "feet": "correct foot anatomy, proper toe count, natural feet, accurate foot proportions",
        "eyes": "both eyes same size, correct eye anatomy, natural eye shape, proper iris size",
        "all": "anatomically correct, proper proportions, symmetrical features, correct anatomy, five fingers, natural body",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "focus_area": (list(cls.ANATOMY_FIXES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("validated_prompt",)
    FUNCTION = "validate"
    CATEGORY = "Mason's Nodes/Content Quality"

    def validate(self, prompt, focus_area):
        fix = self.ANATOMY_FIXES.get(focus_area, "")
        return (f"{prompt}, {fix}",)


class SkinToneMatcher:
    """Ensure consistent skin tone"""
    
    SKIN_TONES = {
        "fair": "fair skin, pale complexion, light skin tone, porcelain skin",
        "light": "light skin, cream complexion, light tan",
        "medium": "medium skin tone, olive complexion, warm skin",
        "tan": "tanned skin, sun-kissed complexion, golden tan",
        "brown": "brown skin, warm brown complexion, rich skin tone",
        "dark": "dark skin, deep brown complexion, dark skin tone",
        "ebony": "ebony skin, very dark complexion, deep dark skin",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "skin_tone": (list(cls.SKIN_TONES.keys()),),
                "add_quality": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("toned_prompt",)
    FUNCTION = "match"
    CATEGORY = "Mason's Nodes/Content Quality"

    def match(self, prompt, skin_tone, add_quality):
        tone_desc = self.SKIN_TONES.get(skin_tone, "")
        if add_quality:
            tone_desc += ", realistic skin texture, natural skin details, pores, subtle skin imperfections"
        return (f"{prompt}, {tone_desc}",)


class BackgroundConsistency:
    """Lock background while subject changes"""
    
    BACKGROUNDS = {
        "studio_white": "white studio background, clean backdrop, professional photography studio",
        "studio_gray": "gray studio background, neutral backdrop, photography studio",
        "studio_black": "black studio background, dark backdrop, dramatic studio",
        "bedroom": "bedroom background, bed visible, indoor domestic setting",
        "outdoor_nature": "outdoor nature background, trees, natural setting, daylight",
        "beach": "beach background, sand, ocean, tropical setting",
        "bathroom": "bathroom setting, tiles, mirror, indoor",
        "pool": "poolside background, water, outdoor leisure setting",
        "blur": "blurred background, bokeh, shallow depth of field, subject focus",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "background": (list(cls.BACKGROUNDS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("bg_prompt",)
    FUNCTION = "set_background"
    CATEGORY = "Mason's Nodes/Content Quality"

    def set_background(self, prompt, background):
        bg_desc = self.BACKGROUNDS.get(background, "")
        return (f"{prompt}, {bg_desc}",)


class DetailFocusZones:
    """Boost detail on specific body regions"""
    
    ZONES = {
        "face": "highly detailed face, intricate facial features, sharp facial details",
        "eyes": "detailed eyes, expressive eyes, sharp eye detail, beautiful eyes",
        "body": "detailed body, defined muscles, skin texture, body definition",
        "hands": "detailed hands, sharp hand details, realistic hands",
        "hair": "detailed hair, individual strands visible, hair texture, flowing hair",
        "skin": "detailed skin, pores visible, realistic skin texture, skin imperfections",
        "clothing": "detailed clothing, fabric texture, cloth folds, clothing details",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "primary_zone": (list(cls.ZONES.keys()),),
                "secondary_zone": (["none"] + list(cls.ZONES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("detailed_prompt",)
    FUNCTION = "focus"
    CATEGORY = "Mason's Nodes/Content Quality"

    def focus(self, prompt, primary_zone, secondary_zone):
        details = self.ZONES.get(primary_zone, "")
        if secondary_zone != "none":
            details += ", " + self.ZONES.get(secondary_zone, "")
        return (f"{prompt}, {details}",)


class AgeController:
    """Fine-tune apparent age"""
    
    AGES = {
        "16-20": "young adult, late teens, youthful appearance, fresh face, early twenties",
        "21-25": "early twenties, young adult, youthful, mid-twenties",
        "26-30": "mid to late twenties, young adult, prime age, late twenties",
        "31-35": "early thirties, mature young adult, established adult",
        "36-40": "mid thirties to forty, mature adult, experienced look",
        "41-50": "forties, mature, distinguished, middle-aged",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "age_range": (list(cls.AGES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("aged_prompt",)
    FUNCTION = "set_age"
    CATEGORY = "Mason's Nodes/Content Quality"

    def set_age(self, prompt, age_range):
        age_desc = self.AGES.get(age_range, "")
        return (f"{prompt}, {age_desc}",)


class BodyTypeSelector:
    """Select body type presets"""
    
    BODY_TYPES = {
        "slim": "slim body, slender figure, thin waist, lean build",
        "athletic": "athletic body, toned muscles, fit physique, defined abs, sporty build",
        "curvy": "curvy body, hourglass figure, full curves, shapely",
        "petite": "petite body, small frame, delicate build, compact figure",
        "tall_slim": "tall and slim, long legs, elongated figure, model proportions",
        "muscular": "muscular body, defined muscles, strong build, powerful physique",
        "voluptuous": "voluptuous body, full figure, generous curves, ample proportions",
        "average": "average body type, normal proportions, natural figure",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "body_type": (list(cls.BODY_TYPES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("body_prompt",)
    FUNCTION = "select"
    CATEGORY = "Mason's Nodes/Content Quality"

    def select(self, prompt, body_type):
        body_desc = self.BODY_TYPES.get(body_type, "")
        return (f"{prompt}, {body_desc}",)


NODE_CLASS_MAPPINGS = {
    "AnatomyValidator": AnatomyValidator,
    "SkinToneMatcher": SkinToneMatcher,
    "BackgroundConsistency": BackgroundConsistency,
    "DetailFocusZones": DetailFocusZones,
    "AgeController": AgeController,
    "BodyTypeSelector": BodyTypeSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnatomyValidator": "🦴 Anatomy Validator",
    "SkinToneMatcher": "🎨 Skin Tone Matcher",
    "BackgroundConsistency": "🖼️ Background Consistency",
    "DetailFocusZones": "🔍 Detail Focus Zones",
    "AgeController": "📅 Age Controller",
    "BodyTypeSelector": "�� Body Type Selector",
}
