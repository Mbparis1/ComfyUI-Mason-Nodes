"""
Mason's Utility Nodes for ComfyUI
Enhanced workflow automation nodes
"""

import random
import os
import json
from datetime import datetime


class PromptRandomizer:
    """Adds random variations to prompts for variety"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "beautiful woman", "multiline": True}),
                "variations": ("STRING", {"default": "blonde hair, brunette, redhead\nblue eyes, green eyes, brown eyes\nsmiling, serious, playful", "multiline": True}),
                "num_variations": ("INT", {"default": 1, "min": 1, "max": 5}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("randomized_prompt",)
    FUNCTION = "randomize"
    CATEGORY = "Mason's Nodes/Utility"

    def randomize(self, base_prompt, variations, num_variations):
        lines = [line.strip() for line in variations.split('\n') if line.strip()]
        selected = []
        for line in lines:
            options = [opt.strip() for opt in line.split(',')]
            if options:
                selected.append(random.choice(options))
        
        result = base_prompt
        if selected:
            result = f"{base_prompt}, {', '.join(selected[:num_variations])}"
        return (result,)


class AutoNegative:
    """Automatically generates comprehensive negative prompts"""
    
    PRESETS = {
        "realistic": "ugly, deformed, blurry, bad anatomy, bad hands, missing fingers, extra fingers, disfigured, low quality, worst quality, watermark, text, signature, jpeg artifacts, cropped, out of frame",
        "artistic": "ugly, blurry, low quality, watermark, text, signature, cropped",
        "anime": "ugly, bad anatomy, blurry, low quality, worst quality, watermark, text, extra limbs, missing limbs, cropped",
        "portrait": "ugly, deformed, blurry, bad anatomy, bad hands, bad face, asymmetrical face, low quality, worst quality, watermark, text, cropped, out of frame, extra limbs",
        "nsfw": "ugly, deformed, blurry, bad anatomy, bad hands, missing fingers, extra fingers, disfigured, low quality, worst quality, watermark, text, signature, child, underage, minor, censored, clothed"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PRESETS.keys()),),
                "additional_negatives": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Utility"

    def generate(self, preset, additional_negatives):
        base = self.PRESETS.get(preset, self.PRESETS["realistic"])
        if additional_negatives.strip():
            return (f"{base}, {additional_negatives.strip()}",)
        return (base,)


class BatchSaver:
    """Saves images with custom naming scheme and metadata"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "prefix": ("STRING", {"default": "generation"}),
                "include_date": ("BOOLEAN", {"default": True}),
                "include_seed": ("BOOLEAN", {"default": True}),
            },
            "optional": {
                "seed": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filename",)
    FUNCTION = "save"
    CATEGORY = "Mason's Nodes/Utility"
    OUTPUT_NODE = True

    def save(self, images, prefix, include_date, include_seed, seed=0):
        parts = [prefix]
        if include_date:
            parts.append(datetime.now().strftime("%Y%m%d_%H%M%S"))
        if include_seed and seed:
            parts.append(f"seed{seed}")
        
        filename = "_".join(parts)
        return (filename,)


class ResolutionCalculator:
    """Calculates optimal resolutions for different aspect ratios"""
    
    PRESETS = {
        "square_512": (512, 512),
        "portrait_512x768": (512, 768),
        "landscape_768x512": (768, 512),
        "portrait_512x640": (512, 640),
        "landscape_640x512": (640, 512),
        "small_square_384": (384, 384),
        "tiny_256": (256, 256),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PRESETS.keys()),),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "calculate"
    CATEGORY = "Mason's Nodes/Utility"

    def calculate(self, preset):
        width, height = self.PRESETS.get(preset, (512, 512))
        return (width, height)


class SeedLogger:
    """Logs seeds of good generations for reuse"""
    
    LOG_FILE = os.path.expanduser("~/AI/ComfyUI/output/seed_log.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0}),
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "rating": (["5_stars", "4_stars", "3_stars", "2_stars", "1_star"],),
                "save_seed": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed",)
    FUNCTION = "log_seed"
    CATEGORY = "Mason's Nodes/Utility"

    def log_seed(self, seed, prompt, rating, save_seed):
        if save_seed:
            try:
                if os.path.exists(self.LOG_FILE):
                    with open(self.LOG_FILE, 'r') as f:
                        data = json.load(f)
                else:
                    data = []
                
                entry = {
                    "seed": seed,
                    "prompt": prompt[:100],
                    "rating": rating,
                    "timestamp": datetime.now().isoformat()
                }
                data.append(entry)
                
                with open(self.LOG_FILE, 'w') as f:
                    json.dump(data, f, indent=2)
                print(f"[SeedLogger] Saved seed {seed} with rating {rating}")
            except Exception as e:
                print(f"[SeedLogger] Error saving: {e}")
        
        return (seed,)


class LoRASwitcher:
    """Randomly selects a LoRA from a list"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "lora_list": ("STRING", {"default": "add_detail.safetensors\ndetail_tweaker.safetensors\nskin_hands.safetensors", "multiline": True}),
                "strength": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.05}),
                "randomize": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING", "FLOAT")
    RETURN_NAMES = ("lora_name", "strength")
    FUNCTION = "select"
    CATEGORY = "Mason's Nodes/Utility"

    def select(self, lora_list, strength, randomize):
        loras = [l.strip() for l in lora_list.split('\n') if l.strip()]
        if not loras:
            return ("", 0.0)
        
        if randomize:
            selected = random.choice(loras)
        else:
            selected = loras[0]
        
        return (selected, strength)


NODE_CLASS_MAPPINGS = {
    "PromptRandomizer": PromptRandomizer,
    "AutoNegative": AutoNegative,
    "BatchSaver": BatchSaver,
    "ResolutionCalculator": ResolutionCalculator,
    "SeedLogger": SeedLogger,
    "LoRASwitcher": LoRASwitcher,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptRandomizer": "Prompt Randomizer",
    "AutoNegative": "Auto Negative Prompt",
    "BatchSaver": "Batch Saver",
    "ResolutionCalculator": "Resolution Calculator",
    "SeedLogger": "Seed Logger",
    "LoRASwitcher": "LoRA Switcher",
}
