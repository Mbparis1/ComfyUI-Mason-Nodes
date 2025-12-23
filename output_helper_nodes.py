"""
Mason's Output Helper Nodes for ComfyUI
Resolution, upscaling, and output preparation - SD 1.5 optimized
"""


class AspectRatioHelper:
    """Get optimal resolutions for different aspect ratios"""
    
    # SD 1.5 optimal resolutions (multiples of 64, under 512x768 for VRAM)
    RATIOS = {
        "1:1_square": {"width": 512, "height": 512, "desc": "Square - portraits, icons"},
        "4:3_standard": {"width": 512, "height": 384, "desc": "Standard - general use"},
        "3:4_portrait": {"width": 384, "height": 512, "desc": "Portrait - vertical photos"},
        "16:9_widescreen": {"width": 512, "height": 288, "desc": "Widescreen - cinematic"},
        "9:16_vertical": {"width": 288, "height": 512, "desc": "Vertical - phone screens"},
        "2:3_photo": {"width": 384, "height": 576, "desc": "Photo ratio - classic photography"},
        "3:2_landscape": {"width": 576, "height": 384, "desc": "Landscape - wide shots"},
        "1:2_tall": {"width": 256, "height": 512, "desc": "Tall - full body vertical"},
        "2:1_panorama": {"width": 512, "height": 256, "desc": "Panorama - wide scenics"},
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "aspect_ratio": (list(cls.RATIOS.keys()),),
                "upscale_factor": ("FLOAT", {"default": 1.0, "min": 1.0, "max": 2.0, "step": 0.5}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "description")
    FUNCTION = "calculate"
    CATEGORY = "Mason's Nodes/Output Helpers"

    def calculate(self, aspect_ratio, upscale_factor):
        ratio = self.RATIOS.get(aspect_ratio, self.RATIOS["1:1_square"])
        width = int(ratio["width"] * upscale_factor)
        height = int(ratio["height"] * upscale_factor)
        # Ensure multiples of 64
        width = (width // 64) * 64
        height = (height // 64) * 64
        return (width, height, ratio["desc"])


class UpscalePrep:
    """Prepare prompts for upscaling passes"""
    
    UPSCALE_MODES = {
        "detail_enhance": "highly detailed, intricate details, sharp focus, fine details visible",
        "face_focus": "detailed face, sharp facial features, clear eyes, defined features",
        "texture_enhance": "detailed textures, fabric texture, skin texture, material details",
        "sharpening": "sharp, crisp, high definition, crystal clear, tack sharp",
        "general": "high resolution, high quality, detailed, enhanced",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "original_prompt": ("STRING", {"default": "", "multiline": True}),
                "upscale_mode": (list(cls.UPSCALE_MODES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "FLOAT")
    RETURN_NAMES = ("upscale_prompt", "suggested_denoise")
    FUNCTION = "prepare"
    CATEGORY = "Mason's Nodes/Output Helpers"

    def prepare(self, original_prompt, upscale_mode):
        enhancement = self.UPSCALE_MODES.get(upscale_mode, "")
        upscale_prompt = f"{original_prompt}, {enhancement}"
        
        # Suggested denoise for img2img upscaling
        denoise_map = {
            "detail_enhance": 0.35,
            "face_focus": 0.30,
            "texture_enhance": 0.40,
            "sharpening": 0.25,
            "general": 0.35,
        }
        denoise = denoise_map.get(upscale_mode, 0.35)
        
        return (upscale_prompt, denoise)


class WatermarkRemovalHints:
    """Add comprehensive watermark/artifact removal to negative prompt"""
    
    REMOVAL_LEVELS = {
        "basic": "watermark, signature, text, logo",
        "standard": "watermark, signature, text, logo, username, copyright, banner, overlay",
        "comprehensive": (
            "watermark, signature, text, logo, username, copyright, banner, overlay, "
            "artist name, website, url, date, timestamp, frame, border, "
            "stock photo watermark, shutterstock, getty images, adobe stock"
        ),
        "aggressive": (
            "watermark, signature, text, logo, username, copyright, banner, overlay, "
            "artist name, website, url, date, timestamp, frame, border, "
            "stock photo watermark, shutterstock, getty images, adobe stock, "
            "any text, any writing, any letters, any numbers, any symbols, "
            "subtitles, captions, credits, title"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "negative_prompt": ("STRING", {"default": "", "multiline": True}),
                "removal_level": (list(cls.REMOVAL_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "add_removal"
    CATEGORY = "Mason's Nodes/Output Helpers"

    def add_removal(self, negative_prompt, removal_level):
        removal = self.REMOVAL_LEVELS.get(removal_level, "")
        if negative_prompt:
            return (f"{negative_prompt}, {removal}",)
        return (removal,)


NODE_CLASS_MAPPINGS = {
    "AspectRatioHelper": AspectRatioHelper,
    "UpscalePrep": UpscalePrep,
    "WatermarkRemovalHints": WatermarkRemovalHints,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatioHelper": "📐 Aspect Ratio Helper",
    "UpscalePrep": "🔍 Upscale Prep",
    "WatermarkRemovalHints": "🚫 Watermark Removal Hints",
}
