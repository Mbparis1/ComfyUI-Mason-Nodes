"""
Mason's Color Science Nodes for ComfyUI
Professional color control - SD 1.5 optimized
"""


class ColorHarmonyController:
    """Apply color theory harmonies"""
    
    HARMONIES = {
        "complementary": "complementary color scheme, opposite colors, high contrast colors, vibrant",
        "analogous": "analogous color scheme, neighboring colors, harmonious, cohesive palette",
        "triadic": "triadic color scheme, three colors evenly spaced, balanced, dynamic",
        "split_complementary": "split complementary colors, nuanced contrast, sophisticated palette",
        "monochromatic": "monochromatic color scheme, single color variations, unified, elegant",
        "warm": "warm color palette, reds oranges yellows, cozy warm tones",
        "cool": "cool color palette, blues greens purples, calm cool tones",
        "neutral": "neutral color palette, earth tones, beiges grays, understated",
        "pastel": "pastel color palette, soft muted colors, gentle tones, dreamy",
        "vibrant": "vibrant color palette, saturated colors, bold bright, eye-catching",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "harmony": (list(cls.HARMONIES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("color_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Color Science"

    def apply(self, prompt, harmony):
        h = self.HARMONIES.get(harmony, "")
        return (f"{prompt}, {h}",)


class SkinToneEnhancer:
    """Professional skin tone control"""
    
    UNDERTONES = {
        "warm": "warm skin undertone, golden undertones, yellow-based skin",
        "cool": "cool skin undertone, pink undertones, blue-based skin",
        "neutral": "neutral skin undertone, balanced undertones, olive undertones",
        "olive": "olive skin undertone, greenish undertone, mediterranean",
    }
    
    WARMTH = {
        "pale": "pale skin, fair complexion, porcelain, very light skin",
        "light": "light skin, fair skin, light complexion",
        "medium": "medium skin tone, tan, warm brown, golden brown",
        "tan": "tanned skin, sun-kissed, bronzed skin, beach tan",
        "deep": "deep skin tone, dark skin, rich brown, dark complexion",
        "ebony": "ebony skin, very dark skin, deep black skin, rich dark",
    }
    
    FLUSH = {
        "none": "",
        "subtle": "subtle skin flush, hint of color in cheeks",
        "healthy": "healthy flush, rosy cheeks, blood circulation visible",
        "flushed": "flushed skin, blushing, pink cheeks, aroused flush",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "undertone": (list(cls.UNDERTONES.keys()),),
                "warmth": (list(cls.WARMTH.keys()),),
                "flush": (list(cls.FLUSH.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("skin_tone_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Color Science"

    def apply(self, prompt, undertone, warmth, flush):
        u = self.UNDERTONES.get(undertone, "")
        w = self.WARMTH.get(warmth, "")
        f = self.FLUSH.get(flush, "")
        if f:
            return (f"{prompt}, {u}, {w}, {f}",)
        return (f"{prompt}, {u}, {w}",)


class ShadowColorController:
    """Control shadow color temperature"""
    
    SHADOW_COLOR = {
        "neutral": "neutral shadows, gray shadows, balanced shadow color",
        "warm": "warm shadows, orange-tinted shadows, golden shadow areas",
        "cool": "cool shadows, blue-tinted shadows, purple shadow areas",
        "magenta": "magenta shadows, pink-tinted shadow areas, fashion shadows",
        "teal": "teal shadows, cyan-tinted shadows, cinematic shadows",
    }
    
    SHADOW_DENSITY = {
        "transparent": "transparent shadows, light shadows, airy",
        "subtle": "subtle shadows, soft shadow density",
        "moderate": "moderate shadows, balanced darkness",
        "deep": "deep shadows, dark shadow areas, rich blacks",
        "crushed": "crushed blacks, very deep shadows, lost shadow detail",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "shadow_color": (list(cls.SHADOW_COLOR.keys()),),
                "density": (list(cls.SHADOW_DENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("shadow_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Color Science"

    def apply(self, prompt, shadow_color, density):
        sc = self.SHADOW_COLOR.get(shadow_color, "")
        d = self.SHADOW_DENSITY.get(density, "")
        return (f"{prompt}, {sc}, {d}",)


class HighlightController:
    """Control highlight characteristics"""
    
    HIGHLIGHT_COLOR = {
        "neutral": "neutral highlights, white highlights, clean specular",
        "warm": "warm highlights, golden highlights, orange specular",
        "cool": "cool highlights, blue highlights, cold specular",
        "creamy": "creamy highlights, soft warm specular, beauty lighting",
    }
    
    HIGHLIGHT_INTENSITY = {
        "subtle": "subtle highlights, soft specular, gentle shine",
        "moderate": "moderate highlights, balanced specular",
        "bright": "bright highlights, strong specular, shiny",
        "blown": "blown highlights, very bright specular, overexposed highlights",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "highlight_color": (list(cls.HIGHLIGHT_COLOR.keys()),),
                "intensity": (list(cls.HIGHLIGHT_INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("highlight_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Color Science"

    def apply(self, prompt, highlight_color, intensity):
        hc = self.HIGHLIGHT_COLOR.get(highlight_color, "")
        i = self.HIGHLIGHT_INTENSITY.get(intensity, "")
        return (f"{prompt}, {hc}, {i}",)


class ColorGradingPro:
    """Professional color grading looks"""
    
    GRADES = {
        "natural": "natural color grading, realistic colors, no color cast",
        "cinematic_teal_orange": "cinematic color grading, teal and orange, blockbuster look",
        "cinematic_blue": "cinematic blue color grade, cold movie look, thriller aesthetic",
        "vintage_warm": "vintage warm color grade, nostalgic, faded warm tones",
        "vintage_cool": "vintage cool color grade, retro cool, faded cool tones",
        "fashion_pink": "fashion color grade, pink tones, editorial look",
        "moody_dark": "moody dark color grade, desaturated, dark aesthetic",
        "bright_airy": "bright airy color grade, lifted shadows, light and airy",
        "golden_hour": "golden hour color grade, warm golden tones, sunset colors",
        "moonlit": "moonlit color grade, blue silver tones, night aesthetic",
        "noir": "noir color grade, high contrast black and white tones, film noir",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "grade": (list(cls.GRADES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("grading_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Color Science"

    def apply(self, prompt, grade):
        g = self.GRADES.get(grade, "")
        return (f"{prompt}, {g}",)


class SaturationController:
    """Precise saturation control"""
    
    SATURATION = {
        "desaturated": "desaturated, muted colors, low saturation, faded",
        "subtle": "subtle saturation, slightly muted, gentle colors",
        "natural": "natural saturation, realistic color intensity",
        "vibrant": "vibrant colors, saturated, punchy colors, colorful",
        "hyper_saturated": "hyper saturated, extremely colorful, intense colors",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "saturation": (list(cls.SATURATION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("saturation_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Color Science"

    def apply(self, prompt, saturation):
        s = self.SATURATION.get(saturation, "")
        return (f"{prompt}, {s}",)


NODE_CLASS_MAPPINGS = {
    "ColorHarmonyController": ColorHarmonyController,
    "SkinToneEnhancer": SkinToneEnhancer,
    "ShadowColorController": ShadowColorController,
    "HighlightController": HighlightController,
    "ColorGradingPro": ColorGradingPro,
    "SaturationController": SaturationController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ColorHarmonyController": "🎨 Color Harmony",
    "SkinToneEnhancer": "🧑 Skin Tone Enhancer",
    "ShadowColorController": "🌑 Shadow Color",
    "HighlightController": "✨ Highlight Controller",
    "ColorGradingPro": "🎬 Color Grading Pro",
    "SaturationController": "🌈 Saturation Controller",
}
