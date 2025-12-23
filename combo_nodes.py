"""
Mason's Combo/Quick Setup Nodes for ComfyUI
All-in-one configuration nodes for fast setup - SD 1.5 optimized
"""

import random


class QuickPortraitSetup:
    """All-in-one portrait configuration"""
    
    GENDER = ["female", "male"]
    ETHNICITY = ["caucasian", "asian", "african", "latina", "mixed"]
    AGE_RANGE = ["young_adult", "adult", "mature"]
    STYLE = ["natural", "glamour", "artistic", "casual"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "gender": (cls.GENDER,),
                "ethnicity": (cls.ETHNICITY,),
                "age_range": (cls.AGE_RANGE,),
                "style": (cls.STYLE,),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Combo Setups"

    def build(self, gender, ethnicity, age_range, style):
        # Gender
        if gender == "female":
            base = "beautiful woman, female"
        else:
            base = "handsome man, male"
        
        # Ethnicity
        eth_map = {
            "caucasian": "caucasian, european features",
            "asian": "asian, east asian features",
            "african": "african american, dark skin",
            "latina": "latina, hispanic features",
            "mixed": "mixed ethnicity, unique features",
        }
        
        # Age
        age_map = {
            "young_adult": "young adult, youthful, early twenties",
            "adult": "adult, mid-twenties to thirties",
            "mature": "mature adult, distinguished",
        }
        
        # Style
        style_map = {
            "natural": "natural beauty, minimal makeup, authentic, candid portrait",
            "glamour": "glamour photography, professional makeup, styled hair, polished",
            "artistic": "artistic portrait, creative lighting, dramatic, editorial",
            "casual": "casual portrait, relaxed, everyday look, natural lighting",
        }
        
        positive = f"{base}, {eth_map.get(ethnicity, '')}, {age_map.get(age_range, '')}, {style_map.get(style, '')}, portrait, close-up, detailed face, sharp focus, high quality, photorealistic"
        
        negative = "bad anatomy, deformed face, ugly, blurry, low quality, watermark, text, bad eyes, crossed eyes, extra fingers, missing fingers, bad hands"
        
        return (positive, negative)


class QuickFullBodySetup:
    """All-in-one full body configuration"""
    
    GENDER = ["female", "male"]
    BODY_TYPE = ["slim", "athletic", "curvy", "petite", "average"]
    POSE = ["standing", "sitting", "lying", "walking", "dynamic"]
    OUTFIT = ["casual", "elegant", "sporty", "swimwear", "lingerie", "nude"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "gender": (cls.GENDER,),
                "body_type": (cls.BODY_TYPE,),
                "pose": (cls.POSE,),
                "outfit": (cls.OUTFIT,),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Combo Setups"

    def build(self, gender, body_type, pose, outfit):
        if gender == "female":
            base = "beautiful woman, female"
        else:
            base = "handsome man, male"
        
        body_map = {
            "slim": "slim body, slender figure",
            "athletic": "athletic body, toned, fit",
            "curvy": "curvy body, hourglass figure",
            "petite": "petite body, small frame",
            "average": "average body type, natural proportions",
        }
        
        pose_map = {
            "standing": "standing pose, full body visible",
            "sitting": "sitting pose, seated",
            "lying": "lying down, reclined",
            "walking": "walking, mid-stride, natural movement",
            "dynamic": "dynamic pose, action, movement",
        }
        
        outfit_map = {
            "casual": "casual clothing, everyday outfit",
            "elegant": "elegant dress, formal attire, sophisticated",
            "sporty": "athletic wear, sports outfit, activewear",
            "swimwear": "swimwear, bikini, swimsuit",
            "lingerie": "lingerie, underwear, intimate apparel",
            "nude": "nude, naked, unclothed, bare skin",
        }
        
        positive = f"{base}, {body_map.get(body_type, '')}, {pose_map.get(pose, '')}, {outfit_map.get(outfit, '')}, full body shot, high quality, photorealistic, detailed"
        
        negative = "bad anatomy, deformed body, extra limbs, missing limbs, bad hands, extra fingers, bad face, ugly, blurry, low quality, watermark"
        
        return (positive, negative)


class QuickNSFWSetup:
    """All-in-one NSFW configuration - use responsibly"""
    
    GENDER = ["female", "male"]
    BODY_TYPE = ["slim", "athletic", "curvy", "petite", "voluptuous"]
    POSE_TYPE = ["standing", "sitting", "lying", "kneeling", "sensual"]
    CLOTHING = ["lingerie", "partial", "nude"]
    MOOD = ["seductive", "playful", "intimate", "artistic", "natural"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "gender": (cls.GENDER,),
                "body_type": (cls.BODY_TYPE,),
                "pose_type": (cls.POSE_TYPE,),
                "clothing": (cls.CLOTHING,),
                "mood": (cls.MOOD,),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Combo Setups"

    def build(self, gender, body_type, pose_type, clothing, mood):
        if gender == "female":
            base = "beautiful woman, female, attractive"
        else:
            base = "handsome man, male, attractive"
        
        body_map = {
            "slim": "slim body, slender, thin waist",
            "athletic": "athletic body, toned muscles, fit physique",
            "curvy": "curvy body, hourglass figure, full curves",
            "petite": "petite body, small frame, delicate",
            "voluptuous": "voluptuous body, full figure, generous curves",
        }
        
        pose_map = {
            "standing": "standing pose, confident stance",
            "sitting": "sitting pose, legs shown",
            "lying": "lying down, reclined on bed",
            "kneeling": "kneeling pose, on knees",
            "sensual": "sensual pose, alluring position",
        }
        
        clothing_map = {
            "lingerie": "wearing lingerie, lace underwear, bra and panties",
            "partial": "partially clothed, clothing slipping, revealing",
            "nude": "nude, naked, bare skin, unclothed",
        }
        
        mood_map = {
            "seductive": "seductive expression, bedroom eyes, alluring",
            "playful": "playful mood, teasing, fun expression",
            "intimate": "intimate mood, soft, romantic atmosphere",
            "artistic": "artistic nude, tasteful, fine art style",
            "natural": "natural look, candid, authentic beauty",
        }
        
        positive = f"{base}, {body_map.get(body_type, '')}, {pose_map.get(pose_type, '')}, {clothing_map.get(clothing, '')}, {mood_map.get(mood, '')}, beautiful skin, detailed body, high quality, photorealistic"
        
        negative = "bad anatomy, deformed body, ugly, extra limbs, missing limbs, bad hands, extra fingers, missing fingers, bad face, crossed eyes, low quality, blurry, watermark, text"
        
        return (positive, negative)


class RandomCharacterGenerator:
    """Generate random character descriptions"""
    
    GENDERS = ["female", "male"]
    ETHNICITIES = ["caucasian", "asian_east", "asian_south", "african", "latina", "middle_eastern", "mixed"]
    BODY_TYPES = ["slim", "athletic", "curvy", "petite", "average", "muscular"]
    HAIR_COLORS = ["blonde", "brunette", "black", "red", "auburn", "platinum"]
    HAIR_STYLES = ["long_straight", "long_wavy", "short", "ponytail", "bun", "braids"]
    EYE_COLORS = ["blue", "green", "brown", "hazel", "gray"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "gender": (["random"] + cls.GENDERS,),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("character_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Combo Setups"

    def generate(self, seed, gender):
        random.seed(seed)
        
        if gender == "random":
            gender = random.choice(self.GENDERS)
        
        ethnicity = random.choice(self.ETHNICITIES)
        body_type = random.choice(self.BODY_TYPES)
        hair_color = random.choice(self.HAIR_COLORS)
        hair_style = random.choice(self.HAIR_STYLES)
        eye_color = random.choice(self.EYE_COLORS)
        
        if gender == "female":
            base = "beautiful woman, female"
        else:
            base = "handsome man, male"
        
        prompt = f"{base}, {ethnicity} ethnicity, {body_type} body type, {hair_color} {hair_style.replace('_', ' ')} hair, {eye_color} eyes"
        
        return (prompt,)


NODE_CLASS_MAPPINGS = {
    "QuickPortraitSetup": QuickPortraitSetup,
    "QuickFullBodySetup": QuickFullBodySetup,
    "QuickNSFWSetup": QuickNSFWSetup,
    "RandomCharacterGenerator": RandomCharacterGenerator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QuickPortraitSetup": "⚡ Quick Portrait Setup",
    "QuickFullBodySetup": "⚡ Quick Full Body Setup",
    "QuickNSFWSetup": "⚡ Quick NSFW Setup",
    "RandomCharacterGenerator": "🎲 Random Character Generator",
}
