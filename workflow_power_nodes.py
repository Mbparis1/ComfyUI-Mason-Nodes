"""
Mason's Workflow Power Nodes for ComfyUI
Debugging, batching, and style tools
"""

import os
import json
from datetime import datetime


class PromptDebugger:
    """Show exactly what's being sent to the model"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "show_length": ("BOOLEAN", {"default": True}),
                "show_tokens_estimate": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("prompt_passthrough", "debug_info")
    FUNCTION = "debug"
    CATEGORY = "Mason's Nodes/Workflow Power"

    def debug(self, prompt, show_length, show_tokens_estimate):
        info_parts = []
        
        if show_length:
            info_parts.append(f"Characters: {len(prompt)}")
        
        if show_tokens_estimate:
            # Rough estimate: ~4 chars per token
            est_tokens = len(prompt) // 4
            info_parts.append(f"Est. tokens: ~{est_tokens}")
            if est_tokens > 75:
                info_parts.append("⚠️ May be truncated (>75 tokens)")
        
        # Count keywords
        keywords = len([w for w in prompt.split(',') if w.strip()])
        info_parts.append(f"Keywords: {keywords}")
        
        debug_info = " | ".join(info_parts)
        print(f"[PromptDebugger] {debug_info}")
        print(f"[PromptDebugger] Full prompt: {prompt[:200]}...")
        
        return (prompt, debug_info)


class BatchQueueBuilder:
    """Set up multiple generations with variations"""
    
    LOG_FILE = os.path.expanduser("~/AI/ComfyUI/output/batch_queue.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
                "variations": ("STRING", {"default": "blonde\nbrunette\nredhead", "multiline": True}),
                "queue_index": ("INT", {"default": 0, "min": 0, "max": 50}),
                "seeds": ("STRING", {"default": "12345, 67890, 11111"}),
            }
        }

    RETURN_TYPES = ("STRING", "INT", "STRING")
    RETURN_NAMES = ("current_prompt", "current_seed", "queue_info")
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Workflow Power"

    def build(self, base_prompt, variations, queue_index, seeds):
        var_list = [v.strip() for v in variations.split('\n') if v.strip()]
        seed_list = [int(s.strip()) for s in seeds.split(',') if s.strip()]
        
        # Cycle through variations and seeds
        var_idx = queue_index % len(var_list) if var_list else 0
        seed_idx = queue_index % len(seed_list) if seed_list else 0
        
        current_var = var_list[var_idx] if var_list else ""
        current_seed = seed_list[seed_idx] if seed_list else 0
        
        prompt = f"{base_prompt}, {current_var}" if current_var else base_prompt
        
        total = len(var_list) * len(seed_list)
        info = f"Queue {queue_index + 1}/{total}: {current_var} (seed {current_seed})"
        
        return (prompt, current_seed, info)


class StyleExtractor:
    """Extract style keywords from a reference prompt"""
    
    STYLE_KEYWORDS = [
        "photorealistic", "cinematic", "dramatic", "soft", "hard lighting",
        "film grain", "bokeh", "shallow depth of field", "studio lighting",
        "natural lighting", "golden hour", "high contrast", "low key",
        "masterpiece", "best quality", "detailed", "sharp", "8k", "4k",
    ]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "reference_prompt": ("STRING", {"default": "", "multiline": True}),
                "target_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("styled_prompt", "extracted_styles")
    FUNCTION = "extract"
    CATEGORY = "Mason's Nodes/Workflow Power"

    def extract(self, reference_prompt, target_prompt):
        ref_lower = reference_prompt.lower()
        found_styles = []
        
        for keyword in self.STYLE_KEYWORDS:
            if keyword in ref_lower:
                found_styles.append(keyword)
        
        styles_str = ", ".join(found_styles)
        styled = f"{target_prompt}, {styles_str}" if found_styles else target_prompt
        
        return (styled, styles_str)


class NegativePromptBuilder:
    """Build comprehensive negative prompts"""
    
    PRESETS = {
        "basic": "bad quality, blurry, low resolution",
        "anatomy": "bad anatomy, bad hands, bad fingers, extra fingers, missing fingers, extra limbs, mutated, deformed",
        "face": "ugly face, distorted face, asymmetrical eyes, cross-eyed, double face",
        "artifacts": "jpeg artifacts, noise, grain, watermark, signature, text",
        "nsfw_quality": "bad anatomy, bad hands, bad proportions, blurry, cropped, deformed, disfigured, duplicate, error, extra arms, extra fingers, extra legs, extra limbs, fused fingers, gross proportions, jpeg artifacts, long neck, low quality, lowres, malformed limbs, missing arms, missing fingers, missing legs, morbid, mutated hands, mutation, mutilated, out of frame, poorly drawn face, poorly drawn hands, signature, text, too many fingers, ugly, username, watermark, worst quality",
        "full": "bad quality, blurry, low resolution, bad anatomy, bad hands, bad fingers, extra fingers, missing fingers, extra limbs, mutated, deformed, ugly face, distorted face, asymmetrical eyes, cross-eyed, jpeg artifacts, noise, watermark, signature, text, worst quality, low quality, normal quality, cropped, out of frame",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PRESETS.keys()),),
                "custom_negatives": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Workflow Power"

    def build(self, preset, custom_negatives):
        base = self.PRESETS.get(preset, "")
        if custom_negatives.strip():
            return (f"{base}, {custom_negatives}",)
        return (base,)


class EthnicitySelector:
    """Select ethnicity with appropriate keywords"""
    
    ETHNICITIES = {
        "caucasian": "caucasian, european features, fair skin",
        "asian": "asian, east asian features, asian appearance",
        "latina": "latina, hispanic features, latin american",
        "african": "african, black, dark skin, african features",
        "indian": "indian, south asian, indian features",
        "middle_eastern": "middle eastern, arabic features, persian",
        "mixed": "mixed ethnicity, multiracial, diverse heritage",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "ethnicity": (list(cls.ETHNICITIES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ethnic_prompt",)
    FUNCTION = "select"
    CATEGORY = "Mason's Nodes/Workflow Power"

    def select(self, prompt, ethnicity):
        ethnic_desc = self.ETHNICITIES.get(ethnicity, "")
        return (f"{prompt}, {ethnic_desc}",)


class MakeupController:
    """Control makeup style"""
    
    MAKEUP = {
        "natural": "natural makeup, minimal makeup, fresh face, subtle makeup",
        "glamour": "glamour makeup, full makeup, perfect makeup, flawless skin",
        "smokey": "smokey eye makeup, dark eye makeup, dramatic eyes",
        "red_lips": "red lipstick, bold lips, classic makeup",
        "nude": "nude makeup, neutral tones, soft colors",
        "no_makeup": "no makeup, bare face, natural skin",
        "artistic": "artistic makeup, colorful makeup, creative makeup",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "makeup_style": (list(cls.MAKEUP.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("makeup_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Workflow Power"

    def apply(self, prompt, makeup_style):
        makeup_desc = self.MAKEUP.get(makeup_style, "")
        return (f"{prompt}, {makeup_desc}",)


NODE_CLASS_MAPPINGS = {
    "PromptDebugger": PromptDebugger,
    "BatchQueueBuilder": BatchQueueBuilder,
    "StyleExtractor": StyleExtractor,
    "NegativePromptBuilder": NegativePromptBuilder,
    "EthnicitySelector": EthnicitySelector,
    "MakeupController": MakeupController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptDebugger": "🔧 Prompt Debugger",
    "BatchQueueBuilder": "📋 Batch Queue Builder",
    "StyleExtractor": "🎨 Style Extractor",
    "NegativePromptBuilder": "🚫 Negative Prompt Builder",
    "EthnicitySelector": "🌍 Ethnicity Selector",
    "MakeupController": "💄 Makeup Controller",
}
