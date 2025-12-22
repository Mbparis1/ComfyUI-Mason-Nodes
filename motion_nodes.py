"""
Mason's Motion/Animation Nodes for ComfyUI
Create smooth animations and frame sequences
"""

import os
import random
import torch
import numpy as np
from PIL import Image


class MotionPromptBuilder:
    """Build prompts for frame sequences with motion keywords"""
    
    MOTIONS = {
        "turning_head": ["looking left", "looking slightly left", "looking forward", "looking slightly right", "looking right"],
        "hair_blow": ["hair still", "hair slightly moving", "hair flowing", "hair blowing in wind", "hair flowing dramatically"],
        "breathing": ["exhaling", "neutral breath", "inhaling", "chest expanded", "neutral breath"],
        "walking_toward": ["far away", "approaching", "getting closer", "close", "very close"],
        "undressing": ["fully clothed", "loosening clothes", "clothes sliding", "partially undressed", "revealing"],
        "expression_change": ["neutral expression", "slight smile", "smiling", "seductive smile", "intense gaze"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "beautiful woman", "multiline": True}),
                "motion_type": (list(cls.MOTIONS.keys()),),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 10}),
                "total_frames": ("INT", {"default": 5, "min": 2, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("prompt", "next_frame")
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Motion"

    def build(self, base_prompt, motion_type, frame_number, total_frames):
        motion_stages = self.MOTIONS.get(motion_type, [""])
        # Map frame number to motion stage
        stage_idx = min(frame_number, len(motion_stages) - 1)
        motion_desc = motion_stages[stage_idx]
        
        prompt = f"{base_prompt}, {motion_desc}"
        next_frame = (frame_number + 1) % total_frames
        
        return (prompt, next_frame)


class BatchFrameSaver:
    """Save images as numbered frames for animation"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "base_name": ("STRING", {"default": "frame"}),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "output_folder": ("STRING", {"default": "animation_output"}),
            }
        }

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("saved_path", "next_frame")
    OUTPUT_NODE = True
    FUNCTION = "save_frame"
    CATEGORY = "Mason's Nodes/Motion"

    def save_frame(self, images, base_name, frame_number, output_folder):
        output_dir = os.path.expanduser(f"~/AI/ComfyUI/output/{output_folder}")
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{base_name}_{frame_number:04d}.png"
        filepath = os.path.join(output_dir, filename)
        
        # Save first image in batch
        img_np = 255. * images[0].cpu().numpy()
        img = Image.fromarray(np.clip(img_np, 0, 255).astype(np.uint8))
        img.save(filepath)
        
        return (filepath, frame_number + 1)


class VideoSettingsCalculator:
    """Calculate optimal settings for animation length and quality"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "desired_duration_seconds": ("FLOAT", {"default": 2.0, "min": 0.5, "max": 10.0}),
                "fps": ("INT", {"default": 10, "min": 5, "max": 30}),
                "quality": (["fast", "balanced", "quality"],),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "STRING")
    RETURN_NAMES = ("total_frames", "steps_per_frame", "frame_delay_ms", "info")
    FUNCTION = "calculate"
    CATEGORY = "Mason's Nodes/Motion"

    def calculate(self, desired_duration_seconds, fps, quality):
        total_frames = int(desired_duration_seconds * fps)
        frame_delay_ms = int(1000 / fps)
        
        steps_map = {"fast": 15, "balanced": 20, "quality": 25}
        steps = steps_map[quality]
        
        est_time_per_frame = steps * 4  # ~4 sec per step on 2GB VRAM
        total_time = total_frames * est_time_per_frame
        
        info = f"{total_frames} frames @ {fps}fps = {desired_duration_seconds}s | Est. generation: {total_time//60}m {total_time%60}s"
        
        return (total_frames, steps, frame_delay_ms, info)


class FrameSeedController:
    """Control seed progression for smooth animations"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "frame_number": ("INT", {"default": 0, "min": 0}),
                "variation_strength": ("FLOAT", {"default": 0.1, "min": 0.0, "max": 1.0}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("frame_seed",)
    FUNCTION = "get_seed"
    CATEGORY = "Mason's Nodes/Motion"

    def get_seed(self, base_seed, frame_number, variation_strength):
        # Small variations for smoother animation
        variation = int(frame_number * variation_strength * 1000)
        return (base_seed + variation,)


NODE_CLASS_MAPPINGS = {
    "MotionPromptBuilder": MotionPromptBuilder,
    "BatchFrameSaver": BatchFrameSaver,
    "VideoSettingsCalculator": VideoSettingsCalculator,
    "FrameSeedController": FrameSeedController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MotionPromptBuilder": "🎬 Motion Prompt Builder",
    "BatchFrameSaver": "💾 Batch Frame Saver",
    "VideoSettingsCalculator": "📊 Video Settings Calculator",
    "FrameSeedController": "🌱 Frame Seed Controller",
}
