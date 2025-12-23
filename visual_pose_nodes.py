"""
Mason's Visual Pose Nodes for ComfyUI
CPU-based OpenPose skeleton drawing and animation - Zero VRAM
"""

import math
import torch
import numpy as np
from PIL import Image, ImageDraw

def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class PoseVisualizer:
    """Draws an OpenPose skeleton based on abstract pose descriptions"""
    
    ARMS = ["down", "up", "t_pose", "crossed", "hands_on_hips"]
    LEGS = ["standing", "sitting", "kneeling", "spread", "walking"]
    VIEW = ["front", "side_left", "side_right", "back"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "arms": (cls.ARMS,),
                "legs": (cls.LEGS,),
                "view": (cls.VIEW,),
                "width": ("INT", {"default": 512, "min": 64, "max": 2048}),
                "height": ("INT", {"default": 512, "min": 64, "max": 2048}),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "draw_pose"
    CATEGORY = "Mason's Nodes/Visual Pose"

    def draw_pose(self, arms, legs, view, width, height):
        # Create black background
        image = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        # Skeleton Colors (OpenPose Standard-ish)
        colors = {
            "body": (0, 0, 255),      # Neck to Hip
            "head": (255, 0, 255),    # Nose/Eyes
            "r_arm": (255, 0, 0),     # Red
            "l_arm": (0, 255, 0),     # Green
            "r_leg": (255, 0, 0),     # Red
            "l_leg": (0, 255, 0),     # Green
        }

        # Abstract coordinate generation (simplified for demo)
        cx, cy = width // 2, height // 2
        
        # Head & Neck
        neck = (cx, cy - 80)
        nose = (cx, cy - 130)
        
        # Hips
        r_hip = (cx - 30, cy + 20)
        l_hip = (cx + 30, cy + 20)
        
        # Shoulders
        r_shoulder = (cx - 50, cy - 80)
        l_shoulder = (cx + 50, cy - 80)
        
        # Process Arms
        if arms == "down":
            r_elbow = (cx - 60, cy - 10)
            r_wrist = (cx - 65, cy + 50)
            l_elbow = (cx + 60, cy - 10)
            l_wrist = (cx + 65, cy + 50)
        elif arms == "up":
            r_elbow = (cx - 70, cy - 120)
            r_wrist = (cx - 80, cy - 170)
            l_elbow = (cx + 70, cy - 120)
            l_wrist = (cx + 80, cy - 170)
        elif arms == "t_pose":
            r_elbow = (cx - 110, cy - 80)
            r_wrist = (cx - 170, cy - 80)
            l_elbow = (cx + 110, cy - 80)
            l_wrist = (cx + 170, cy - 80)
        elif arms == "crossed":
            r_elbow = (cx - 60, cy - 40)
            r_wrist = (cx + 20, cy - 50)
            l_elbow = (cx + 60, cy - 40)
            l_wrist = (cx - 20, cy - 50)
        else: # hands on hips
            r_elbow = (cx - 90, cy - 30)
            r_wrist = (cx - 40, cy + 10)
            l_elbow = (cx + 90, cy - 30)
            l_wrist = (cx + 40, cy + 10)

        # Process Legs
        if legs == "standing":
            r_knee = (cx - 35, cy + 100)
            r_ankle = (cx - 40, cy + 180)
            l_knee = (cx + 35, cy + 100)
            l_ankle = (cx + 40, cy + 180)
        elif legs == "spread":
            r_knee = (cx - 60, cy + 100)
            r_ankle = (cx - 90, cy + 180)
            l_knee = (cx + 60, cy + 100)
            l_ankle = (cx + 90, cy + 180)
        elif legs == "kneeling":
            r_knee = (cx - 35, cy + 100)
            r_ankle = (cx - 35, cy + 180) # effectively simplified
            l_knee = (cx + 35, cy + 100)
            l_ankle = (cx + 35, cy + 180)
            # Adjust height for kneeling logic if simpler
        else: # Walking/Sitting default fallback
            r_knee = (cx - 35, cy + 90)
            r_ankle = (cx - 35, cy + 160)
            l_knee = (cx + 50, cy + 110)
            l_ankle = (cx + 55, cy + 180)

        # Draw Lines (Thickness 4-8)
        # Body
        draw.line([nose, neck], fill=colors["body"], width=4)
        draw.line([neck, r_shoulder], fill=colors["r_arm"], width=4)
        draw.line([neck, l_shoulder], fill=colors["l_arm"], width=4)
        draw.line([neck, r_hip], fill=colors["body"], width=4) # Simplified spine
        draw.line([neck, l_hip], fill=colors["body"], width=4)

        # Arms
        draw.line([r_shoulder, r_elbow], fill=colors["r_arm"], width=4)
        draw.line([r_elbow, r_wrist], fill=colors["r_arm"], width=4)
        draw.line([l_shoulder, l_elbow], fill=colors["l_arm"], width=4)
        draw.line([l_elbow, l_wrist], fill=colors["l_arm"], width=4)

        # Legs
        draw.line([r_hip, r_knee], fill=colors["r_leg"], width=4)
        draw.line([r_knee, r_ankle], fill=colors["r_leg"], width=4)
        draw.line([l_hip, l_knee], fill=colors["l_leg"], width=4)
        draw.line([l_knee, l_ankle], fill=colors["l_leg"], width=4)

        # Circles for joints
        for pt in [nose, neck, r_shoulder, l_shoulder, r_elbow, l_elbow, 
                  r_wrist, l_wrist, r_hip, l_hip, r_knee, l_knee, r_ankle, l_ankle]:
            draw.ellipse([pt[0]-4, pt[1]-4, pt[0]+4, pt[1]+4], fill=(255,255,255))

        out_tensor = pil2tensor(image)
        mask = torch.zeros((1, height, width), dtype=torch.float32) # Simple dummy mask
        
        return (out_tensor, mask)


class SkeletonBuilder:
    """Manual control over every joint angle for custom poses"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "r_arm_angle": ("INT", {"default": 270, "min": 0, "max": 360}),
                "l_arm_angle": ("INT", {"default": 90, "min": 0, "max": 360}),
                "r_leg_angle": ("INT", {"default": 270, "min": 0, "max": 360}),
                "l_leg_angle": ("INT", {"default": 270, "min": 0, "max": 360}),
                "width": ("INT", {"default": 512, "min": 64, "max": 2048}),
                "height": ("INT", {"default": 512, "min": 64, "max": 2048}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "build_skeleton"
    CATEGORY = "Mason's Nodes/Visual Pose"

    def build_skeleton(self, r_arm_angle, l_arm_angle, r_leg_angle, l_leg_angle, width, height):
        # Simplified math to project angles to coordinates
        image = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        cx, cy = width // 2, height // 2
        
        # Center Body
        neck = (cx, cy - 80)
        
        # Helper to get end point from start+angle+length
        def get_pt(start, angle, length):
            rad = math.radians(angle)
            return (start[0] + length * math.cos(rad), start[1] + length * math.sin(rad))
        
        r_shoulder = (cx - 40, cy - 80)
        l_shoulder = (cx + 40, cy - 80)
        r_hip = (cx - 30, cy + 20)
        l_hip = (cx + 30, cy + 20)
        
        # Calculate limbs based on angles
        r_elbow = get_pt(r_shoulder, r_arm_angle, 50)
        r_wrist = get_pt(r_elbow, r_arm_angle, 45) # Straight arm logic for simplicity
        
        l_elbow = get_pt(l_shoulder, l_arm_angle, 50)
        l_wrist = get_pt(l_elbow, l_arm_angle, 45)
        
        r_knee = get_pt(r_hip, r_leg_angle, 70)
        r_ankle = get_pt(r_knee, r_leg_angle, 60)
        
        l_knee = get_pt(l_hip, l_leg_angle, 70)
        l_ankle = get_pt(l_knee, l_leg_angle, 60)
        
        # Draw (Red/Green sides)
        draw.line([neck, r_shoulder], fill=(255,0,0), width=4)
        draw.line([r_shoulder, r_elbow], fill=(255,0,0), width=4)
        draw.line([r_elbow, r_wrist], fill=(255,0,0), width=4)
        
        draw.line([neck, l_shoulder], fill=(0,255,0), width=4)
        draw.line([l_shoulder, l_elbow], fill=(0,255,0), width=4)
        draw.line([l_elbow, l_wrist], fill=(0,255,0), width=4)
        
        draw.line([neck, r_hip], fill=(0,0,255), width=4)
        draw.line([r_hip, r_knee], fill=(255,0,0), width=4)
        draw.line([r_knee, r_ankle], fill=(255,0,0), width=4)

        draw.line([neck, l_hip], fill=(0,0,255), width=4)
        draw.line([l_hip, l_knee], fill=(0,255,0), width=4)
        draw.line([l_knee, l_ankle], fill=(0,255,0), width=4)

        return (pil2tensor(image),)


class PoseAnimationGenerator:
    """Generates a batch of OpenPose frames interpolating between two states"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start_arms": (["down", "up", "t_pose"],),
                "end_arms": (["down", "up", "t_pose"],),
                "frames": ("INT", {"default": 16, "min": 2, "max": 120}),
                "width": ("INT", {"default": 512}),
                "height": ("INT", {"default": 512}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "animate"
    CATEGORY = "Mason's Nodes/Visual Pose"

    def animate(self, start_arms, end_arms, frames, width, height):
        # Generate batch
        batch = []
        
        # Define key points map (Angle driven for smoother interpolation)
        angles = {"down": 90, "t_pose": 0, "up": -90} # Simplified degrees relative to shoulder
        
        start_deg = angles.get(start_arms, 90)
        end_deg = angles.get(end_arms, 90)
        
        for i in range(frames):
            t = i / (frames - 1)
            cur_deg = start_deg + (end_deg - start_deg) * t
            
            # Draw frame
            img_tensor = SkeletonBuilder().build_skeleton(
                int(180 - cur_deg), # Right arm mirrors
                int(cur_deg),       # Left arm
                90, 90,             # Legs straight down (90 deg from horizontal hip line... roughly)
                width, height
            )[0]
            batch.append(img_tensor)
            
        return (torch.cat(batch, dim=0),)


NODE_CLASS_MAPPINGS = {
    "PoseVisualizer": PoseVisualizer,
    "SkeletonBuilder": SkeletonBuilder,
    "PoseAnimationGenerator": PoseAnimationGenerator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PoseVisualizer": "🦴 Visual Pose: Presets",
    "SkeletonBuilder": "🦴 Visual Pose: Manual Builder",
    "PoseAnimationGenerator": "🏃 Visual Pose: Animation Batch",
}
