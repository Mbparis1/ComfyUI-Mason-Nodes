"""
Mason's Surface Physics & Interaction Nodes for ComfyUI
Advanced control over skin, fluids, fabric, and soft body physics.
"""

class SkinPhysicsPro:
    """Advanced Skin Physics and Rendering"""
    
    TEXTURE = {
        "natural_pores": "high detailed skin texture, pores visible, micro details",
        "goosebumps": "goosebumps, cold skin, raised hair, reaction",
        "flushed": "flushed skin, reddish skin, blood flow, blushing",
        "veiny": "visible veins, vascularity, thin skin",
        "bruised": "bruised skin, rough skin, markings, discoloration",
        "perfect_smooth": "airbrushed skin, smooth texture, flawless",
    }
    
    SUBSURFACE = {
        "strong_scattering": "strong subsurface scattering, translucent skin, glowing skin",
        "waxy": "waxy skin, candle-like sheen, artificial softness",
        "sweaty": "sweat sheen, oily skin, wet skin, glistening",
        "matte": "matte finish, dry skin, powdery look",
        "radiant": "radiant skin, healthy glow, inner light",
    }
    
    INTERACTION = {
        "indentation": "skin indentation, finger marks, pressure marks, pressed skin",
        "stretching": "stretched skin, tight skin, pulled skin",
        "wrinkling": "wrinkled skin, folded skin, compressed skin",
        "redness": "red marks, slap marks, hand print, reaction redness",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "texture": (list(cls.TEXTURE.keys()),),
                "subsurface": (list(cls.SUBSURFACE.keys()),),
                "interaction": (list(cls.INTERACTION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Physics & Interaction"

    def generate(self, prompt, texture, subsurface, interaction):
        t = self.TEXTURE.get(texture, "")
        s = self.SUBSURFACE.get(subsurface, "")
        i = self.INTERACTION.get(interaction, "")
        
        positive = f"{prompt}, {t}, {s}, {i}"
        negative = "plastic skin, plastic doll, overly smooth, blurring"
        
        return (positive, negative)


class FluidDynamicsPro:
    """Liquid Physics and Wet Effects"""
    
    TYPE = {
        "sweat": "heavy sweat, beads of sweat, trickling sweat, drenched",
        "water": "water droplets, wet body, rain drops, soaked",
        "oil": "baby oil, massage oil, slick body, high gloss",
        "lotion": "white lotion, creamy fluid, smeared lotion",
        "viscous": "viscous fluid, slime, thick liquid, sticky",
        "milk": "milk bath, white liquid, milky covering",
    }
    
    BEHAVIOR = {
        "running": "running liquid, drips running down, trails on skin",
        "beading": "water beading, hydrophobic skin, droplets sitting on skin",
        "pooling": "pooling liquid, accumulated fluid, puddles",
        "splashing": "splashing, liquid impact, frozen motion splash",
        "clinging": "fluid clinging to curves, surface tension",
    }
    
    COVERAGE = {
        "light_mist": "light mist, sprayed, misty",
        "damp": "damp skin, slightly wet, moist",
        "soaked": "completely soaked, drenched from head to toe",
        "dripping": "dripping wet, overflow, pouring off",
        "submerged": "underwater, submerged, floating in liquid",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "fluid_type": (list(cls.TYPE.keys()),),
                "behavior": (list(cls.BEHAVIOR.keys()),),
                "coverage": (list(cls.COVERAGE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Physics & Interaction"

    def generate(self, prompt, fluid_type, behavior, coverage):
        t = self.TYPE.get(fluid_type, "")
        b = self.BEHAVIOR.get(behavior, "")
        c = self.COVERAGE.get(coverage, "")
        
        positive = f"{prompt}, {t}, {b}, {c}"
        negative = "bad water, bad liquid, pixelated liquid"
        
        return (positive, negative)


class FabricPhysicsPro:
    """Clothing Physics and Interaction"""
    
    MATERIAL = {
        "cotton": "cotton fabric, soft folds, matte textile",
        "silk": "silk fabric, shiny, flowing, smooth drapes",
        "latex": "latex, tight rubber, glossy, reflection, form fitting",
        "leather": "leather, stiff folds, textured leather, shiny",
        "sheer": "sheer fabric, see-through, transparent cloth, gauze",
        "denim": "denim, stiff fabric, rough texture, jeans",
    }
    
    STATE = {
        "loose": "loose fit, hanging loosely, draped",
        "tight": "skin tight, bursting seams, straining fabric",
        "wet": "wet clothes, clinging to body, translucent when wet",
        "torn": "ripped clothes, torn fabric, distressed, shredded",
        "unzipped": "unzipped, open clothes, falling off shoulders",
        "crumpled": "crumpled clothes, messy pile, discarded clothes",
    }
    
    INTERACTION = {
        "bunching": "bunching up, gathered fabric, folds",
        "stretching": "stretched fabric, tension lines, pulling",
        "gap": "clothing gap, peekaboo, lifted skirt",
        "falling": "clothes falling down, wardrobe malfunction",
        "grabbing": "hand grabbing clothes, pulling fabric, fistful of cloth",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "material": (list(cls.MATERIAL.keys()),),
                "state": (list(cls.STATE.keys()),),
                "interaction": (list(cls.INTERACTION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Physics & Interaction"

    def generate(self, prompt, material, state, interaction):
        m = self.MATERIAL.get(material, "")
        s = self.STATE.get(state, "")
        i = self.INTERACTION.get(interaction, "")
        
        positive = f"{prompt}, {m}, {s}, {i}"
        negative = "melting clothes, fused clothes"
        
        return (positive, negative)


class SoftBodyPro:
    """Soft Body Physics and Deformation"""
    
    AREA = {
        "breasts": "breasts, bust, cleavage",
        "thighs": "thighs, legs, thick thighs",
        "buttocks": "buttocks, ass, glutes",
        "stomach": "stomach, belly, tummy, midriff",
        "cheeks": "cheeks, face, jawline",
    }
    
    ACTION = {
        "squeeze": "squeezing, compressed, squished, hand squeeze_pro",
        "press": "pressed against, flattened against glass, pressed together",
        "jiggle": "soft motion, dynamic movement, gravity effect",
        "impact": "slap impact, shockwave, ripple",
        "grab": "firm grab, fingers sinking in, holding tight",
    }
    
    FIRMNESS = {
        "soft": "extremely soft, marshmallow soft, yielding",
        "natural": "natural firmness, realistic jiggle",
        "firm": "firm muscle, toned, hard body",
        "loose": "loose skin, heavy, sagging slightly",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "area": (list(cls.AREA.keys()),),
                "action": (list(cls.ACTION.keys()),),
                "firmness": (list(cls.FIRMNESS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Physics & Interaction"

    def generate(self, prompt, area, action, firmness):
        ar = self.AREA.get(area, "")
        ac = self.ACTION.get(action, "")
        f = self.FIRMNESS.get(firmness, "")
        
        positive = f"{prompt}, {ar}, {ac}, {f}"
        negative = "hard body, plastic, rigid"
        
        return (positive, negative)


NODE_CLASS_MAPPINGS = {
    "SkinPhysicsPro": SkinPhysicsPro,
    "FluidDynamicsPro": FluidDynamicsPro,
    "FabricPhysicsPro": FabricPhysicsPro,
    "SoftBodyPro": SoftBodyPro,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SkinPhysicsPro": "🧴 Skin Physics Pro",
    "FluidDynamicsPro": "💦 Fluid Dynamics Pro",
    "FabricPhysicsPro": "👕 Fabric Physics Pro",
    "SoftBodyPro": "🤏 Soft Body Pro",
}
