"""
Mason's Prompt Engineering Pro Nodes for ComfyUI
Advanced prompt weighting and optimization - SD 1.5 optimized
"""


class PromptWeightingHelper:
    """Easily apply emphasis weights to prompt segments"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt_segment": ("STRING", {"default": "", "multiline": True}),
                "weight": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 2.0, "step": 0.05}),
                "apply_weight": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weighted_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Prompt Engineering"

    def apply(self, prompt_segment, weight, apply_weight):
        if not apply_weight or weight == 1.0:
            return (prompt_segment,)
        
        # Apply weight to the entire segment
        weighted = f"({prompt_segment}:{weight:.2f})"
        return (weighted,)


class TokenCountAnalyzer:
    """Analyzes prompt for token count and CLIP limit warnings"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "warn_threshold": ("INT", {"default": 75, "min": 50, "max": 150}),
            }
        }

    RETURN_TYPES = ("STRING", "INT", "STRING")
    RETURN_NAMES = ("prompt_passthrough", "word_count", "status")
    FUNCTION = "analyze"
    CATEGORY = "Mason's Nodes/Prompt Engineering"

    def analyze(self, prompt, warn_threshold):
        words = prompt.split()
        word_count = len(words)
        
        if word_count > warn_threshold:
            status = f"⚠️ WARNING: {word_count} words (limit: {warn_threshold}). Consider trimming."
        elif word_count > warn_threshold * 0.8:
            status = f"⚡ CAUTION: {word_count} words. Approaching limit."
        else:
            status = f"✅ OK: {word_count} words. Well within limit."
        
        return (prompt, word_count, status)


class PromptOptimizer:
    """Removes redundant words and optimizes prompt structure"""
    
    REDUNDANT_PAIRS = [
        ("very ", ""),
        ("really ", ""),
        ("extremely ", ""),
        ("  ", " "),
    ]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "remove_redundant": ("BOOLEAN", {"default": True}),
                "trim_spaces": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("optimized_prompt",)
    FUNCTION = "optimize"
    CATEGORY = "Mason's Nodes/Prompt Engineering"

    def optimize(self, prompt, remove_redundant, trim_spaces):
        result = prompt
        
        if remove_redundant:
            for old, new in self.REDUNDANT_PAIRS:
                result = result.replace(old, new)
        
        if trim_spaces:
            result = " ".join(result.split())
        
        return (result,)


class PromptCombinerPro:
    """Advanced prompt combining with priority and deduplication"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "priority_prompt": ("STRING", {"default": "", "multiline": True}),
                "secondary_prompt": ("STRING", {"default": "", "multiline": True}),
                "tertiary_prompt": ("STRING", {"default": "", "multiline": True}),
                "separator": (["comma", "period", "none"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("combined_prompt",)
    FUNCTION = "combine"
    CATEGORY = "Mason's Nodes/Prompt Engineering"

    def combine(self, priority_prompt, secondary_prompt, tertiary_prompt, separator):
        parts = [p.strip() for p in [priority_prompt, secondary_prompt, tertiary_prompt] if p.strip()]
        
        sep_map = {
            "comma": ", ",
            "period": ". ",
            "none": " ",
        }
        sep = sep_map.get(separator, ", ")
        
        return (sep.join(parts),)


class MegaPromptBuilder:
    """Builds a comprehensive one-liner prompt from core components"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject": ("STRING", {"default": "1girl, beautiful woman", "multiline": False}),
                "style": ("STRING", {"default": "photorealistic, 8k", "multiline": False}),
                "environment": ("STRING", {"default": "studio lighting, simple background", "multiline": False}),
                "quality_tags": ("STRING", {"default": "masterpiece, best quality, ultra detailed", "multiline": False}),
            },
            "optional": {
                "pose": ("STRING", {"default": "", "multiline": False}),
                "clothing": ("STRING", {"default": "", "multiline": False}),
                "expression": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("mega_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Prompt Engineering"

    def build(self, subject, style, environment, quality_tags, pose="", clothing="", expression=""):
        # Priority order: Quality, Subject, Style, Clothing, Pose, Expression, Environment
        parts = [quality_tags, subject, style]
        if clothing: parts.append(clothing)
        if pose: parts.append(pose)
        if expression: parts.append(expression)
        parts.append(environment)
        
        return (", ".join([p.strip() for p in parts if p.strip()]),)


NODE_CLASS_MAPPINGS = {
    "PromptWeightingHelper": PromptWeightingHelper,
    "TokenCountAnalyzer": TokenCountAnalyzer,
    "PromptOptimizer": PromptOptimizer,
    "PromptCombinerPro": PromptCombinerPro,
    "MegaPromptBuilder": MegaPromptBuilder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptWeightingHelper": "⚖️ Prompt Weighting Helper",
    "TokenCountAnalyzer": "📊 Token Count Analyzer",
    "PromptOptimizer": "✨ Prompt Optimizer",
    "PromptCombinerPro": "🔗 Prompt Combiner Pro",
    "MegaPromptBuilder": "🧠 Mega Prompt Builder",
}
