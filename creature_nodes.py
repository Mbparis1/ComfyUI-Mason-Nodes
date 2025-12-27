"""
Mason's Creature & Animal Nodes for ComfyUI
Realistic animals and fantasy creatures - SD 1.5 optimized
"""


class RealisticAnimalPro:
    """Creates highly detailed, realistic animal prompts"""
    
    ANIMALS = {
        "wolf": "majestic wolf, detailed fur, piercing eyes, wild canine",
        "lion": "regal lion, flowing mane, king of beasts, powerful feline",
        "eagle": "majestic eagle, spread wings, sharp talons, fierce raptor",
        "horse": "magnificent horse, glossy coat, flowing mane, noble steed",
        "tiger": "fierce tiger, striped coat, powerful predator, jungle cat",
        "bear": "massive bear, thick fur, powerful build, forest giant",
        "dragon": "mythical dragon, scales, wings, fire breathing, legendary beast",
        "owl": "wise owl, large eyes, feathered, nocturnal hunter",
        "deer": "graceful deer, antlers, forest creature, elegant",
        "raven": "dark raven, glossy black feathers, intelligent bird",
    }
    
    TEXTURES = {
        "fur": "highly detailed fur, individual hair strands, realistic texture",
        "feathers": "detailed feathers, layered plumage, iridescent sheen",
        "scales": "detailed scales, reptilian texture, reflective surface",
        "smooth": "smooth skin, sleek appearance, wet look",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "animal": (list(cls.ANIMALS.keys()),),
                "texture": (list(cls.TEXTURES.keys()),),
                "age": (["young", "adult", "elderly", "ancient"],),
                "mood": (["calm", "fierce", "majestic", "playful", "menacing"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("animal_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Creatures"

    def apply(self, prompt, animal, texture, age, mood):
        parts = [prompt]
        parts.append(self.ANIMALS.get(animal, ""))
        parts.append(self.TEXTURES.get(texture, ""))
        
        age_map = {
            "young": "young animal, youthful, small",
            "adult": "adult animal, full grown, prime of life",
            "elderly": "old animal, weathered, wise appearance",
            "ancient": "ancient creature, mythical age, timeless",
        }
        parts.append(age_map.get(age, ""))
        
        mood_map = {
            "calm": "calm demeanor, peaceful, serene",
            "fierce": "fierce expression, aggressive, ready to attack",
            "majestic": "majestic pose, regal, commanding presence",
            "playful": "playful attitude, energetic, fun",
            "menacing": "menacing look, dark, threatening",
        }
        parts.append(mood_map.get(mood, ""))
        
        return (", ".join([p for p in parts if p]),)


class FantasyCreatureMaster:
    """Creates fantasy and mythological creatures"""
    
    CREATURES = {
        "undead_pirate": "undead pirate, Davy Jones style, barnacles, tentacles, decaying flesh, cursed sailor",
        "mermaid": "beautiful mermaid, fish tail, scales, underwater, ocean creature, aquatic",
        "centaur": "powerful centaur, half-horse half-human, mythological, Greek legend",
        "minotaur": "fearsome minotaur, bull head, muscular body, labyrinth dweller",
        "phoenix": "majestic phoenix, fire wings, rebirth, legendary bird, flames",
        "kraken": "massive kraken, giant tentacles, sea monster, ocean depths",
        "werewolf": "terrifying werewolf, wolf-man hybrid, full moon, transformation",
        "vampire": "elegant vampire, pale skin, fangs, immortal, gothic",
        "fairy": "delicate fairy, gossamer wings, tiny, magical glow, forest spirit",
        "demon": "fearsome demon, horns, dark skin, hellfire, supernatural",
        "angel": "divine angel, white wings, halo, heavenly light, celestial",
        "golem": "stone golem, ancient construct, animated rock, magical creation",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "creature": (list(cls.CREATURES.keys()),),
                "style": (["realistic", "dark_fantasy", "ethereal", "horror", "epic"],),
                "detail_level": (["standard", "highly_detailed", "hyper_detailed"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("creature_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Creatures"

    def apply(self, prompt, creature, style, detail_level):
        parts = [prompt]
        parts.append(self.CREATURES.get(creature, ""))
        
        style_map = {
            "realistic": "photorealistic, realistic rendering, believable",
            "dark_fantasy": "dark fantasy style, moody, gothic atmosphere",
            "ethereal": "ethereal quality, glowing, otherworldly, mystical",
            "horror": "horror style, terrifying, nightmare fuel, disturbing",
            "epic": "epic scale, grandiose, legendary, awe-inspiring",
        }
        parts.append(style_map.get(style, ""))
        
        detail_map = {
            "highly_detailed": "highly detailed, intricate features",
            "hyper_detailed": "hyper detailed, extreme detail, every texture visible",
        }
        if detail_level != "standard":
            parts.append(detail_map.get(detail_level, ""))
        
        return (", ".join([p for p in parts if p]),)


class CreatureTexturePro:
    """Advanced texture control for creatures"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "primary_texture": (["fur", "scales", "feathers", "skin", "chitin", "bark"],),
                "texture_condition": (["pristine", "battle_scarred", "wet", "dusty", "glowing"],),
                "color_pattern": (["solid", "spotted", "striped", "mottled", "gradient", "iridescent"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("texture_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Creatures"

    def apply(self, prompt, primary_texture, texture_condition, color_pattern):
        parts = [prompt]
        
        texture_map = {
            "fur": "detailed fur texture, soft coat, individual hairs",
            "scales": "detailed scales, overlapping pattern, reptilian",
            "feathers": "layered feathers, detailed plumage, bird-like",
            "skin": "detailed skin, pores, natural texture",
            "chitin": "chitinous exoskeleton, insectoid armor, hard shell",
            "bark": "bark-like skin, wooden texture, tree-like",
        }
        parts.append(texture_map.get(primary_texture, ""))
        
        condition_map = {
            "pristine": "pristine condition, perfect, unblemished",
            "battle_scarred": "battle scarred, wounds, scratches, weathered",
            "wet": "wet surface, glistening, water droplets",
            "dusty": "dusty, dirt particles, weathered appearance",
            "glowing": "glowing, bioluminescent, magical light emanating",
        }
        parts.append(condition_map.get(texture_condition, ""))
        
        pattern_map = {
            "spotted": "spotted pattern, dots, leopard-like",
            "striped": "striped pattern, tiger stripes, zebra-like",
            "mottled": "mottled coloring, patches, camouflage",
            "gradient": "gradient coloring, color transition, ombre",
            "iridescent": "iridescent, color-shifting, rainbow sheen",
        }
        if color_pattern != "solid":
            parts.append(pattern_map.get(color_pattern, ""))
        
        return (", ".join([p for p in parts if p]),)


NODE_CLASS_MAPPINGS = {
    "RealisticAnimalPro": RealisticAnimalPro,
    "FantasyCreatureMaster": FantasyCreatureMaster,
    "CreatureTexturePro": CreatureTexturePro,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RealisticAnimalPro": "🦁 Realistic Animal Pro",
    "FantasyCreatureMaster": "🐉 Fantasy Creature Master",
    "CreatureTexturePro": "🎨 Creature Texture Pro",
}
