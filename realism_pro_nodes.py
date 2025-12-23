"""
Mason's Realism Maximizer Nodes for ComfyUI
Achieve LoRA-quality realism through pure prompts - SD 1.5 optimized
"""


class PhotorealismMaximizer:
    """Maximum photorealism enhancement - replaces realism LoRAs"""
    
    LEVELS = {
        "subtle": (
            "photorealistic, realistic, natural looking"
        ),
        "moderate": (
            "photorealistic, hyperrealistic, realistic photo, natural skin, "
            "realistic lighting, professional photography"
        ),
        "high": (
            "photorealistic, hyperrealistic, ultra realistic photo, "
            "professionally photographed, natural skin texture, realistic pores, "
            "realistic lighting, subsurface scattering, 8k uhd, dslr quality, "
            "raw photo, unedited photo"
        ),
        "maximum": (
            "photorealistic, hyperrealistic, ultra realistic photograph, "
            "indistinguishable from real photo, professional photography, "
            "natural skin with pores and imperfections, subsurface scattering, "
            "realistic eye reflections, realistic hair strands, natural lighting, "
            "8k uhd, shot on Canon EOS R5, 85mm lens, raw photo, unprocessed, "
            "no filters, genuine photograph, award winning photography"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "level": (list(cls.LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("realism_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Realism Pro"

    def apply(self, prompt, level):
        l = self.LEVELS.get(level, "")
        return (f"{prompt}, {l}",)


class SkinRealismPro:
    """Professional skin realism - replaces skin texture LoRAs"""
    
    SKIN_QUALITY = {
        "smooth_beauty": (
            "smooth skin, flawless complexion, beauty retouched, "
            "poreless skin, perfect skin, magazine skin"
        ),
        "natural_healthy": (
            "natural skin, healthy skin, subtle pores visible, "
            "natural complexion, real skin texture, slight imperfections"
        ),
        "detailed_realistic": (
            "detailed skin texture, visible pores, realistic skin, "
            "natural skin imperfections, subsurface scattering, "
            "skin translucency, natural skin oils"
        ),
        "hyperrealistic": (
            "hyperrealistic skin, every pore visible, skin texture detail, "
            "subsurface scattering, skin translucency, natural oils, "
            "fine vellus hair, realistic skin imperfections, "
            "authentic human skin, dermatologically accurate"
        ),
    }
    
    SKIN_CONDITION = {
        "perfect": "perfect skin, no blemishes, flawless",
        "healthy": "healthy skin, natural glow, good condition",
        "natural": "natural skin condition, minor imperfections, authentic",
        "weathered": "weathered skin, life experience, character lines",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "quality": (list(cls.SKIN_QUALITY.keys()),),
                "condition": (list(cls.SKIN_CONDITION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("skin_realism_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Realism Pro"

    def apply(self, prompt, quality, condition):
        q = self.SKIN_QUALITY.get(quality, "")
        c = self.SKIN_CONDITION.get(condition, "")
        return (f"{prompt}, {q}, {c}",)


class HairRealismPro:
    """Professional hair realism - replaces hair LoRAs"""
    
    HAIR_DETAIL = {
        "basic": "hair, styled hair",
        "detailed": "detailed hair, visible hair strands, natural hair",
        "hyperrealistic": (
            "hyperrealistic hair, individual strands visible, "
            "hair texture detail, natural hair shine, flyaway hairs, "
            "realistic hair movement, subsurface scattering in hair"
        ),
    }
    
    HAIR_QUALITY = {
        "silky": "silky hair, smooth hair, shiny healthy hair, glossy",
        "natural": "natural hair texture, authentic hair, realistic shine",
        "textured": "textured hair, natural waves, volume, body",
        "damaged": "slightly damaged hair, realistic wear, authentic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "detail": (list(cls.HAIR_DETAIL.keys()),),
                "quality": (list(cls.HAIR_QUALITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("hair_realism_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Realism Pro"

    def apply(self, prompt, detail, quality):
        d = self.HAIR_DETAIL.get(detail, "")
        q = self.HAIR_QUALITY.get(quality, "")
        return (f"{prompt}, {d}, {q}",)


class EyeRealismPro:
    """Professional eye realism - the windows to the soul"""
    
    EYE_DETAIL = {
        "basic": "detailed eyes, clear eyes",
        "enhanced": "highly detailed eyes, sharp iris, clear sclera, defined pupil",
        "hyperrealistic": (
            "hyperrealistic eyes, incredibly detailed iris, visible iris fibers, "
            "realistic reflections in eyes, catchlights, moist eyes, "
            "natural eye veins in sclera, photorealistic eye detail, "
            "soul in the eyes, lifelike gaze"
        ),
    }
    
    CATCHLIGHTS = {
        "none": "",
        "single": "single catchlight in eyes, window reflection",
        "dual": "dual catchlights, studio lights reflected in eyes",
        "ring": "ring light catchlight, circular reflection in eyes",
        "natural": "natural light reflection in eyes, authentic catchlight",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "detail": (list(cls.EYE_DETAIL.keys()),),
                "catchlights": (list(cls.CATCHLIGHTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("eye_realism_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Realism Pro"

    def apply(self, prompt, detail, catchlights):
        d = self.EYE_DETAIL.get(detail, "")
        c = self.CATCHLIGHTS.get(catchlights, "")
        if c:
            return (f"{prompt}, {d}, {c}",)
        return (f"{prompt}, {d}",)


class AntiAIDetection:
    """Remove AI tells and artifacts - makes images look more real"""
    
    LEVELS = {
        "subtle": (
            "natural imperfections, not too perfect, "
            "authentic photograph, genuine photo"
        ),
        "moderate": (
            "natural imperfections, not too perfect, asymmetrical features, "
            "authentic photograph, genuine photo, not AI generated, "
            "realistic flaws, human imperfection"
        ),
        "aggressive": (
            "natural imperfections, deliberate asymmetry, authentic photograph, "
            "genuine human, not computer generated, not AI, not cgi, "
            "real person, actual photograph, documentary style, "
            "candid moment, unposed, natural moment, imperfect but real"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "level": (list(cls.LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("anti_ai_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Realism Pro"

    def apply(self, prompt, level):
        l = self.LEVELS.get(level, "")
        return (f"{prompt}, {l}",)


class MaterialRealism:
    """Realistic material and fabric rendering"""
    
    MATERIALS = {
        "silk": "realistic silk fabric, shiny smooth silk, silk sheen, luxurious silk texture",
        "cotton": "realistic cotton fabric, soft cotton texture, natural cotton weave",
        "lace": "realistic lace, intricate lace pattern, delicate lace texture",
        "leather": "realistic leather, leather texture, leather grain, natural leather",
        "denim": "realistic denim, denim weave, blue jean texture",
        "satin": "realistic satin, satin sheen, smooth satin surface, glossy satin",
        "velvet": "realistic velvet, velvet texture, plush velvet, soft velvet surface",
        "mesh": "realistic mesh, see-through mesh, mesh pattern, fishnet texture",
        "latex": "realistic latex, shiny latex, latex shine, rubber texture",
        "metal": "realistic metal, metallic surface, metal sheen, polished metal",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "material": (list(cls.MATERIALS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("material_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Realism Pro"

    def apply(self, prompt, material):
        m = self.MATERIALS.get(material, "")
        return (f"{prompt}, {m}",)


NODE_CLASS_MAPPINGS = {
    "PhotorealismMaximizer": PhotorealismMaximizer,
    "SkinRealismPro": SkinRealismPro,
    "HairRealismPro": HairRealismPro,
    "EyeRealismPro": EyeRealismPro,
    "AntiAIDetection": AntiAIDetection,
    "MaterialRealism": MaterialRealism,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PhotorealismMaximizer": "🎯 Photorealism Maximizer",
    "SkinRealismPro": "✨ Skin Realism Pro",
    "HairRealismPro": "💇 Hair Realism Pro",
    "EyeRealismPro": "👁️ Eye Realism Pro",
    "AntiAIDetection": "🛡️ Anti-AI Detection",
    "MaterialRealism": "🧵 Material Realism",
}
