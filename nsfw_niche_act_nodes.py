"""
Mason's Niche NSFW Act & Dynamic Nodes for ComfyUI
Specific niche acts, roleplay dynamics, and detailed scenarios - SD 1.5 optimized
"""

class BDSMActController:
    """Controls BDSM dynamics and specific acts"""
    
    DYNAMIC = {
        "bondage": "bondage, rope bondage, shibari, tied up, restraints, bound wrists",
        "suspension": "suspension bondage, hanging, suspended in air, rope suspension",
        "spanking": "spanking, paddling, red butt, hand print on ass, impact play",
        "domination": "domination, dominating, standing over, foot on chest, superior pose",
        "submission": "submission, kneeling, bowing, begging, submissive pose",
        "pet_play": "pet play, puppy play, wearing collar, leash, on all fours",
        "gagged": "gagged, ball gag, ring gag, tape gag, silenced",
        "blindfolded": "blindfolded, eye mask, sensory deprivation",
    }
    
    INTENSITY = {
        "soft": "soft bondage, sensual, gentle restraint, playful",
        "moderate": "moderate intensity, firm restraints, strict",
        "hard": "hardcore, strict bondage, intense, severe",
        "extreme": "extreme bondage, tight ropes, heavy impact, cruel",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "dynamic": (list(cls.DYNAMIC.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Niche"

    def generate(self, prompt, dynamic, intensity):
        d = self.DYNAMIC.get(dynamic, "")
        i = self.INTENSITY.get(intensity, "")
        return (f"{prompt}, {d}, {i}", "vanilla, boring, loose ropes")


class RoleplayScenarioBuilder:
    """Builds specific roleplay scenarios with outfits and settings"""
    
    SCENARIO = {
        "teacher_student": "teacher student roleplay, classroom setting, naughty student, strict teacher",
        "nurse_patient": "nurse patient roleplay, hospital bed, sexy nurse uniform, medical exam",
        "boss_secretary": "boss secretary roleplay, office desk, skirt lifted, under desk",
        "maid_master": "maid master roleplay, french maid outfit, cleaning, serving",
        "police_arrest": "police roleplay, handcuffed, against car, sexy cop",
        "cheerleader": "cheerleader roleplay, locker room, pom poms, skirt",
        "gym_trainer": "gym trainer roleplay, yoga pants, workout equipment, spotting",
        "fantasy_elf": "fantasy roleplay, elf ears, fantasy armor, forest setting",
    }
    
    ACTION = {
        "seducing": "seducing, teasing, flirting, exposing",
        "caught": "caught in act, surprised, wardrobe malfunction",
        "punished": "being punished, detention, discipline",
        "rewarded": "being rewarded, good girl, earning it",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "scenario": (list(cls.SCENARIO.keys()),),
                "action": (list(cls.ACTION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Niche"

    def generate(self, prompt, scenario, action):
        s = self.SCENARIO.get(scenario, "")
        a = self.ACTION.get(action, "")
        return (f"{prompt}, {s}, {a}", "civilian clothes, boring setting")


class SoloPlayMaster:
    """Detailed control over solo acts and masturbation"""
    
    ACT = {
        "rubbing_clit": "rubbing clit, fingers on clit, masturbating, pleasure",
        "fingering_pussy": "fingering pussy, fingers inside, spreading lips",
        "anal_play": "anal play, fingers in ass, gaping",
        "stroking_cock": "stroking cock, jerking off, masturbating",
        "squeezing_breasts": "squeezing breasts, fondling tits, pinching nipples",
        "humping_pillow": "humping pillow, grinding, friction",
    }
    
    EXPRESSION = {
        "enjoyment": "enjoying, biting lip, eyes closed, smiling",
        "intense_orgasm": "orgasm face, arching back, toes curled, screaming",
        "teasing_camera": "looking at camera, teasing viewer, one finger",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "act": (list(cls.ACT.keys()),),
                "expression": (list(cls.EXPRESSION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Niche"

    def generate(self, prompt, act, expression):
        a = self.ACT.get(act, "")
        e = self.EXPRESSION.get(expression, "")
        return (f"{prompt}, {a}, {e}", "partner, two people")


class ToyController:
    """Specific sex toys and their usage"""
    
    TOY = {
        "dildo_realistic": "realistic dildo, flesh colored dildo, veins",
        "dildo_glass": "glass dildo, clear toy, crystal wand",
        "vibrator_wand": "magic wand vibrator, hitachi, buzzing",
        "vibrator_rabbit": "rabbit vibrator, dual stimulation",
        "butt_plug": "butt plug, jeweled plug, fox tail plug",
        "strap_on": "strap-on dildo, harness, pegging",
        "fucking_machine": "fucking machine, mechanical sex, machine thrusting",
        "beads": "anal beads, pull beads",
    }
    
    PLACEMENT = {
        "in_hand": "holding toy, showing toy",
        "inserting": "inserting toy, pushing in",
        "inside_pussy": "toy inside pussy, stuffed, filling",
        "inside_ass": "toy inside ass, anal plug inserted",
        "on_clit": "toy on clit, vibrating against clit",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "toy": (list(cls.TOY.keys()),),
                "placement": (list(cls.PLACEMENT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Niche"

    def generate(self, prompt, toy, placement):
        t = self.TOY.get(toy, "")
        p = self.PLACEMENT.get(placement, "")
        return (f"{prompt}, {t}, {p}", "bad anatomy")


class AftermathSceneController:
    """Controls the post-sex scene details"""
    
    DETAILS = {
        "cum_mess": "cum mess, covered in cum, dripping, puddle",
        "sweaty_exhausted": "sweaty body, exhausted, heavy breathing, messy hair",
        "disheveled_sheets": "messy bed, disheveled sheets, stained sheets",
        "cuddling": "cuddling, aftercare, holding each other, sleeping",
        "clothing_scattered": "clothes on floor, discarded clothing, underwear on floor",
        "cream_dripping": "creampie dripping, leaking, overflowing",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "details": (list(cls.DETAILS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Niche"

    def generate(self, prompt, details):
        d = self.DETAILS.get(details, "")
        return (f"{prompt}, {d}, aftermath", "clean, tidy")


class POVRealismPro:
    """Immersive POV specialized controller"""
    
    ACTION = {
        "grabbing_camera": "grabbing camera, holding camera, touching lens",
        "looking_at_viewer": "looking at viewer, eye contact, sultry gaze",
        "reaching_out": "reaching out to viewer, hand towards camera",
        "legs_over_shoulder": "legs over shoulders POV, looking down",
        "receiving_oral_pov": "receiving oral POV, looking down at head",
        "cum_on_lens": "cum on camera lens, blurred spots",
    }
    
    IMMERSION = {
        "high": "immersive, you are there, first person view",
        "fisheye": "fisheye lens, gropro style, wide angle POV",
        "phone_selfie": "mirror selfie, holding phone, phone screen visible",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "action": (list(cls.ACTION.keys()),),
                "immersion": (list(cls.IMMERSION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Niche"

    def generate(self, prompt, action, immersion):
        a = self.ACTION.get(action, "")
        i = self.IMMERSION.get(immersion, "")
        return (f"{prompt}, {a}, {i}, pov", "third person, tripod")


NODE_CLASS_MAPPINGS = {
    "BDSMActController": BDSMActController,
    "RoleplayScenarioBuilder": RoleplayScenarioBuilder,
    "SoloPlayMaster": SoloPlayMaster,
    "ToyController": ToyController,
    "AftermathSceneController": AftermathSceneController,
    "POVRealismPro": POVRealismPro,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BDSMActController": "⛓️ BDSM Act Controller",
    "RoleplayScenarioBuilder": "🎭 Roleplay Scenario Builder",
    "SoloPlayMaster": "🤳 Solo Play Master",
    "ToyController": "🧸 Sex Toy Controller",
    "AftermathSceneController": "🛏️ Aftermath Scene",
    "POVRealismPro": "👀 POV Realism Pro",
}
