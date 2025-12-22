"""
Mason's Consistency Helper Nodes for ComfyUI
Keep characters, faces, and scenes consistent - Optimized for SD 1.5
"""

import os
import json


class CharacterSheetGenerator:
    """Lock character traits across generations - SD 1.5 optimized"""
    
    CHAR_FILE = os.path.expanduser("~/AI/ComfyUI/output/characters.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "action": (["create", "load", "list"],),
                "character_name": ("STRING", {"default": "character1"}),
                "hair": ("STRING", {"default": "long blonde hair"}),
                "eyes": ("STRING", {"default": "blue eyes"}),
                "body_type": ("STRING", {"default": "slim, athletic"}),
                "age": ("STRING", {"default": "25 years old, young adult"}),
                "skin": ("STRING", {"default": "fair skin, smooth skin"}),
                "distinguishing": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("character_prompt", "status")
    FUNCTION = "process"
    CATEGORY = "Mason's Nodes/Consistency"

    def process(self, action, character_name, hair, eyes, body_type, age, skin, distinguishing):
        if os.path.exists(self.CHAR_FILE):
            with open(self.CHAR_FILE, 'r') as f:
                characters = json.load(f)
        else:
            characters = {}
        
        if action == "create":
            char_data = {
                "hair": hair, "eyes": eyes, "body_type": body_type,
                "age": age, "skin": skin, "distinguishing": distinguishing
            }
            characters[character_name] = char_data
            with open(self.CHAR_FILE, 'w') as f:
                json.dump(characters, f, indent=2)
            
            prompt = f"{hair}, {eyes}, {body_type}, {age}, {skin}"
            if distinguishing:
                prompt += f", {distinguishing}"
            return (prompt, f"Created '{character_name}'")
        
        elif action == "load":
            if character_name in characters:
                c = characters[character_name]
                prompt = f"{c['hair']}, {c['eyes']}, {c['body_type']}, {c['age']}, {c['skin']}"
                if c.get('distinguishing'):
                    prompt += f", {c['distinguishing']}"
                return (prompt, f"Loaded '{character_name}'")
            return ("", f"'{character_name}' not found")
        
        elif action == "list":
            names = ", ".join(characters.keys()) if characters else "No characters saved"
            return ("", f"Characters: {names}")
        
        return ("", "Unknown action")


class FaceLocker:
    """Keep same face across frames - SD 1.5 keywords"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "face_shape": (["oval", "round", "square", "heart", "oblong"],),
                "nose": (["small", "medium", "prominent", "button", "straight"],),
                "lips": (["thin", "medium", "full", "pouty"],),
                "cheekbones": (["subtle", "defined", "high", "prominent"],),
                "jaw": (["soft", "defined", "angular", "rounded"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("face_locked_prompt",)
    FUNCTION = "lock"
    CATEGORY = "Mason's Nodes/Consistency"

    def lock(self, prompt, face_shape, nose, lips, cheekbones, jaw):
        face_desc = f"{face_shape} face, {nose} nose, {lips} lips, {cheekbones} cheekbones, {jaw} jawline, consistent facial features"
        return (f"{prompt}, {face_desc}",)


class OutfitSaver:
    """Save/recall specific outfit combinations"""
    
    OUTFIT_FILE = os.path.expanduser("~/AI/ComfyUI/output/outfits.json")
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "action": (["save", "load", "list"],),
                "outfit_name": ("STRING", {"default": "outfit1"}),
                "outfit_description": ("STRING", {"default": "red dress, high heels", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("outfit_prompt", "status")
    FUNCTION = "process"
    CATEGORY = "Mason's Nodes/Consistency"

    def process(self, action, outfit_name, outfit_description):
        if os.path.exists(self.OUTFIT_FILE):
            with open(self.OUTFIT_FILE, 'r') as f:
                outfits = json.load(f)
        else:
            outfits = {}
        
        if action == "save":
            outfits[outfit_name] = outfit_description
            with open(self.OUTFIT_FILE, 'w') as f:
                json.dump(outfits, f, indent=2)
            return (outfit_description, f"Saved '{outfit_name}'")
        
        elif action == "load":
            if outfit_name in outfits:
                return (outfits[outfit_name], f"Loaded '{outfit_name}'")
            return ("", f"'{outfit_name}' not found")
        
        elif action == "list":
            return ("", f"Outfits: {', '.join(outfits.keys())}")
        
        return ("", "Unknown action")


class SceneContinuity:
    """Maintain scene elements across shots - SD 1.5 optimized"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject_prompt": ("STRING", {"default": "", "multiline": True}),
                "location": ("STRING", {"default": "bedroom"}),
                "time_of_day": ("STRING", {"default": "afternoon, natural light"}),
                "props": ("STRING", {"default": "bed, pillows, curtains"}),
                "atmosphere": ("STRING", {"default": "intimate, warm"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("continuous_prompt",)
    FUNCTION = "maintain"
    CATEGORY = "Mason's Nodes/Consistency"

    def maintain(self, subject_prompt, location, time_of_day, props, atmosphere):
        scene = f"in {location}, {time_of_day}, {props} visible, {atmosphere} atmosphere, consistent scene, continuous setting"
        return (f"{subject_prompt}, {scene}",)


NODE_CLASS_MAPPINGS = {
    "CharacterSheetGenerator": CharacterSheetGenerator,
    "FaceLocker": FaceLocker,
    "OutfitSaver": OutfitSaver,
    "SceneContinuity": SceneContinuity,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CharacterSheetGenerator": "👤 Character Sheet",
    "FaceLocker": "🔒 Face Locker",
    "OutfitSaver": "👔 Outfit Saver",
    "SceneContinuity": "🎬 Scene Continuity",
}
