"""
Mason's Period Costume Nodes for ComfyUI
Historical and fantasy clothing - SD 1.5 optimized
"""


class PirateCostumePro:
    """Authentic pirate and nautical costumes"""
    
    RANKS = {
        "captain": "pirate captain, tricorn hat, elaborate coat, commanding presence",
        "quartermaster": "pirate quartermaster, practical clothing, weapons visible",
        "swashbuckler": "swashbuckler, dashing rogue, rapier, flamboyant",
        "deck_hand": "deck hand, simple clothes, weathered, working class",
        "naval_officer": "naval officer, military uniform, brass buttons, formal",
    }
    
    CONDITIONS = {
        "pristine": "clean clothing, well-maintained, wealthy appearance",
        "weathered": "weathered clothing, sun-bleached, salt-stained, sea worn",
        "battle_worn": "battle damaged, torn fabric, blood stains, combat veteran",
        "cursed": "cursed pirate, ghostly, decaying clothes, supernatural",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "rank": (list(cls.RANKS.keys()),),
                "condition": (list(cls.CONDITIONS.keys()),),
                "accessories": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pirate_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Costumes"

    def apply(self, prompt, rank, condition, accessories):
        parts = [prompt]
        parts.append(self.RANKS.get(rank, ""))
        parts.append(self.CONDITIONS.get(condition, ""))
        
        if accessories:
            parts.append("pirate accessories, compass, telescope, gold coins, jeweled rings")
        
        return (", ".join([p for p in parts if p]),)


class MedievalArmorPro:
    """Medieval armor and knight equipment"""
    
    ARMOR_TYPES = {
        "full_plate": "full plate armor, polished steel, knight in shining armor",
        "chainmail": "chainmail armor, metal rings, flexible protection",
        "leather": "leather armor, studded, ranger style, flexible",
        "fantasy_plate": "fantasy plate armor, ornate engravings, magical runes",
        "blackened": "blackened armor, dark knight, menacing appearance",
        "royal_guard": "royal guard armor, ceremonial, gold trim, prestigious",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "armor_type": (list(cls.ARMOR_TYPES.keys()),),
                "helmet": (["none", "open_face", "closed_helm", "crown_helm", "horned"],),
                "condition": (["pristine", "battle_scarred", "ancient", "enchanted"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("armor_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Costumes"

    def apply(self, prompt, armor_type, helmet, condition):
        parts = [prompt]
        parts.append(self.ARMOR_TYPES.get(armor_type, ""))
        
        helmet_map = {
            "open_face": "open face helmet, visible features",
            "closed_helm": "closed helmet, full face protection, visor",
            "crown_helm": "crowned helmet, royal, king's helm",
            "horned": "horned helmet, viking style, intimidating",
        }
        if helmet != "none":
            parts.append(helmet_map.get(helmet, ""))
        
        condition_map = {
            "battle_scarred": "battle scarred armor, dents, scratches, veteran knight",
            "ancient": "ancient armor, patina, historical artifact",
            "enchanted": "enchanted armor, glowing runes, magical protection",
        }
        if condition != "pristine":
            parts.append(condition_map.get(condition, ""))
        
        return (", ".join([p for p in parts if p]),)


class HistoricalClothingMaster:
    """Various historical period clothing"""
    
    ERAS = {
        "victorian": "Victorian era clothing, 19th century, formal, elaborate",
        "renaissance": "Renaissance clothing, 15th-16th century, doublet, puffy sleeves",
        "ancient_roman": "Ancient Roman clothing, toga, sandals, classical",
        "ancient_greek": "Ancient Greek clothing, chiton, draped fabric, classical",
        "ancient_egyptian": "Ancient Egyptian clothing, linen, gold jewelry, pharaoh style",
        "japanese_edo": "Edo period Japanese, kimono, traditional patterns, samurai",
        "chinese_imperial": "Chinese imperial clothing, silk robes, dragon embroidery",
        "art_deco": "Art Deco era, 1920s fashion, flapper, geometric patterns",
        "steampunk": "Steampunk clothing, Victorian with gears, brass goggles, industrial",
        "cyberpunk": "Cyberpunk clothing, neon accents, tech wear, futuristic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "era": (list(cls.ERAS.keys()),),
                "social_class": (["peasant", "merchant", "noble", "royalty"],),
                "gender_style": (["masculine", "feminine", "androgynous"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("historical_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Costumes"

    def apply(self, prompt, era, social_class, gender_style):
        parts = [prompt]
        parts.append(self.ERAS.get(era, ""))
        
        class_map = {
            "peasant": "peasant clothing, simple, work-worn, humble",
            "merchant": "merchant class, quality fabric, practical elegance",
            "noble": "noble attire, fine fabrics, jewelry, aristocratic",
            "royalty": "royal clothing, lavish, crown, regal bearing",
        }
        parts.append(class_map.get(social_class, ""))
        
        return (", ".join([p for p in parts if p]),)


NODE_CLASS_MAPPINGS = {
    "PirateCostumePro": PirateCostumePro,
    "MedievalArmorPro": MedievalArmorPro,
    "HistoricalClothingMaster": HistoricalClothingMaster,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PirateCostumePro": "🏴‍☠️ Pirate Costume Pro",
    "MedievalArmorPro": "⚔️ Medieval Armor Pro",
    "HistoricalClothingMaster": "👑 Historical Clothing Master",
}
