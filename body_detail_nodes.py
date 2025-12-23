"""
Mason's Body Detail Nodes for ComfyUI
Replace body enhancement LoRAs with prompt engineering - SD 1.5 optimized
"""


class MuscleDefinitionController:
    """Control muscle definition levels"""
    
    DEFINITIONS = {
        "none": "no muscle definition, soft body, undefined muscles",
        "toned": "toned body, light muscle definition, fit appearance",
        "athletic": "athletic build, visible muscle tone, sporty physique",
        "defined": "defined muscles, clear muscle separation, fitness model",
        "ripped": "ripped muscles, very defined, low body fat, cut",
        "bodybuilder": "bodybuilder physique, extreme muscle mass, competition ready",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "definition": (list(cls.DEFINITIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("muscle_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Body Detail"

    def apply(self, prompt, definition):
        muscle = self.DEFINITIONS.get(definition, "")
        return (f"{prompt}, {muscle}",)


class AbsController:
    """Control abdominal definition"""
    
    ABS_LEVELS = {
        "none": "no visible abs, soft stomach, flat tummy",
        "flat": "flat stomach, slim waist, no definition",
        "hint": "hint of abs, slight definition, toned stomach",
        "four_pack": "four pack abs, upper ab definition, athletic core",
        "six_pack": "six pack abs, defined abdominal muscles, ripped core",
        "eight_pack": "eight pack abs, extreme definition, shredded abs",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "abs_level": (list(cls.ABS_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("abs_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Body Detail"

    def apply(self, prompt, abs_level):
        abs_desc = self.ABS_LEVELS.get(abs_level, "")
        return (f"{prompt}, {abs_desc}",)


class BodyProportionEnhancer:
    """Control body proportions and ratios"""
    
    WAIST_HIP = {
        "narrow_waist": "narrow waist, tiny waist, cinched waist, extreme hourglass",
        "defined_waist": "defined waist, clear waist curve, feminine shape",
        "natural": "natural waist, normal proportions, healthy shape",
        "straight": "straight waist, rectangular shape, athletic build",
    }
    
    HIPS = {
        "narrow": "narrow hips, slim hips, boyish figure",
        "moderate": "moderate hips, proportional, balanced",
        "wide": "wide hips, curvy hips, feminine hips",
        "very_wide": "very wide hips, extremely curvy, exaggerated curves",
    }
    
    SHOULDERS = {
        "narrow": "narrow shoulders, petite frame, delicate build",
        "balanced": "balanced shoulders, proportional, natural",
        "broad": "broad shoulders, wide shoulders, athletic frame",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "waist": (list(cls.WAIST_HIP.keys()),),
                "hips": (list(cls.HIPS.keys()),),
                "shoulders": (list(cls.SHOULDERS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("proportion_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Body Detail"

    def apply(self, prompt, waist, hips, shoulders):
        w = self.WAIST_HIP.get(waist, "")
        h = self.HIPS.get(hips, "")
        s = self.SHOULDERS.get(shoulders, "")
        return (f"{prompt}, {w}, {h}, {s}",)


class SkinShineController:
    """Control body skin shine and moisture"""
    
    SHINE_LEVELS = {
        "dry": "dry skin, matte skin, no shine, natural matte",
        "natural": "natural skin, slight sheen, healthy look",
        "sheen": "slight sheen, healthy glow, natural moisture",
        "glowing": "glowing skin, luminous body, radiant",
        "oiled": "oiled skin, body oil, glistening, massage oil look",
        "wet": "wet skin, water droplets, soaking wet, dripping",
        "sweaty": "sweaty skin, perspiration, workout sheen, glistening sweat",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "shine": (list(cls.SHINE_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("shine_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Body Detail"

    def apply(self, prompt, shine):
        sh = self.SHINE_LEVELS.get(shine, "")
        return (f"{prompt}, {sh}",)


class VeinVisibilityController:
    """Control vein visibility for athletic look"""
    
    VEIN_LEVELS = {
        "none": "no visible veins, smooth skin surface",
        "subtle": "subtle veins, faint vascular definition",
        "visible": "visible veins, vascular, athletic vascularity",
        "prominent": "prominent veins, very vascular, bodybuilder veins",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "visibility": (list(cls.VEIN_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("vein_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Body Detail"

    def apply(self, prompt, visibility):
        vein = self.VEIN_LEVELS.get(visibility, "")
        return (f"{prompt}, {vein}",)


class BodyHairController:
    """Control body hair appearance"""
    
    BODY_HAIR = {
        "smooth": "smooth skin, hairless, waxed, clean shaven body",
        "peach_fuzz": "peach fuzz, very fine body hair, barely visible",
        "light": "light body hair, minimal hair, natural sparse hair",
        "natural": "natural body hair, normal amount, authentic",
        "hairy": "hairy body, visible body hair, natural coverage",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "hair_level": (list(cls.BODY_HAIR.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("body_hair_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Body Detail"

    def apply(self, prompt, hair_level):
        hair = self.BODY_HAIR.get(hair_level, "")
        return (f"{prompt}, {hair}",)


class SweatController:
    """Control sweat and perspiration effects"""
    
    SWEAT_LEVELS = {
        "none": "dry skin, no sweat, cool and dry",
        "light_sheen": "light sweat sheen, slight perspiration, dewy",
        "workout": "workout sweat, exercising sweat, athletic perspiration",
        "heavy": "heavy sweat, dripping perspiration, soaked in sweat",
        "post_workout": "post-workout glow, cooling down, drying sweat",
    }
    
    AREAS = {
        "full_body": "sweat all over body, full body perspiration",
        "face_neck": "sweat on face and neck, facial perspiration",
        "chest": "sweat on chest, décolletage perspiration",
        "back": "sweat on back, back perspiration",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "sweat_level": (list(cls.SWEAT_LEVELS.keys()),),
                "area": (list(cls.AREAS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("sweat_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Body Detail"

    def apply(self, prompt, sweat_level, area):
        sweat = self.SWEAT_LEVELS.get(sweat_level, "")
        ar = self.AREAS.get(area, "")
        if sweat_level == "none":
            return (f"{prompt}, {sweat}",)
        return (f"{prompt}, {sweat}, {ar}",)


class TattooController:
    """Control tattoo appearance and placement"""
    
    STYLES = {
        "none": "no tattoos, clean skin, tattoo-free",
        "small_discrete": "small discrete tattoo, tiny tattoo, minimal ink",
        "tribal": "tribal tattoo, tribal design, bold black patterns",
        "floral": "floral tattoo, flower tattoo, botanical ink",
        "japanese": "Japanese tattoo, irezumi style, traditional Japanese",
        "blackwork": "blackwork tattoo, solid black designs, bold ink",
        "watercolor": "watercolor tattoo, colorful, artistic splashes",
        "realistic": "realistic tattoo, photorealistic ink, portrait tattoo",
        "script": "script tattoo, lettering, text tattoo, quote",
    }
    
    PLACEMENTS = {
        "arm": "arm tattoo, sleeve, bicep tattoo",
        "back": "back tattoo, spine tattoo, full back piece",
        "chest": "chest tattoo, sternum tattoo",
        "leg": "leg tattoo, thigh tattoo, calf tattoo",
        "shoulder": "shoulder tattoo, shoulder blade",
        "hip": "hip tattoo, side body tattoo",
        "multiple": "multiple tattoos, various placements, tattooed",
    }
    
    COVERAGE = {
        "single": "single tattoo, one piece",
        "few": "few tattoos, scattered ink",
        "moderate": "moderate tattoo coverage, several pieces",
        "heavily_tattooed": "heavily tattooed, extensive coverage, lots of ink",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.STYLES.keys()),),
                "placement": (list(cls.PLACEMENTS.keys()),),
                "coverage": (list(cls.COVERAGE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("tattoo_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Body Detail"

    def apply(self, prompt, style, placement, coverage):
        if style == "none":
            return (f"{prompt}, {self.STYLES.get('none', '')}",)
        st = self.STYLES.get(style, "")
        pl = self.PLACEMENTS.get(placement, "")
        cov = self.COVERAGE.get(coverage, "")
        return (f"{prompt}, {st}, {pl}, {cov}",)


NODE_CLASS_MAPPINGS = {
    "MuscleDefinitionController": MuscleDefinitionController,
    "AbsController": AbsController,
    "BodyProportionEnhancer": BodyProportionEnhancer,
    "SkinShineController": SkinShineController,
    "VeinVisibilityController": VeinVisibilityController,
    "BodyHairController": BodyHairController,
    "SweatController": SweatController,
    "TattooController": TattooController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MuscleDefinitionController": "💪 Muscle Definition",
    "AbsController": "🔥 Abs Controller",
    "BodyProportionEnhancer": "📐 Body Proportions",
    "SkinShineController": "✨ Skin Shine Controller",
    "VeinVisibilityController": "🩸 Vein Visibility",
    "BodyHairController": "🧔 Body Hair Controller",
    "SweatController": "💦 Sweat Controller",
    "TattooController": "🖋️ Tattoo Controller",
}
