"""
Mason's Batch & Productivity Nodes for ComfyUI
Tools for mass production and workflow optimization - SD 1.5 optimized
"""

import random
import json
import os
import datetime


class BatchVariationGenerator:
    """Generates multiple prompt variations for batch processing"""
    
    VARIATION_TYPES = {
        "pose": ["standing", "sitting", "lying down", "kneeling", "bending over"],
        "expression": ["smiling", "serious", "seductive", "surprised", "pleasure"],
        "lighting": ["studio lighting", "natural light", "dramatic shadows", "soft glow", "neon"],
        "angle": ["front view", "side view", "three-quarter view", "from above", "from below"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
                "variation_type": (list(cls.VARIATION_TYPES.keys()),),
                "variation_index": ("INT", {"default": 0, "min": 0, "max": 4, "step": 1}),
                "randomize": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("varied_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Productivity"

    def generate(self, base_prompt, variation_type, variation_index, randomize):
        variations = self.VARIATION_TYPES.get(variation_type, [])
        if randomize:
            variation = random.choice(variations)
        else:
            variation = variations[variation_index % len(variations)]
        return (f"{base_prompt}, {variation}",)


class PromptRecipeSaver:
    """Saves successful prompt combinations for reuse"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt_to_save": ("STRING", {"default": "", "multiline": True}),
                "recipe_name": ("STRING", {"default": "my_recipe"}),
                "save_enabled": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt_passthrough",)
    FUNCTION = "save_recipe"
    OUTPUT_NODE = True
    CATEGORY = "Mason's Nodes/Productivity"

    def save_recipe(self, prompt_to_save, recipe_name, save_enabled):
        if save_enabled and prompt_to_save.strip():
            recipe_dir = os.path.join(os.path.dirname(__file__), "saved_recipes")
            os.makedirs(recipe_dir, exist_ok=True)
            
            safe_name = "".join(c for c in recipe_name if c.isalnum() or c in "_-").strip()
            filepath = os.path.join(recipe_dir, f"{safe_name}.txt")
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(prompt_to_save)
            print(f"Recipe saved: {filepath}")
            
        return (prompt_to_save,)


class PromptRecipeLoader:
    """Loads a saved prompt recipe"""
    
    @classmethod
    def INPUT_TYPES(cls):
        recipe_dir = os.path.join(os.path.dirname(__file__), "saved_recipes")
        recipes = ["(none)"]
        if os.path.exists(recipe_dir):
            recipes += [f[:-4] for f in os.listdir(recipe_dir) if f.endswith(".txt")]
        return {
            "required": {
                "recipe_name": (recipes,),
                "fallback_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("loaded_prompt",)
    FUNCTION = "load_recipe"
    CATEGORY = "Mason's Nodes/Productivity"

    def load_recipe(self, recipe_name, fallback_prompt):
        if recipe_name == "(none)":
            return (fallback_prompt,)
            
        recipe_dir = os.path.join(os.path.dirname(__file__), "saved_recipes")
        filepath = os.path.join(recipe_dir, f"{recipe_name}.txt")
        
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                return (f.read(),)
        return (fallback_prompt,)


class ABComparisonNode:
    """Creates two prompt variations for side-by-side comparison"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
                "variation_a": ("STRING", {"default": "soft lighting"}),
                "variation_b": ("STRING", {"default": "dramatic lighting"}),
                "output_selection": (["A", "B", "random"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt_a", "prompt_b", "selected_prompt")
    FUNCTION = "compare"
    CATEGORY = "Mason's Nodes/Productivity"

    def compare(self, base_prompt, variation_a, variation_b, output_selection):
        prompt_a = f"{base_prompt}, {variation_a}"
        prompt_b = f"{base_prompt}, {variation_b}"
        
        if output_selection == "A":
            selected = prompt_a
        elif output_selection == "B":
            selected = prompt_b
        else:
            selected = random.choice([prompt_a, prompt_b])
            
        return (prompt_a, prompt_b, selected)


NODE_CLASS_MAPPINGS = {
    "BatchVariationGenerator": BatchVariationGenerator,
    "PromptRecipeSaver": PromptRecipeSaver,
    "PromptRecipeLoader": PromptRecipeLoader,
    "ABComparisonNode": ABComparisonNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BatchVariationGenerator": "🔄 Batch Variation Generator",
    "PromptRecipeSaver": "💾 Prompt Recipe Saver",
    "PromptRecipeLoader": "📂 Prompt Recipe Loader",
    "ABComparisonNode": "⚖️ A/B Comparison Node",
}
