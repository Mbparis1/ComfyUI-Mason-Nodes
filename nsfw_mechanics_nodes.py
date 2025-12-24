"""
Mason's NSFW Mechanics Nodes for ComfyUI
Deep anatomical control and specific mechanics - SD 1.5 optimized
"""

class OralTechniqueMaster:
    """Hyper-specific control for oral sex techniques"""
    
    TECHNIQUE = {
        "vacuum_seal": "vacuum seal technique, suction focus, hollow cheeks, extreme suction",
        "deep_throat_training": "deep throat training, pushing past gag reflex, tears in eyes, wet chin",
        "ball_cupping": "cupping balls, fondling testicles, hand under balls",
        "double_hand_twist": "two handed twist, double hand grip, milking motion",
        "eye_contact_hold": "maintaining eye contact, looking up, subservient gaze",
        "sloppy_mess": "sloppy technique, lots of spit, drool strings, messy face",
        "teasing_tip": "teasing the tip, tongue swirls, just the head, licking frenulum",
        "throat_bulge": "visible throat bulge, swallowing shape, neck distension",
    }
    
    INTENSITY = {
        "sensual": "sensual pace, savouring, slow licks",
        "enthusiastic": "enthusiastic bobbing, eager, active",
        "aggressive": "aggressive face fucking, forced depth, choking",
        "worship": "worshipping, devout, treating like god",
        "desperate": "desperate, need it, begging for it",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "technique": (list(cls.TECHNIQUE.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Mechanics"

    def generate(self, prompt, technique, intensity):
        tech = self.TECHNIQUE.get(technique, "")
        inten = self.INTENSITY.get(intensity, "")
        
        positive = f"{prompt}, {tech}, {inten}"
        negative = "dry mouth, boring, passive, bad anatomy"
        
        return (positive, negative)


class PenetrationMechanics:
    """Physics and mechanics of penetration"""
    
    MOTION = {
        "grinding": "grinding hips, circular motion, rubbing clit",
        "pounding": "pounding hard, slapping skin, balls slapping",
        "slow_slide": "slow sliding, inch by inch, feeling texture",
        "jackhammer": "jackhammer speed, blur motion, intense fucking",
        "bottoming_out": "bottoming out, hitting cervix, too deep",
    }
    
    INTERNAL_FIT = {
        "tight_fit": "tight fit, gripping, skin stretching",
        "loose_gap": "loose gap, cavernous, gaping",
        "perfect_mold": "perfect mold, wrapping around, suction",
        "stretching_limit": "stretching to limit, white skin, tearing sensation",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "motion": (list(cls.MOTION.keys()),),
                "internal_fit": (list(cls.INTERNAL_FIT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Mechanics"

    def generate(self, prompt, motion, internal_fit):
        mot = self.MOTION.get(motion, "")
        fit = self.INTERNAL_FIT.get(internal_fit, "")
        
        return (f"{prompt}, {mot}, {fit}", "bad physics, clipping, floating")


class AnalSpecialist:
    """Specific mechanics for anal play"""
    
    PREP_STAGE = {
        "lube_application": "applying lube, shiny hole, dripping lube, oiling up",
        "finger_stretching": "stretching with fingers, one finger, two fingers, prying open",
        "toy_warmup": "anal plug warmup, training plug, jewel plug",
        "cleaning": "enema prep, clean hole, shower scene",
    }
    
    CONDITION = {
        "tight_virgin": "tight virgin hole, resistance, pucker",
        "relaxed": "relaxed muscle, easy entry, willing",
        "rosebud": "rosebud, prolapse, pink sock, inside out",
        "gaping_aftermath": "gaping hole, staying open, twitching, used hole",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "prep_stage": (list(cls.PREP_STAGE.keys()),),
                "condition": (list(cls.CONDITION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Mechanics"

    def generate(self, prompt, prep_stage, condition):
        prep = self.PREP_STAGE.get(prep_stage, "")
        cond = self.CONDITION.get(condition, "")
        
        return (f"{prompt}, {prep}, {cond}", "poop, dirty, messy, blood")


class SexualDynamicsMaster:
    """The emotional and physical vibe of the act"""
    
    DYNAMIC = {
        "rough_domination": "rough sex, pulling hair, choking, slapping, domination",
        "gentle_romance": "romantic sex, kissing, holding hands, eye contact, love making",
        "primal_lust": "primal lust, animalistic, sweating, biting, scratching",
        "breeding_intent": "breeding sex, filling up, creampie focus, impregnation",
        "lazy_morning": "lazy morning sex, sleepy, messy hair, sunlight, slow",
        "drunk_sloppy": "drunk sex, sloppy, uncoordinated, messy, inhibitions lost",
    }
    
    FACIAL_REACTION = {
        "ahegao_extreme": "extreme ahegao, crossed eyes, tongue out, drooling",
        "biting_lip": "biting lower lip, holding back moan, pleasure pain",
        "eyes_rolled_back": "eyes rolled back, white eyes, unconscious from pleasure",
        "crying_pleasure": "crying from pleasure, tears streaming, happy tears",
        "angry_sex": "angry face, scowl, hate fucking, intense stare",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "dynamic": (list(cls.DYNAMIC.keys()),),
                "facial_reaction": (list(cls.FACIAL_REACTION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Mechanics"

    def generate(self, prompt, dynamic, facial_reaction):
        dyn = self.DYNAMIC.get(dynamic, "")
        face = self.FACIAL_REACTION.get(facial_reaction, "")
        
        return (f"{prompt}, {dyn}, {face}", "bored face, emotionless, dead eyes")


class CumShotMechanics:
    """Physics of ejaculation"""
    
    TRAJECTORY = {
        "shooting_rope": "shooting ropes, high velocity cum, flying through air, projectile",
        "dribbling_leak": "leaking out, dribbling down, gravity flow, oozing",
        "explosive_burst": "explosive burst, covering everything, massive load",
        "internal_pump": "pumping inside, filling up, belly bulge from cum",
    }
    
    CONSISTENCY = {
        "thick_white": "thick white cum, opaque, heavy consistency",
        "creamy": "creamy texture, milky, frothy",
        "watery_clear": "clear precum, watery, translucent",
        "sticky_strings": "sticky strings, connecting mouths, messy webs",
    }
    
    TARGET = {
        "eye_shot": "cum in eye, blinded by cum, blinking",
        "hair_glob": "cum in hair, matted hair, extraction",
        "tongue_catch": "catching on tongue, open mouth catch",
        "tits_coating": "glazed tits, covering breasts, dripping nipples",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "trajectory": (list(cls.TRAJECTORY.keys()),),
                "consistency": (list(cls.CONSISTENCY.keys()),),
                "target": (list(cls.TARGET.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Mechanics"

    def generate(self, prompt, trajectory, consistency, target):
        traj = self.TRAJECTORY.get(trajectory, "")
        const = self.CONSISTENCY.get(consistency, "")
        targ = self.TARGET.get(target, "")
        
        return (f"{prompt}, {traj}, {const}, {targ}", "blood, urine, feces")


NODE_CLASS_MAPPINGS = {
    "OralTechniqueMaster": OralTechniqueMaster,
    "PenetrationMechanics": PenetrationMechanics,
    "AnalSpecialist": AnalSpecialist,
    "SexualDynamicsMaster": SexualDynamicsMaster,
    "CumShotMechanics": CumShotMechanics,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OralTechniqueMaster": "👅 Oral Technique Master",
    "PenetrationMechanics": "🔩 Penetration Mechanics",
    "AnalSpecialist": "🍩 Anal Specialist",
    "SexualDynamicsMaster": "❤️‍🔥 Sexual Dynamics Master",
    "CumShotMechanics": "💦 Cumshot Mechanics",
}
