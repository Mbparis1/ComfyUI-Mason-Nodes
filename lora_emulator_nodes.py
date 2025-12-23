"""
Mason's LoRA Emulator Nodes for ComfyUI
Replicate popular LoRA effects through prompt engineering combinations
Zero VRAM overhead - SD 1.5 optimized
"""


class DetailEnhancerLoRA:
    """Emulates detail/quality enhancement LoRAs like 'add_detail' or 'more_details'"""
    
    STRENGTH = {
        "subtle": 0.3,
        "light": 0.5,
        "medium": 0.7,
        "strong": 0.9,
        "maximum": 1.0,
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "strength": (list(cls.STRENGTH.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, strength):
        s = self.STRENGTH.get(strength, 0.7)
        
        # Base detail enhancement
        base_details = "highly detailed, intricate details, fine details"
        
        # Scale prompts based on strength
        if s >= 0.9:
            detail_prompt = (
                f"{prompt}, extremely detailed, ultra detailed, hyper detailed, "
                "intricate details everywhere, fine texture details, "
                "detailed skin texture, detailed fabric texture, detailed background, "
                "sharp focus, tack sharp, 8k uhd, high resolution, masterpiece quality"
            )
        elif s >= 0.7:
            detail_prompt = (
                f"{prompt}, highly detailed, very detailed, intricate details, "
                "fine details visible, detailed textures, sharp focus, "
                "high quality, professional quality"
            )
        elif s >= 0.5:
            detail_prompt = (
                f"{prompt}, detailed, good details, clear details, "
                "sharp, high quality"
            )
        else:
            detail_prompt = f"{prompt}, detailed, sharp focus"
        
        negative = "blurry, low quality, low resolution, pixelated, jpeg artifacts, noise"
        
        return (detail_prompt, negative)


class SkinTextureLoRA:
    """Emulates skin texture/realism LoRAs"""
    
    SKIN_TYPE = {
        "flawless_beauty": "flawless",
        "natural_realistic": "natural",
        "hyperrealistic": "hyper",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "skin_type": (list(cls.SKIN_TYPE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, skin_type):
        if skin_type == "flawless_beauty":
            skin_prompt = (
                f"{prompt}, flawless skin, perfect skin, smooth porcelain skin, "
                "beauty photography skin, magazine cover skin, retouched skin, "
                "glowing complexion, even skin tone, no blemishes"
            )
            negative = "acne, blemishes, wrinkles, skin imperfections, pores"
            
        elif skin_type == "hyperrealistic":
            skin_prompt = (
                f"{prompt}, hyperrealistic skin, ultra realistic skin texture, "
                "visible pores, subsurface scattering, skin translucency, "
                "natural skin oils, fine vellus hair on skin, realistic imperfections, "
                "authentic human skin, dermatologically accurate"
            )
            negative = "plastic skin, fake skin, waxy skin, painted skin, airbrushed"
            
        else:  # natural_realistic
            skin_prompt = (
                f"{prompt}, natural skin, realistic skin texture, "
                "healthy skin, subtle pores, natural complexion, "
                "authentic skin appearance, genuine skin texture"
            )
            negative = "plastic skin, fake skin, over-retouched, artificial skin"
        
        return (skin_prompt, negative)


class PhotorealismLoRA:
    """Emulates photorealism LoRAs - the most powerful emulation"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "intensity": (["light", "medium", "strong", "ultimate"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, intensity):
        if intensity == "ultimate":
            pos = (
                f"{prompt}, photorealistic, hyperrealistic, ultra realistic photograph, "
                "indistinguishable from real photo, professional photography, "
                "natural skin with pores and imperfections, subsurface scattering, "
                "realistic eye reflections, realistic hair strands, natural lighting, "
                "8k uhd, shot on Canon EOS R5, 85mm lens, raw photo, unprocessed, "
                "no filters, genuine photograph, award winning photography, "
                "detailed skin texture, detailed eyes, detailed hair, "
                "anatomically correct, natural proportions"
            )
            neg = (
                "cartoon, anime, illustration, painting, drawing, sketch, "
                "3d render, cgi, fake, artificial, plastic, airbrushed, "
                "oversaturated, overexposed, underexposed, blurry, "
                "bad anatomy, deformed, mutated, extra limbs"
            )
            
        elif intensity == "strong":
            pos = (
                f"{prompt}, photorealistic, hyperrealistic, ultra realistic photo, "
                "professional photography, natural skin texture, realistic pores, "
                "realistic lighting, subsurface scattering, 8k uhd, dslr quality, "
                "raw photo, detailed, sharp focus"
            )
            neg = (
                "cartoon, anime, illustration, painting, 3d render, cgi, "
                "fake, artificial, blurry, bad anatomy"
            )
            
        elif intensity == "medium":
            pos = (
                f"{prompt}, photorealistic, realistic photo, natural looking, "
                "professional photography, realistic lighting, detailed, sharp"
            )
            neg = "cartoon, anime, illustration, painting, blurry"
            
        else:  # light
            pos = f"{prompt}, photorealistic, realistic, natural looking, detailed"
            neg = "cartoon, anime, illustration"
        
        return (pos, neg)


class GlamourLoRA:
    """Emulates glamour/beauty photography LoRAs"""
    
    STYLE = {
        "soft_glamour": "soft",
        "high_fashion": "fashion",
        "playboy_style": "playboy",
        "boudoir": "boudoir",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.STYLE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, style):
        if style == "soft_glamour":
            pos = (
                f"{prompt}, glamour photography, soft glamour lighting, "
                "beauty photography, soft focus beauty, polished look, "
                "flawless skin, professional glamour, magazine quality, "
                "studio lighting, beauty dish lighting"
            )
        elif style == "high_fashion":
            pos = (
                f"{prompt}, high fashion photography, vogue style, "
                "editorial fashion, runway quality, avant-garde, "
                "dramatic lighting, fashion model, designer aesthetic, "
                "magazine cover quality"
            )
        elif style == "playboy_style":
            pos = (
                f"{prompt}, playboy photography style, classic glamour, "
                "centerfold quality, smooth lighting, flawless skin, "
                "sensual yet classy, professional adult photography, "
                "soft shadows, beauty lighting"
            )
        else:  # boudoir
            pos = (
                f"{prompt}, boudoir photography, intimate lighting, "
                "romantic atmosphere, soft sensual lighting, "
                "private photography session, bedroom photography, "
                "tasteful intimate, warm lighting"
            )
        
        neg = (
            "amateur, low quality, harsh lighting, unflattering, "
            "bad skin, blemishes, poorly lit, snapshot"
        )
        
        return (pos, neg)


class BodyEnhancementLoRA:
    """Emulates body enhancement/proportions LoRAs"""
    
    ENHANCEMENT = {
        "slim_fit": "slim",
        "athletic": "athletic",
        "curvy": "curvy",
        "voluptuous": "voluptuous",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "enhancement": (list(cls.ENHANCEMENT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, enhancement):
        if enhancement == "slim_fit":
            pos = (
                f"{prompt}, slim fit body, slender figure, thin waist, "
                "lean physique, model proportions, elegant figure, "
                "long legs, graceful body, delicate frame"
            )
        elif enhancement == "athletic":
            pos = (
                f"{prompt}, athletic body, toned muscles, fit physique, "
                "defined abs, muscular but feminine, sports model, "
                "strong and lean, visible muscle definition"
            )
        elif enhancement == "curvy":
            pos = (
                f"{prompt}, curvy body, hourglass figure, wide hips, "
                "narrow waist, full curves, womanly figure, "
                "generous proportions, classic curves"
            )
        else:  # voluptuous
            pos = (
                f"{prompt}, voluptuous body, full figure, large curves, "
                "generous bust, wide hips, thick thighs, "
                "abundant curves, full proportions"
            )
        
        neg = "bad anatomy, deformed body, disproportionate, mutated"
        
        return (pos, neg)


class FaceEnhancementLoRA:
    """Emulates face enhancement/beauty LoRAs"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "enhancement": (["natural_beauty", "model_perfect", "ethereal", "striking"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, enhancement):
        if enhancement == "natural_beauty":
            pos = (
                f"{prompt}, beautiful face, natural beauty, "
                "symmetrical features, clear skin, bright eyes, "
                "defined features, natural makeup, healthy glow"
            )
        elif enhancement == "model_perfect":
            pos = (
                f"{prompt}, model face, perfect features, "
                "high cheekbones, defined jawline, pouty lips, "
                "striking eyes, flawless complexion, "
                "magazine cover face, supermodel features"
            )
        elif enhancement == "ethereal":
            pos = (
                f"{prompt}, ethereal beauty, angelic face, "
                "delicate features, luminous skin, doe eyes, "
                "soft features, dreamy beauty, fairy-like"
            )
        else:  # striking
            pos = (
                f"{prompt}, striking face, bold features, "
                "dramatic bone structure, intense eyes, "
                "powerful beauty, unique features, memorable face"
            )
        
        neg = (
            "ugly face, deformed face, asymmetric face, bad eyes, "
            "crossed eyes, bad skin, blemishes"
        )
        
        return (pos, neg)


class EyeEnhancementLoRA:
    """Emulates eye enhancement LoRAs"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (["captivating", "detailed_realistic", "anime_influenced", "sultry"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, style):
        if style == "captivating":
            pos = (
                f"{prompt}, captivating eyes, mesmerizing gaze, "
                "beautiful eyes, expressive eyes, soulful eyes, "
                "bright clear eyes, detailed iris, catchlights"
            )
        elif style == "detailed_realistic":
            pos = (
                f"{prompt}, hyperrealistic eyes, incredibly detailed iris, "
                "visible iris fibers, realistic reflections in eyes, "
                "natural eye veins in sclera, photorealistic eye detail, "
                "moist eyes, natural catchlights"
            )
        elif style == "anime_influenced":
            pos = (
                f"{prompt}, large expressive eyes, anime-style eyes, "
                "sparkling eyes, bright colored iris, "
                "highlighted eyes, glossy eyes"
            )
        else:  # sultry
            pos = (
                f"{prompt}, sultry eyes, bedroom eyes, seductive gaze, "
                "half-lidded eyes, smoky eyes, intense stare, "
                "alluring eyes, mysterious gaze"
            )
        
        neg = "bad eyes, deformed eyes, asymmetric eyes, crossed eyes, empty eyes"
        
        return (pos, neg)


class LoRAStackEmulator:
    """
    Ultimate LoRA stack emulator - combines multiple effects like using multiple LoRAs
    This is the most powerful node for LoRA replacement
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "photorealism": (["off", "light", "medium", "strong"],),
                "detail_level": (["off", "subtle", "medium", "high"],),
                "skin_quality": (["off", "natural", "flawless", "hyperreal"],),
                "glamour_style": (["off", "soft", "fashion", "boudoir"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "emulate_stack"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate_stack(self, prompt, photorealism, detail_level, skin_quality, glamour_style):
        pos_parts = [prompt]
        neg_parts = []
        
        # Photorealism
        if photorealism != "off":
            realism_map = {
                "light": "photorealistic, realistic",
                "medium": "photorealistic, hyperrealistic, realistic photo, natural skin",
                "strong": (
                    "photorealistic, hyperrealistic, ultra realistic photograph, "
                    "8k uhd, dslr quality, raw photo, subsurface scattering"
                ),
            }
            pos_parts.append(realism_map.get(photorealism, ""))
            neg_parts.append("cartoon, anime, illustration, painting, 3d render")
        
        # Detail
        if detail_level != "off":
            detail_map = {
                "subtle": "detailed, sharp focus",
                "medium": "highly detailed, intricate details, sharp",
                "high": "extremely detailed, hyper detailed, intricate details everywhere, masterpiece",
            }
            pos_parts.append(detail_map.get(detail_level, ""))
            neg_parts.append("blurry, low quality, low resolution")
        
        # Skin
        if skin_quality != "off":
            skin_map = {
                "natural": "natural skin, realistic skin texture, healthy skin",
                "flawless": "flawless skin, perfect skin, smooth porcelain skin, glowing",
                "hyperreal": "hyperrealistic skin, visible pores, subsurface scattering, skin translucency",
            }
            pos_parts.append(skin_map.get(skin_quality, ""))
            neg_parts.append("bad skin, plastic skin, artificial")
        
        # Glamour
        if glamour_style != "off":
            glamour_map = {
                "soft": "glamour photography, soft lighting, beauty lighting",
                "fashion": "high fashion photography, editorial, vogue style, magazine quality",
                "boudoir": "boudoir photography, intimate lighting, romantic atmosphere",
            }
            pos_parts.append(glamour_map.get(glamour_style, ""))
            neg_parts.append("amateur, poorly lit, unflattering")
        
        positive = ", ".join([p for p in pos_parts if p])
        negative = ", ".join([n for n in neg_parts if n])
        
        if not negative:
            negative = "low quality, bad anatomy"
        
        return (positive, negative)


NODE_CLASS_MAPPINGS = {
    "DetailEnhancerLoRA": DetailEnhancerLoRA,
    "SkinTextureLoRA": SkinTextureLoRA,
    "PhotorealismLoRA": PhotorealismLoRA,
    "GlamourLoRA": GlamourLoRA,
    "BodyEnhancementLoRA": BodyEnhancementLoRA,
    "FaceEnhancementLoRA": FaceEnhancementLoRA,
    "EyeEnhancementLoRA": EyeEnhancementLoRA,
    "LoRAStackEmulator": LoRAStackEmulator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DetailEnhancerLoRA": "🔧 Detail Enhancer (LoRA Emulator)",
    "SkinTextureLoRA": "✨ Skin Texture (LoRA Emulator)",
    "PhotorealismLoRA": "📷 Photorealism (LoRA Emulator)",
    "GlamourLoRA": "💄 Glamour (LoRA Emulator)",
    "BodyEnhancementLoRA": "💪 Body Enhancement (LoRA Emulator)",
    "FaceEnhancementLoRA": "👸 Face Enhancement (LoRA Emulator)",
    "EyeEnhancementLoRA": "👁️ Eye Enhancement (LoRA Emulator)",
    "LoRAStackEmulator": "⚡ LoRA Stack Emulator (ULTIMATE)",
}
