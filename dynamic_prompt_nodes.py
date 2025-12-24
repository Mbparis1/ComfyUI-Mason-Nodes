"""
Mason's Dynamic Prompt Nodes for ComfyUI
Automation for prompt variation and randomization - SD 1.5 optimized
"""

import random
import re

class WildcardProcessor:
    """Parses {option1|option2} syntax and selects random options"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("processed_text",)
    FUNCTION = "process"
    CATEGORY = "Mason's Nodes/Automation"

    def process(self, text, seed):
        random.seed(seed)
        
        def replace_match(match):
            options = match.group(1).split('|')
            return random.choice(options).strip()
        
        # Recursive processing for nested wildcards {red|{dark|light} blue}
        result = text
        while '{' in result and '}' in result:
            # Find innermost braces
            new_result = re.sub(r'\{([^{}]*)\}', replace_match, result)
            if new_result == result:
                break
            result = new_result
            
        return (result,)


class PromptCycler:
    """Cycles through a list of prompts sequentially based on a counter"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_list": ("STRING", {"default": "Option 1\nOption 2\nOption 3", "multiline": True}),
                "index": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "loops": ("INT", {"default": 1, "min": 1, "max": 100}), # How many times to repeat each item before moving on
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("current_item",)
    FUNCTION = "cycle"
    CATEGORY = "Mason's Nodes/Automation"

    def cycle(self, text_list, index, loops):
        items = [line.strip() for line in text_list.splitlines() if line.strip()]
        if not items:
            return ("",)
            
        # Calculate effective index
        effective_index = (index // loops) % len(items)
        return (items[effective_index],)


class RandomNumberGenerator:
    """Generates random numbers for other nodes"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "min_value": ("FLOAT", {"default": 0.0, "min": -10000.0, "max": 10000.0}),
                "max_value": ("FLOAT", {"default": 1.0, "min": -10000.0, "max": 10000.0}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "is_integer": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("float_value", "int_value")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Automation"

    def generate(self, min_value, max_value, seed, is_integer):
        random.seed(seed)
        
        if is_integer:
            val = random.randint(int(min_value), int(max_value))
            return (float(val), val)
        else:
            val = random.uniform(min_value, max_value)
            return (val, int(val))


class DynamicWeightController:
    """Randomizes the weight of a keyword within a range: (keyword:1.2)"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "keyword": ("STRING", {"default": "", "multiline": False}),
                "min_weight": ("FLOAT", {"default": 0.8, "min": 0.0, "max": 3.0, "step": 0.05}),
                "max_weight": ("FLOAT", {"default": 1.4, "min": 0.0, "max": 3.0, "step": 0.05}),
                "probability": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.05}), # Chance to include at all
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weighted_string",)
    FUNCTION = "process"
    CATEGORY = "Mason's Nodes/Automation"

    def process(self, keyword, min_weight, max_weight, probability, seed):
        random.seed(seed)
        
        if random.random() > probability:
            return ("",)
            
        weight = random.uniform(min_weight, max_weight)
        return (f"({keyword}:{weight:.2f})",)


NODE_CLASS_MAPPINGS = {
    "WildcardProcessor": WildcardProcessor,
    "PromptCycler": PromptCycler,
    "RandomNumberGenerator": RandomNumberGenerator,
    "DynamicWeightController": DynamicWeightController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WildcardProcessor": "🎲 Wildcard Processor {a|b}",
    "PromptCycler": "🔄 Prompt List Cycler",
    "RandomNumberGenerator": "🔢 Random Generator",
    "DynamicWeightController": "⚖️ Dynamic Weight",
}
