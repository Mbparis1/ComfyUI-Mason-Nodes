"""
Mason's Photorealism Nodes for ComfyUI
Nodes to make AI images look like real photographs
"""


class PhotorealismBooster:
    """Adds photorealistic quality tags to prompts"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "quality_level": (["ultra", "high", "medium"],),
                "camera_style": (["professional_dslr", "iphone", "film_camera", "studio", "candid", "none"],),
                "lighting": (["natural", "studio", "golden_hour", "soft", "dramatic", "none"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("enhanced_prompt",)
    FUNCTION = "boost"
    CATEGORY = "Mason's Nodes/Photorealism"

    QUALITY_TAGS = {
        "ultra": "photorealistic, hyperrealistic, ultra detailed, 8k uhd, dslr, high quality, film grain, Fujifilm XT3, sharp focus, detailed skin texture, subsurface scattering, professional photography",
        "high": "photorealistic, realistic, detailed, high quality, sharp focus, professional photography, 4k, detailed skin",
        "medium": "realistic, detailed, good quality, sharp focus"
    }
    
    CAMERA_TAGS = {
        "professional_dslr": "shot on Canon EOS R5, 85mm lens, f/1.8 aperture, shallow depth of field, bokeh",
        "iphone": "shot on iPhone 15 Pro, natural smartphone photography, authentic look",
        "film_camera": "shot on 35mm film, Kodak Portra 400, film grain, vintage aesthetic, analog photography",
        "studio": "studio photography, professional lighting setup, beauty dish, softbox lighting",
        "candid": "candid photography, natural moment, unposed, authentic, lifestyle photography",
        "none": ""
    }
    
    LIGHTING_TAGS = {
        "natural": "natural lighting, soft daylight, ambient light, realistic shadows",
        "studio": "studio lighting, three-point lighting, controlled lighting, professional",
        "golden_hour": "golden hour lighting, warm sunlight, magic hour, orange and gold tones",
        "soft": "soft diffused lighting, overcast, even lighting, no harsh shadows",
        "dramatic": "dramatic lighting, chiaroscuro, strong contrast, moody atmosphere",
        "none": ""
    }

    def boost(self, prompt, quality_level, camera_style, lighting):
        parts = [prompt.strip()]
        
        if quality_level in self.QUALITY_TAGS:
            parts.append(self.QUALITY_TAGS[quality_level])
        
        if camera_style != "none" and camera_style in self.CAMERA_TAGS:
            parts.append(self.CAMERA_TAGS[camera_style])
            
        if lighting != "none" and lighting in self.LIGHTING_TAGS:
            parts.append(self.LIGHTING_TAGS[lighting])
        
        return (", ".join(parts),)


class AntiAIArtifacts:
    """Generates negative prompts that specifically combat AI-looking artifacts"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "focus_area": (["full_body", "face", "hands", "all"],),
                "additional_negatives": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("anti_ai_negatives",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Photorealism"

    # Common AI tells and artifacts to avoid
    BASE_NEGATIVES = "artificial, fake, cgi, 3d render, digital art, illustration, painting, drawing, anime, cartoon, plastic skin, waxy skin, oversmoothed, airbrushed, uncanny valley, unrealistic, unnatural"
    
    FACE_NEGATIVES = "asymmetrical eyes, different eye colors, cross-eyed, uneven pupils, blurry face, distorted face, extra eyes, missing eyes, weird eyes, creepy eyes, wonky face, morphed face, unnatural smile, fake smile, teeth artifacts, extra teeth, missing teeth"
    
    HANDS_NEGATIVES = "bad hands, malformed hands, missing fingers, extra fingers, fused fingers, mutated hands, too many fingers, long fingers, extra limbs, missing limbs, floating limbs, disconnected limbs, mangled hands, disproportionate hands"
    
    BODY_NEGATIVES = "bad anatomy, disproportionate body, wrong proportions, extra limbs, missing limbs, disconnected body parts, unnatural pose, impossible pose, twisted torso, merged body parts"
    
    QUALITY_NEGATIVES = "low quality, worst quality, lowres, blurry, noisy, grainy, jpeg artifacts, compression artifacts, watermark, text, signature, username, artist name, logo"

    def generate(self, focus_area, additional_negatives):
        parts = [self.BASE_NEGATIVES, self.QUALITY_NEGATIVES]
        
        if focus_area == "face" or focus_area == "all":
            parts.append(self.FACE_NEGATIVES)
        
        if focus_area == "hands" or focus_area == "all":
            parts.append(self.HANDS_NEGATIVES)
            
        if focus_area == "full_body" or focus_area == "all":
            parts.append(self.BODY_NEGATIVES)
        
        if additional_negatives.strip():
            parts.append(additional_negatives.strip())
        
        return (", ".join(parts),)


class RealisticSkinEnhancer:
    """Adds skin-specific realism tags"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "skin_type": (["natural", "flawless", "textured", "freckled", "tanned"],),
                "detail_level": (["maximum", "high", "natural"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("skin_enhanced_prompt",)
    FUNCTION = "enhance"
    CATEGORY = "Mason's Nodes/Photorealism"

    SKIN_TAGS = {
        "natural": "natural skin, realistic skin texture, visible pores, skin imperfections, natural complexion",
        "flawless": "clear skin, smooth skin, healthy skin, glowing skin, even skin tone",
        "textured": "highly detailed skin, visible pores, skin texture, realistic skin detail, subsurface scattering",
        "freckled": "freckles, natural freckles, sun spots, natural skin marks, realistic freckles",
        "tanned": "sun-kissed skin, tanned skin, warm skin tone, bronze complexion, healthy tan"
    }
    
    DETAIL_TAGS = {
        "maximum": "8k skin detail, hyperrealistic skin, every pore visible, ultra detailed skin texture, microscopic skin detail, subsurface scattering, skin translucency",
        "high": "detailed skin texture, realistic pores, natural skin detail, subsurface scattering",
        "natural": "natural skin, realistic skin, believable skin texture"
    }

    def enhance(self, prompt, skin_type, detail_level):
        parts = [prompt.strip()]
        
        if skin_type in self.SKIN_TAGS:
            parts.append(self.SKIN_TAGS[skin_type])
            
        if detail_level in self.DETAIL_TAGS:
            parts.append(self.DETAIL_TAGS[detail_level])
        
        return (", ".join(parts),)


class RealisticSettings:
    """Outputs optimal settings for photorealistic generation"""
    
    PRESETS = {
        "maximum_quality": {"steps": 30, "cfg": 7.0, "sampler": "dpmpp_2m", "scheduler": "karras"},
        "balanced": {"steps": 25, "cfg": 7.5, "sampler": "euler_ancestral", "scheduler": "normal"},
        "fast_realistic": {"steps": 20, "cfg": 7.0, "sampler": "dpmpp_sde", "scheduler": "karras"},
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PRESETS.keys()),),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT", "STRING", "STRING")
    RETURN_NAMES = ("steps", "cfg", "sampler", "scheduler")
    FUNCTION = "get_settings"
    CATEGORY = "Mason's Nodes/Photorealism"

    def get_settings(self, preset):
        settings = self.PRESETS.get(preset, self.PRESETS["balanced"])
        return (settings["steps"], settings["cfg"], settings["sampler"], settings["scheduler"])


# Register nodes
NODE_CLASS_MAPPINGS = {
    "PhotorealismBooster": PhotorealismBooster,
    "AntiAIArtifacts": AntiAIArtifacts,
    "RealisticSkinEnhancer": RealisticSkinEnhancer,
    "RealisticSettings": RealisticSettings,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PhotorealismBooster": "📷 Photorealism Booster",
    "AntiAIArtifacts": "🚫 Anti-AI Artifacts",
    "RealisticSkinEnhancer": "✨ Realistic Skin Enhancer", 
    "RealisticSettings": "⚙️ Realistic Settings",
}
