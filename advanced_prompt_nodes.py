"""
Mason's Advanced Prompt Building Nodes for ComfyUI
Master-level prompt construction tools
"""

import random


class SceneBuilder:
    """Combine subject + setting + lighting + action into a complete scene"""
    
    SETTINGS = {
        "bedroom": "in a luxurious bedroom, silk sheets, soft ambient lighting",
        "studio": "in a professional photo studio, white backdrop, studio lighting",
        "outdoor": "outdoors, natural setting, golden hour sunlight",
        "bathroom": "in an elegant bathroom, marble surfaces, soft lighting",
        "pool": "by a swimming pool, water reflections, bright daylight",
        "office": "in a modern office, professional setting",
        "beach": "on a tropical beach, ocean waves, sunset lighting",
    }
    
    LIGHTING = {
        "soft": "soft diffused lighting, gentle shadows",
        "dramatic": "dramatic lighting, strong shadows, high contrast",
        "natural": "natural lighting, realistic illumination",
        "studio": "professional studio lighting, three-point setup",
        "golden_hour": "golden hour lighting, warm tones, long shadows",
        "neon": "neon lighting, vibrant colors, cyberpunk aesthetic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject": ("STRING", {"default": "beautiful woman", "multiline": True}),
                "setting": (list(cls.SETTINGS.keys()),),
                "lighting": (list(cls.LIGHTING.keys()),),
                "action": ("STRING", {"default": "posing confidently"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_prompt",)
    FUNCTION = "build_scene"
    CATEGORY = "Mason's Nodes/Advanced Prompts"

    def build_scene(self, subject, setting, lighting, action):
        setting_desc = self.SETTINGS.get(setting, "")
        lighting_desc = self.LIGHTING.get(lighting, "")
        prompt = f"{subject}, {action}, {setting_desc}, {lighting_desc}"
        return (prompt,)


class OutfitGenerator:
    """Generate random or specific outfit descriptions"""
    
    TOPS = ["crop top", "tank top", "bikini top", "lace bra", "button-up shirt", "sweater", "tube top", "sports bra", "corset"]
    BOTTOMS = ["shorts", "skirt", "jeans", "bikini bottom", "yoga pants", "miniskirt", "thong", "panties", "leggings"]
    ACCESSORIES = ["choker", "necklace", "earrings", "bracelet", "belly chain", "anklet", "hair accessories"]
    STYLES = ["casual", "elegant", "sporty", "seductive", "professional", "beach", "lingerie"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "style": (cls.STYLES,),
                "include_top": ("BOOLEAN", {"default": True}),
                "include_bottom": ("BOOLEAN", {"default": True}),
                "include_accessory": ("BOOLEAN", {"default": False}),
                "seed": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("outfit_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Advanced Prompts"

    def generate(self, style, include_top, include_bottom, include_accessory, seed):
        random.seed(seed)
        parts = []
        
        if include_top:
            parts.append(random.choice(self.TOPS))
        if include_bottom:
            parts.append(random.choice(self.BOTTOMS))
        if include_accessory:
            parts.append(random.choice(self.ACCESSORIES))
        
        outfit = ", ".join(parts) if parts else "nude"
        return (f"wearing {outfit}, {style} style",)


class ExpressionController:
    """Control facial expressions precisely"""
    
    EXPRESSIONS = {
        "neutral": "neutral expression, relaxed face",
        "smile": "gentle smile, happy expression",
        "seductive": "seductive expression, bedroom eyes, slight smirk",
        "sultry": "sultry look, half-lidded eyes, parted lips",
        "confident": "confident expression, direct gaze, slight smile",
        "playful": "playful expression, teasing smile, sparkling eyes",
        "intense": "intense gaze, focused expression, piercing eyes",
        "surprised": "surprised expression, wide eyes, open mouth",
        "laughing": "laughing, genuine smile, joyful expression",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "expression": (list(cls.EXPRESSIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt_with_expression",)
    FUNCTION = "add_expression"
    CATEGORY = "Mason's Nodes/Advanced Prompts"

    def add_expression(self, prompt, expression):
        expr_desc = self.EXPRESSIONS.get(expression, "")
        return (f"{prompt}, {expr_desc}",)


class LightingDirector:
    """Professional lighting setups"""
    
    SETUPS = {
        "rembrandt": "Rembrandt lighting, triangle shadow on cheek, dramatic, professional portrait lighting",
        "butterfly": "butterfly lighting, shadow under nose, glamour photography lighting",
        "split": "split lighting, half face illuminated, dramatic shadows, film noir style",
        "rim": "rim lighting, backlit, glowing edges, silhouette highlights",
        "high_key": "high key lighting, bright, minimal shadows, clean look",
        "low_key": "low key lighting, dark, dramatic shadows, moody atmosphere",
        "golden_hour": "golden hour lighting, warm orange tones, long soft shadows, magic hour",
        "blue_hour": "blue hour lighting, cool blue tones, twilight atmosphere",
        "window": "window light, soft natural lighting, gentle shadows, indoor natural light",
        "candlelight": "candlelight, warm flickering light, intimate atmosphere, soft glow",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "lighting_setup": (list(cls.SETUPS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lit_prompt",)
    FUNCTION = "apply_lighting"
    CATEGORY = "Mason's Nodes/Advanced Prompts"

    def apply_lighting(self, prompt, lighting_setup):
        lighting_desc = self.SETUPS.get(lighting_setup, "")
        return (f"{prompt}, {lighting_desc}",)


NODE_CLASS_MAPPINGS = {
    "SceneBuilder": SceneBuilder,
    "OutfitGenerator": OutfitGenerator,
    "ExpressionController": ExpressionController,
    "LightingDirector": LightingDirector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SceneBuilder": "🎬 Scene Builder",
    "OutfitGenerator": "👗 Outfit Generator",
    "ExpressionController": "😊 Expression Controller",
    "LightingDirector": "💡 Lighting Director",
}
