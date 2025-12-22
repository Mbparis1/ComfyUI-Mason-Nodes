"""
Mason's Pose Direction Nodes for ComfyUI
Nodes for precise pose and position control
"""


class PoseDirector:
    """Generates detailed pose descriptions for specific positions"""
    
    POSES = {
        "bent_over_away": "bent over, bending forward at waist, legs spread wide for balance, back arched, from behind, rear view, facing away from viewer, backside visible, standing bent position",
        "bent_over_side": "bent over, bending forward, side view, profile view, arched back, legs apart",
        "on_all_fours": "on all fours, hands and knees, crawling position, from behind, rear view, facing away",
        "standing_away": "standing, back to viewer, rear view, from behind, facing away, looking over shoulder",
        "lying_face_down": "lying face down, prone position, on stomach, from behind view, rear visible",
        "lying_on_back": "lying on back, supine position, legs spread, facing viewer, from above angle",
        "sitting_spread": "sitting, legs spread wide apart, facing viewer, open position",
        "kneeling_away": "kneeling, on knees, from behind, rear view, facing away from viewer",
        "squatting": "squatting position, legs spread wide, low stance, facing viewer",
        "leaning_forward": "leaning forward, bent at waist, hands on surface, rear prominent, from behind"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"default": "beautiful woman", "multiline": True}),
                "pose": (list(cls.POSES.keys()),),
                "add_details": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("posed_prompt",)
    FUNCTION = "direct"
    CATEGORY = "Mason's Nodes/NSFW"

    def direct(self, base_prompt, pose, add_details):
        pose_desc = self.POSES.get(pose, "")
        
        if add_details:
            extras = "detailed anatomy, realistic proportions, natural pose, proper perspective"
            return (f"{base_prompt}, {pose_desc}, {extras}",)
        
        return (f"{base_prompt}, {pose_desc}",)


class CameraAngle:
    """Controls camera angle and perspective"""
    
    ANGLES = {
        "from_behind": "from behind, rear view, back view, behind the subject",
        "from_below": "from below, low angle, looking up, worms eye view",
        "from_above": "from above, high angle, looking down, birds eye view",
        "side_view": "side view, profile, from the side, lateral view",
        "front_view": "front view, facing viewer, head on, direct view",
        "three_quarter_behind": "three quarter view from behind, slight angle, mostly rear view",
        "pov": "pov, point of view, first person perspective, viewer perspective"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "angle": (list(cls.ANGLES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("angled_prompt",)
    FUNCTION = "set_angle"
    CATEGORY = "Mason's Nodes/NSFW"

    def set_angle(self, prompt, angle):
        angle_desc = self.ANGLES.get(angle, "")
        return (f"{prompt}, {angle_desc}",)


class BodyPosition:
    """Fine-tune body part positions"""
    
    LEG_DESC = {
        "spread_wide": "legs spread wide apart, wide stance",
        "together": "legs together, closed stance",
        "one_raised": "one leg raised, leg lifted",
        "apart": "legs apart, open stance",
        "open": "legs open, spread position"
    }
    
    ARM_DESC = {
        "at_sides": "arms at sides, relaxed arms",
        "raised": "arms raised, arms up",
        "behind_back": "arms behind back, hands behind",
        "reaching_forward": "arms reaching forward, hands forward",
        "on_hips": "hands on hips, arms akimbo"
    }
    
    BACK_DESC = {
        "arched": "arched back, curved spine, back arched inward",
        "straight": "straight back, upright posture",
        "curved": "curved back, rounded spine",
        "natural": "natural posture, relaxed back"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "legs": (list(cls.LEG_DESC.keys()),),
                "arms": (list(cls.ARM_DESC.keys()),),
                "back": (list(cls.BACK_DESC.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("positioned_prompt",)
    FUNCTION = "position"
    CATEGORY = "Mason's Nodes/NSFW"

    def position(self, prompt, legs, arms, back):
        parts = [prompt]
        parts.append(self.LEG_DESC.get(legs, ""))
        parts.append(self.ARM_DESC.get(arms, ""))
        parts.append(self.BACK_DESC.get(back, ""))
        return (", ".join([p for p in parts if p]),)


NODE_CLASS_MAPPINGS = {
    "PoseDirector": PoseDirector,
    "CameraAngle": CameraAngle,
    "BodyPosition": BodyPosition,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PoseDirector": "Pose Director",
    "CameraAngle": "Camera Angle",
    "BodyPosition": "Body Position",
}
