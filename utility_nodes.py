"""
Mason Nodes - Utility Nodes
Text combination, prompt building, and workflow helper nodes
"""

class MasonTextCombine:
    """Combine multiple text strings with a separator for building prompts."""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "separator": ("STRING", {"default": ", ", "multiline": False}),
            },
            "optional": {
                "text1": ("STRING", {"forceInput": True}),
                "text2": ("STRING", {"forceInput": True}),
                "text3": ("STRING", {"forceInput": True}),
                "text4": ("STRING", {"forceInput": True}),
                "text5": ("STRING", {"forceInput": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("combined_text",)
    FUNCTION = "combine"
    CATEGORY = "Mason/Utilities"
    
    def combine(self, separator=", ", text1="", text2="", text3="", text4="", text5=""):
        # Collect all non-empty texts
        texts = []
        for text in [text1, text2, text3, text4, text5]:
            if text and text.strip():
                texts.append(text.strip())
        
        # Combine with separator
        return (separator.join(texts),)


class MasonPromptBuilder:
    """Build complete prompts with structured sections for optimal generation."""
    
    SUBJECT_TEMPLATES = {
        "Portrait": "1 person, portrait, face focus, head and shoulders",
        "Full Body": "1 person, full body, standing pose",
        "Half Body": "1 person, upper body, waist up",
        "Group": "multiple people, group shot",
        "Action": "1 person, dynamic pose, action shot",
        "Custom": "",
    }
    
    QUALITY_BASES = {
        "Ultra Quality": "masterpiece, best quality, ultra detailed, extremely detailed, professional, 8k uhd, sharp focus, intricate details, perfect anatomy",
        "High Quality": "best quality, highly detailed, sharp, professional",
        "Standard": "good quality, detailed",
        "RAW Photo": "raw photo, dslr, film grain, natural lighting, candid",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "quality_base": (list(cls.QUALITY_BASES.keys()), {"default": "Ultra Quality"}),
                "subject_type": (list(cls.SUBJECT_TEMPLATES.keys()), {"default": "Portrait"}),
            },
            "optional": {
                "character_prompt": ("STRING", {"forceInput": True}),
                "style_prompt": ("STRING", {"forceInput": True}),
                "lighting_prompt": ("STRING", {"forceInput": True}),
                "additional": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("full_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason/Utilities"
    
    def build(self, quality_base, subject_type, character_prompt="", style_prompt="", lighting_prompt="", additional=""):
        parts = []
        
        # Quality first
        if self.QUALITY_BASES[quality_base]:
            parts.append(self.QUALITY_BASES[quality_base])
        
        # Subject template
        if subject_type != "Custom" and self.SUBJECT_TEMPLATES[subject_type]:
            parts.append(self.SUBJECT_TEMPLATES[subject_type])
        
        # Character from selector node
        if character_prompt and character_prompt.strip():
            parts.append(character_prompt.strip())
        
        # Style 
        if style_prompt and style_prompt.strip():
            parts.append(style_prompt.strip())
        
        # Lighting
        if lighting_prompt and lighting_prompt.strip():
            parts.append(lighting_prompt.strip())
        
        # Additional details
        if additional and additional.strip():
            parts.append(additional.strip())
        
        return (", ".join(parts),)


class MasonNegativeBuilder:
    """Build comprehensive negative prompts for different content types."""
    
    PRESETS = {
        "Photorealistic": "deformed, distorted, disfigured, bad anatomy, wrong anatomy, extra limbs, missing limbs, floating limbs, mutated hands, extra fingers, missing fingers, fused fingers, too many fingers, long neck, mutation, poorly drawn face, poorly drawn hands, bad proportions, gross proportions, malformed limbs, cross-eyed, blurry, low quality, jpeg artifacts, signature, watermark, username, artist name, ugly, tiling, out of frame, text, logo",
        "Anime": "deformed, distorted, disfigured, bad anatomy, wrong anatomy, extra limbs, missing limbs, floating limbs, mutated hands, extra fingers, missing fingers, long neck, mutation, poorly drawn face, poorly drawn hands, bad proportions, malformed limbs, cross-eyed, blurry, low quality, signature, watermark, text, 3d, realistic, photo",
        "NSFW Safe": "child, underage, minor, censored, bar censor, mosaic, pixelated, blurry, deformed, bad anatomy, missing limbs, extra limbs, mutated hands, extra fingers",
        "Maximum Quality": "worst quality, low quality, normal quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, artist name, deformed, distorted, disfigured",
        "Minimal": "low quality, blurry, bad anatomy",
        "Custom": "",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PRESETS.keys()), {"default": "Photorealistic"}),
            },
            "optional": {
                "additional_negatives": ("STRING", {"default": "", "multiline": True}),
                "character_negative": ("STRING", {"forceInput": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason/Utilities"
    
    def build(self, preset, additional_negatives="", character_negative=""):
        parts = []
        
        # Preset negative
        if preset != "Custom" and self.PRESETS[preset]:
            parts.append(self.PRESETS[preset])
        
        # Character selector's negative (if provided)
        if character_negative and character_negative.strip():
            parts.append(character_negative.strip())
        
        # Additional
        if additional_negatives and additional_negatives.strip():
            parts.append(additional_negatives.strip())
        
        # Remove duplicates while preserving order
        seen = set()
        unique_parts = []
        for part in ", ".join(parts).split(", "):
            part = part.strip()
            if part and part.lower() not in seen:
                seen.add(part.lower())
                unique_parts.append(part)
        
        return (", ".join(unique_parts),)


class MasonSeedGenerator:
    """Generate or display seeds for reproducible generation."""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "mode": (["fixed", "random", "increment"], {"default": "random"}),
            }
        }
    
    RETURN_TYPES = ("INT", "STRING")
    RETURN_NAMES = ("seed", "seed_string")
    FUNCTION = "generate"
    CATEGORY = "Mason/Utilities"
    
    def generate(self, seed, mode):
        import random
        if mode == "random":
            seed = random.randint(0, 0xffffffffffffffff)
        elif mode == "increment":
            seed = seed + 1
        # fixed keeps the same seed
        
        return (seed, str(seed))


NODE_CLASS_MAPPINGS = {
    "MasonTextCombine": MasonTextCombine,
    "MasonPromptBuilder": MasonPromptBuilder,
    "MasonNegativeBuilder": MasonNegativeBuilder,
    "MasonSeedGenerator": MasonSeedGenerator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonTextCombine": "🔗 Text Combine (Multi-Prompt)",
    "MasonPromptBuilder": "📝 Prompt Builder (Structured)",
    "MasonNegativeBuilder": "❌ Negative Prompt Builder",
    "MasonSeedGenerator": "🎲 Seed Generator",
}
