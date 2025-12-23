"""
Mason's Artistic Style Nodes for ComfyUI
Replace style LoRAs with prompt engineering - SD 1.5 optimized
"""


class RenderStyleController:
    """Control overall render style"""
    
    STYLES = {
        "photorealistic": "photorealistic, photo, realistic, photograph, real life",
        "hyperrealistic": "hyperrealistic, ultra realistic, extremely detailed photograph",
        "cinematic": "cinematic, movie still, film scene, blockbuster movie look",
        "oil_painting": "oil painting, painted, traditional art, brush strokes visible",
        "watercolor": "watercolor painting, watercolor art, soft washes, delicate colors",
        "digital_art": "digital art, digital painting, concept art, artstation style",
        "3d_render": "3D render, CGI, rendered, octane render, unreal engine",
        "anime": "anime style, anime art, Japanese animation, cel shaded",
        "manga": "manga style, black and white manga, Japanese comic art",
        "illustration": "illustration, illustrated, book illustration, editorial art",
        "sketch": "sketch, pencil drawing, graphite, hand-drawn",
        "charcoal": "charcoal drawing, charcoal art, dramatic contrast, smudged",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.STYLES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("style_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Artistic Style"

    def apply(self, prompt, style):
        s = self.STYLES.get(style, "")
        return (f"{prompt}, {s}",)


class ArtMovementController:
    """Apply art movement styles"""
    
    MOVEMENTS = {
        "renaissance": "Renaissance art style, classical painting, old master technique",
        "baroque": "Baroque art style, dramatic light, chiaroscuro, Caravaggio style",
        "impressionist": "Impressionist style, visible brushwork, light focus, Monet style",
        "expressionist": "Expressionist style, emotional, bold colors, distorted",
        "art_nouveau": "Art Nouveau style, flowing lines, organic forms, decorative",
        "art_deco": "Art Deco style, geometric, glamorous, 1920s aesthetic",
        "pop_art": "Pop Art style, bold colors, comic style, Warhol inspired",
        "surrealist": "Surrealist style, dreamlike, Dali inspired, impossible imagery",
        "minimalist": "Minimalist style, clean, simple, essential elements only",
        "abstract": "Abstract art style, non-representational, geometric shapes",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "movement": (list(cls.MOVEMENTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("movement_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Artistic Style"

    def apply(self, prompt, movement):
        m = self.MOVEMENTS.get(movement, "")
        return (f"{prompt}, {m}",)


class ColorPaletteController:
    """Control color palette and scheme"""
    
    PALETTES = {
        "warm": "warm color palette, orange red yellow, warm tones, cozy colors",
        "cool": "cool color palette, blue green purple, cool tones, calming colors",
        "neutral": "neutral color palette, beige gray brown, muted colors, earth tones",
        "vibrant": "vibrant colors, saturated, bold colors, punchy, eye-catching",
        "muted": "muted colors, desaturated, soft colors, subtle palette",
        "pastel": "pastel colors, soft light colors, gentle hues, dreamy palette",
        "neon": "neon colors, fluorescent, bright glow, cyberpunk colors",
        "monochrome": "monochromatic, single color palette, tonal, cohesive",
        "complementary": "complementary colors, contrasting palette, color theory",
        "analogous": "analogous colors, harmonious palette, related hues",
        "earthy": "earthy colors, natural tones, organic palette, nature inspired",
        "jewel_tones": "jewel tone colors, rich saturated, ruby emerald sapphire",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "palette": (list(cls.PALETTES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("palette_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Artistic Style"

    def apply(self, prompt, palette):
        p = self.PALETTES.get(palette, "")
        return (f"{prompt}, {p}",)


class ContrastStyleController:
    """Control image contrast style"""
    
    CONTRASTS = {
        "flat": "flat contrast, low contrast, soft shadows, even lighting",
        "low_key": "low key lighting, mostly dark, dramatic shadows, noir",
        "high_key": "high key lighting, bright, minimal shadows, airy",
        "normal": "normal contrast, balanced light and shadow",
        "high_contrast": "high contrast, strong shadows, bright highlights",
        "hdr": "HDR style, extreme dynamic range, tone mapped, surreal",
        "silhouette": "silhouette, backlit, dark figure, bright background",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "contrast": (list(cls.CONTRASTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("contrast_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Artistic Style"

    def apply(self, prompt, contrast):
        c = self.CONTRASTS.get(contrast, "")
        return (f"{prompt}, {c}",)


class DetailLevelController:
    """Control level of detail in image"""
    
    DETAILS = {
        "soft_dreamy": "soft focus, dreamy, ethereal, gauzy, romantic blur",
        "soft": "soft details, gentle, slight blur, diffused",
        "natural": "natural level of detail, realistic sharpness",
        "sharp": "sharp details, crisp, well-defined edges",
        "very_sharp": "very sharp, ultra detailed, crisp edges, tack sharp",
        "hyper_detailed": "hyper detailed, intricate details, extreme resolution, microscopic detail",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "detail": (list(cls.DETAILS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("detail_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Artistic Style"

    def apply(self, prompt, detail):
        d = self.DETAILS.get(detail, "")
        return (f"{prompt}, {d}",)


class AnimeRealisticBlender:
    """Blend between anime and realistic styles"""
    
    BLENDS = {
        "pure_anime": "anime style, cel shaded, 2D animation, Japanese animation, flat colors",
        "mostly_anime": "semi-realistic anime, detailed anime, anime with realistic shading",
        "anime_leaning": "anime-influenced, stylized realistic, large eyes, anime proportions",
        "balanced": "semi-realistic, stylized, between anime and realistic, mixed style",
        "realistic_leaning": "realistic with anime influence, slight stylization, natural proportions",
        "mostly_realistic": "realistic style, subtle anime influence, photographic with style",
        "pure_realistic": "photorealistic, real person, photograph, no stylization",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "blend": (list(cls.BLENDS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("blend_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Artistic Style"

    def apply(self, prompt, blend):
        b = self.BLENDS.get(blend, "")
        return (f"{prompt}, {b}",)


NODE_CLASS_MAPPINGS = {
    "RenderStyleController": RenderStyleController,
    "ArtMovementController": ArtMovementController,
    "ColorPaletteController": ColorPaletteController,
    "ContrastStyleController": ContrastStyleController,
    "DetailLevelController": DetailLevelController,
    "AnimeRealisticBlender": AnimeRealisticBlender,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RenderStyleController": "🎨 Render Style",
    "ArtMovementController": "🖼️ Art Movement",
    "ColorPaletteController": "🌈 Color Palette",
    "ContrastStyleController": "⚫ Contrast Style",
    "DetailLevelController": "🔍 Detail Level",
    "AnimeRealisticBlender": "🎭 Anime/Realistic Blend",
}
