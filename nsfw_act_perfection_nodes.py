"""
Mason's NSFW Act Perfection Nodes for ComfyUI
Specialized "Master" nodes for specific acts with fluid and physics logic.
"""

class DeepThroatMaster:
    """Advanced control for oral depth and reactions"""
    
    DEPTH = {
        "gag_reflex": "gagging, eyes watering, visible strain, choking, throat bulge",
        "deep_take": "taking it deep, throat fucking, balls deep in mouth, seamless deepthroat",
        "training": "practicing deepthroat, mouth stretched wide, resisting gag",
        "extreme_push": "face pushed into crotch, nose pressed against skin, muffled noises",
    }
    
    FLUID_INTERACTION = {
        "drool_mess": "thick saliva strings, slobber, wet chin, messy face",
        "tears": "tearing up, crying from depth, mascara running",
        "choking_cough": "coughing, sputtering, red face",
        "clean": "clean execution, professional, enthusiastic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "depth_mechanic": (list(cls.DEPTH.keys()),),
                "reaction": (list(cls.FLUID_INTERACTION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Act Perfection"

    def generate(self, prompt, depth_mechanic, reaction):
        d = self.DEPTH.get(depth_mechanic, "")
        r = self.FLUID_INTERACTION.get(reaction, "")
        
        positive = f"{prompt}, {d}, {r}"
        negative = "dry mouth, boring, bad anatomy"
        
        return (positive, negative)


class AnalSpecialist:
    """Specialized control for anal acts"""
    
    ACTION = {
        "insertion_start": "anal insertion, tip just inside, tight sphincter, stretching ring",
        "full_depth": "balls deep anal, ass swallowing cock, fully inserted",
        "gaping": "gaping anus, rosebud, stretched hole, after anal",
        "double_anal": "double anal, two dicks one hole, extreme stretching",
        "ass_to_mouth": "ass to mouth, atm, tasting ass",
    }
    
    DETAIL = {
        "lube_shine": "shiny lube, wet anus, dripping lube, oil",
        "rough_texture": "goosebumps on ass, red slap marks, gripped cheeks",
        "straining": "straining muscles, toes curled, arching back",
        "pleasure": "ahegao, eyes rolled back, drooling, immense pleasure",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "action": (list(cls.ACTION.keys()),),
                "detail": (list(cls.DETAIL.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Act Perfection"

    def generate(self, prompt, action, detail):
        a = self.ACTION.get(action, "")
        d = self.DETAIL.get(detail, "")
        
        positive = f"{prompt}, {a}, {d}"
        negative = "vaginal, wrong hole, bad anatomy"
        
        return (positive, negative)


class CreamPieMechanic:
    """Internal fluids and leakage logic"""
    
    TYPE = {
        "leaking": "leaking creampie, dripping cum, mess between legs",
        "overflowing": "overflowing creampie, cum gushing out, massive load",
        "filled": "stuffed with cum, belly bulge, full",
        "dried": "dried cum on thighs, crusty, aftercare",
    }
    
    VISCOSITY = {
        "thick": "thick white cum, opaque liquid, heavy texture",
        "runny": "runny cum, translucent mix, wet mess",
        "frothy": "frothy cum, bubbly, mixed fluids",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "type": (list(cls.TYPE.keys()),),
                "viscosity": (list(cls.VISCOSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fluid_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Act Perfection"

    def generate(self, prompt, type, viscosity):
        t = self.TYPE.get(type, "")
        v = self.VISCOSITY.get(viscosity, "")
        return (f"{prompt}, {t}, {v}",)


class FacialFinishPro:
    """Precision facial cumshot control"""
    
    TARGET = {
        "eyes_sealed": "cum sealing eyes shut, covered eyes, blinded by cum",
        "mouth_full": "mouth full of cum, leaking from corners, chipmunk cheeks",
        "hair_matted": "cum in hair, matted hair, sticky strands",
        "glazed_face": "glazed face, full face coating, bukkake aftermath",
        "glasses_covered": "cum on glasses, blinded, messy eyewear",
    }
    
    REACTION = {
        "surprise": "surprised expression, eyes wide, mouth open",
        "disgust": "disgusted face, tongue out, scrunching nose",
        "enjoyment": "licking lips, tasting, happy smile, thumbs up",
        "dazed": "dazed expression, thousand yard stare, mind break",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "target": (list(cls.TARGET.keys()),),
                "reaction": (list(cls.REACTION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Act Perfection"

    def generate(self, prompt, target, reaction):
        t = self.TARGET.get(target, "")
        r = self.REACTION.get(reaction, "")
        
        positive = f"{prompt}, {t}, {r}"
        negative = "clean face, no cum"
        
        return (positive, negative)


class PhysicsInteractionEngine:
    """Simulates physical mesh deformations via prompts"""
    
    INTERACTION = {
        "cheek_press": "cheek pressed against surface, squished face, glass press",
        "breast_squish": "breasts pressed together, cleavage squeeze, hands squeezing boobs",
        "butt_squeeze": "grabbing ass, fingers sinking into skin, firm grip",
        "thigh_compression": "thighs squished, sitting on thighs, crossed legs pressure",
    }
    
    SEVERITY = {
        "light": "light touch, slight indentation",
        "medium": "firm pressure, visible deformation",
        "heavy": "extreme pressure, flattened, distorted by force",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "interaction": (list(cls.INTERACTION.keys()),),
                "severity": (list(cls.SEVERITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("phys_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Act Perfection"

    def generate(self, prompt, interaction, severity):
        i = self.INTERACTION.get(interaction, "")
        s = self.SEVERITY.get(severity, "")
        return (f"{prompt}, {i}, {s}",)


NODE_CLASS_MAPPINGS = {
    "DeepThroatMaster": DeepThroatMaster,
    "AnalSpecialist": AnalSpecialist,
    "CreamPieMechanic": CreamPieMechanic,
    "FacialFinishPro": FacialFinishPro,
    "PhysicsInteractionEngine": PhysicsInteractionEngine,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepThroatMaster": "😮 Deep Throat Master",
    "AnalSpecialist": "🍩 Anal Specialist",
    "CreamPieMechanic": "🥧 Cream Pie Mechanic",
    "FacialFinishPro": "💦 Facial Finish Pro",
    "PhysicsInteractionEngine": "🤲 Physics Engine",
}
