"""
Mason's Camera Effects Nodes for ComfyUI
Replace camera/lens LoRAs with prompt engineering - SD 1.5 optimized
"""


class LensTypeController:
    """Control lens type simulation"""
    
    LENSES = {
        "standard": "standard lens, normal perspective, 50mm equivalent",
        "wide_angle": "wide angle lens, wide perspective, expansive view, 24mm",
        "ultra_wide": "ultra wide angle, fisheye effect, extreme wide, distorted edges",
        "telephoto": "telephoto lens, compressed perspective, distant shot, 200mm",
        "macro": "macro lens, extreme close-up, tiny details visible, magnified",
        "tilt_shift": "tilt-shift lens, miniature effect, selective focus, toy-like",
        "portrait": "portrait lens, 85mm, beautiful bokeh, flattering perspective",
        "anamorphic": "anamorphic lens, cinematic, horizontal flares, oval bokeh",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "lens": (list(cls.LENSES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lens_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Camera Effects"

    def apply(self, prompt, lens):
        l = self.LENSES.get(lens, "")
        return (f"{prompt}, {l}",)


class FilmStockController:
    """Simulate different film stocks"""
    
    FILM_STOCKS = {
        "digital": "digital photography, clean digital sensor, modern camera",
        "kodak_portra": "Kodak Portra 400, warm skin tones, soft colors, film photography",
        "kodak_gold": "Kodak Gold 200, warm tones, saturated, consumer film look",
        "fuji_velvia": "Fuji Velvia, vibrant colors, high saturation, vivid",
        "fuji_superia": "Fuji Superia, cool tones, green shift, classic film",
        "ilford_hp5": "Ilford HP5, black and white, grainy, classic monochrome",
        "kodak_trix": "Kodak Tri-X 400, black and white, contrasty, photojournalism",
        "cinestill_800": "Cinestill 800T, tungsten balanced, halation, neon glow",
        "polaroid": "Polaroid instant film, faded colors, vintage, soft vignette",
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
    CATEGORY = "Mason's Nodes/Camera Effects"

    def apply(self, prompt, film_stock):
        f = self.FILM_STOCKS.get(film_stock, "")
        return (f"{prompt}, {f}",)


class ChromaticAberrationController:
    """Control chromatic aberration effect"""
    
    ABERRATION = {
        "none": "no chromatic aberration, clean edges, sharp without fringing",
        "subtle": "subtle chromatic aberration, slight color fringing, realistic lens",
        "moderate": "moderate chromatic aberration, visible color separation, artistic",
        "heavy": "heavy chromatic aberration, strong RGB split, glitch aesthetic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "aberration": (list(cls.ABERRATION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("aberration_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Camera Effects"

    def apply(self, prompt, aberration):
        ab = self.ABERRATION.get(aberration, "")
        return (f"{prompt}, {ab}",)


class FilmGrainController:
    """Control film grain intensity"""
    
    GRAIN = {
        "none": "no grain, clean digital, smooth image, noiseless",
        "fine": "fine film grain, subtle texture, delicate grain, ISO 100",
        "light": "light film grain, gentle texture, natural grain, ISO 400",
        "medium": "medium film grain, visible grain, textured, ISO 800",
        "heavy": "heavy film grain, prominent grain, noisy, ISO 3200",
        "extreme": "extreme film grain, very grainy, high ISO look, pushed film",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "grain": (list(cls.GRAIN.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("grain_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Camera Effects"

    def apply(self, prompt, grain):
        g = self.GRAIN.get(grain, "")
        return (f"{prompt}, {g}",)


class VintageFilterController:
    """Apply vintage era filters"""
    
    VINTAGE = {
        "none": "modern photography, contemporary look, clean digital",
        "1950s": "1950s photography style, black and white, classic Hollywood",
        "1960s": "1960s photography, mod style, saturated colors, retro",
        "1970s": "1970s photography, warm orange tones, soft focus, disco era",
        "1980s": "1980s photography, neon colors, bright, synthwave aesthetic",
        "1990s": "1990s photography, desaturated, grunge aesthetic, film look",
        "2000s": "2000s photography, oversaturated, digital camera look",
        "instant_film": "instant film, Polaroid style, faded, warm vintage",
        "daguerreotype": "daguerreotype style, very old photo, sepia, antique",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "era": (list(cls.VINTAGE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("vintage_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Camera Effects"

    def apply(self, prompt, era):
        v = self.VINTAGE.get(era, "")
        return (f"{prompt}, {v}",)


class LensFlareController:
    """Control lens flare effects"""
    
    FLARES = {
        "none": "no lens flare, clean image, no optical artifacts",
        "subtle": "subtle lens flare, slight glow from light source",
        "natural": "natural lens flare, realistic sun flare, organic light bloom",
        "cinematic": "cinematic lens flare, blue anamorphic flare, dramatic",
        "anamorphic": "anamorphic lens flare, horizontal streak, cinematic look",
        "starburst": "starburst lens flare, pointed light rays, star effect",
        "rainbow": "rainbow lens flare, colorful light dispersion, prismatic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "flare": (list(cls.FLARES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("flare_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Camera Effects"

    def apply(self, prompt, flare):
        f = self.FLARES.get(flare, "")
        return (f"{prompt}, {f}",)


NODE_CLASS_MAPPINGS = {
    "LensTypeController": LensTypeController,
    "FilmStockController": FilmStockController,
    "ChromaticAberrationController": ChromaticAberrationController,
    "FilmGrainController": FilmGrainController,
    "VintageFilterController": VintageFilterController,
    "LensFlareController": LensFlareController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LensTypeController": "📷 Lens Type Controller",
    "FilmStockController": "🎞️ Film Stock Controller",
    "ChromaticAberrationController": "🌈 Chromatic Aberration",
    "FilmGrainController": "🌾 Film Grain Controller",
    "VintageFilterController": "📼 Vintage Filter",
    "LensFlareController": "✨ Lens Flare Controller",
}
