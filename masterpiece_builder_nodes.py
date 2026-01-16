"""
Mason Nodes - Masterpiece Builder
One-click complete scene generation with all elements combined
"""

class MasterpieceBuilder:
    """All-in-one masterpiece prompt generator with every detail."""
    
    SUBJECTS = {
        "Beautiful Woman": "beautiful woman, feminine, elegant, attractive, detailed face, perfect skin",
        "Handsome Man": "handsome man, masculine, attractive, detailed face, strong jawline",
        "Couple": "romantic couple, man and woman together, intimate, loving gaze",
        "Fantasy Character": "fantasy character, magical, ethereal, mystical aura",
        "Cyberpunk Character": "cyberpunk character, neon lights, futuristic, chrome accents",
        "Anime Girl": "anime girl, cute, beautiful, expressive eyes, anime style",
        "Anime Boy": "anime boy, handsome, detailed, anime style",
        "Goddess": "goddess, divine beauty, radiant, celestial, perfect",
        "Warrior": "warrior, battle-ready, fierce, powerful, armored",
        "Model": "professional model, stunning, photogenic, flawless",
    }
    
    AGES = {
        "Young Adult (20s)": "young adult, 20 years old, youthful, fresh",
        "Adult (30s)": "adult, 30 years old, mature beauty",
        "Mature (40s)": "mature, 40 years old, elegant, refined",
        "Teen (18-19)": "young, 18 years old, youthful",
    }
    
    BODY_TYPES = {
        "Slim": "slim figure, slender, graceful",
        "Athletic": "athletic build, toned, fit, muscular definition",
        "Curvy": "curvy figure, hourglass shape, voluptuous",
        "Petite": "petite, small frame, delicate",
        "Muscular": "muscular, defined muscles, powerful build",
        "Average": "average build, natural proportions",
    }
    
    SKIN_TONES = {
        "Fair/Pale": "fair skin, pale complexion, porcelain skin",
        "Light": "light skin, soft complexion",
        "Medium/Olive": "olive skin, medium complexion, warm undertones",
        "Tan": "tan skin, sun-kissed, golden complexion",
        "Brown": "brown skin, rich complexion, warm tones",
        "Dark": "dark skin, deep complexion, beautiful contrast",
    }
    
    HAIR_STYLES = {
        "Long Flowing": "long flowing hair, silky, wavy ends",
        "Short Bob": "short bob haircut, sleek, modern",
        "Pixie Cut": "pixie cut, short stylish hair",
        "Curly Long": "long curly hair, voluminous curls",
        "Straight Long": "long straight hair, sleek, shiny",
        "Ponytail": "hair in ponytail, neat, stylish",
        "Braided": "braided hair, intricate braids",
        "Messy/Tousled": "messy tousled hair, effortless, windswept",
        "Updo/Bun": "hair in elegant updo, sophisticated bun",
    }
    
    HAIR_COLORS = {
        "Blonde": "blonde hair, golden locks",
        "Brunette": "brunette hair, rich brown",
        "Black": "black hair, dark as night",
        "Red/Auburn": "red hair, auburn, fiery",
        "Platinum": "platinum blonde, silvery white",
        "Pink": "pink hair, vibrant, colorful",
        "Blue": "blue hair, striking, unique",
        "Purple": "purple hair, mystical, vibrant",
        "Ombre": "ombre hair, gradient color",
        "Silver/Grey": "silver grey hair, elegant, striking",
    }
    
    EYE_COLORS = {
        "Blue": "blue eyes, crystal clear, piercing",
        "Green": "green eyes, emerald, captivating",
        "Brown": "brown eyes, warm, expressive",
        "Hazel": "hazel eyes, multi-toned, unique",
        "Grey": "grey eyes, striking, mysterious",
        "Amber": "amber eyes, golden, intense",
        "Violet": "violet eyes, rare, mesmerizing",
        "Heterochromia": "heterochromia, different colored eyes",
    }
    
    EXPRESSIONS = {
        "Seductive": "seductive expression, bedroom eyes, alluring smile",
        "Confident": "confident expression, self-assured, powerful gaze",
        "Innocent": "innocent expression, pure, sweet smile",
        "Mysterious": "mysterious expression, enigmatic, subtle smile",
        "Happy/Joyful": "happy expression, bright smile, joyful",
        "Serious/Intense": "serious expression, intense gaze, focused",
        "Playful": "playful expression, mischievous smile, fun",
        "Sultry": "sultry expression, smoldering look, sensual",
        "Peaceful": "peaceful expression, serene, calm",
    }
    
    OUTFITS = {
        "Elegant Dress": "elegant flowing dress, formal, sophisticated",
        "Casual": "casual outfit, relaxed, comfortable clothes",
        "Lingerie": "sexy lingerie, lace, seductive",
        "Bikini": "bikini, swimwear, beach ready",
        "Fantasy Armor": "fantasy armor, ornate, magical",
        "Formal Suit": "formal suit, professional, sharp",
        "Cyberpunk": "cyberpunk outfit, neon accents, futuristic",
        "Traditional": "traditional clothing, cultural, elegant",
        "Athletic Wear": "athletic wear, sports outfit, fit",
        "Nude": "nude, naked, bare skin, artistic",
        "See-through": "see-through clothing, transparent fabric",
        "Leather": "leather outfit, edgy, bold",
        "Latex": "latex outfit, shiny, form-fitting",
    }
    
    SETTINGS = {
        "Studio": "professional studio, perfect lighting, clean background",
        "Beach": "beach setting, ocean waves, sand, sunset",
        "Forest": "forest setting, trees, nature, dappled sunlight",
        "City": "city backdrop, urban, skyscrapers",
        "Bedroom": "bedroom setting, intimate, soft lighting",
        "Fantasy World": "fantasy world, magical landscape, ethereal",
        "Cyberpunk City": "cyberpunk city, neon lights, rain, futuristic",
        "Outdoor Garden": "garden setting, flowers, nature, beautiful",
        "Night Club": "nightclub, neon lights, party atmosphere",
        "Luxury Interior": "luxury interior, opulent, rich decor",
        "Plain Background": "plain background, simple, focus on subject",
    }
    
    LIGHTING = {
        "Studio Professional": "professional studio lighting, softbox, perfect exposure",
        "Golden Hour": "golden hour lighting, warm sunlight, beautiful shadows",
        "Dramatic": "dramatic lighting, high contrast, deep shadows",
        "Soft/Diffused": "soft diffused lighting, gentle, flattering",
        "Neon/Cyberpunk": "neon lighting, colorful, cyberpunk atmosphere",
        "Natural": "natural lighting, realistic, outdoor light",
        "Cinematic": "cinematic lighting, movie-like, professional",
        "Rim Light": "rim lighting, backlit, glowing edges",
        "Low Key": "low key lighting, dark, moody, mysterious",
        "High Key": "high key lighting, bright, minimal shadows",
    }
    
    CAMERA = {
        "Portrait": "portrait shot, head and shoulders, intimate",
        "Full Body": "full body shot, head to toe, complete view",
        "Close-up Face": "close-up face shot, detailed features",
        "Medium Shot": "medium shot, waist up",
        "3/4 View": "three quarter view, angled perspective",
        "From Above": "shot from above, looking down",
        "From Below": "shot from below, looking up, powerful",
        "Side Profile": "side profile, silhouette angle",
        "Dutch Angle": "dutch angle, tilted frame, dynamic",
    }
    
    QUALITY = {
        "Ultra": "masterpiece, best quality, ultra detailed, 8k uhd, photorealistic, professional photography, intricate details, sharp focus",
        "High": "masterpiece, best quality, highly detailed, sharp focus, professional",
        "Standard": "high quality, detailed, good composition",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject": (list(cls.SUBJECTS.keys()), {"default": "Beautiful Woman"}),
                "age": (list(cls.AGES.keys()), {"default": "Young Adult (20s)"}),
                "body_type": (list(cls.BODY_TYPES.keys()), {"default": "Athletic"}),
                "skin_tone": (list(cls.SKIN_TONES.keys()), {"default": "Fair/Pale"}),
                "hair_style": (list(cls.HAIR_STYLES.keys()), {"default": "Long Flowing"}),
                "hair_color": (list(cls.HAIR_COLORS.keys()), {"default": "Blonde"}),
                "eye_color": (list(cls.EYE_COLORS.keys()), {"default": "Blue"}),
                "expression": (list(cls.EXPRESSIONS.keys()), {"default": "Confident"}),
                "outfit": (list(cls.OUTFITS.keys()), {"default": "Elegant Dress"}),
                "setting": (list(cls.SETTINGS.keys()), {"default": "Studio"}),
                "lighting": (list(cls.LIGHTING.keys()), {"default": "Studio Professional"}),
                "camera": (list(cls.CAMERA.keys()), {"default": "Portrait"}),
                "quality": (list(cls.QUALITY.keys()), {"default": "Ultra"}),
            },
            "optional": {
                "additional_details": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("masterpiece_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason/Masterpiece"
    
    def build(self, subject, age, body_type, skin_tone, hair_style, hair_color, 
              eye_color, expression, outfit, setting, lighting, camera, quality, 
              additional_details=""):
        
        parts = [
            self.QUALITY[quality],
            self.SUBJECTS[subject],
            self.AGES[age],
            self.BODY_TYPES[body_type],
            self.SKIN_TONES[skin_tone],
            self.HAIR_STYLES[hair_style],
            self.HAIR_COLORS[hair_color],
            self.EYE_COLORS[eye_color],
            self.EXPRESSIONS[expression],
            self.OUTFITS[outfit],
            self.CAMERA[camera],
            self.SETTINGS[setting],
            self.LIGHTING[lighting],
        ]
        
        if additional_details.strip():
            parts.append(additional_details.strip())
        
        return (", ".join(parts),)


class MasterpieceNegative:
    """Comprehensive negative prompt for masterpiece quality."""
    
    LEVELS = {
        "Standard": "worst quality, low quality, blurry, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, watermark, text, signature",
        "Comprehensive": "worst quality, low quality, normal quality, blurry, bad anatomy, bad proportions, bad hands, missing fingers, extra fingers, fused fingers, too many fingers, extra limbs, missing limbs, deformed, disfigured, mutated, ugly, duplicate, morbid, mutilated, poorly drawn face, extra legs, extra arms, cloned face, gross proportions, malformed limbs, missing arms, missing legs, extra digit, fewer digits, cropped, worst face, watermark, username, text, signature, jpeg artifacts, grainy, pixelated",
        "NSFW Safe": "worst quality, low quality, blurry, bad anatomy, bad hands, censored, mosaic, bar censor, pixelated genitals, deformed genitals, unrealistic body, broken anatomy, extra limbs, missing limbs, watermark, text, ugly face, disfigured",
        "Photorealistic": "cartoon, anime, illustration, painting, drawing, art, sketch, 3d render, cgi, worst quality, low quality, blurry, bad anatomy, unrealistic, plastic skin, uncanny valley",
        "Anime": "realistic, photorealistic, photo, 3d, worst quality, low quality, bad anatomy, bad proportions, extra limbs, missing limbs, deformed",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "level": (list(cls.LEVELS.keys()), {"default": "Comprehensive"}),
            },
            "optional": {
                "additional_negatives": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason/Masterpiece"
    
    def generate(self, level, additional_negatives=""):
        neg = self.LEVELS[level]
        if additional_negatives.strip():
            neg += ", " + additional_negatives.strip()
        return (neg,)


NODE_CLASS_MAPPINGS = {
    "MasonMasterpieceBuilder": MasterpieceBuilder,
    "MasonMasterpieceNegative": MasterpieceNegative,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonMasterpieceBuilder": "🎨 Masterpiece Builder (All-in-One)",
    "MasonMasterpieceNegative": "🚫 Masterpiece Negative Prompt",
}
