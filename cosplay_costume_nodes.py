"""
Mason's Cosplay & Costume Nodes for ComfyUI
Specific outfit archetypes and highly detailed costumes - SD 1.5 optimized
"""

class HeroineCatsuit:
    """Superheroine and tactical catsuit controller"""
    
    MATERIAL = {
        "latex": "latex catsuit, shiny latex, tight",
        "spandex": "spandex bodysuit, lycra, matte finish",
        "armor_plate": "armored bodysuit, sci-fi armor plating, tactical gear",
        "leotard": "high cut leotard, exposed legs",
    }
    
    DETAILS = {
        "utility_belt": "utility belt, pouches, gadgets",
        "mask": "domino mask, cowl, helmet",
        "glowing_lights": "glowing neon lights, circuit patterns, tron style",
        "battle_damage": "battle damage, torn suit, scratches, dirt",
        "unzipped": "unzipped chest, cleavage exposure",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "material": (list(cls.MATERIAL.keys()),),
                "details": (list(cls.DETAILS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Cosplay"

    def generate(self, prompt, material, details):
        m = self.MATERIAL.get(material, "")
        d = self.DETAILS.get(details, "")
        return (f"{prompt}, {m}, {d}, superheroine style", "civilian clothes")


class MagicalGirlOutfit:
    """Detailed magical girl anime style outfits"""
    
    STYLE = {
        "classic_sailor": "sailor fuku, pleated skirt, big bow, tiara",
        "idol_singer": "idol dress, frills, microphone, sparkly",
        "gothic_lolita": "gothic lolita, black lace, bonnet, petticoat",
        "angel_form": "angelic dress, feathers, wings, halo",
    }
    
    ELEMENTS = {
        "frills_bows": "lots of frills, ribbons, big bows",
        "gemstones": "magical gems, brooch, glowing crystals",
        "wand_staff": "holding magical wand, magical staff",
        "sparkles": "sparkles, magical aura, floating petals",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.STYLE.keys()),),
                "elements": (list(cls.ELEMENTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Cosplay"

    def generate(self, prompt, style, elements):
        s = self.STYLE.get(style, "")
        e = self.ELEMENTS.get(elements, "")
        return (f"{prompt}, {s}, {e}, magical girl aesthetic", "boring clothes")


class FantasyArmorSet:
    """Fantasy armor ranging from practical to bikini armor"""
    
    TYPE = {
        "bikini_armor": "bikini armor, chainmail bikini, exposing skin",
        "plate_armor": "full plate armor, knight armor, shiny metal",
        "leather_rogue": "leather armor, rogue gear, hood, straps",
        "mage_robes": "wizard robes, silk robes, embroidery",
        "barbarian_furs": "barbarian furs, loincloth, savage look",
    }
    
    CONDITION = {
        "pristine": "pristine condition, polished, shiny",
        "rusty": "rusty, old, ancient",
        "damaged": "damaged armor, cracked, dents",
        "enchanted": "enchanted armor, glowing runes, magical aura",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "armor_type": (list(cls.TYPE.keys()),),
                "condition": (list(cls.CONDITION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Cosplay"

    def generate(self, prompt, armor_type, condition):
        t = self.TYPE.get(armor_type, "")
        c = self.CONDITION.get(condition, "")
        return (f"{prompt}, {t}, {c}", "modern clothes")


class SchoolUniformPro:
    """Highly detailed school uniform variations"""
    
    STYLE = {
        "sailor_uniform": "sailor uniform, seifuku, navy collar",
        "blazer_style": "blazer uniform, button up shirt, tie",
        "sweater_vest": "sweater vest, beige vest, white shirt",
        "gym_clothes": "gym uniform, bloomers, t-shirt",
        "swimsuit": "school swimsuit, sukumizu, navy blue one piece",
    }
    
    SKIRT = {
        "mini_skirt": "mini skirt, short skirt, thigh high socks",
        "long_skirt": "long skirt, calf length, modest",
        "plaid_skirt": "plaid skirt, tartan pattern",
        "pleated_skirt": "pleated skirt, knife pleats",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.STYLE.keys()),),
                "skirt": (list(cls.SKIRT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Cosplay"

    def generate(self, prompt, style, skirt):
        s = self.STYLE.get(style, "")
        sk = self.SKIRT.get(skirt, "")
        return (f"{prompt}, {s}, {sk}", "casual clothes")


class CyberneticSuit:
    """Sci-fi and cybernetic body enhancements"""
    
    SUIT = {
        "plug_suit": "plug suit, eva style, skin tight, interface headset",
        "cyborg_body": "cyborg body, mechanical joints, synthetic skin",
        "android": "android, robot joints, panel lines",
        "holographic": "holographic clothing, digital outfit, glitch effect",
    }
    
    DETAILS = {
        "wires_cables": "wires connecting to body, data cables",
        "glowing_circuits": "glowing circuits, neon lines, blue light",
        "transparent_skin": "transparent skin panels, visible machinery",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "suit_type": (list(cls.SUIT.keys()),),
                "details": (list(cls.DETAILS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Cosplay"

    def generate(self, prompt, suit_type, details):
        s = self.SUIT.get(suit_type, "")
        d = self.DETAILS.get(details, "")
        return (f"{prompt}, {s}, {d}, sci-fi masterpiece", "fantasy, medieval")


NODE_CLASS_MAPPINGS = {
    "HeroineCatsuit": HeroineCatsuit,
    "MagicalGirlOutfit": MagicalGirlOutfit,
    "FantasyArmorSet": FantasyArmorSet,
    "SchoolUniformPro": SchoolUniformPro,
    "CyberneticSuit": CyberneticSuit,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HeroineCatsuit": "🦹 Heroine/Catsuit",
    "MagicalGirlOutfit": "✨ Magical Girl Outfit",
    "FantasyArmorSet": "🛡️ Fantasy Armor",
    "SchoolUniformPro": "🎒 School Uniform Pro",
    "CyberneticSuit": "🤖 Cybernetic/Sci-Fi Suit",
}
