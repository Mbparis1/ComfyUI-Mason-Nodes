"""
Mason's Image Enhancement Nodes for ComfyUI
Post-processing and image quality control through prompts - SD 1.5 optimized
"""


class SharpeningController:
    """Add sharpness keywords to prompts for crisper images"""
    
    SHARPNESS_LEVELS = {
        "subtle": "sharp focus, clear details",
        "medium": "very sharp, highly detailed, crisp focus, sharp edges",
        "strong": "extremely sharp, razor sharp focus, hyper detailed, ultra crisp",
        "razor": "razor sharp, extreme detail, pixel perfect sharpness, tack sharp, surgical precision"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "sharpness": (list(cls.SHARPNESS_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("sharpened_prompt",)
    FUNCTION = "sharpen"
    CATEGORY = "Mason's Nodes/Image Enhancement"

    def sharpen(self, prompt, sharpness):
        sharpness_desc = self.SHARPNESS_LEVELS.get(sharpness, "")
        return (f"{prompt}, {sharpness_desc}",)


class ContrastController:
    """Control contrast levels through prompts"""
    
    CONTRAST_LEVELS = {
        "flat": "low contrast, flat lighting, soft tones, minimal shadows",
        "natural": "natural contrast, balanced tones, realistic shadows",
        "punchy": "high contrast, vivid tones, strong shadows, dynamic range",
        "dramatic": "extreme contrast, deep blacks, bright highlights, chiaroscuro, dramatic shadows",
        "film_noir": "film noir contrast, harsh shadows, stark lighting, black and white aesthetic"
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
    RETURN_NAMES = ("contrasted_prompt",)
    FUNCTION = "apply_contrast"
    CATEGORY = "Mason's Nodes/Image Enhancement"

    def apply_contrast(self, prompt, contrast):
        contrast_desc = self.CONTRAST_LEVELS.get(contrast, "")
        return (f"{prompt}, {contrast_desc}",)


class SaturationController:
    """Boost or reduce color saturation through prompts"""
    
    SATURATION_LEVELS = {
        "desaturated": "muted colors, desaturated, low saturation, faded tones",
        "natural": "natural colors, realistic saturation, true to life colors",
        "vibrant": "vibrant colors, rich saturation, vivid hues, colorful",
        "hyper_saturated": "hyper saturated, extremely vibrant colors, intense hues, color explosion",
        "monochrome": "monochrome, black and white, grayscale, no color"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "saturation": (list(cls.SATURATION_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("saturated_prompt",)
    FUNCTION = "apply_saturation"
    CATEGORY = "Mason's Nodes/Image Enhancement"

    def apply_saturation(self, prompt, saturation):
        saturation_desc = self.SATURATION_LEVELS.get(saturation, "")
        return (f"{prompt}, {saturation_desc}",)


class NoiseTextureEnhancer:
    """Add film grain/noise for realism"""
    
    NOISE_TYPES = {
        "none": "",
        "subtle_grain": "subtle film grain, fine texture, organic feel",
        "medium_grain": "film grain, analog texture, grainy aesthetic, 35mm film look",
        "heavy_grain": "heavy film grain, coarse texture, vintage film, raw aesthetic",
        "digital_noise": "digital noise, high ISO look, low light texture",
        "cinematic_grain": "cinematic film grain, Kodak Portra texture, professional film stock"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "noise_type": (list(cls.NOISE_TYPES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("textured_prompt",)
    FUNCTION = "add_noise"
    CATEGORY = "Mason's Nodes/Image Enhancement"

    def add_noise(self, prompt, noise_type):
        noise_desc = self.NOISE_TYPES.get(noise_type, "")
        if noise_desc:
            return (f"{prompt}, {noise_desc}",)
        return (prompt,)


class VignetteController:
    """Add vignette effect keywords for focused compositions"""
    
    VIGNETTE_STYLES = {
        "none": "",
        "subtle": "subtle vignette, slightly darkened edges, gentle falloff",
        "medium": "vignette effect, darkened corners, center-focused lighting",
        "strong": "strong vignette, dark edges, spotlight center, dramatic falloff",
        "artistic": "artistic vignette, dreamy edges, soft corner blur, vintage look"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "vignette": (list(cls.VIGNETTE_STYLES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("vignetted_prompt",)
    FUNCTION = "add_vignette"
    CATEGORY = "Mason's Nodes/Image Enhancement"

    def add_vignette(self, prompt, vignette):
        vignette_desc = self.VIGNETTE_STYLES.get(vignette, "")
        if vignette_desc:
            return (f"{prompt}, {vignette_desc}",)
        return (prompt,)


class DepthOfFieldSimulator:
    """Simulate bokeh/depth blur through prompts"""
    
    DOF_PRESETS = {
        "everything_sharp": "everything in focus, deep depth of field, no blur, sharp throughout",
        "slight_bokeh": "slight bokeh, gentle background blur, shallow depth of field",
        "portrait_dof": "portrait depth of field, subject sharp, blurred background, creamy bokeh",
        "extreme_bokeh": "extreme bokeh, very shallow depth of field, dreamy background blur, f/1.4 aperture",
        "tilt_shift": "tilt shift effect, selective focus, miniature look, dramatic blur gradient",
        "foreground_blur": "foreground blur, background sharp, depth layering"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "depth_of_field": (list(cls.DOF_PRESETS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("dof_prompt",)
    FUNCTION = "apply_dof"
    CATEGORY = "Mason's Nodes/Image Enhancement"

    def apply_dof(self, prompt, depth_of_field):
        dof_desc = self.DOF_PRESETS.get(depth_of_field, "")
        return (f"{prompt}, {dof_desc}",)


NODE_CLASS_MAPPINGS = {
    "SharpeningController": SharpeningController,
    "ContrastController": ContrastController,
    "SaturationController": SaturationController,
    "NoiseTextureEnhancer": NoiseTextureEnhancer,
    "VignetteController": VignetteController,
    "DepthOfFieldSimulator": DepthOfFieldSimulator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SharpeningController": "🔪 Sharpening Controller",
    "ContrastController": "⚡ Contrast Controller",
    "SaturationController": "🎨 Saturation Controller",
    "NoiseTextureEnhancer": "📷 Noise/Texture Enhancer",
    "VignetteController": "🔲 Vignette Controller",
    "DepthOfFieldSimulator": "🔭 Depth of Field Simulator",
}
