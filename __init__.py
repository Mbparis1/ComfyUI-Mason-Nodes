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

# Import image enhancement nodes
from .image_enhancement_nodes import NODE_CLASS_MAPPINGS as IMG_ENH_MAPPINGS
from .image_enhancement_nodes import NODE_DISPLAY_NAME_MAPPINGS as IMG_ENH_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(IMG_ENH_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(IMG_ENH_DISPLAY_MAPPINGS)

# Import expression interpolation nodes
from .expression_interpolation_nodes import NODE_CLASS_MAPPINGS as EXPR_MAPPINGS
from .expression_interpolation_nodes import NODE_DISPLAY_NAME_MAPPINGS as EXPR_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(EXPR_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(EXPR_DISPLAY_MAPPINGS)

# Import outfit descriptor nodes
from .outfit_descriptor_nodes import NODE_CLASS_MAPPINGS as OUTFIT_MAPPINGS
from .outfit_descriptor_nodes import NODE_DISPLAY_NAME_MAPPINGS as OUTFIT_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(OUTFIT_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(OUTFIT_DISPLAY_MAPPINGS)

# Import composition nodes
from .composition_nodes import NODE_CLASS_MAPPINGS as COMP_MAPPINGS
from .composition_nodes import NODE_DISPLAY_NAME_MAPPINGS as COMP_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(COMP_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(COMP_DISPLAY_MAPPINGS)

# Import advanced lighting nodes
from .advanced_lighting_nodes import NODE_CLASS_MAPPINGS as ADV_LIGHT_MAPPINGS
from .advanced_lighting_nodes import NODE_DISPLAY_NAME_MAPPINGS as ADV_LIGHT_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ADV_LIGHT_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ADV_LIGHT_DISPLAY_MAPPINGS)

# Import skin detail nodes
from .skin_detail_nodes import NODE_CLASS_MAPPINGS as SKIN_MAPPINGS
from .skin_detail_nodes import NODE_DISPLAY_NAME_MAPPINGS as SKIN_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(SKIN_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(SKIN_DISPLAY_MAPPINGS)

# Import hair detail nodes
from .hair_detail_nodes import NODE_CLASS_MAPPINGS as HAIR_MAPPINGS
from .hair_detail_nodes import NODE_DISPLAY_NAME_MAPPINGS as HAIR_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(HAIR_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(HAIR_DISPLAY_MAPPINGS)

# Import body detail nodes
from .body_detail_nodes import NODE_CLASS_MAPPINGS as BODY_MAPPINGS
from .body_detail_nodes import NODE_DISPLAY_NAME_MAPPINGS as BODY_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(BODY_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(BODY_DISPLAY_MAPPINGS)

# Import face detail nodes
from .face_detail_nodes import NODE_CLASS_MAPPINGS as FACE_MAPPINGS
from .face_detail_nodes import NODE_DISPLAY_NAME_MAPPINGS as FACE_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(FACE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(FACE_DISPLAY_MAPPINGS)

# Import clothing detail nodes
from .clothing_detail_nodes import NODE_CLASS_MAPPINGS as CLOTHING_MAPPINGS
from .clothing_detail_nodes import NODE_DISPLAY_NAME_MAPPINGS as CLOTHING_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(CLOTHING_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CLOTHING_DISPLAY_MAPPINGS)

# Import environment detail nodes
from .environment_detail_nodes import NODE_CLASS_MAPPINGS as ENV_MAPPINGS
from .environment_detail_nodes import NODE_DISPLAY_NAME_MAPPINGS as ENV_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ENV_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ENV_DISPLAY_MAPPINGS)

# Import camera effects nodes
from .camera_effects_nodes import NODE_CLASS_MAPPINGS as CAM_MAPPINGS
from .camera_effects_nodes import NODE_DISPLAY_NAME_MAPPINGS as CAM_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(CAM_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CAM_DISPLAY_MAPPINGS)

# Import artistic style nodes
from .artistic_style_nodes import NODE_CLASS_MAPPINGS as ART_MAPPINGS
from .artistic_style_nodes import NODE_DISPLAY_NAME_MAPPINGS as ART_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ART_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ART_DISPLAY_MAPPINGS)

# Import motion master nodes
from .motion_master_nodes import NODE_CLASS_MAPPINGS as MOTION_MASTER_MAPPINGS
from .motion_master_nodes import NODE_DISPLAY_NAME_MAPPINGS as MOTION_MASTER_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(MOTION_MASTER_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MOTION_MASTER_DISPLAY_MAPPINGS)

# Import scene preset nodes
from .scene_preset_nodes import NODE_CLASS_MAPPINGS as SCENE_PRESET_MAPPINGS
from .scene_preset_nodes import NODE_DISPLAY_NAME_MAPPINGS as SCENE_PRESET_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(SCENE_PRESET_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(SCENE_PRESET_DISPLAY_MAPPINGS)

# Import interaction nodes
from .interaction_nodes import NODE_CLASS_MAPPINGS as INTERACTION_MAPPINGS
from .interaction_nodes import NODE_DISPLAY_NAME_MAPPINGS as INTERACTION_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(INTERACTION_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(INTERACTION_DISPLAY_MAPPINGS)

# Import negative helper nodes
from .negative_helper_nodes import NODE_CLASS_MAPPINGS as NEG_HELPER_MAPPINGS
from .negative_helper_nodes import NODE_DISPLAY_NAME_MAPPINGS as NEG_HELPER_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(NEG_HELPER_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NEG_HELPER_DISPLAY_MAPPINGS)

# Import combo nodes
from .combo_nodes import NODE_CLASS_MAPPINGS as COMBO_MAPPINGS
from .combo_nodes import NODE_DISPLAY_NAME_MAPPINGS as COMBO_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(COMBO_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(COMBO_DISPLAY_MAPPINGS)

# Import prompt utility nodes
from .prompt_utility_nodes import NODE_CLASS_MAPPINGS as PROMPT_UTIL_MAPPINGS
from .prompt_utility_nodes import NODE_DISPLAY_NAME_MAPPINGS as PROMPT_UTIL_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(PROMPT_UTIL_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(PROMPT_UTIL_DISPLAY_MAPPINGS)

# Import randomizer nodes
from .randomizer_nodes import NODE_CLASS_MAPPINGS as RANDOMIZER_MAPPINGS
from .randomizer_nodes import NODE_DISPLAY_NAME_MAPPINGS as RANDOMIZER_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(RANDOMIZER_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(RANDOMIZER_DISPLAY_MAPPINGS)

# Import output helper nodes
from .output_helper_nodes import NODE_CLASS_MAPPINGS as OUTPUT_HELPER_MAPPINGS
from .output_helper_nodes import NODE_DISPLAY_NAME_MAPPINGS as OUTPUT_HELPER_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(OUTPUT_HELPER_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(OUTPUT_HELPER_DISPLAY_MAPPINGS)

# Import NSFW content nodes
from .nsfw_content_nodes import NODE_CLASS_MAPPINGS as NSFW_CONTENT_MAPPINGS
from .nsfw_content_nodes import NODE_DISPLAY_NAME_MAPPINGS as NSFW_CONTENT_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(NSFW_CONTENT_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NSFW_CONTENT_DISPLAY_MAPPINGS)

# Import NSFW scene nodes
from .nsfw_scene_nodes import NODE_CLASS_MAPPINGS as NSFW_SCENE_MAPPINGS
from .nsfw_scene_nodes import NODE_DISPLAY_NAME_MAPPINGS as NSFW_SCENE_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(NSFW_SCENE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NSFW_SCENE_DISPLAY_MAPPINGS)

# Import photography pro nodes
from .photography_pro_nodes import NODE_CLASS_MAPPINGS as PHOTO_PRO_MAPPINGS
from .photography_pro_nodes import NODE_DISPLAY_NAME_MAPPINGS as PHOTO_PRO_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(PHOTO_PRO_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(PHOTO_PRO_DISPLAY_MAPPINGS)

# Import realism pro nodes
from .realism_pro_nodes import NODE_CLASS_MAPPINGS as REALISM_PRO_MAPPINGS
from .realism_pro_nodes import NODE_DISPLAY_NAME_MAPPINGS as REALISM_PRO_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(REALISM_PRO_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(REALISM_PRO_DISPLAY_MAPPINGS)

# Import color science nodes
from .color_science_nodes import NODE_CLASS_MAPPINGS as COLOR_SCIENCE_MAPPINGS
from .color_science_nodes import NODE_DISPLAY_NAME_MAPPINGS as COLOR_SCIENCE_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(COLOR_SCIENCE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(COLOR_SCIENCE_DISPLAY_MAPPINGS)

# Import model style nodes
from .model_style_nodes import NODE_CLASS_MAPPINGS as MODEL_STYLE_MAPPINGS
from .model_style_nodes import NODE_DISPLAY_NAME_MAPPINGS as MODEL_STYLE_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(MODEL_STYLE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MODEL_STYLE_DISPLAY_MAPPINGS)

# Import LoRA emulator nodes
from .lora_emulator_nodes import NODE_CLASS_MAPPINGS as LORA_EMULATOR_MAPPINGS
from .lora_emulator_nodes import NODE_DISPLAY_NAME_MAPPINGS as LORA_EMULATOR_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(LORA_EMULATOR_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(LORA_EMULATOR_DISPLAY_MAPPINGS)

# Import extended LoRA emulator nodes
from .lora_emulator_extended_nodes import NODE_CLASS_MAPPINGS as LORA_EXT_MAPPINGS
from .lora_emulator_extended_nodes import NODE_DISPLAY_NAME_MAPPINGS as LORA_EXT_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(LORA_EXT_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(LORA_EXT_DISPLAY_MAPPINGS)

# Import system optimization nodes
from .system_optimization_nodes import NODE_CLASS_MAPPINGS as SYS_OPT_MAPPINGS
from .system_optimization_nodes import NODE_DISPLAY_NAME_MAPPINGS as SYS_OPT_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(SYS_OPT_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(SYS_OPT_DISPLAY_MAPPINGS)

# Import accessory detail nodes
from .accessory_detail_nodes import NODE_CLASS_MAPPINGS as ACCESSORY_MAPPINGS
from .accessory_detail_nodes import NODE_DISPLAY_NAME_MAPPINGS as ACCESSORY_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ACCESSORY_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ACCESSORY_DISPLAY_MAPPINGS)

# Import advanced control nodes
from .advanced_control_nodes import NODE_CLASS_MAPPINGS as ADV_CONTROL_MAPPINGS
from .advanced_control_nodes import NODE_DISPLAY_NAME_MAPPINGS as ADV_CONTROL_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ADV_CONTROL_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ADV_CONTROL_DISPLAY_MAPPINGS)

# Import micro detail nodes
from .micro_detail_nodes import NODE_CLASS_MAPPINGS as MICRO_MAPPINGS
from .micro_detail_nodes import NODE_DISPLAY_NAME_MAPPINGS as MICRO_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(MICRO_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MICRO_DISPLAY_MAPPINGS)

# Import efficiency nodes
from .efficiency_nodes import NODE_CLASS_MAPPINGS as EFFICIENCY_MAPPINGS
from .efficiency_nodes import NODE_DISPLAY_NAME_MAPPINGS as EFFICIENCY_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(EFFICIENCY_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(EFFICIENCY_DISPLAY_MAPPINGS)

# Import NSFW LoRA emulator nodes
from .nsfw_lora_emulator_nodes import NODE_CLASS_MAPPINGS as NSFW_LORA_MAPPINGS
from .nsfw_lora_emulator_nodes import NODE_DISPLAY_NAME_MAPPINGS as NSFW_LORA_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(NSFW_LORA_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NSFW_LORA_DISPLAY_MAPPINGS)

# Import NSFW act nodes
from .nsfw_act_nodes import NODE_CLASS_MAPPINGS as NSFW_ACT_MAPPINGS
from .nsfw_act_nodes import NODE_DISPLAY_NAME_MAPPINGS as NSFW_ACT_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(NSFW_ACT_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NSFW_ACT_DISPLAY_MAPPINGS)

# Import niche NSFW act nodes
from .nsfw_niche_act_nodes import NODE_CLASS_MAPPINGS as NSFW_NICHE_MAPPINGS
from .nsfw_niche_act_nodes import NODE_DISPLAY_NAME_MAPPINGS as NSFW_NICHE_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(NSFW_NICHE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NSFW_NICHE_DISPLAY_MAPPINGS)

# Import NSFW Mechanics nodes
from .nsfw_mechanics_nodes import NODE_CLASS_MAPPINGS as NSFW_MECH_MAPPINGS
from .nsfw_mechanics_nodes import NODE_DISPLAY_NAME_MAPPINGS as NSFW_MECH_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(NSFW_MECH_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NSFW_MECH_DISPLAY_MAPPINGS)

# Import Pose Architect nodes
from .pose_architect_nodes import NODE_CLASS_MAPPINGS as POSE_ARCHITECT_MAPPINGS
from .pose_architect_nodes import NODE_DISPLAY_NAME_MAPPINGS as POSE_ARCHITECT_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(POSE_ARCHITECT_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(POSE_ARCHITECT_DISPLAY_MAPPINGS)

# Import Fantasy NSFW nodes
from .fantasy_nsfw_nodes import NODE_CLASS_MAPPINGS as FANTASY_NSFW_MAPPINGS
from .fantasy_nsfw_nodes import NODE_DISPLAY_NAME_MAPPINGS as FANTASY_NSFW_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(FANTASY_NSFW_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(FANTASY_NSFW_DISPLAY_MAPPINGS)

# Import Cosplay nodes
from .cosplay_costume_nodes import NODE_CLASS_MAPPINGS as COSPLAY_MAPPINGS
from .cosplay_costume_nodes import NODE_DISPLAY_NAME_MAPPINGS as COSPLAY_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(COSPLAY_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(COSPLAY_DISPLAY_MAPPINGS)

# Import Visual Pose nodes
from .visual_pose_nodes import NODE_CLASS_MAPPINGS as VISUAL_POSE_MAPPINGS
from .visual_pose_nodes import NODE_DISPLAY_NAME_MAPPINGS as VISUAL_POSE_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(VISUAL_POSE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(VISUAL_POSE_DISPLAY_MAPPINGS)

# Import Automation & Utility nodes
from .dynamic_prompt_nodes import NODE_CLASS_MAPPINGS as DYNAMIC_PROMPT_MAPPINGS
from .dynamic_prompt_nodes import NODE_DISPLAY_NAME_MAPPINGS as DYNAMIC_PROMPT_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(DYNAMIC_PROMPT_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(DYNAMIC_PROMPT_DISPLAY_MAPPINGS)

from .pose_preset_nodes import NODE_CLASS_MAPPINGS as POSE_PRESET_MAPPINGS
from .pose_preset_nodes import NODE_DISPLAY_NAME_MAPPINGS as POSE_PRESET_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(POSE_PRESET_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(POSE_PRESET_DISPLAY_MAPPINGS)

from .workflow_utils_nodes import NODE_CLASS_MAPPINGS as WORKFLOW_UTILS_MAPPINGS
from .workflow_utils_nodes import NODE_DISPLAY_NAME_MAPPINGS as WORKFLOW_UTILS_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(WORKFLOW_UTILS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(WORKFLOW_UTILS_DISPLAY_MAPPINGS)

# Import Phase 10: The Master's Touch
from .aesthetic_nodes import NODE_CLASS_MAPPINGS as AESTHETIC_MAPPINGS
from .aesthetic_nodes import NODE_DISPLAY_NAME_MAPPINGS as AESTHETIC_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(AESTHETIC_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(AESTHETIC_DISPLAY_MAPPINGS)

from .interaction_nodes import NODE_CLASS_MAPPINGS as INTERACTION_MAPPINGS
from .interaction_nodes import NODE_DISPLAY_NAME_MAPPINGS as INTERACTION_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(INTERACTION_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(INTERACTION_DISPLAY_MAPPINGS)

from .expression_nodes import NODE_CLASS_MAPPINGS as EXPRESSION_MAPPINGS
from .expression_nodes import NODE_DISPLAY_NAME_MAPPINGS as EXPRESSION_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(EXPRESSION_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(EXPRESSION_DISPLAY_MAPPINGS)

from .narrative_nodes import NODE_CLASS_MAPPINGS as NARRATIVE_MAPPINGS
from .narrative_nodes import NODE_DISPLAY_NAME_MAPPINGS as NARRATIVE_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(NARRATIVE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NARRATIVE_DISPLAY_MAPPINGS)

from .extreme_nsfw_nodes import NODE_CLASS_MAPPINGS as EXTREME_NSFW_MAPPINGS
from .extreme_nsfw_nodes import NODE_DISPLAY_NAME_MAPPINGS as EXTREME_NSFW_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(EXTREME_NSFW_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(EXTREME_NSFW_DISPLAY_MAPPINGS)

# Import Phase 10 Implementation (The Master's Touch - New Files)
from .aesthetic_direction_nodes import NODE_CLASS_MAPPINGS as AESTHETIC_DIR_MAPPINGS
from .aesthetic_direction_nodes import NODE_DISPLAY_NAME_MAPPINGS as AESTHETIC_DIR_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(AESTHETIC_DIR_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(AESTHETIC_DIR_DISPLAY_MAPPINGS)

from .surface_physics_nodes import NODE_CLASS_MAPPINGS as SURF_PHYS_MAPPINGS
from .surface_physics_nodes import NODE_DISPLAY_NAME_MAPPINGS as SURF_PHYS_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(SURF_PHYS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(SURF_PHYS_DISPLAY_MAPPINGS)

from .micro_expressions_nodes import NODE_CLASS_MAPPINGS as MICRO_EXPR_MAPPINGS
from .micro_expressions_nodes import NODE_DISPLAY_NAME_MAPPINGS as MICRO_EXPR_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(MICRO_EXPR_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MICRO_EXPR_DISPLAY_MAPPINGS)

from .narrative_scenario_nodes import NODE_CLASS_MAPPINGS as NAR_SCENARIO_MAPPINGS
from .narrative_scenario_nodes import NODE_DISPLAY_NAME_MAPPINGS as NAR_SCENARIO_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(NAR_SCENARIO_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NAR_SCENARIO_DISPLAY_MAPPINGS)

# Import Phase 11: Act Perfection
from .nsfw_act_perfection_nodes import NODE_CLASS_MAPPINGS as ACT_PERFECTION_MAPPINGS
from .nsfw_act_perfection_nodes import NODE_DISPLAY_NAME_MAPPINGS as ACT_PERFECTION_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ACT_PERFECTION_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ACT_PERFECTION_DISPLAY_MAPPINGS)

# Import Phase 12: Pose & ControlNet Mastery
from .pose_architect_advanced_nodes import NODE_CLASS_MAPPINGS as POSE_ADV_MAPPINGS
from .pose_architect_advanced_nodes import NODE_DISPLAY_NAME_MAPPINGS as POSE_ADV_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(POSE_ADV_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(POSE_ADV_DISPLAY_MAPPINGS)

# Import Phase 13: Advanced Enhancements
from .batch_helper_nodes import NODE_CLASS_MAPPINGS as BATCH_HELPER_MAPPINGS
from .batch_helper_nodes import NODE_DISPLAY_NAME_MAPPINGS as BATCH_HELPER_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(BATCH_HELPER_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(BATCH_HELPER_DISPLAY_MAPPINGS)

from .niche_fetish_nodes import NODE_CLASS_MAPPINGS as NICHE_FETISH_MAPPINGS
from .niche_fetish_nodes import NODE_DISPLAY_NAME_MAPPINGS as NICHE_FETISH_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(NICHE_FETISH_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(NICHE_FETISH_DISPLAY_MAPPINGS)

from .environment_detail_nodes import NODE_CLASS_MAPPINGS as ENV_DETAIL_MAPPINGS
from .environment_detail_nodes import NODE_DISPLAY_NAME_MAPPINGS as ENV_DETAIL_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ENV_DETAIL_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ENV_DETAIL_DISPLAY_MAPPINGS)

from .qol_nodes import NODE_CLASS_MAPPINGS as QOL_MAPPINGS
from .qol_nodes import NODE_DISPLAY_NAME_MAPPINGS as QOL_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(QOL_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(QOL_DISPLAY_MAPPINGS)

# Import Phase 14: Cinema & Fantasy Suite
from .creature_nodes import NODE_CLASS_MAPPINGS as CREATURE_MAPPINGS
from .creature_nodes import NODE_DISPLAY_NAME_MAPPINGS as CREATURE_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(CREATURE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CREATURE_DISPLAY_MAPPINGS)

from .cinematic_nodes import NODE_CLASS_MAPPINGS as CINEMATIC_MAPPINGS
from .cinematic_nodes import NODE_DISPLAY_NAME_MAPPINGS as CINEMATIC_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(CINEMATIC_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CINEMATIC_DISPLAY_MAPPINGS)

from .period_costume_nodes import NODE_CLASS_MAPPINGS as PERIOD_COSTUME_MAPPINGS
from .period_costume_nodes import NODE_DISPLAY_NAME_MAPPINGS as PERIOD_COSTUME_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(PERIOD_COSTUME_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(PERIOD_COSTUME_DISPLAY_MAPPINGS)

from .environmental_fx_nodes import NODE_CLASS_MAPPINGS as ENV_FX_MAPPINGS
from .environmental_fx_nodes import NODE_DISPLAY_NAME_MAPPINGS as ENV_FX_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ENV_FX_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ENV_FX_DISPLAY_MAPPINGS)

# Import Phase 15: Final Perfection Suite
from .prompt_engineering_nodes import NODE_CLASS_MAPPINGS as PROMPT_ENG_MAPPINGS
from .prompt_engineering_nodes import NODE_DISPLAY_NAME_MAPPINGS as PROMPT_ENG_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(PROMPT_ENG_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(PROMPT_ENG_DISPLAY_MAPPINGS)

from .multi_character_nodes import NODE_CLASS_MAPPINGS as MULTI_CHAR_MAPPINGS
from .multi_character_nodes import NODE_DISPLAY_NAME_MAPPINGS as MULTI_CHAR_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(MULTI_CHAR_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MULTI_CHAR_DISPLAY_MAPPINGS)

from .material_nodes import NODE_CLASS_MAPPINGS as MATERIAL_MAPPINGS
from .material_nodes import NODE_DISPLAY_NAME_MAPPINGS as MATERIAL_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(MATERIAL_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MATERIAL_DISPLAY_MAPPINGS)

from .vehicle_nodes import NODE_CLASS_MAPPINGS as VEHICLE_MAPPINGS
from .vehicle_nodes import NODE_DISPLAY_NAME_MAPPINGS as VEHICLE_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(VEHICLE_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(VEHICLE_DISPLAY_MAPPINGS)

from .architecture_nodes import NODE_CLASS_MAPPINGS as ARCH_MAPPINGS
from .architecture_nodes import NODE_DISPLAY_NAME_MAPPINGS as ARCH_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(ARCH_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(ARCH_DISPLAY_MAPPINGS)

from .weapon_prop_nodes import NODE_CLASS_MAPPINGS as WEAPON_MAPPINGS
from .weapon_prop_nodes import NODE_DISPLAY_NAME_MAPPINGS as WEAPON_DISPLAY_MAPPINGS
NODE_CLASS_MAPPINGS.update(WEAPON_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(WEAPON_DISPLAY_MAPPINGS)

# Import private nodes (local only, not tracked by git)
try:
    from .private_nodes import NODE_CLASS_MAPPINGS as PRIVATE_MAPPINGS
    from .private_nodes import NODE_DISPLAY_NAME_MAPPINGS as PRIVATE_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(PRIVATE_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(PRIVATE_DISPLAY_MAPPINGS)
except ImportError:
    pass  # Private nodes file doesn't exist, skip
