"""
Mason's Micro Detail Nodes for ComfyUI
Fine-grained control over small but important details - SD 1.5 optimized
"""


class EyelashController:
    """Control eyelash appearance - often overlooked but important"""
    
    LASH_LENGTH = {
        "natural": "natural eyelashes, normal lash length",
        "long": "long eyelashes, extended lashes, dramatic lashes",
        "very_long": "very long eyelashes, extreme lash length, doll-like lashes",
    }
    
    LASH_STYLE = {
        "natural": "natural lashes, no mascara",
        "mascara": "mascara, darkened lashes, defined lashes",
        "false_lashes": "false eyelashes, fake lashes, glamour lashes",
        "wispy": "wispy lashes, feathery lash extensions",
        "dramatic": "dramatic lashes, thick voluminous lashes",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "length": (list(cls.LASH_LENGTH.keys()),),
                "style": (list(cls.LASH_STYLE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lash_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Micro Details"

    def apply(self, prompt, length, style):
        l = self.LASH_LENGTH.get(length, "")
        s = self.LASH_STYLE.get(style, "")
        return (f"{prompt}, {l}, {s}",)


class LipMoistureController:
    """Control lip glossiness and moisture"""
    
    MOISTURE = {
        "matte": "matte lips, no shine, flat lip color",
        "satin": "satin lips, slight sheen, natural moisture",
        "glossy": "glossy lips, lip gloss, shiny lips, wet looking lips",
        "wet": "wet lips, very glossy, dripping gloss, just licked lips",
    }
    
    LIP_COLOR_INTENSITY = {
        "natural": "natural lip color, nude lips",
        "tinted": "tinted lips, subtle color, soft wash",
        "bold": "bold lip color, saturated, statement lips",
        "deep": "deep lip color, dark lips, rich pigment",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "moisture": (list(cls.MOISTURE.keys()),),
                "color_intensity": (list(cls.LIP_COLOR_INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lip_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Micro Details"

    def apply(self, prompt, moisture, color_intensity):
        m = self.MOISTURE.get(moisture, "")
        c = self.LIP_COLOR_INTENSITY.get(color_intensity, "")
        return (f"{prompt}, {m}, {c}",)


class SkinHighlightPlacement:
    """Control where skin catches light"""
    
    HIGHLIGHT_AREAS = {
        "cheekbones": "highlights on cheekbones, glowing cheekbones, lit cheekbones",
        "nose_bridge": "highlight on nose bridge, nose highlight",
        "forehead": "forehead highlight, glowing forehead",
        "collar_bones": "collar bone highlights, lit collar bones, defined clavicle",
        "shoulders": "shoulder highlights, lit shoulders, gleaming shoulders",
        "chest": "chest highlights, decolletage glow, lit upper chest",
        "full_face": "full face highlights, glowing skin, dewy face",
    }
    
    INTENSITY = {
        "subtle": "subtle highlights, soft glow, gentle shine",
        "moderate": "moderate highlights, visible glow, healthy shine",
        "strong": "strong highlights, bright glow, very luminous",
        "intense": "intense highlights, extreme glow, dazzling shine",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "highlight_area": (list(cls.HIGHLIGHT_AREAS.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("highlight_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Micro Details"

    def apply(self, prompt, highlight_area, intensity):
        h = self.HIGHLIGHT_AREAS.get(highlight_area, "")
        i = self.INTENSITY.get(intensity, "")
        return (f"{prompt}, {h}, {i}",)


class MoodAtmosphereController:
    """Set the overall mood and atmosphere"""
    
    MOODS = {
        "romantic": (
            "romantic mood, romantic atmosphere, soft lighting, "
            "warm tones, intimate feeling, love in the air"
        ),
        "mysterious": (
            "mysterious mood, enigmatic atmosphere, dramatic shadows, "
            "intriguing, secretive, noir feeling"
        ),
        "playful": (
            "playful mood, fun atmosphere, bright colors, "
            "joyful energy, lighthearted, spirited"
        ),
        "intense": (
            "intense mood, powerful atmosphere, dramatic, "
            "strong emotion, passionate, fierce"
        ),
        "serene": (
            "serene mood, peaceful atmosphere, calm, "
            "tranquil, zen, relaxed energy"
        ),
        "sensual": (
            "sensual mood, intimate atmosphere, seductive, "
            "alluring, provocative energy, bedroom vibes"
        ),
        "elegant": (
            "elegant mood, sophisticated atmosphere, refined, "
            "classy, tasteful, graceful energy"
        ),
        "edgy": (
            "edgy mood, rebellious atmosphere, bold, "
            "alternative, punk energy, unconventional"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "mood": (list(cls.MOODS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("mood_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Micro Details"

    def apply(self, prompt, mood):
        m = self.MOODS.get(mood, "")
        return (f"{prompt}, {m}",)


class FilmStockEmulator:
    """Emulate specific film stocks and their color science"""
    
    FILM_STOCKS = {
        "kodak_portra_400": (
            "shot on Kodak Portra 400, warm skin tones, "
            "soft contrast, filmic colors, film photography, "
            "natural warmth, wedding photography look"
        ),
        "kodak_portra_800": (
            "shot on Kodak Portra 800, warm tones, "
            "slightly grainy, film aesthetic, available light"
        ),
        "fuji_pro_400h": (
            "shot on Fuji Pro 400H, pastel tones, "
            "muted colors, soft greens, ethereal look"
        ),
        "kodak_ektar_100": (
            "shot on Kodak Ektar 100, vivid colors, "
            "high saturation, punchy, vibrant film"
        ),
        "ilford_hp5": (
            "shot on Ilford HP5, black and white film, "
            "classic grain, timeless monochrome"
        ),
        "cinestill_800t": (
            "shot on CineStill 800T, tungsten balanced, "
            "halation glow around lights, cinematic"
        ),
        "kodachrome": (
            "shot on Kodachrome, rich saturated colors, "
            "vintage look, classic americana"
        ),
        "polaroid": (
            "polaroid film, instant camera look, "
            "faded colors, vintage polaroid aesthetic"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "film_stock": (list(cls.FILM_STOCKS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("film_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Micro Details"

    def apply(self, prompt, film_stock):
        f = self.FILM_STOCKS.get(film_stock, "")
        return (f"{prompt}, {f}",)


class InstagramFilterEmulator:
    """Emulate popular Instagram filter looks"""
    
    FILTERS = {
        "clarendon": (
            "clarendon filter, bright highlights, intensified shadows, "
            "cool tones, vibrant colors"
        ),
        "gingham": (
            "gingham filter, vintage faded look, "
            "slight yellow tint, dreamy"
        ),
        "juno": (
            "juno filter, warm glowing tones, "
            "enhanced reds and oranges, sun-kissed"
        ),
        "lark": (
            "lark filter, desaturated greens, "
            "brightened blue sky, airy"
        ),
        "sierra": (
            "sierra filter, faded vintage look, "
            "soft contours, radial glow"
        ),
        "valencia": (
            "valencia filter, warm tint, "
            "faded vintage, antique feeling"
        ),
        "vsco_a6": (
            "vsco a6 filter, faded analog, "
            "muted tones, hint of fade"
        ),
        "no_filter": "no filter, natural colors, unedited look",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "filter_style": (list(cls.FILTERS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filter_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Micro Details"

    def apply(self, prompt, filter_style):
        f = self.FILTERS.get(filter_style, "")
        return (f"{prompt}, {f}",)


class SpecificFocusEnhancer:
    """Enhance specific body areas for focus shots"""
    
    FOCUS_AREAS = {
        "eyes_closeup": (
            "extreme closeup on eyes, eye detail shot, "
            "iris detail, captivating eyes, sharp eye focus"
        ),
        "lips_closeup": (
            "closeup on lips, lip detail shot, "
            "mouth focus, sensual lips, detailed lips"
        ),
        "cleavage_focus": (
            "focus on cleavage, decolletage, "
            "bust emphasis, chest focus"
        ),
        "legs_focus": (
            "focus on legs, leg emphasis, "
            "long legs prominent, thigh focus"
        ),
        "back_focus": (
            "focus on back, spine visible, "
            "back muscles, back tattoo focus"
        ),
        "posterior_focus": (
            "focus on posterior, rear emphasis, "
            "buttocks prominent, curves emphasized"
        ),
        "midriff_focus": (
            "focus on midriff, stomach emphasis, "
            "waist focus, abs visible"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "focus_area": (list(cls.FOCUS_AREAS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("focus_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Micro Details"

    def apply(self, prompt, focus_area):
        f = self.FOCUS_AREAS.get(focus_area, "")
        return (f"{prompt}, {f}",)


class MovementFreezeController:
    """Control how movement is captured/frozen"""
    
    MOVEMENT = {
        "frozen_sharp": (
            "frozen motion, sharp action, high shutter speed, "
            "crisp movement, no motion blur"
        ),
        "slight_blur": (
            "slight motion blur, dynamic, speed sense, "
            "subtle movement, artistic blur"
        ),
        "hair_motion": (
            "hair in motion, flowing hair, hair movement, "
            "dynamic hair, wind in hair"
        ),
        "fabric_motion": (
            "fabric in motion, flowing dress, moving clothes, "
            "wind-blown fabric, dynamic clothing"
        ),
        "action_peak": (
            "peak of action, decisive moment, "
            "perfect timing, action frozen"
        ),
        "long_exposure": (
            "long exposure effect, light trails, "
            "smooth motion, ethereal movement"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "movement": (list(cls.MOVEMENT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("movement_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Micro Details"

    def apply(self, prompt, movement):
        m = self.MOVEMENT.get(movement, "")
        return (f"{prompt}, {m}",)


NODE_CLASS_MAPPINGS = {
    "EyelashController": EyelashController,
    "LipMoistureController": LipMoistureController,
    "SkinHighlightPlacement": SkinHighlightPlacement,
    "MoodAtmosphereController": MoodAtmosphereController,
    "FilmStockEmulator": FilmStockEmulator,
    "InstagramFilterEmulator": InstagramFilterEmulator,
    "SpecificFocusEnhancer": SpecificFocusEnhancer,
    "MovementFreezeController": MovementFreezeController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EyelashController": "👁️ Eyelash Controller",
    "LipMoistureController": "💋 Lip Moisture",
    "SkinHighlightPlacement": "✨ Skin Highlight Placement",
    "MoodAtmosphereController": "🎭 Mood/Atmosphere",
    "FilmStockEmulator": "🎞️ Film Stock Emulator",
    "InstagramFilterEmulator": "📱 Instagram Filter",
    "SpecificFocusEnhancer": "🔍 Specific Focus Enhancer",
    "MovementFreezeController": "💨 Movement/Freeze",
}
