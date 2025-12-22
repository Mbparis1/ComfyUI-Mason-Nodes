"""
GIF Conversion Node for ComfyUI
Creates GIFs from image sequences
"""

import os
import glob
import subprocess
from PIL import Image
import numpy as np
import torch


class ImagesToGIF:
    """Converts a batch of images to an animated GIF"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "filename": ("STRING", {"default": "animation"}),
                "frame_delay": ("INT", {"default": 100, "min": 20, "max": 2000, "step": 10}),
                "loop": ("INT", {"default": 0, "min": 0, "max": 100}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("gif_path",)
    OUTPUT_NODE = True
    FUNCTION = "create_gif"
    CATEGORY = "Mason's Nodes/Format Conversion"

    def create_gif(self, images, filename, frame_delay, loop):
        output_dir = os.path.expanduser("~/AI/ComfyUI/output")
        os.makedirs(output_dir, exist_ok=True)
        
        gif_path = os.path.join(output_dir, f"{filename}.gif")
        
        # Convert tensor images to PIL
        pil_images = []
        for image in images:
            img_np = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(img_np, 0, 255).astype(np.uint8))
            pil_images.append(img)
        
        if pil_images:
            # Save as GIF
            pil_images[0].save(
                gif_path,
                save_all=True,
                append_images=pil_images[1:] if len(pil_images) > 1 else [],
                duration=frame_delay,
                loop=loop
            )
        
        return (gif_path,)


class LoadImageSequence:
    """Loads multiple images from a folder as a batch"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": ("STRING", {"default": "~/AI/ComfyUI/output"}),
                "pattern": ("STRING", {"default": "animation_frame_*.png"}),
                "max_images": ("INT", {"default": 10, "min": 1, "max": 100}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)
    FUNCTION = "load_sequence"
    CATEGORY = "Mason's Nodes/Format Conversion"

    def load_sequence(self, folder_path, pattern, max_images):
        folder = os.path.expanduser(folder_path)
        files = sorted(glob.glob(os.path.join(folder, pattern)))[:max_images]
        
        images = []
        for f in files:
            img = Image.open(f).convert('RGB')
            img_np = np.array(img).astype(np.float32) / 255.0
            images.append(torch.from_numpy(img_np))
        
        if images:
            batch = torch.stack(images)
            return (batch,)
        else:
            # Return empty tensor if no images found
            return (torch.zeros(1, 512, 512, 3),)


# Node mappings
NODE_CLASS_MAPPINGS = {
    "ImagesToGIF": ImagesToGIF,
    "LoadImageSequence": LoadImageSequence,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImagesToGIF": "🎬 Images to GIF",
    "LoadImageSequence": "📁 Load Image Sequence",
}
