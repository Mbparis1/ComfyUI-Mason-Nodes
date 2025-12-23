"""
Mason's Skin Detail Nodes for ComfyUI
Replace skin/beauty LoRAs with prompt engineering - SD 1.5 optimized
"""


class SkinTextureController:
    """Control skin texture appearance"""
    
    TEXTURES = {
        "porcelain": "porcelain skin, flawless smooth skin, doll-like perfection, no pores visible",
        "matte": "matte skin, non-reflective skin, soft matte finish, even skin texture",
        "dewy": "dewy skin, healthy glow, luminous skin, fresh moisturized appearance",
        "oily": "oily skin, shiny skin, reflective skin surface, glossy complexion",
        "natural": "natural skin texture, realistic skin, visible pores, slight imperfections",
        "textured": "textured skin, visible pores, realistic skin detail, natural imperfections",
        "freckled": "freckled skin, cute freckles, natural freckle pattern, sun-kissed freckles",
        "weathered": "weathered skin, mature skin texture, life-experienced look",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "texture": (list(cls.TEXTURES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("skin_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Skin Detail"

    def apply(self, prompt, texture):
        tex = self.TEXTURES.get(texture, "")
        return (f"{prompt}, {tex}",)


class MakeupDetailer:
    """Control foundation and base makeup"""
    
    FOUNDATION = {
        "none": "no makeup, bare face, natural skin",
        "light": "light makeup, natural look, minimal foundation, subtle enhancement",
        "natural": "natural makeup, even skin tone, light coverage foundation",
        "full_coverage": "full coverage foundation, flawless base, even complexion, airbrushed look",
        "dewy_finish": "dewy foundation, glowing base, luminous finish, healthy glow",
        "matte_finish": "matte foundation, shine-free, velvety finish, no oil",
        "heavy_glamour": "heavy glamour makeup, full glam, thick foundation, dramatic makeup",
    }
    
    CONTOURING = {
        "none": "",
        "subtle": "subtle contouring, natural shadows, slight definition",
        "defined": "defined contouring, sculpted cheekbones, shaped face",
        "dramatic": "dramatic contouring, strong shadows, chiseled look, heavy sculpting",
    }
    
    BLUSH = {
        "none": "",
        "light_pink": "light pink blush, rosy cheeks, subtle flush",
        "coral": "coral blush, warm peachy glow, sun-kissed cheeks",
        "berry": "berry blush, deep pink flush, bold cheek color",
        "bronzed": "bronzed blush, sun-kissed glow, warm bronze cheeks",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "foundation": (list(cls.FOUNDATION.keys()),),
                "contouring": (list(cls.CONTOURING.keys()),),
                "blush": (list(cls.BLUSH.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("makeup_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Skin Detail"

    def apply(self, prompt, foundation, contouring, blush):
        parts = [prompt, self.FOUNDATION.get(foundation, "")]
        if contouring != "none":
            parts.append(self.CONTOURING.get(contouring, ""))
        if blush != "none":
            parts.append(self.BLUSH.get(blush, ""))
        return (", ".join([p for p in parts if p]),)


class EyeMakeupController:
    """Control eye makeup in detail"""
    
    EYESHADOW = {
        "none": "no eyeshadow, bare eyelids",
        "nude": "nude eyeshadow, natural eye, subtle lid color",
        "smoky": "smoky eye, dark smoky eyeshadow, smudged eyeliner, sultry eye",
        "glitter": "glitter eyeshadow, sparkly lids, shimmery eye makeup",
        "colorful": "colorful eyeshadow, bold eye color, artistic eye makeup",
        "cut_crease": "cut crease eyeshadow, defined crease, sharp eyeshadow",
        "gradient": "gradient eyeshadow, blended colors, ombre eye",
    }
    
    EYELINER = {
        "none": "no eyeliner",
        "thin": "thin eyeliner, subtle line, natural definition",
        "winged": "winged eyeliner, cat eye, sharp wing, dramatic liner",
        "thick": "thick eyeliner, bold line, heavy liner",
        "smudged": "smudged eyeliner, smoky line, smeared liner, grunge look",
        "graphic": "graphic eyeliner, artistic liner, creative eye design",
    }
    
    LASHES = {
        "natural": "natural lashes, normal eyelashes",
        "mascara": "mascara, defined lashes, coated eyelashes, longer lashes",
        "false_natural": "false lashes, natural style, enhanced lashes",
        "dramatic": "dramatic false lashes, long lashes, voluminous lashes, heavy lashes",
        "wispy": "wispy lashes, fluttery false lashes, delicate lash look",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "eyeshadow": (list(cls.EYESHADOW.keys()),),
                "eyeliner": (list(cls.EYELINER.keys()),),
                "lashes": (list(cls.LASHES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("eye_makeup_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Skin Detail"

    def apply(self, prompt, eyeshadow, eyeliner, lashes):
        parts = [prompt]
        parts.append(self.EYESHADOW.get(eyeshadow, ""))
        parts.append(self.EYELINER.get(eyeliner, ""))
        parts.append(self.LASHES.get(lashes, ""))
        return (", ".join([p for p in parts if p]),)


class LipController:
    """Control lip appearance and makeup"""
    
    LIP_COLOR = {
        "natural": "natural lips, bare lips, no lipstick",
        "nude": "nude lipstick, natural lip color, MLBB shade",
        "pink": "pink lipstick, soft pink lips, feminine lip color",
        "red": "red lipstick, classic red lips, bold red",
        "berry": "berry lips, deep berry lipstick, wine colored lips",
        "coral": "coral lipstick, peachy orange lips, warm lip color",
        "plum": "plum lipstick, deep purple lips, dramatic lip color",
        "brown": "brown lipstick, nude brown lips, 90s lip",
    }
    
    LIP_FINISH = {
        "natural": "",
        "matte": "matte lips, velvet finish, non-glossy",
        "glossy": "glossy lips, lip gloss, shiny lips, wet look lips",
        "satin": "satin lips, soft sheen, semi-matte finish",
        "metallic": "metallic lips, shimmer lip, chrome finish",
    }
    
    LIP_SHAPE = {
        "natural": "",
        "overlined": "overlined lips, fuller appearance, enhanced lip shape",
        "cupids_bow": "defined cupid's bow, sharp lip peaks",
        "full": "full lips, plump lips, pouty lips",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "color": (list(cls.LIP_COLOR.keys()),),
                "finish": (list(cls.LIP_FINISH.keys()),),
                "shape": (list(cls.LIP_SHAPE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lip_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Skin Detail"

    def apply(self, prompt, color, finish, shape):
        parts = [prompt, self.LIP_COLOR.get(color, "")]
        if finish != "natural":
            parts.append(self.LIP_FINISH.get(finish, ""))
        if shape != "natural":
            parts.append(self.LIP_SHAPE.get(shape, ""))
        return (", ".join([p for p in parts if p]),)


class BlemishController:
    """Control skin blemishes and marks"""
    
    FRECKLES = {
        "none": "no freckles, clear skin",
        "light": "light freckles, sparse freckles, subtle freckle pattern",
        "moderate": "moderate freckles, natural freckle coverage",
        "heavy": "heavy freckles, lots of freckles, dense freckle pattern",
        "sun_spots": "sun spots, age spots, solar lentigines",
    }
    
    MOLES = {
        "none": "",
        "beauty_mark": "beauty mark, single mole, attractive mole placement",
        "multiple": "multiple moles, natural moles, scattered moles",
    }
    
    IMPERFECTIONS = {
        "flawless": "flawless skin, no blemishes, perfect skin",
        "minimal": "minimal imperfections, mostly clear skin",
        "natural": "natural skin imperfections, realistic skin, authentic look",
        "visible": "visible imperfections, realistic blemishes, authentic skin texture",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "freckles": (list(cls.FRECKLES.keys()),),
                "moles": (list(cls.MOLES.keys()),),
                "skin_condition": (list(cls.IMPERFECTIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("blemish_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Skin Detail"

    def apply(self, prompt, freckles, moles, skin_condition):
        parts = [prompt, self.FRECKLES.get(freckles, "")]
        if moles != "none":
            parts.append(self.MOLES.get(moles, ""))
        parts.append(self.IMPERFECTIONS.get(skin_condition, ""))
        return (", ".join([p for p in parts if p]),)


class SkinAgeEffects:
    """Control skin age-related appearance"""
    
    SKIN_AGE = {
        "youthful": "youthful skin, young skin, smooth texture, firm skin, no wrinkles",
        "young_adult": "young adult skin, healthy skin, minimal lines, fresh appearance",
        "mature_glow": "mature glowing skin, well-maintained, slight character lines",
        "natural_aging": "natural aging, fine lines, authentic skin texture",
        "mature": "mature skin, visible lines, experienced appearance, aged gracefully",
    }
    
    FIRMNESS = {
        "very_firm": "very firm skin, tight skin, no sagging, taut",
        "firm": "firm skin, good elasticity, youthful firmness",
        "natural": "natural skin firmness, age-appropriate tone",
        "soft": "soft skin, relaxed skin tone, gentle features",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "skin_age": (list(cls.SKIN_AGE.keys()),),
                "firmness": (list(cls.FIRMNESS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("age_effect_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Skin Detail"

    def apply(self, prompt, skin_age, firmness):
        age = self.SKIN_AGE.get(skin_age, "")
        firm = self.FIRMNESS.get(firmness, "")
        return (f"{prompt}, {age}, {firm}",)


class TanLineController:
    """Control tan lines and sun exposure effects"""
    
    TAN_TYPES = {
        "none": "even skin tone, no tan lines, uniform coloring",
        "bikini": "bikini tan lines, swimsuit tan marks, visible tan contrast",
        "one_piece": "one-piece swimsuit tan lines, tank top tan",
        "strapless": "strapless tan lines, no strap marks, tube top tan",
        "sports_bra": "sports bra tan lines, athletic wear tan marks",
        "thong": "thong tan lines, minimal coverage tan, high contrast",
        "nude_tan": "nude tan, all-over tan, no visible tan lines",
    }
    
    INTENSITY = {
        "subtle": "subtle tan lines, faint contrast, light tan marks",
        "moderate": "moderate tan lines, visible contrast, clear tan marks",
        "strong": "strong tan lines, high contrast, very visible, sharp edges",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "tan_type": (list(cls.TAN_TYPES.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("tan_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Skin Detail"

    def apply(self, prompt, tan_type, intensity):
        tan = self.TAN_TYPES.get(tan_type, "")
        intense = self.INTENSITY.get(intensity, "")
        if tan_type == "none":
            return (f"{prompt}, {tan}",)
        return (f"{prompt}, {tan}, {intense}",)


NODE_CLASS_MAPPINGS = {
    "SkinTextureController": SkinTextureController,
    "MakeupDetailer": MakeupDetailer,
    "EyeMakeupController": EyeMakeupController,
    "LipController": LipController,
    "BlemishController": BlemishController,
    "SkinAgeEffects": SkinAgeEffects,
    "TanLineController": TanLineController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SkinTextureController": "🧴 Skin Texture Controller",
    "MakeupDetailer": "💄 Makeup Detailer",
    "EyeMakeupController": "👁️ Eye Makeup Controller",
    "LipController": "💋 Lip Controller",
    "BlemishController": "⚫ Blemish Controller",
    "SkinAgeEffects": "✨ Skin Age Effects",
    "TanLineController": "☀️ Tan Line Controller",
}
