"""
Mason's Workflow Helper Nodes for ComfyUI
Productivity tools for efficient workflows
"""

import os
import json
from datetime import datetime


class FavoritesLibrary:
    """Save and load favorite prompts"""
    
    FAVORITES_FILE = os.path.expanduser("~/AI/ComfyUI/output/favorite_prompts.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "action": (["save", "load", "list"],),
                "slot_name": ("STRING", {"default": "favorite1"}),
                "prompt_to_save": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("prompt", "status")
    FUNCTION = "process"
    CATEGORY = "Mason's Nodes/Workflow"

    def process(self, action, slot_name, prompt_to_save):
        if os.path.exists(self.FAVORITES_FILE):
            with open(self.FAVORITES_FILE, 'r') as f:
                favorites = json.load(f)
        else:
            favorites = {}
        
        if action == "save":
            favorites[slot_name] = {"prompt": prompt_to_save, "saved": datetime.now().isoformat()}
            with open(self.FAVORITES_FILE, 'w') as f:
                json.dump(favorites, f, indent=2)
            return (prompt_to_save, f"Saved to '{slot_name}'")
        
        elif action == "load":
            if slot_name in favorites:
                return (favorites[slot_name]["prompt"], f"Loaded from '{slot_name}'")
            return ("", f"'{slot_name}' not found")
        
        elif action == "list":
            slots = ", ".join(favorites.keys()) if favorites else "No favorites saved"
            return ("", f"Available: {slots}")
        
        return ("", "Unknown action")


class QuickABCompare:
    """Store two prompts for A/B comparison"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt_a": ("STRING", {"default": "", "multiline": True}),
                "prompt_b": ("STRING", {"default": "", "multiline": True}),
                "select": (["A", "B"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("selected_prompt", "comparison")
    FUNCTION = "compare"
    CATEGORY = "Mason's Nodes/Workflow"

    def compare(self, prompt_a, prompt_b, select):
        selected = prompt_a if select == "A" else prompt_b
        comparison = f"A: {prompt_a[:50]}...\nB: {prompt_b[:50]}...\nSelected: {select}"
        return (selected, comparison)


class PromptCombiner:
    """Combine multiple prompt parts intelligently"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject": ("STRING", {"default": "", "multiline": True}),
                "style": ("STRING", {"default": "", "multiline": True}),
                "quality": ("STRING", {"default": "", "multiline": True}),
            },
            "optional": {
                "extra1": ("STRING", {"default": "", "multiline": True}),
                "extra2": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("combined_prompt",)
    FUNCTION = "combine"
    CATEGORY = "Mason's Nodes/Workflow"

    def combine(self, subject, style, quality, extra1="", extra2=""):
        parts = [p.strip() for p in [subject, style, quality, extra1, extra2] if p.strip()]
        return (", ".join(parts),)


class RandomFromList:
    """Pick random item from a newline-separated list"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "items": ("STRING", {"default": "item1\nitem2\nitem3", "multiline": True}),
                "seed": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("selected",)
    FUNCTION = "pick"
    CATEGORY = "Mason's Nodes/Workflow"

    def pick(self, items, seed):
        import random
        random.seed(seed)
        item_list = [i.strip() for i in items.split('\n') if i.strip()]
        if item_list:
            return (random.choice(item_list),)
        return ("",)


NODE_CLASS_MAPPINGS = {
    "FavoritesLibrary": FavoritesLibrary,
    "QuickABCompare": QuickABCompare,
    "PromptCombiner": PromptCombiner,
    "RandomFromList": RandomFromList,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FavoritesLibrary": "⭐ Favorites Library",
    "QuickABCompare": "🔀 Quick A/B Compare",
    "PromptCombiner": "�� Prompt Combiner",
    "RandomFromList": "🎲 Random From List",
}
