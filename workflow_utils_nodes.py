"""
Mason's Workflow Utility Nodes for ComfyUI
Project structure, saving, and simplification tools - SD 1.5 optimized
"""

import os
import datetime
import json

class ProjectFolderCreator:
    """Auto-creates a structured folder path: output/date/project_name"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "project_name": ("STRING", {"default": "MyProject"}),
                "include_date": ("BOOLEAN", {"default": True}),
                "base_folder": ("STRING", {"default": "outputs"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("folder_path",)
    FUNCTION = "create_folder"
    CATEGORY = "Mason's Nodes/Automation"

    def create_folder(self, project_name, include_date, base_folder):
        # Sanitize name
        safe_name = "".join([c for c in project_name if c.isalnum() or c in (' ', '-', '_')]).strip()
        safe_name = safe_name.replace(" ", "_")
        
        path_parts = [base_folder]
        
        if include_date:
            date_str = datetime.datetime.now().strftime("%Y-%m-%d")
            path_parts.append(date_str)
            
        path_parts.append(safe_name)
        
        # Absolute path relative to ComfyUI root presumably, but we return relative for save nodes
        full_path = os.path.join(*path_parts)
        
        return (full_path,)


class WorkflowStateSaver:
    """Saves the current prompt settings to a log file"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "folder_path": ("STRING", {"default": "outputs/logs"}),
                "filename_prefix": ("STRING", {"default": "log"}),
                "content_to_save": ("STRING", {"default": "", "multiline": True}),
                "enable_saving": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "save_log"
    OUTPUT_NODE = True
    CATEGORY = "Mason's Nodes/Automation"

    def save_log(self, folder_path, filename_prefix, content_to_save, enable_saving):
        if not enable_saving:
            return {}
            
        # Ensure directory exists (relative to CWD which is usually ComfyUI root)
        try:
            os.makedirs(folder_path, exist_ok=True)
            
            timestamp = datetime.datetime.now().strftime("%H-%M-%S")
            filename = f"{filename_prefix}_{timestamp}.txt"
            filepath = os.path.join(folder_path, filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content_to_save)
                
            print(f"Log saved to: {filepath}")
        except Exception as e:
            print(f"Failed to save log: {e}")
            
        return {}


class StringConcatenator:
    """Concatenates up to 5 strings into one prompt"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "separator": ("STRING", {"default": ", "}),
            },
            "optional": {
                "text_a": ("STRING", {"forceInput": True}),
                "text_b": ("STRING", {"forceInput": True}),
                "text_c": ("STRING", {"forceInput": True}),
                "text_d": ("STRING", {"forceInput": True}),
                "text_e": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("concatenated_text",)
    FUNCTION = "concatenate"
    CATEGORY = "Mason's Nodes/Automation"

    def concatenate(self, separator=", ", text_a="", text_b="", text_c="", text_d="", text_e=""):
        parts = [t for t in [text_a, text_b, text_c, text_d, text_e] if t and t.strip()]
        return (separator.join(parts),)


class SimpleTextNode:
    """Simple text box that outputs a string (useful for workflow organization)"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "output_text"
    CATEGORY = "Mason's Nodes/Automation"

    def output_text(self, text):
        return (text,)



NODE_CLASS_MAPPINGS = {
    "ProjectFolderCreator": ProjectFolderCreator,
    "WorkflowStateSaver": WorkflowStateSaver,
    "StringConcatenator": StringConcatenator,
    "SimpleTextNode": SimpleTextNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ProjectFolderCreator": "📁 Project Folder Creator",
    "WorkflowStateSaver": "💾 Workflow State Saver",
    "StringConcatenator": "🔗 String Concatenator",
    "SimpleTextNode": "📝 Simple Text Node",
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ProjectFolderCreator": "📁 Project Folder Creator",
    "WorkflowStateSaver": "💾 Workflow State Saver",
}
