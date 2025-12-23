"""
Mason's Prompt Utility Nodes for ComfyUI
Prompt manipulation and organization - SD 1.5 optimized
"""

import re


class PromptCombiner:
    """Combine multiple prompt inputs intelligently"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt_1": ("STRING", {"default": "", "multiline": True}),
            },
            "optional": {
                "prompt_2": ("STRING", {"default": "", "multiline": True}),
                "prompt_3": ("STRING", {"default": "", "multiline": True}),
                "prompt_4": ("STRING", {"default": "", "multiline": True}),
                "prompt_5": ("STRING", {"default": "", "multiline": True}),
                "separator": ("STRING", {"default": ", "}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("combined_prompt",)
    FUNCTION = "combine"
    CATEGORY = "Mason's Nodes/Prompt Utilities"

    def combine(self, prompt_1, prompt_2="", prompt_3="", prompt_4="", prompt_5="", separator=", "):
        prompts = [p.strip() for p in [prompt_1, prompt_2, prompt_3, prompt_4, prompt_5] if p.strip()]
        combined = separator.join(prompts)
        # Clean up multiple commas
        combined = re.sub(r',\s*,', ',', combined)
        combined = re.sub(r'\s+', ' ', combined)
        return (combined.strip(),)


class PromptPrioritizer:
    """Add emphasis weights to important prompt elements"""
    
    WEIGHT_PRESETS = {
        "subtle": 1.1,
        "light": 1.2,
        "medium": 1.3,
        "strong": 1.4,
        "very_strong": 1.5,
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "element_to_emphasize": ("STRING", {"default": ""}),
                "weight": (list(cls.WEIGHT_PRESETS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weighted_prompt",)
    FUNCTION = "prioritize"
    CATEGORY = "Mason's Nodes/Prompt Utilities"

    def prioritize(self, prompt, element_to_emphasize, weight):
        if not element_to_emphasize.strip():
            return (prompt,)
        
        weight_val = self.WEIGHT_PRESETS.get(weight, 1.2)
        weighted_element = f"({element_to_emphasize}:{weight_val})"
        
        # Replace element with weighted version if it exists
        if element_to_emphasize in prompt:
            result = prompt.replace(element_to_emphasize, weighted_element)
        else:
            # Add at beginning with weight
            result = f"{weighted_element}, {prompt}"
        
        return (result,)


class PromptCleaner:
    """Clean and normalize prompt formatting"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "remove_duplicates": ("BOOLEAN", {"default": True}),
                "lowercase": ("BOOLEAN", {"default": False}),
                "fix_spacing": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("cleaned_prompt",)
    FUNCTION = "clean"
    CATEGORY = "Mason's Nodes/Prompt Utilities"

    def clean(self, prompt, remove_duplicates, lowercase, fix_spacing):
        result = prompt
        
        # Lowercase if requested
        if lowercase:
            result = result.lower()
        
        # Fix spacing
        if fix_spacing:
            # Fix multiple spaces
            result = re.sub(r'\s+', ' ', result)
            # Fix comma spacing
            result = re.sub(r'\s*,\s*', ', ', result)
            # Remove multiple commas
            result = re.sub(r',(\s*,)+', ',', result)
        
        # Remove duplicates
        if remove_duplicates:
            parts = [p.strip() for p in result.split(',')]
            seen = set()
            unique_parts = []
            for part in parts:
                if part.lower() not in seen and part:
                    seen.add(part.lower())
                    unique_parts.append(part)
            result = ', '.join(unique_parts)
        
        return (result.strip(),)


NODE_CLASS_MAPPINGS = {
    "PromptCombiner": PromptCombiner,
    "PromptPrioritizer": PromptPrioritizer,
    "PromptCleaner": PromptCleaner,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptCombiner": "🔗 Prompt Combiner",
    "PromptPrioritizer": "⬆️ Prompt Prioritizer",
    "PromptCleaner": "🧹 Prompt Cleaner",
}
