"""
Mason's Quality of Life Nodes for ComfyUI
One-click presets and prompt conflict detection - SD 1.5 optimized
"""


class OneClickPresets:
    """One-click optimal settings for common use cases"""
    
    PRESETS = {
        "quick_draft": {
            "description": "Fast preview generation",
            "steps": 15,
            "cfg": 7.0,
            "sampler": "euler_a",
            "width": 384,
            "height": 512,
        },
        "balanced": {
            "description": "Good quality, reasonable speed",
            "steps": 25,
            "cfg": 7.5,
            "sampler": "dpmpp_2m",
            "width": 512,
            "height": 768,
        },
        "high_quality": {
            "description": "Best quality, slower",
            "steps": 40,
            "cfg": 7.0,
            "sampler": "dpmpp_2m_sde",
            "width": 512,
            "height": 768,
        },
        "low_vram_safe": {
            "description": "Optimized for 2GB VRAM",
            "steps": 20,
            "cfg": 7.0,
            "sampler": "euler",
            "width": 384,
            "height": 512,
        },
        "nsfw_optimized": {
            "description": "Best for NSFW content",
            "steps": 30,
            "cfg": 6.5,
            "sampler": "dpmpp_2m",
            "width": 512,
            "height": 768,
        },
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PRESETS.keys()),),
            }
        }

    RETURN_TYPES = ("INT", "FLOAT", "STRING", "INT", "INT", "STRING")
    RETURN_NAMES = ("steps", "cfg", "sampler_name", "width", "height", "description")
    FUNCTION = "get_preset"
    CATEGORY = "Mason's Nodes/QoL"

    def get_preset(self, preset):
        p = self.PRESETS.get(preset, self.PRESETS["balanced"])
        return (p["steps"], p["cfg"], p["sampler"], p["width"], p["height"], p["description"])


class PromptConflictDetector:
    """Detects common prompt conflicts and provides warnings"""
    
    CONFLICTS = [
        (["standing", "sitting"], "Position conflict: standing vs sitting"),
        (["indoors", "outdoors"], "Location conflict: indoors vs outdoors"),
        (["day", "night"], "Time conflict: day vs night"),
        (["clothed", "nude", "naked"], "Clothing conflict: clothed vs nude"),
        (["solo", "couple", "group"], "Subject count conflict"),
        (["happy", "sad", "angry"], "Expression conflict"),
        (["photorealistic", "anime", "cartoon"], "Style conflict"),
    ]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("prompt_passthrough", "warnings")
    FUNCTION = "detect"
    CATEGORY = "Mason's Nodes/QoL"

    def detect(self, prompt):
        prompt_lower = prompt.lower()
        warnings = []
        
        for conflict_group, warning_msg in self.CONFLICTS:
            found = [term for term in conflict_group if term in prompt_lower]
            if len(found) > 1:
                warnings.append(f"⚠️ {warning_msg}: found '{', '.join(found)}'")
        
        # Check for token overload
        word_count = len(prompt.split())
        if word_count > 75:
            warnings.append(f"⚠️ Token overload: {word_count} words (recommended max: 75)")
        
        warning_str = "\n".join(warnings) if warnings else "✅ No conflicts detected"
        return (prompt, warning_str)


class NegativePromptHelper:
    """Generates optimal negative prompts for specific content types"""
    
    CONTENT_TYPES = {
        "photorealistic": (
            "cartoon, anime, illustration, 3d render, cgi, fake, drawing, painting, "
            "sketch, low quality, blurry, out of focus, bad anatomy, deformed"
        ),
        "nsfw": (
            "bad anatomy, deformed genitals, missing limbs, extra limbs, "
            "bad hands, extra fingers, missing fingers, ugly, disgusting, "
            "low quality, blurry, watermark, text"
        ),
        "portrait": (
            "bad face, asymmetric face, deformed eyes, bad eyes, crossed eyes, "
            "ugly, bad teeth, deformed mouth, bad anatomy, blurry, low quality"
        ),
        "full_body": (
            "bad anatomy, wrong proportions, extra limbs, missing limbs, "
            "floating limbs, disconnected limbs, bad hands, extra fingers, "
            "missing fingers, bad feet, extra toes"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "content_type": (list(cls.CONTENT_TYPES.keys()),),
                "additional_negatives": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/QoL"

    def generate(self, content_type, additional_negatives):
        base = self.CONTENT_TYPES.get(content_type, "")
        if additional_negatives.strip():
            return (f"{base}, {additional_negatives}",)
        return (base,)


NODE_CLASS_MAPPINGS = {
    "OneClickPresets": OneClickPresets,
    "PromptConflictDetector": PromptConflictDetector,
    "NegativePromptHelper": NegativePromptHelper,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OneClickPresets": "⚡ One-Click Presets",
    "PromptConflictDetector": "🔍 Prompt Conflict Detector",
    "NegativePromptHelper": "🚫 Negative Prompt Helper",
}
