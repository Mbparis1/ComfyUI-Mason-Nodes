"""
Mason's Memory/History Nodes for ComfyUI
Track and compare generation settings for productivity
"""

import os
import json
from datetime import datetime


class SettingsLogger:
    """Logs all generation settings to a searchable history file"""
    
    LOG_FILE = os.path.expanduser("~/AI/ComfyUI/output/generation_history.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "negative": ("STRING", {"default": "", "multiline": True}),
                "seed": ("INT", {"default": 0}),
                "steps": ("INT", {"default": 20}),
                "cfg": ("FLOAT", {"default": 7.0}),
                "sampler": ("STRING", {"default": "euler"}),
                "model": ("STRING", {"default": "unknown"}),
                "rating": (["excellent", "good", "okay", "poor", "unrated"],),
                "notes": ("STRING", {"default": "", "multiline": True}),
                "save_entry": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("images", "log_status")
    FUNCTION = "log_settings"
    CATEGORY = "Mason's Nodes/Memory"
    OUTPUT_NODE = True

    def log_settings(self, images, prompt, negative, seed, steps, cfg, sampler, model, rating, notes, save_entry):
        if not save_entry:
            return (images, "Logging disabled")
        
        try:
            if os.path.exists(self.LOG_FILE):
                with open(self.LOG_FILE, 'r') as f:
                    history = json.load(f)
            else:
                history = []
            
            entry = {
                "id": len(history) + 1,
                "timestamp": datetime.now().isoformat(),
                "prompt": prompt[:500],
                "negative": negative[:300],
                "seed": seed,
                "steps": steps,
                "cfg": cfg,
                "sampler": sampler,
                "model": model,
                "rating": rating,
                "notes": notes,
            }
            
            history.append(entry)
            
            with open(self.LOG_FILE, 'w') as f:
                json.dump(history, f, indent=2)
            
            return (images, f"Saved entry #{entry['id']} - {rating}")
            
        except Exception as e:
            return (images, f"Error: {str(e)}")


class SettingsViewer:
    """View and search past generation settings"""
    
    LOG_FILE = os.path.expanduser("~/AI/ComfyUI/output/generation_history.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "filter_rating": (["all", "excellent", "good", "okay", "poor"],),
                "search_prompt": ("STRING", {"default": ""}),
                "show_last_n": ("INT", {"default": 5, "min": 1, "max": 50}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("history_report",)
    FUNCTION = "view_history"
    CATEGORY = "Mason's Nodes/Memory"

    def view_history(self, filter_rating, search_prompt, show_last_n):
        try:
            if not os.path.exists(self.LOG_FILE):
                return ("No history yet. Use Settings Logger to save entries.",)
            
            with open(self.LOG_FILE, 'r') as f:
                history = json.load(f)
            
            if filter_rating != "all":
                history = [h for h in history if h.get("rating") == filter_rating]
            
            if search_prompt.strip():
                search = search_prompt.lower()
                history = [h for h in history if search in h.get("prompt", "").lower()]
            
            history = history[-show_last_n:]
            
            if not history:
                return ("No matching entries found.",)
            
            lines = [f"=== History ({len(history)} entries) ===\n"]
            for entry in reversed(history):
                lines.append(f"#{entry.get('id')} [{entry.get('rating')}] Seed:{entry.get('seed')} Steps:{entry.get('steps')} CFG:{entry.get('cfg')}")
                lines.append(f"  Prompt: {entry.get('prompt', '')[:80]}...")
                lines.append("")
            
            return ("\n".join(lines),)
            
        except Exception as e:
            return (f"Error: {str(e)}",)


class SettingsRecall:
    """Recall settings from a specific history entry by ID"""
    
    LOG_FILE = os.path.expanduser("~/AI/ComfyUI/output/generation_history.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "entry_id": ("INT", {"default": 1, "min": 1}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "INT", "INT", "FLOAT", "STRING")
    RETURN_NAMES = ("prompt", "negative", "seed", "steps", "cfg", "sampler")
    FUNCTION = "recall"
    CATEGORY = "Mason's Nodes/Memory"

    def recall(self, entry_id):
        try:
            if not os.path.exists(self.LOG_FILE):
                return ("No history", "", 0, 20, 7.0, "euler")
            
            with open(self.LOG_FILE, 'r') as f:
                history = json.load(f)
            
            for h in history:
                if h.get("id") == entry_id:
                    return (h.get("prompt", ""), h.get("negative", ""), h.get("seed", 0),
                            h.get("steps", 20), h.get("cfg", 7.0), h.get("sampler", "euler"))
            
            return (f"Entry #{entry_id} not found", "", 0, 20, 7.0, "euler")
            
        except Exception as e:
            return (f"Error: {str(e)}", "", 0, 20, 7.0, "euler")


class CompareSettings:
    """Compare two history entries side by side"""
    
    LOG_FILE = os.path.expanduser("~/AI/ComfyUI/output/generation_history.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "entry_id_1": ("INT", {"default": 1, "min": 1}),
                "entry_id_2": ("INT", {"default": 2, "min": 1}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("comparison",)
    FUNCTION = "compare"
    CATEGORY = "Mason's Nodes/Memory"

    def compare(self, entry_id_1, entry_id_2):
        try:
            if not os.path.exists(self.LOG_FILE):
                return ("No history yet.",)
            
            with open(self.LOG_FILE, 'r') as f:
                history = json.load(f)
            
            e1 = e2 = None
            for h in history:
                if h.get("id") == entry_id_1: e1 = h
                if h.get("id") == entry_id_2: e2 = h
            
            if not e1 or not e2:
                return ("One or both entries not found.",)
            
            lines = [
                f"=== #{entry_id_1} vs #{entry_id_2} ===",
                f"Rating:  {e1.get('rating')} vs {e2.get('rating')}",
                f"Seed:    {e1.get('seed')} vs {e2.get('seed')}",
                f"Steps:   {e1.get('steps')} vs {e2.get('steps')}",
                f"CFG:     {e1.get('cfg')} vs {e2.get('cfg')}",
                f"Sampler: {e1.get('sampler')} vs {e2.get('sampler')}",
            ]
            return ("\n".join(lines),)
            
        except Exception as e:
            return (f"Error: {str(e)}",)


NODE_CLASS_MAPPINGS = {
    "SettingsLogger": SettingsLogger,
    "SettingsViewer": SettingsViewer,
    "SettingsRecall": SettingsRecall,
    "CompareSettings": CompareSettings,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SettingsLogger": "📝 Settings Logger",
    "SettingsViewer": "👁️ Settings Viewer", 
    "SettingsRecall": "🔄 Settings Recall",
    "CompareSettings": "⚖️ Compare Settings",
}
