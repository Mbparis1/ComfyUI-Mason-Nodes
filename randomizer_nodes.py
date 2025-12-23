"""
Mason's Randomizer Nodes for ComfyUI
Generate variations and random selections - SD 1.5 optimized
"""

import random


class VariationGenerator:
    """Generate subtle prompt variations for batch exploration"""
    
    VARIATION_TYPES = {
        "lighting": ["soft lighting", "dramatic lighting", "natural lighting", "studio lighting", "golden hour lighting"],
        "angle": ["front view", "three-quarter view", "side view", "low angle", "high angle"],
        "expression": ["neutral expression", "slight smile", "serious expression", "happy expression", "thoughtful expression"],
        "mood": ["serene mood", "mysterious mood", "cheerful mood", "intense mood", "relaxed mood"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
                "variation_type": (list(cls.VARIATION_TYPES.keys()),),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("varied_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Randomizers"

    def generate(self, base_prompt, variation_type, seed):
        random.seed(seed)
        variations = self.VARIATION_TYPES.get(variation_type, [])
        if variations:
            selected = random.choice(variations)
            return (f"{base_prompt}, {selected}",)
        return (base_prompt,)


class OutfitRandomizer:
    """Generate random outfit combinations"""
    
    TOPS = ["t-shirt", "blouse", "crop top", "tank top", "sweater", "dress shirt", "off-shoulder top"]
    BOTTOMS = ["jeans", "skirt", "shorts", "leggings", "dress pants", "mini skirt"]
    DRESSES = ["cocktail dress", "sundress", "evening gown", "bodycon dress", "maxi dress"]
    SWIMWEAR = ["bikini", "one-piece swimsuit", "string bikini", "high-waisted bikini"]
    LINGERIE = ["lace bra and panties", "silk lingerie set", "teddy", "bodysuit", "corset"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "category": (["casual", "formal", "dress", "swimwear", "lingerie"],),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("outfit_prompt",)
    FUNCTION = "randomize"
    CATEGORY = "Mason's Nodes/Randomizers"

    def randomize(self, category, seed):
        random.seed(seed)
        
        if category == "casual":
            top = random.choice(self.TOPS)
            bottom = random.choice(self.BOTTOMS)
            return (f"wearing {top} and {bottom}, casual outfit",)
        elif category == "formal":
            top = random.choice(["dress shirt", "blouse", "elegant top"])
            bottom = random.choice(["dress pants", "pencil skirt", "formal skirt"])
            return (f"wearing {top} and {bottom}, formal attire",)
        elif category == "dress":
            dress = random.choice(self.DRESSES)
            return (f"wearing {dress}, elegant",)
        elif category == "swimwear":
            swim = random.choice(self.SWIMWEAR)
            return (f"wearing {swim}, at pool or beach",)
        elif category == "lingerie":
            ling = random.choice(self.LINGERIE)
            return (f"wearing {ling}, intimate apparel",)
        
        return ("",)


class PoseRandomizer:
    """Generate random pose selections"""
    
    STANDING = ["standing straight", "standing with hand on hip", "leaning against wall", "contrapposto stance", "confident stance"]
    SITTING = ["sitting on chair", "sitting on floor", "sitting with legs crossed", "sitting casually", "sitting on bed edge"]
    LYING = ["lying on back", "lying on side", "lying on stomach", "reclining", "sprawled out"]
    DYNAMIC = ["walking", "running", "dancing", "jumping", "stretching"]
    SENSUAL = ["arched back pose", "looking over shoulder", "hands in hair", "seductive lean", "alluring recline"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "category": (["standing", "sitting", "lying", "dynamic", "sensual"],),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose_prompt",)
    FUNCTION = "randomize"
    CATEGORY = "Mason's Nodes/Randomizers"

    def randomize(self, category, seed):
        random.seed(seed)
        
        pose_map = {
            "standing": self.STANDING,
            "sitting": self.SITTING,
            "lying": self.LYING,
            "dynamic": self.DYNAMIC,
            "sensual": self.SENSUAL,
        }
        
        poses = pose_map.get(category, self.STANDING)
        selected = random.choice(poses)
        return (f"{selected} pose",)


class SeedExplorer:
    """Generate seed variations for batch testing"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "variation_index": ("INT", {"default": 0, "min": 0, "max": 100}),
                "variation_spread": ("INT", {"default": 100, "min": 1, "max": 10000}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("varied_seed",)
    FUNCTION = "explore"
    CATEGORY = "Mason's Nodes/Randomizers"

    def explore(self, base_seed, variation_index, variation_spread):
        varied_seed = base_seed + (variation_index * variation_spread)
        return (varied_seed,)


NODE_CLASS_MAPPINGS = {
    "VariationGenerator": VariationGenerator,
    "OutfitRandomizer": OutfitRandomizer,
    "PoseRandomizer": PoseRandomizer,
    "SeedExplorer": SeedExplorer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VariationGenerator": "🎲 Variation Generator",
    "OutfitRandomizer": "👗 Outfit Randomizer",
    "PoseRandomizer": "🕺 Pose Randomizer",
    "SeedExplorer": "🔢 Seed Explorer",
}
