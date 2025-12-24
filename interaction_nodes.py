"""
Mason's Surface Physics & Interaction Nodes
Logic for physical contact and material reactions - SD 1.5 optimized
"""

class SkinInteractionMaster:
    """Controls visual cues for physical touch and pressure on skin"""
    
    INTERACTIONS = {
        "gentle_touch": "light touch on skin, gentle contact, fingers resting on skin",
        "firm_press": "firm pressure on skin, skin indentation, fingers pressing into skin",
        "squeezing": "squeezing skin, skin deformation, firm grip, visible pressure",
        "indentation": "deep skin indentation, finger marks on skin, pressure points",
        "skin_pinch": "skin being pinched, small skin fold, fingers grasping skin",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "interaction": (list(cls.INTERACTIONS.keys()),),
                "intensity": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0, "step": 0.1}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("interaction_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Physics"

    def apply(self, prompt, interaction, intensity):
        i = self.INTERACTIONS.get(interaction, "")
        if intensity > 1.2:
            i = f"heavy {i}, extreme pressure"
        elif intensity < 0.8:
            i = f"slight {i}, subtle contact"
        return (f"{prompt}, {i}",)

class FabricDynamics:
    """Controls how clothing interacts with the body and movement"""
    
    EFFECTS = {
        "tight_stretch": "fabric stretching over body, tight fit, material tension, fabric straining",
        "form_hug": "form-fitting fabric, hugging every curve, material following body contours",
        "pulling": "fabric being pulled, material tension from grasp, strained seams",
        "sheer_cling": "sheer fabric clinging to wet skin, material sticking to body, translucent wet look",
        "loose_drape": "loose fabric draping, material hanging naturally, soft folds",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "effect": (list(cls.EFFECTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fabric_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Physics"

    def apply(self, prompt, effect):
        e = self.EFFECTS.get(effect, "")
        return (f"{prompt}, {e}",)

class FluidInterfacer:
    """How fluids interact with and coat surfaces"""
    
    INTERACTIONS = {
        "pooling": "fluid pooling in crevices, liquid gathering on surface, thick coating",
        "dripping": "fluid dripping down skin, liquid trails, slow drips",
        "smeared": "smeared fluid on skin, messy coating, liquid spread across surface",
        "splattered": "fluid splatter, liquid droplets on skin, messy splatter pattern",
        "glistening_wet": "glistening wet surface, thin film of liquid, glossy sheen",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "interaction": (list(cls.INTERACTIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fluid_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Physics"

    def apply(self, prompt, interaction):
        i = self.INTERACTIONS.get(interaction, "")
        return (f"{prompt}, {i}",)

NODE_CLASS_MAPPINGS = {
    "SkinInteractionMaster": SkinInteractionMaster,
    "FabricDynamics": FabricDynamics,
    "FluidInterfacer": FluidInterfacer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SkinInteractionMaster": "🤝 Skin Interaction Master",
    "FabricDynamics": "👕 Fabric Dynamics",
    "FluidInterfacer": "💧 Fluid Interfacer",
}
