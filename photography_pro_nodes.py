"""
Mason's Photography Technique Nodes for ComfyUI
Professional photography replication without LoRAs - SD 1.5 optimized
"""


class PhotographyStyleMaster:
    """Replicate specific photography styles like a LoRA would"""
    
    STYLES = {
        "fashion_editorial": (
            "fashion editorial photography, high fashion, magazine quality, "
            "professional model photography, vogue style, editorial lighting, "
            "sharp focus, designer aesthetic, runway quality"
        ),
        "glamour": (
            "glamour photography, glamour lighting, soft focus beauty, "
            "high-end beauty photography, polished, flawless skin, "
            "professional glamour shoot, magazine cover quality"
        ),
        "boudoir": (
            "boudoir photography, intimate lighting, romantic atmosphere, "
            "soft sensual lighting, private photography session, "
            "tasteful intimate photography, bedroom photography"
        ),
        "playboy_style": (
            "playboy photography style, classic playboy lighting, "
            "glamour nude photography, professional adult photography, "
            "centerfold quality, smooth lighting, flawless skin"
        ),
        "sports_illustrated": (
            "sports illustrated swimsuit style, beach photography, "
            "tropical setting, athletic models, sun-kissed skin, "
            "action sports photography, dynamic beach shots"
        ),
        "maxim_fhm": (
            "maxim magazine style, fhm photography, mens magazine aesthetic, "
            "sexy but classy, provocative poses, studio lighting"
        ),
        "fine_art_nude": (
            "fine art nude photography, artistic nude, museum quality, "
            "tasteful nude art, classical poses, gallery worthy, "
            "artistic lighting, chiaroscuro"
        ),
        "catalog": (
            "catalog photography, commercial photography, clean white background, "
            "product photography style, e-commerce quality, neutral lighting"
        ),
        "portrait_studio": (
            "professional portrait studio, studio portrait lighting, "
            "headshot quality, corporate portrait style, clean background, "
            "professional studio setup"
        ),
        "natural_light": (
            "natural light photography, window light portrait, "
            "golden hour photography, soft natural lighting, "
            "available light, authentic natural look"
        ),
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
    CATEGORY = "Mason's Nodes/Photography Pro"

    def apply(self, prompt, style):
        s = self.STYLES.get(style, "")
        return (f"{prompt}, {s}",)


class BokehController:
    """Control background blur and bokeh effects"""
    
    BOKEH_INTENSITY = {
        "none": "sharp background, everything in focus, deep depth of field",
        "subtle": "subtle background blur, slight bokeh, f/4 aperture",
        "moderate": "moderate bokeh, background blur, f/2.8 aperture, shallow depth",
        "strong": "strong bokeh, heavy background blur, f/2 aperture, creamy bokeh",
        "extreme": "extreme bokeh, very shallow depth of field, f/1.4 aperture, dreamy blur",
    }
    
    BOKEH_SHAPE = {
        "circular": "circular bokeh, round light orbs, bubble bokeh",
        "hexagonal": "hexagonal bokeh, 6-blade aperture, geometric lights",
        "octagonal": "octagonal bokeh, 8-blade aperture",
        "smooth": "smooth bokeh, creamy background, no harsh edges",
        "swirly": "swirly bokeh, vintage lens effect, helios bokeh",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "intensity": (list(cls.BOKEH_INTENSITY.keys()),),
                "shape": (list(cls.BOKEH_SHAPE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("bokeh_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Photography Pro"

    def apply(self, prompt, intensity, shape):
        i = self.BOKEH_INTENSITY.get(intensity, "")
        s = self.BOKEH_SHAPE.get(shape, "")
        return (f"{prompt}, {i}, {s}",)


class LensSimulator:
    """Simulate specific lens characteristics"""
    
    LENS_TYPES = {
        "35mm": "35mm lens, street photography focal length, environmental portrait",
        "50mm": "50mm lens, nifty fifty, natural perspective, standard lens",
        "85mm": "85mm lens, portrait lens, slight compression, flattering perspective",
        "135mm": "135mm lens, telephoto portrait, strong compression, isolated subject",
        "200mm": "200mm telephoto, strong background compression, paparazzi look",
        "macro": "macro lens, extreme close-up capability, detailed texture",
        "wide_24mm": "24mm wide angle, environmental portrait, context shown",
        "fisheye": "fisheye lens, distorted edges, ultra wide, barrel distortion",
    }
    
    LENS_QUALITY = {
        "budget": "budget lens, slight softness, chromatic aberration",
        "professional": "professional lens, sharp, high quality glass",
        "vintage": "vintage lens, unique rendering, character, glow highlights",
        "zeiss": "zeiss lens quality, clinical sharpness, perfect contrast",
        "leica": "leica lens quality, magical rendering, 3D pop, smooth bokeh",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "lens_type": (list(cls.LENS_TYPES.keys()),),
                "lens_quality": (list(cls.LENS_QUALITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lens_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Photography Pro"

    def apply(self, prompt, lens_type, lens_quality):
        lt = self.LENS_TYPES.get(lens_type, "")
        lq = self.LENS_QUALITY.get(lens_quality, "")
        return (f"{prompt}, {lt}, {lq}",)


class FocusPrecisionController:
    """Control focus with precision"""
    
    FOCUS_TYPE = {
        "tack_sharp": "tack sharp focus, perfectly sharp, razor sharp details",
        "sharp": "sharp focus, clear details, good focus",
        "soft_focus": "soft focus, dreamy sharpness, romantic blur",
        "artistic_blur": "artistic blur, intentional softness, painterly",
    }
    
    FOCUS_POINT = {
        "eyes": "focus on eyes, sharp eyes, eye detail",
        "face": "focus on face, facial features sharp",
        "full_body": "full body in focus, entire figure sharp",
        "selective": "selective focus, subject sharp, rest blurred",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "focus_type": (list(cls.FOCUS_TYPE.keys()),),
                "focus_point": (list(cls.FOCUS_POINT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("focus_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Photography Pro"

    def apply(self, prompt, focus_type, focus_point):
        ft = self.FOCUS_TYPE.get(focus_type, "")
        fp = self.FOCUS_POINT.get(focus_point, "")
        return (f"{prompt}, {ft}, {fp}",)


class ContrastMaster:
    """Master control over image contrast"""
    
    CONTRAST_LEVELS = {
        "flat": "flat lighting, low contrast, shadow detail preserved, film flat",
        "low": "low contrast, soft lighting, gentle tones",
        "medium": "medium contrast, balanced lighting, natural tones",
        "high": "high contrast, dramatic lighting, deep blacks, bright highlights",
        "extreme": "extreme contrast, very high contrast, stark lighting, bold",
        "hdr": "HDR look, high dynamic range, detail in shadows and highlights",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "contrast": (list(cls.CONTRAST_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("contrast_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Photography Pro"

    def apply(self, prompt, contrast):
        c = self.CONTRAST_LEVELS.get(contrast, "")
        return (f"{prompt}, {c}",)


class ExposureController:
    """Control exposure and lighting ratio"""
    
    EXPOSURE = {
        "underexposed": "underexposed, dark, moody, shadows dominant",
        "slightly_under": "slightly underexposed, moody, rich shadows",
        "perfect": "perfectly exposed, balanced exposure, ideal lighting",
        "slightly_over": "slightly overexposed, bright, airy, light",
        "overexposed": "overexposed, very bright, high key, washed highlights",
    }
    
    KEY_FILL_RATIO = {
        "flat_1_1": "flat lighting, 1:1 ratio, no shadows, even illumination",
        "subtle_2_1": "subtle shadows, 2:1 ratio, gentle modeling",
        "moderate_3_1": "moderate shadows, 3:1 ratio, defined features",
        "dramatic_4_1": "dramatic shadows, 4:1 ratio, strong modeling",
        "extreme_8_1": "extreme shadows, 8:1 ratio, chiaroscuro, stark",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "exposure": (list(cls.EXPOSURE.keys()),),
                "key_fill_ratio": (list(cls.KEY_FILL_RATIO.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("exposure_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Photography Pro"

    def apply(self, prompt, exposure, key_fill_ratio):
        e = self.EXPOSURE.get(exposure, "")
        k = self.KEY_FILL_RATIO.get(key_fill_ratio, "")
        return (f"{prompt}, {e}, {k}",)


NODE_CLASS_MAPPINGS = {
    "PhotographyStyleMaster": PhotographyStyleMaster,
    "BokehController": BokehController,
    "LensSimulator": LensSimulator,
    "FocusPrecisionController": FocusPrecisionController,
    "ContrastMaster": ContrastMaster,
    "ExposureController": ExposureController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PhotographyStyleMaster": "📷 Photography Style Master",
    "BokehController": "🔵 Bokeh Controller",
    "LensSimulator": "🔭 Lens Simulator",
    "FocusPrecisionController": "🎯 Focus Precision",
    "ContrastMaster": "⚫ Contrast Master",
    "ExposureController": "☀️ Exposure Controller",
}
