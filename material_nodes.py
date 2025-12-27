"""
Mason's Material Library Nodes for ComfyUI
Detailed material and texture prompts - SD 1.5 optimized
"""


class FabricMaterialPro:
    """Detailed fabric and textile materials"""
    
    FABRICS = {
        "silk": "luxurious silk fabric, smooth sheen, flowing material, glossy",
        "velvet": "rich velvet, soft pile, deep color saturation, plush",
        "leather": "genuine leather, natural grain, supple texture, worn-in",
        "latex": "shiny latex, reflective surface, tight fit, glossy rubber",
        "lace": "delicate lace, intricate pattern, see-through, feminine",
        "denim": "classic denim, woven texture, casual, sturdy fabric",
        "satin": "smooth satin, light reflecting surface, elegant drape",
        "wool": "warm wool, textured knit, cozy, natural fibers",
        "chiffon": "sheer chiffon, lightweight, flowing, ethereal",
        "cotton": "soft cotton, natural texture, comfortable, breathable",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "fabric": (list(cls.FABRICS.keys()),),
                "condition": (["pristine", "worn", "wet", "wrinkled", "stretched"],),
                "color_quality": (["solid", "patterned", "gradient", "metallic"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fabric_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Materials"

    def apply(self, prompt, fabric, condition, color_quality):
        parts = [prompt]
        parts.append(self.FABRICS.get(fabric, ""))
        
        condition_map = {
            "pristine": "pristine condition, new, perfect",
            "worn": "worn fabric, aged, broken in, comfortable",
            "wet": "wet fabric, damp, clinging, transparent when wet",
            "wrinkled": "wrinkled fabric, creased, textured folds",
            "stretched": "stretched fabric, tight, form-fitting, strained",
        }
        parts.append(condition_map.get(condition, ""))
        
        color_map = {
            "patterned": "patterned fabric, printed design",
            "gradient": "gradient coloring, ombre effect",
            "metallic": "metallic thread, shimmer, sparkle",
        }
        if color_quality != "solid":
            parts.append(color_map.get(color_quality, ""))
        
        return (", ".join([p for p in parts if p]),)


class MetalMaterialPro:
    """Metallic materials and finishes"""
    
    METALS = {
        "gold": "pure gold, warm yellow metal, precious, gleaming",
        "silver": "polished silver, cool metallic sheen, reflective",
        "bronze": "aged bronze, warm brown metal, historical, patina",
        "steel": "polished steel, cold metal, industrial, chromatic",
        "copper": "burnished copper, reddish metal, warm tones",
        "iron": "wrought iron, dark metal, heavy, strong",
        "platinum": "platinum finish, white metal, luxurious, premium",
        "brass": "antique brass, golden alloy, vintage appeal",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "metal": (list(cls.METALS.keys()),),
                "finish": (["polished", "brushed", "matte", "oxidized", "hammered"],),
                "wear": (["new", "light_wear", "battle_worn", "ancient"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("metal_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Materials"

    def apply(self, prompt, metal, finish, wear):
        parts = [prompt]
        parts.append(self.METALS.get(metal, ""))
        
        finish_map = {
            "polished": "mirror polish, highly reflective",
            "brushed": "brushed finish, directional texture",
            "matte": "matte finish, non-reflective, subtle",
            "oxidized": "oxidized surface, patina, aged",
            "hammered": "hammered texture, hand-forged appearance",
        }
        parts.append(finish_map.get(finish, ""))
        
        wear_map = {
            "light_wear": "light wear, minor scratches",
            "battle_worn": "battle worn, dents, deep scratches, history",
            "ancient": "ancient artifact, archaeological, extreme age",
        }
        if wear != "new":
            parts.append(wear_map.get(wear, ""))
        
        return (", ".join([p for p in parts if p]),)


class OrganicMaterialPro:
    """Organic and natural materials"""
    
    MATERIALS = {
        "wood": "natural wood grain, organic texture, warm brown tones",
        "stone": "natural stone, mineral texture, geological patterns",
        "bone": "polished bone, ivory-like, organic curves, skeletal",
        "shell": "iridescent shell, mother of pearl, oceanic",
        "coral": "ocean coral, branching structure, underwater life",
        "crystal": "natural crystal, faceted, light-catching, gemstone",
        "amber": "fossilized amber, golden translucent, prehistoric",
        "jade": "jade stone, green mineral, smooth, precious",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "material": (list(cls.MATERIALS.keys()),),
                "treatment": (["natural", "polished", "carved", "raw"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("organic_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Materials"

    def apply(self, prompt, material, treatment):
        parts = [prompt]
        parts.append(self.MATERIALS.get(material, ""))
        
        treatment_map = {
            "polished": "polished surface, smooth finish, refined",
            "carved": "intricately carved, artistic, detailed work",
            "raw": "raw natural state, unprocessed, rough texture",
        }
        if treatment != "natural":
            parts.append(treatment_map.get(treatment, ""))
        
        return (", ".join([p for p in parts if p]),)


NODE_CLASS_MAPPINGS = {
    "FabricMaterialPro": FabricMaterialPro,
    "MetalMaterialPro": MetalMaterialPro,
    "OrganicMaterialPro": OrganicMaterialPro,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FabricMaterialPro": "🧵 Fabric Material Pro",
    "MetalMaterialPro": "⚙️ Metal Material Pro",
    "OrganicMaterialPro": "🌿 Organic Material Pro",
}
