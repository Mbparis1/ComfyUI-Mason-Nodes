"""
Mason's Fantasy & NSFW Nodes for ComfyUI
Non-human, fantasy, and exotic content controllers - SD 1.5 optimized
"""

class FantasySkinLoRA:
    """Controls exotic skin colors and textures"""
    
    COLOR = {
        "green_orc": "green skin, orc skin, olive skin",
        "blue_avatar": "blue skin, alien skin, bioluminescent skin",
        "red_demon": "red skin, demon skin, hellish skin",
        "purple_drow": "purple skin, dark elf skin, drow skin",
        "grey_undead": "grey skin, pale skin, undead skin",
        "gold_metallic": "gold skin, metallic skin, shiny",
        "pale_vampire": "pale white skin, translucent skin, vampire skin",
    }
    
    TEXTURE = {
        "smooth": "smooth skin",
        "scales": "scaled skin, dragon scales, reptilian skin",
        "fur": "furry, fur covered, soft fur",
        "chitin": "chitin plating, insectoid armor, hard shell",
        "slime": "slime covered, slimy skin, wet slime",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "skin_color": (list(cls.COLOR.keys()),),
                "texture": (list(cls.TEXTURE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Fantasy NSFW"

    def generate(self, prompt, skin_color, texture):
        c = self.COLOR.get(skin_color, "")
        t = self.TEXTURE.get(texture, "")
        return (f"{prompt}, {c}, {t}", "human skin, normal skin")


class AppendageController:
    """Controls extra limbs, wings, tails, and ears"""
    
    ITEM = {
        "angel_wings": "angel wings, white feathered wings, large wings",
        "demon_wings": "demon wings, bat wings, leathery wings",
        "fairy_wings": "fairy wings, insect wings, translucent wings",
        "demon_tail": "demon tail, spade tail, prehensile tail",
        "cat_tail": "cat tail, fluffy tail",
        "fox_tails": "nine tails, fox tail, kitsune",
        "elf_ears": "elf ears, pointed ears, long ears",
        "devil_horns": "devil horns, ram horns, curved horns",
        "antlers": "antlers, deer horns, branching antlers",
    }
    
    SIZE = {
        "small_cute": "small, cute, subtle",
        "medium": "medium size, proportional",
        "large_epic": "large, epic, massive, huge",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "appendage": (list(cls.ITEM.keys()),),
                "size": (list(cls.SIZE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Fantasy NSFW"

    def generate(self, prompt, appendage, size):
        a = self.ITEM.get(appendage, "")
        s = self.SIZE.get(size, "")
        return (f"{prompt}, {s} {a}", "missing wings, missing tail")


class CreatureMorphLoRA:
    """Controls monster girl / fantasy species traits"""
    
    SPECIES = {
        "succubus": "succubus, demon girl, horns, wings, tail, seductive",
        "goblin_girl": "goblin girl, shortstack, green skin, pointed ears, energetic",
        "orc_girl": "orc girl, muscular, tusks, green skin, strong",
        "vampire": "vampire, fangs, pale skin, red eyes, elegant",
        "dark_elf": "dark elf, drow, purple skin, white hair, matriarch",
        "slime_girl": "slime girl, translucent body, liquid body, blob",
        "centaur": "centaur, horse body, half human half horse",
        "lamia": "lamia, snake body, half human half snake, scales",
        "harpy": "harpy, bird wings, talons, feathers",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "species": (list(cls.SPECIES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Fantasy NSFW"

    def generate(self, prompt, species):
        s = self.SPECIES.get(species, "")
        return (f"{prompt}, {s}, monster girl", "human, boring")


class TransformationAct:
    """Controls transformation sequences"""
    
    STAGE = {
        "beginning": "beginning transformation, glowing skin, clothes tearing",
        "mid_transformation": "mid transformation, mutating, changing shape, hybrid form",
        "stuck": "stuck in transformation, half transformed, uneven",
        "complete": "fully transformed, final form, complete change",
    }
    
    EFFECT = {
        "tearing_clothes": "clothes tearing apart, ripping seams, buttons popping",
        "glowing_aura": "glowing aura, magical energy, light rays",
        "goo_meld": "melting, goo dripping, liquid transition",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "stage": (list(cls.STAGE.keys()),),
                "effect": (list(cls.EFFECT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Fantasy NSFW"

    def generate(self, prompt, stage, effect):
        s = self.STAGE.get(stage, "")
        e = self.EFFECT.get(effect, "")
        return (f"{prompt}, {s}, {e}", "static, normal")


class MagicalFluidsLoRA:
    """Fantasy bodily fluids and effects"""
    
    FLUID = {
        "glowing_cum": "glowing cum, bioluminescent semen, neon fluid",
        "slime": "green slime, viscous slime, sticky goo",
        "black_ichor": "black ichor, dark fluid, shadow essence",
        "gold_nectar": "golden nectar, liquid gold, ambrosia",
        "mist": "magical mist, vapor, smoke",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "fluid_type": (list(cls.FLUID.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Fantasy NSFW"

    def generate(self, prompt, fluid_type):
        f = self.FLUID.get(fluid_type, "")
        return (f"{prompt}, {f}", "normal fluids")


class MonsterSizeController:
    """Size difference and giantess/tiny themes"""
    
    SIZE = {
        "giantess": "giantess, giant woman, towering, looking down",
        "tiny": "tiny, fairy size, minigirl, inches tall",
        "tall": "tall woman, amazon, 7ft tall",
        "shortstack": "shortstack, short and curvy, thick",
    }
    
    PERSPECTIVE = {
        "viewer_tiny": "viewer is tiny, giantess POV, looking up at giant",
        "viewer_giant": "viewer is giant, looking down at tiny, holding in hand",
        "macro_crush": "macro stomp, crushing under foot",
        "vore_mouth": "vore mouth, inside mouth view, maw",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "size_theme": (list(cls.SIZE.keys()),),
                "perspective": (list(cls.PERSPECTIVE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Fantasy NSFW"

    def generate(self, prompt, size_theme, perspective):
        s = self.SIZE.get(size_theme, "")
        p = self.PERSPECTIVE.get(perspective, "")
        return (f"{prompt}, {s}, {p}", "normal size, same height")


NODE_CLASS_MAPPINGS = {
    "FantasySkinLoRA": FantasySkinLoRA,
    "AppendageController": AppendageController,
    "CreatureMorphLoRA": CreatureMorphLoRA,
    "TransformationAct": TransformationAct,
    "MagicalFluidsLoRA": MagicalFluidsLoRA,
    "MonsterSizeController": MonsterSizeController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FantasySkinLoRA": "🐉 Fantasy Skin & Texture",
    "AppendageController": "🐉 Wings/Tails/Horns",
    "CreatureMorphLoRA": "👹 Creature Morph (LoRA)",
    "TransformationAct": "✨ Transformation Sequence",
    "MagicalFluidsLoRA": "🧪 Magical Fluids",
    "MonsterSizeController": "📏 Giantess/Size Difference",
}
