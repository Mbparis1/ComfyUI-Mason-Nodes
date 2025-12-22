"""
Mason's Quality Control Nodes for ComfyUI
Optimize settings and track results
"""

import os
import json
import time
from datetime import datetime


class LoRAStrengthOptimizer:
    """Suggest optimal LoRA strengths based on content type"""
    
    RECOMMENDATIONS = {
        "photorealistic": {"add_detail": 0.5, "skin_hands": 0.4, "lcm_lora": 0.8},
        "artistic": {"add_detail": 0.7, "skin_hands": 0.3, "lcm_lora": 0.6},
        "fast_preview": {"lcm_lora": 1.0, "add_detail": 0.3},
        "high_detail": {"add_detail": 0.8, "detail_tweaker": 0.6, "skin_hands": 0.5},
        "soft_skin": {"skin_hands": 0.7, "add_detail": 0.3},
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "content_type": (list(cls.RECOMMENDATIONS.keys()),),
            }
        }

    RETURN_TYPES = ("FLOAT", "FLOAT", "FLOAT", "STRING")
    RETURN_NAMES = ("lora1_strength", "lora2_strength", "lora3_strength", "recommendation")
    FUNCTION = "optimize"
    CATEGORY = "Mason's Nodes/Quality Control"

    def optimize(self, content_type):
        rec = self.RECOMMENDATIONS.get(content_type, {})
        strengths = list(rec.values())[:3] + [0.0, 0.0, 0.0]  # Pad to 3
        
        info = f"Recommended for {content_type}: " + ", ".join([f"{k}={v}" for k, v in rec.items()])
        
        return (strengths[0], strengths[1], strengths[2], info)


class CFGStepsRecommender:
    """Recommend CFG and steps for 2GB VRAM optimization"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "priority": (["speed", "balanced", "quality"],),
                "using_lcm": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("FLOAT", "INT", "STRING")
    RETURN_NAMES = ("cfg", "steps", "info")
    FUNCTION = "recommend"
    CATEGORY = "Mason's Nodes/Quality Control"

    def recommend(self, priority, using_lcm):
        if using_lcm:
            settings = {"speed": (1.5, 4), "balanced": (1.8, 6), "quality": (2.0, 8)}
        else:
            settings = {"speed": (6.0, 15), "balanced": (7.0, 20), "quality": (7.5, 25)}
        
        cfg, steps = settings[priority]
        est_time = steps * (2 if using_lcm else 4)  # seconds per step
        info = f"CFG {cfg}, {steps} steps | Est. time: ~{est_time}s"
        
        return (cfg, steps, info)


class BestSeedFinder:
    """Track and recall seeds that produced good results"""
    
    SEED_FILE = os.path.expanduser("~/AI/ComfyUI/output/best_seeds.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "action": (["save_seed", "get_random_good_seed", "list_all"],),
                "seed": ("INT", {"default": 0}),
                "rating": (["excellent", "good", "average"],),
                "notes": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("INT", "STRING")
    RETURN_NAMES = ("seed", "status")
    FUNCTION = "process"
    CATEGORY = "Mason's Nodes/Quality Control"

    def process(self, action, seed, rating, notes):
        if os.path.exists(self.SEED_FILE):
            with open(self.SEED_FILE, 'r') as f:
                seeds = json.load(f)
        else:
            seeds = []
        
        if action == "save_seed":
            seeds.append({"seed": seed, "rating": rating, "notes": notes, "time": datetime.now().isoformat()})
            with open(self.SEED_FILE, 'w') as f:
                json.dump(seeds, f, indent=2)
            return (seed, f"Saved seed {seed} with rating '{rating}'")
        
        elif action == "get_random_good_seed":
            good_seeds = [s for s in seeds if s["rating"] in ["excellent", "good"]]
            if good_seeds:
                import random
                chosen = random.choice(good_seeds)
                return (chosen["seed"], f"Retrieved seed {chosen['seed']} ({chosen['rating']})")
            return (seed, "No good seeds saved yet")
        
        elif action == "list_all":
            if seeds:
                info = "\n".join([f"Seed {s['seed']}: {s['rating']}" for s in seeds[-10:]])
                return (seeds[-1]["seed"], info)
            return (0, "No seeds saved yet")
        
        return (seed, "Unknown action")


class GenerationTimer:
    """Track generation time for optimization"""
    
    _start_times = {}
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "generation_id": ("STRING", {"default": "gen1"}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("images", "time_info")
    FUNCTION = "end_timer"
    CATEGORY = "Mason's Nodes/Quality Control"

    def end_timer(self, images, generation_id):
        # Since we can't easily start timer in workflow, just return when this node runs
        current_time = datetime.now().strftime("%H:%M:%S")
        return (images, f"Completed at {current_time}")


NODE_CLASS_MAPPINGS = {
    "LoRAStrengthOptimizer": LoRAStrengthOptimizer,
    "CFGStepsRecommender": CFGStepsRecommender,
    "BestSeedFinder": BestSeedFinder,
    "GenerationTimer": GenerationTimer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoRAStrengthOptimizer": "⚙️ LoRA Strength Optimizer",
    "CFGStepsRecommender": "�� CFG/Steps Recommender",
    "BestSeedFinder": "�� Best Seed Finder",
    "GenerationTimer": "⏱️ Generation Timer",
}
