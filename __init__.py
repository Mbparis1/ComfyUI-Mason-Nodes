"""
Custom Automation Nodes for ComfyUI
Created for Mason's NSFW content creation workflow
"""

import os
import glob
import random
from PIL import Image
import numpy as np


class BatchPromptGenerator:
    """Generates random prompts from a list for batch processing"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "beautiful woman, photorealistic", "multiline": True}),
                "variations": ("STRING", {"default": "blonde hair\nbrunette\nredhead\nblack hair", "multiline": True}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Automation"

    def generate(self, base_prompt, variations, seed):
        random.seed(seed)
        variation_list = [v.strip() for v in variations.split('\n') if v.strip()]
        if variation_list:
            chosen = random.choice(variation_list)
            full_prompt = f"{base_prompt}, {chosen}"
        else:
            full_prompt = base_prompt
        return (full_prompt,)


class QualityTagsInjector:
    """Automatically adds quality enhancement tags to prompts"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "quality_level": (["standard", "high", "ultra"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("enhanced_prompt",)
    FUNCTION = "enhance"
    CATEGORY = "Mason's Nodes/Automation"

    def enhance(self, prompt, quality_level):
        quality_tags = {
            "standard": "high quality, detailed",
            "high": "masterpiece, best quality, highly detailed, sharp focus, 8k",
            "ultra": "masterpiece, best quality, ultra detailed, photorealistic, 8k uhd, professional photography, sharp focus, intricate details"
        }
        enhanced = f"{prompt}, {quality_tags[quality_level]}"
        return (enhanced,)


# Node mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "BatchPromptGenerator": BatchPromptGenerator,
    "QualityTagsInjector": QualityTagsInjector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BatchPromptGenerator": "🎲 Batch Prompt Generator",
    "QualityTagsInjector": "✨ Quality Tags Injector",
}

# Import GIF converter nodes
from .gif_converter import NODE_CLASS_MAPPINGS as GIF_MAPPINGS
from .gif_converter import NODE_DISPLAY_NAME_MAPPINGS as GIF_DISPLAY_MAPPINGS

