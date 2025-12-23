"""
Mason's System Optimization Nodes for ComfyUI
Provides guidance on CPU offloading and memory optimization
"""


class SystemOptimizationGuide:
    """
    Provides recommended ComfyUI launch arguments for your system
    Does not modify anything - just outputs guidance text
    """
    
    VRAM_PROFILES = {
        "2gb_vram": {
            "args": "--lowvram --disable-xformers",
            "description": "2GB VRAM: Maximum CPU offloading, slower but works",
            "tips": [
                "Use 512x512 or lower resolution",
                "Avoid LoRAs entirely (use our emulator nodes!)",
                "Close other GPU applications",
                "Generate one image at a time",
            ]
        },
        "4gb_vram": {
            "args": "--medvram",
            "description": "4GB VRAM: Moderate CPU offloading",
            "tips": [
                "Can use 512x768 resolution",
                "Limit to 1-2 small LoRAs",
                "Use our LoRA emulators instead",
            ]
        },
        "6gb_vram": {
            "args": "--normalvram",
            "description": "6GB VRAM: Normal operation with some limits",
            "tips": [
                "Can use 768x768 resolution",
                "Can use a few LoRAs",
            ]
        },
        "8gb_plus": {
            "args": "",
            "description": "8GB+ VRAM: Full operation",
            "tips": [
                "Full resolution support",
                "Multiple LoRAs possible",
            ]
        },
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "vram_size": (list(cls.VRAM_PROFILES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("launch_command", "tips")
    FUNCTION = "guide"
    CATEGORY = "Mason's Nodes/System"

    def guide(self, vram_size):
        profile = self.VRAM_PROFILES.get(vram_size, self.VRAM_PROFILES["2gb_vram"])
        
        base_command = "python main.py"
        if profile["args"]:
            command = f"{base_command} {profile['args']}"
        else:
            command = base_command
        
        tips = profile["description"] + "\n\nTips:\n"
        for tip in profile["tips"]:
            tips += f"• {tip}\n"
        
        return (command, tips)


class MotionContentGuide:
    """
    Provides guidance on motion/video content with limited VRAM
    """
    
    MOTION_METHODS = {
        "frame_by_frame": {
            "name": "Frame-by-Frame Generation (RECOMMENDED)",
            "vram_req": "Same as single image (2GB OK)",
            "description": (
                "Generate individual frames with consistent settings, "
                "then compile into video with FFmpeg. "
                "This is the BEST method for low VRAM systems."
            ),
            "workflow": (
                "1. Use ConsistentSubjectLock node for character consistency\n"
                "2. Use PoseTransitionBuilder for smooth pose changes\n"
                "3. Use BatchAnimationBuilder for frame-specific prompts\n"
                "4. Generate each frame individually\n"
                "5. Use VideoCompileHelper to get FFmpeg command\n"
                "6. Run FFmpeg to compile video"
            ),
        },
        "animatediff_lightning": {
            "name": "AnimateDiff Lightning (Experimental)",
            "vram_req": "4GB+ VRAM minimum",
            "description": (
                "AnimateDiff Lightning is faster and uses less VRAM "
                "than standard AnimateDiff. May work on 4GB systems."
            ),
            "workflow": (
                "1. Install AnimateDiff nodes from ComfyUI Manager\n"
                "2. Use Lightning motion model\n"
                "3. Reduce motion frames to 8-16\n"
                "4. Use 384x512 resolution"
            ),
        },
        "deforum": {
            "name": "Deforum-style (Zoom/Pan)",
            "vram_req": "Same as single image (2GB OK)",
            "description": (
                "Create zoom/pan animations by generating images "
                "with slight camera movement between frames."
            ),
            "workflow": (
                "1. Generate base image\n"
                "2. Use img2img with slight zoom/pan\n"
                "3. Repeat for each frame\n"
                "4. Compile with FFmpeg"
            ),
        },
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "method": (list(cls.MOTION_METHODS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("method_name", "requirements", "workflow_guide")
    FUNCTION = "guide"
    CATEGORY = "Mason's Nodes/System"

    def guide(self, method):
        info = self.MOTION_METHODS.get(method, self.MOTION_METHODS["frame_by_frame"])
        return (info["name"], info["vram_req"], info["description"] + "\n\n" + info["workflow"])


class OptimalSettingsCalculator:
    """
    Calculate optimal generation settings for your VRAM
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "vram_gb": ("FLOAT", {"default": 2.0, "min": 1.0, "max": 24.0, "step": 0.5}),
                "content_type": (["portrait", "full_body", "landscape", "motion_frame"],),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "steps", "sampler_recommendation")
    FUNCTION = "calculate"
    CATEGORY = "Mason's Nodes/System"

    def calculate(self, vram_gb, content_type):
        # Base resolution by VRAM
        if vram_gb <= 2:
            base_size = 384
            max_size = 512
        elif vram_gb <= 4:
            base_size = 512
            max_size = 640
        elif vram_gb <= 6:
            base_size = 512
            max_size = 768
        else:
            base_size = 512
            max_size = 1024
        
        # Adjust by content type
        if content_type == "portrait":
            width = base_size
            height = int(base_size * 1.33)  # 3:4
        elif content_type == "full_body":
            width = base_size
            height = int(base_size * 1.5)  # 2:3
        elif content_type == "landscape":
            width = int(base_size * 1.5)
            height = base_size
        else:  # motion_frame - keep small for speed
            width = base_size
            height = base_size
        
        # Ensure multiples of 64
        width = (width // 64) * 64
        height = (height // 64) * 64
        
        # Clamp to max
        width = min(width, max_size)
        height = min(height, max_size)
        
        # Steps based on VRAM (more VRAM = can afford more steps)
        if vram_gb <= 2:
            steps = 20
        elif vram_gb <= 4:
            steps = 25
        else:
            steps = 30
        
        # Sampler recommendation
        if vram_gb <= 2:
            sampler = "euler_a (fast, 20 steps OK)"
        elif vram_gb <= 4:
            sampler = "dpmpp_2m_sde karras (balanced)"
        else:
            sampler = "dpmpp_2m_sde karras or dpmpp_sde"
        
        return (width, height, steps, sampler)


NODE_CLASS_MAPPINGS = {
    "SystemOptimizationGuide": SystemOptimizationGuide,
    "MotionContentGuide": MotionContentGuide,
    "OptimalSettingsCalculator": OptimalSettingsCalculator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SystemOptimizationGuide": "⚙️ System Optimization Guide",
    "MotionContentGuide": "🎬 Motion Content Guide",
    "OptimalSettingsCalculator": "📊 Optimal Settings Calculator",
}
