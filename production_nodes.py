"""
Mason's Production Workflow Nodes for ComfyUI
Project organization and metadata management
"""

import os
import json
from datetime import datetime


class ProjectOrganizer:
    """Auto-name and sort outputs by project"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "project_name": ("STRING", {"default": "project1"}),
                "category": ("STRING", {"default": "portraits"}),
                "auto_increment": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("output_folder", "filename_prefix")
    FUNCTION = "organize"
    CATEGORY = "Mason's Nodes/Production"

    def organize(self, project_name, category, auto_increment):
        base_dir = os.path.expanduser(f"~/AI/ComfyUI/output/{project_name}/{category}")
        os.makedirs(base_dir, exist_ok=True)
        
        # Count existing files for auto-increment
        if auto_increment:
            existing = len([f for f in os.listdir(base_dir) if f.endswith('.png')]) if os.path.exists(base_dir) else 0
            prefix = f"{project_name}_{category}_{existing + 1:04d}"
        else:
            prefix = f"{project_name}_{category}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        return (base_dir, prefix)


class MetadataEmbedder:
    """Save prompt/settings as text file alongside image"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "output_folder": ("STRING", {"default": ""}),
                "filename": ("STRING", {"default": "image"}),
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "negative": ("STRING", {"default": "", "multiline": True}),
                "seed": ("INT", {"default": 0}),
                "steps": ("INT", {"default": 20}),
                "cfg": ("FLOAT", {"default": 7.0}),
                "model": ("STRING", {"default": "dreamshaper_8"}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("images", "metadata_path")
    OUTPUT_NODE = True
    FUNCTION = "embed"
    CATEGORY = "Mason's Nodes/Production"

    def embed(self, images, output_folder, filename, prompt, negative, seed, steps, cfg, model):
        folder = output_folder if output_folder else os.path.expanduser("~/AI/ComfyUI/output")
        os.makedirs(folder, exist_ok=True)
        
        metadata = {
            "prompt": prompt,
            "negative_prompt": negative,
            "seed": seed,
            "steps": steps,
            "cfg": cfg,
            "model": model,
            "generated": datetime.now().isoformat(),
        }
        
        meta_path = os.path.join(folder, f"{filename}_metadata.json")
        with open(meta_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return (images, meta_path)


class ThumbnailGenerator:
    """Create contact sheet info for batch outputs"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "batch_name": ("STRING", {"default": "batch1"}),
                "image_index": ("INT", {"default": 0, "min": 0}),
                "total_in_batch": ("INT", {"default": 1, "min": 1}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("images", "batch_info")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Production"

    def generate(self, images, batch_name, image_index, total_in_batch):
        info = f"Batch: {batch_name} | Image {image_index + 1} of {total_in_batch}"
        return (images, info)


class VersionTracker:
    """Track iterations of same concept"""
    
    VERSION_FILE = os.path.expanduser("~/AI/ComfyUI/output/versions.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "concept_name": ("STRING", {"default": "concept1"}),
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "notes": ("STRING", {"default": "", "multiline": True}),
                "rating": (["1_poor", "2_okay", "3_good", "4_great", "5_excellent"],),
            }
        }

    RETURN_TYPES = ("INT", "STRING")
    RETURN_NAMES = ("version_number", "history")
    FUNCTION = "track"
    CATEGORY = "Mason's Nodes/Production"

    def track(self, concept_name, prompt, notes, rating):
        if os.path.exists(self.VERSION_FILE):
            with open(self.VERSION_FILE, 'r') as f:
                versions = json.load(f)
        else:
            versions = {}
        
        if concept_name not in versions:
            versions[concept_name] = []
        
        version_num = len(versions[concept_name]) + 1
        
        versions[concept_name].append({
            "version": version_num,
            "prompt": prompt[:200],
            "notes": notes,
            "rating": rating,
            "timestamp": datetime.now().isoformat(),
        })
        
        with open(self.VERSION_FILE, 'w') as f:
            json.dump(versions, f, indent=2)
        
        # Build history string
        history_items = versions[concept_name][-5:]  # Last 5
        history = "\n".join([f"v{v['version']}: {v['rating']} - {v['notes'][:30]}" for v in history_items])
        
        return (version_num, history)


NODE_CLASS_MAPPINGS = {
    "ProjectOrganizer": ProjectOrganizer,
    "MetadataEmbedder": MetadataEmbedder,
    "ThumbnailGenerator": ThumbnailGenerator,
    "VersionTracker": VersionTracker,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ProjectOrganizer": "📁 Project Organizer",
    "MetadataEmbedder": "📋 Metadata Embedder",
    "ThumbnailGenerator": "🖼️ Thumbnail Generator",
    "VersionTracker": "📝 Version Tracker",
}