# Merge all node mappings
NODE_CLASS_MAPPINGS.update(GIF_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(GIF_DISPLAY_MAPPINGS)


# Import utility nodes
from .utility_nodes import NODE_CLASS_MAPPINGS as UTILITY_MAPPINGS
from .utility_nodes import NODE_DISPLAY_NAME_MAPPINGS as UTILITY_DISPLAY_MAPPINGS

# Merge utility node mappings
NODE_CLASS_MAPPINGS.update(UTILITY_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(UTILITY_DISPLAY_MAPPINGS)

# Import photorealism nodes
from .photorealism_nodes import NODE_CLASS_MAPPINGS as PHOTO_MAPPINGS
from .photorealism_nodes import NODE_DISPLAY_NAME_MAPPINGS as PHOTO_DISPLAY_MAPPINGS

# Merge photorealism node mappings
NODE_CLASS_MAPPINGS.update(PHOTO_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(PHOTO_DISPLAY_MAPPINGS)

# Import pose nodes
from .pose_nodes import NODE_CLASS_MAPPINGS as POSE_MAPPINGS
from .pose_nodes import NODE_DISPLAY_NAME_MAPPINGS as POSE_DISPLAY_MAPPINGS

# Merge pose node mappings
NODE_CLASS_MAPPINGS.update(POSE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(POSE_DISPLAY_MAPPINGS)

# Import memory nodes
from .memory_nodes import NODE_CLASS_MAPPINGS as MEMORY_MAPPINGS
from .memory_nodes import NODE_DISPLAY_NAME_MAPPINGS as MEMORY_DISPLAY_MAPPINGS

# Merge memory node mappings
NODE_CLASS_MAPPINGS.update(MEMORY_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MEMORY_DISPLAY_MAPPINGS)

# Import motion nodes
from .motion_nodes import NODE_CLASS_MAPPINGS as MOTION_MAPPINGS
from .motion_nodes import NODE_DISPLAY_NAME_MAPPINGS as MOTION_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(MOTION_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MOTION_DISPLAY_MAPPINGS)

# Import advanced prompt nodes
from .advanced_prompt_nodes import NODE_CLASS_MAPPINGS as ADVANCED_MAPPINGS
from .advanced_prompt_nodes import NODE_DISPLAY_NAME_MAPPINGS as ADVANCED_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ADVANCED_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ADVANCED_DISPLAY_MAPPINGS)

# Import quality control nodes
from .quality_control_nodes import NODE_CLASS_MAPPINGS as QC_MAPPINGS
from .quality_control_nodes import NODE_DISPLAY_NAME_MAPPINGS as QC_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(QC_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(QC_DISPLAY_MAPPINGS)

# Import workflow helper nodes
from .workflow_helper_nodes import NODE_CLASS_MAPPINGS as WORKFLOW_MAPPINGS
from .workflow_helper_nodes import NODE_DISPLAY_NAME_MAPPINGS as WORKFLOW_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(WORKFLOW_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(WORKFLOW_DISPLAY_MAPPINGS)

# Import motion advanced nodes
from .motion_advanced_nodes import NODE_CLASS_MAPPINGS as MOTION_ADV_MAPPINGS
from .motion_advanced_nodes import NODE_DISPLAY_NAME_MAPPINGS as MOTION_ADV_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(MOTION_ADV_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MOTION_ADV_DISPLAY_MAPPINGS)

# Import content quality nodes
from .content_quality_nodes import NODE_CLASS_MAPPINGS as CQ_MAPPINGS
from .content_quality_nodes import NODE_DISPLAY_NAME_MAPPINGS as CQ_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(CQ_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CQ_DISPLAY_MAPPINGS)

# Import advanced content nodes
from .advanced_content_nodes import NODE_CLASS_MAPPINGS as AC_MAPPINGS
from .advanced_content_nodes import NODE_DISPLAY_NAME_MAPPINGS as AC_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(AC_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(AC_DISPLAY_MAPPINGS)

# Import workflow power nodes
from .workflow_power_nodes import NODE_CLASS_MAPPINGS as WP_MAPPINGS
from .workflow_power_nodes import NODE_DISPLAY_NAME_MAPPINGS as WP_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(WP_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(WP_DISPLAY_MAPPINGS)

# Import smart prompt nodes
from .smart_prompt_nodes import NODE_CLASS_MAPPINGS as SMART_MAPPINGS
from .smart_prompt_nodes import NODE_DISPLAY_NAME_MAPPINGS as SMART_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(SMART_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(SMART_DISPLAY_MAPPINGS)

# Import consistency nodes
from .consistency_nodes import NODE_CLASS_MAPPINGS as CONS_MAPPINGS
from .consistency_nodes import NODE_DISPLAY_NAME_MAPPINGS as CONS_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(CONS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CONS_DISPLAY_MAPPINGS)

# Import specialized content nodes
from .specialized_content_nodes import NODE_CLASS_MAPPINGS as SPEC_MAPPINGS
from .specialized_content_nodes import NODE_DISPLAY_NAME_MAPPINGS as SPEC_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(SPEC_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(SPEC_DISPLAY_MAPPINGS)

# Import production nodes
from .production_nodes import NODE_CLASS_MAPPINGS as PROD_MAPPINGS
from .production_nodes import NODE_DISPLAY_NAME_MAPPINGS as PROD_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(PROD_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(PROD_DISPLAY_MAPPINGS)

# Import animation extended nodes
from .animation_extended_nodes import NODE_CLASS_MAPPINGS as ANIM_EXT_MAPPINGS
from .animation_extended_nodes import NODE_DISPLAY_NAME_MAPPINGS as ANIM_EXT_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ANIM_EXT_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ANIM_EXT_DISPLAY_MAPPINGS)

# Import style master nodes
from .style_master_nodes import NODE_CLASS_MAPPINGS as STYLE_MAPPINGS
from .style_master_nodes import NODE_DISPLAY_NAME_MAPPINGS as STYLE_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(STYLE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(STYLE_DISPLAY_MAPPINGS)

# Import master control nodes
from .master_control_nodes import NODE_CLASS_MAPPINGS as MASTER_MAPPINGS
from .master_control_nodes import NODE_DISPLAY_NAME_MAPPINGS as MASTER_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(MASTER_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MASTER_DISPLAY_MAPPINGS)

# Import realistic motion nodes
from .realistic_motion_nodes import NODE_CLASS_MAPPINGS as REAL_MOTION_MAPPINGS
from .realistic_motion_nodes import NODE_DISPLAY_NAME_MAPPINGS as REAL_MOTION_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(REAL_MOTION_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(REAL_MOTION_DISPLAY_MAPPINGS)
