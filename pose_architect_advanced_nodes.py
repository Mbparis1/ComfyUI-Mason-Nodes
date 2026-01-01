"""
Mason's Advanced Pose & ControlNet Nodes for ComfyUI
Parametric "Stick Figure" control and advanced ControlNet settings.
"""

class BoneManipulator:
    """Parametric control over specific body joints"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "head_tilt": ("FLOAT", {"default": 0.0, "min": -90.0, "max": 90.0, "step": 5.0}),
                "neck_turn": ("FLOAT", {"default": 0.0, "min": -90.0, "max": 90.0, "step": 5.0}),
                "left_arm_angle": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 180.0, "step": 5.0}),
                "right_arm_angle": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 180.0, "step": 5.0}),
                "spine_bend": ("FLOAT", {"default": 0.0, "min": -45.0, "max": 45.0, "step": 5.0}),
                "leg_spread": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 120.0, "step": 5.0}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose_description",)
    FUNCTION = "calculate"
    CATEGORY = "Mason's Nodes/Pose Advanced"

    def calculate(self, head_tilt, neck_turn, left_arm_angle, right_arm_angle, spine_bend, leg_spread):
        # Translates sliders into descriptive text for OpenPose-like interpretation
        description = []
        if head_tilt > 10: description.append("head tilted right")
        elif head_tilt < -10: description.append("head tilted left")
        
        if neck_turn > 20: description.append("looking right")
        elif neck_turn < -20: description.append("looking left")
        
        if left_arm_angle > 130: description.append("left arm raised high")
        elif left_arm_angle > 80: description.append("left arm out to side")
        elif left_arm_angle > 45: description.append("left arm slightly raised")
        
        if right_arm_angle > 130: description.append("right arm raised high")
        elif right_arm_angle > 80: description.append("right arm out to side")
        elif right_arm_angle > 45: description.append("right arm slightly raised")
        
        if leg_spread > 80: description.append("legs spread very wide")
        elif leg_spread > 40: description.append("legs shoulder width apart")
        
        return (", ".join(description),)


class TextToOpenPose:
    """Generates OpenPose-compatible prompts from text"""
    
    POSE_TYPE = {
        "t_pose": "standing T-pose, arms spread straight out, legs together",
        "a_pose": "standing A-pose, arms down at 45 degrees, legs slightly apart",
        "warrior_pose": "yoga warrior pose, lunge, arms outstretched",
        "lotus_pose": "sitting lotus position, crossed legs, hands on knees",
        "fetal_position": "curled up on side, knees to chest, fetal position",
        "walking": "walking pose, one leg forward, arms swinging",
        "running": "running pose, dynamic stride, arms pumping",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pose": (list(cls.POSE_TYPE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("openpose_text",)
    FUNCTION = "convert"
    CATEGORY = "Mason's Nodes/Pose Advanced"

    def convert(self, pose):
        return (self.POSE_TYPE.get(pose, ""),)


class ControlNetMaster:
    """Advanced ControlNet Settings Helper"""
    
    MODE = {
        "balanced": "balanced control, standard influence",
        "my_prompt_is_more_important": "low controlnet strength, high prompt adherence",
        "controlnet_is_more_important": "high controlnet strength, strict structural adherence",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0, "step": 0.1}),
                "start_percent": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.05}),
                "end_percent": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.05}),
                "mode": (list(cls.MODE.keys()),),
            }
        }

    RETURN_TYPES = ("FLOAT", "FLOAT", "FLOAT")
    RETURN_NAMES = ("strength", "start", "end")
    FUNCTION = "settings"
    CATEGORY = "Mason's Nodes/Pose Advanced"

    def settings(self, strength, start_percent, end_percent, mode):
        # Adjust strength based on mode logic
        final_strength = strength
        if mode == "my_prompt_is_more_important":
            final_strength *= 0.6
        elif mode == "controlnet_is_more_important":
            final_strength *= 1.2
            
        return (final_strength, start_percent, end_percent)


NODE_CLASS_MAPPINGS = {
    "BoneManipulator": BoneManipulator,
    "TextToOpenPose": TextToOpenPose,
    "ControlNetMaster": ControlNetMaster,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BoneManipulator": "🦴 Bone Manipulator (Stick Figure)",
    "TextToOpenPose": "📝 Text to Pose",
    "ControlNetMaster": "🎮 ControlNet Master",
}
