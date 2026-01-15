import torch
import gc
import comfy.model_management

class SmartMemoryManager:
    """
    Intelligent Memory Management for Low VRAM Systems (e.g., GT 1030 2GB).
    Allows manual triggers for VRAM cleanup and model offloading.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "any_input": ("*",), # Pass-through anything
                "mode": (["Soft Cleanup", "Aggressive Cleanup", "Force Unload All"],),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("output",)
    FUNCTION = "manage_memory"
    CATEGORY = "Mason's Nodes/System"

    def manage_memory(self, any_input, mode):
        print(f"🧹 SmartMemoryManager: Executing {mode}...")
        
        if mode == "Soft Cleanup":
            comfy.model_management.soft_empty_cache()
            
        elif mode == "Aggressive Cleanup":
            comfy.model_management.soft_empty_cache()
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                torch.cuda.ipc_collect()
                
        elif mode == "Force Unload All":
            # This is the "Nuclear" option
            comfy.model_management.unload_all_models()
            comfy.model_management.soft_empty_cache()
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

        # Return the input unchanged so the workflow continues
        return (any_input,)

class VRAMMonitor:
    """
    Returns current VRAM usage statistics.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    RETURN_TYPES = ("STRING", "FLOAT", "FLOAT")
    RETURN_NAMES = ("status_text", "free_vram_gb", "used_vram_gb")
    FUNCTION = "get_status"
    CATEGORY = "Mason's Nodes/System"

    def get_status(self):
        if not torch.cuda.is_available():
            return ("No CUDA", 0.0, 0.0)
        
        free, total = torch.cuda.mem_get_info()
        free_gb = free / (1024**3)
        total_gb = total / (1024**3)
        used_gb = total_gb - free_gb
        
        status = f"VRAM: {used_gb:.2f}GB / {total_gb:.2f}GB (Free: {free_gb:.2f}GB)"
        return (status, free_gb, used_gb)

NODE_CLASS_MAPPINGS = {
    "SmartMemoryManager": SmartMemoryManager,
    "VRAMMonitor": VRAMMonitor
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SmartMemoryManager": "🧠 Smart Memory Manager (Output)",
    "VRAMMonitor": "📊 VRAM Monitor"
}
