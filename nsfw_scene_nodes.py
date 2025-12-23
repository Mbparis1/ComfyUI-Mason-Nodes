"""
Mason's NSFW Scene Nodes for ComfyUI
Scene and scenario control for adult content - SD 1.5 optimized
"""


class NSFWScenarioBuilder:
    """Build complete NSFW scenario descriptions"""
    
    SCENARIOS = {
        "bedroom_solo": "alone in bedroom, solo scene, private moment, intimate setting",
        "bedroom_couple": "couple in bedroom, intimate scene, romantic encounter",
        "shower": "in shower, water running, wet skin, steamy bathroom",
        "bathtub": "in bathtub, bubble bath, relaxing, wet and soapy",
        "pool": "at pool, wet skin, swimwear or nude, poolside",
        "beach": "at beach, sandy, tropical setting, swimwear",
        "studio_shoot": "professional studio shoot, glamour photography, posed",
        "boudoir": "boudoir setting, intimate photography, lingerie shoot",
        "massage": "massage scene, oil on skin, relaxing, sensual touch",
        "mirror": "in front of mirror, self-admiring, reflection visible",
        "outdoors": "outdoors, nature setting, exhibitionist, open air",
        "hotel": "hotel room, travel romance, hotel bedroom, temporary",
    }
    
    TIME = {
        "morning": "morning light, fresh awakening, sunrise glow",
        "afternoon": "afternoon light, warm daylight, golden",
        "evening": "evening, sunset, warm romantic light",
        "night": "night time, dark, intimate lighting",
        "candlelit": "candlelit, romantic flames, warm flickering",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "scenario": (list(cls.SCENARIOS.keys()),),
                "time_of_day": (list(cls.TIME.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scenario_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/NSFW Scenes"

    def build(self, prompt, scenario, time_of_day):
        scen = self.SCENARIOS.get(scenario, "")
        time = self.TIME.get(time_of_day, "")
        return (f"{prompt}, {scen}, {time}",)


class FetishElementController:
    """Control fetish and kink elements"""
    
    ELEMENTS = {
        "none": "",
        "stockings": "wearing stockings, thigh-high stockings, nylon",
        "heels": "wearing high heels, stilettos, sexy shoes",
        "collar": "wearing collar, neck collar, bondage collar",
        "cuffs": "wearing cuffs, wrist cuffs, restraints",
        "corset": "wearing corset, tight lacing, waist cinched",
        "latex": "wearing latex, shiny rubber, tight latex",
        "leather": "wearing leather, leather outfit, dominatrix",
        "lace": "wearing lace, delicate lace, see-through lace",
        "chains": "chains, chain accessory, metal chains",
        "blindfold": "wearing blindfold, eyes covered, sensory deprivation",
    }
    
    INTENSITY = {
        "subtle": "subtle, hint of, barely visible",
        "visible": "clearly visible, obvious, prominent",
        "dominant": "dominant element, main focus, emphasized",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "element": (list(cls.ELEMENTS.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fetish_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Scenes"

    def apply(self, prompt, element, intensity):
        elem = self.ELEMENTS.get(element, "")
        if not elem:
            return (prompt,)
        intense = self.INTENSITY.get(intensity, "")
        return (f"{prompt}, {elem}, {intense}",)


class DominanceController:
    """Control dominant/submissive dynamics"""
    
    ROLES = {
        "neutral": "",
        "dominant": "dominant pose, in control, powerful stance, alpha energy",
        "submissive": "submissive pose, yielding, vulnerable, passive",
        "playful_dom": "playfully dominant, teasing control, mischievous power",
        "willing_sub": "willingly submissive, eager to please, devoted",
        "switch": "switching dynamic, equal power, balanced interaction",
    }
    
    BODY_LANGUAGE = {
        "none": "",
        "standing_over": "standing over, looking down, towering",
        "kneeling_before": "kneeling before, looking up, below",
        "holding_down": "holding down, pinning, restraining",
        "being_held": "being held down, pinned, restrained",
        "presenting": "presenting self, offering, displaying",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "role": (list(cls.ROLES.keys()),),
                "body_language": (list(cls.BODY_LANGUAGE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("dynamic_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Scenes"

    def apply(self, prompt, role, body_language):
        r = self.ROLES.get(role, "")
        bl = self.BODY_LANGUAGE.get(body_language, "")
        parts = [prompt]
        if r:
            parts.append(r)
        if bl:
            parts.append(bl)
        return (", ".join(parts),)


class FluidEffectsController:
    """Control wet/fluid effects on body"""
    
    FLUID_TYPES = {
        "none": "",
        "water_droplets": "water droplets on skin, beaded water, fresh from shower",
        "sweat": "sweaty skin, perspiration, glistening sweat",
        "oil": "oiled skin, massage oil, shiny oiled body",
        "lotion": "lotion on skin, moisturized, creamy smooth",
        "soap": "soapy skin, lathered, bubble bath foam",
        "rain": "rain soaked, wet from rain, dripping",
    }
    
    COVERAGE = {
        "light": "light coverage, subtle sheen, barely visible",
        "moderate": "moderate coverage, visible wetness, glistening",
        "heavy": "heavy coverage, dripping wet, soaked",
        "artistic": "artistic placement, strategic drops, aesthetic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "fluid": (list(cls.FLUID_TYPES.keys()),),
                "coverage": (list(cls.COVERAGE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fluid_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Scenes"

    def apply(self, prompt, fluid, coverage):
        fl = self.FLUID_TYPES.get(fluid, "")
        if not fl:
            return (prompt,)
        cov = self.COVERAGE.get(coverage, "")
        return (f"{prompt}, {fl}, {cov}",)


class HairPlayController:
    """Control hair in sensual contexts"""
    
    HAIR_STATES = {
        "natural": "natural hair, as styled",
        "messy_bed": "messy bed hair, tousled, just woke up",
        "wet": "wet hair, dripping, slicked back",
        "windblown": "windblown hair, flowing, dynamic",
        "disheveled": "disheveled hair, wild, post-passion",
        "grabbed": "hair being grabbed, pulled, held",
        "covering": "hair covering body, draped over, hair as cover",
        "flipped": "hair flipped, hair toss, flowing motion",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "hair_state": (list(cls.HAIR_STATES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("hair_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Scenes"

    def apply(self, prompt, hair_state):
        hair = self.HAIR_STATES.get(hair_state, "")
        return (f"{prompt}, {hair}",)


class GazeIntensityController:
    """Control eye contact and gaze in sensual contexts"""
    
    GAZE_TYPES = {
        "direct_seductive": "seductive direct eye contact, bedroom eyes, inviting gaze",
        "looking_away_coy": "looking away coyly, shy glance, bashful",
        "eyes_closed_pleasure": "eyes closed in pleasure, lost in moment, ecstasy",
        "half_lidded": "half-lidded eyes, drowsy sensual, sleepy seductive",
        "looking_up": "looking up through lashes, doe eyes, innocent yet knowing",
        "looking_back": "looking back over shoulder, glancing behind, inviting",
        "intense_stare": "intense stare, piercing eyes, hypnotic gaze",
        "dreamy": "dreamy gaze, soft focus eyes, faraway look",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "gaze": (list(cls.GAZE_TYPES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("gaze_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Scenes"

    def apply(self, prompt, gaze):
        g = self.GAZE_TYPES.get(gaze, "")
        return (f"{prompt}, {g}",)


NODE_CLASS_MAPPINGS = {
    "NSFWScenarioBuilder": NSFWScenarioBuilder,
    "FetishElementController": FetishElementController,
    "DominanceController": DominanceController,
    "FluidEffectsController": FluidEffectsController,
    "HairPlayController": HairPlayController,
    "GazeIntensityController": GazeIntensityController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NSFWScenarioBuilder": "🔞 NSFW Scenario Builder",
    "FetishElementController": "⛓️ Fetish Element",
    "DominanceController": "👑 Dominance Controller",
    "FluidEffectsController": "💦 Fluid Effects",
    "HairPlayController": "💇 Hair Play",
    "GazeIntensityController": "👁️ Gaze Intensity",
}
