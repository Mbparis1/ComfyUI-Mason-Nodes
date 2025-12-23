"""
Mason's Clothing Detail Nodes for ComfyUI
Replace clothing LoRAs with prompt engineering - SD 1.5 optimized
"""


class ClothingFitController:
    """Control how clothing fits the body"""
    
    FITS = {
        "skin_tight": "skin-tight clothing, second-skin fit, body-hugging, form-fitting",
        "tight": "tight clothing, fitted, snug fit, close to body",
        "fitted": "fitted clothing, tailored fit, following body contours",
        "relaxed": "relaxed fit clothing, comfortable fit, easy fit",
        "loose": "loose clothing, baggy, oversized fit",
        "oversized": "oversized clothing, very loose, baggy style, streetwear fit",
        "flowing": "flowing clothing, draping fabric, billowing, ethereal",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "fit": (list(cls.FITS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fit_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Clothing Detail"

    def apply(self, prompt, fit):
        f = self.FITS.get(fit, "")
        return (f"{prompt}, {f}",)


class ClothingWrinkleController:
    """Control clothing wrinkles and creases"""
    
    WRINKLES = {
        "pristine": "pristine clothing, no wrinkles, perfectly pressed, immaculate",
        "smooth": "smooth clothing, minimal wrinkles, well-maintained",
        "natural": "natural fabric folds, realistic creases, lived-in look",
        "wrinkled": "wrinkled clothing, creased fabric, rumpled",
        "heavily_wrinkled": "heavily wrinkled, very creased, disheveled fabric",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "wrinkle_level": (list(cls.WRINKLES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("wrinkle_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Clothing Detail"

    def apply(self, prompt, wrinkle_level):
        wr = self.WRINKLES.get(wrinkle_level, "")
        return (f"{prompt}, {wr}",)


class TransparencyController:
    """Control clothing transparency and sheerness"""
    
    TRANSPARENCIES = {
        "opaque": "opaque fabric, solid material, no transparency",
        "slightly_sheer": "slightly sheer, hint of skin visible, subtle transparency",
        "sheer": "sheer fabric, see-through material, transparent clothing",
        "very_sheer": "very sheer, highly transparent, barely there fabric",
        "mesh": "mesh fabric, net material, visible skin through mesh",
        "wet_look": "wet-look transparency, clinging wet fabric, visible through",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "transparency": (list(cls.TRANSPARENCIES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("transparency_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Clothing Detail"

    def apply(self, prompt, transparency):
        trans = self.TRANSPARENCIES.get(transparency, "")
        return (f"{prompt}, {trans}",)


class WetClothingController:
    """Control wet clothing effects"""
    
    WET_LEVELS = {
        "dry": "dry clothing, normal fabric, not wet",
        "damp": "damp clothing, slightly wet, moisture visible",
        "wet": "wet clothing, soaked fabric, clinging when wet",
        "soaking": "soaking wet clothing, dripping water, completely drenched",
        "transparent_wet": "wet transparent, see-through when wet, clinging wet fabric",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "wet_level": (list(cls.WET_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("wet_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Clothing Detail"

    def apply(self, prompt, wet_level):
        wet = self.WET_LEVELS.get(wet_level, "")
        return (f"{prompt}, {wet}",)


class ClothingDamageController:
    """Control clothing damage and wear"""
    
    DAMAGE_LEVELS = {
        "pristine": "pristine clothing, brand new, perfect condition",
        "worn": "worn clothing, slightly faded, well-worn",
        "distressed": "distressed clothing, intentional wear, fashion distressed",
        "ripped": "ripped clothing, torn fabric, holes in clothes",
        "tattered": "tattered clothing, very torn, heavily damaged, rags",
        "burned": "burned clothing, fire damage, scorched fabric",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "damage_level": (list(cls.DAMAGE_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("damage_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Clothing Detail"

    def apply(self, prompt, damage_level):
        dmg = self.DAMAGE_LEVELS.get(damage_level, "")
        return (f"{prompt}, {dmg}",)


class ClothingPatternController:
    """Control clothing patterns and prints"""
    
    PATTERNS = {
        "solid": "solid color clothing, single color, no pattern",
        "striped": "striped pattern, stripes, linear pattern",
        "plaid": "plaid pattern, checkered, tartan",
        "polka_dot": "polka dot pattern, dots, spotted",
        "floral": "floral pattern, flower print, botanical design",
        "animal_print": "animal print, leopard or zebra pattern, wild print",
        "geometric": "geometric pattern, shapes, modern print",
        "camouflage": "camouflage pattern, camo print, military pattern",
        "tie_dye": "tie-dye pattern, swirl colors, hippie style",
        "abstract": "abstract pattern, artistic print, unique design",
        "paisley": "paisley pattern, ornate design, bohemian",
        "houndstooth": "houndstooth pattern, classic check, sophisticated",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "pattern": (list(cls.PATTERNS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pattern_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Clothing Detail"

    def apply(self, prompt, pattern):
        pat = self.PATTERNS.get(pattern, "")
        return (f"{prompt}, {pat}",)


NODE_CLASS_MAPPINGS = {
    "ClothingFitController": ClothingFitController,
    "ClothingWrinkleController": ClothingWrinkleController,
    "TransparencyController": TransparencyController,
    "WetClothingController": WetClothingController,
    "ClothingDamageController": ClothingDamageController,
    "ClothingPatternController": ClothingPatternController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ClothingFitController": "👔 Clothing Fit",
    "ClothingWrinkleController": "👕 Clothing Wrinkles",
    "TransparencyController": "🔍 Transparency Controller",
    "WetClothingController": "💧 Wet Clothing",
    "ClothingDamageController": "🔥 Clothing Damage",
    "ClothingPatternController": "🎨 Clothing Pattern",
}
