"""
Mason's Pose Architect Nodes for ComfyUI
Virtual "Stick Figure" control via text rig sliders - SD 1.5 optimized
"""

class UpperBodyRig:
    """Controls arms, shoulders, and torso rotation"""
    
    ARMS = {
        "down_sides": "arms down by sides, relaxed arms",
        "crossed_chest": "arms crossed over chest, confident pose",
        "hands_on_hips": "hands on hips, akimbo",
        "reaching_up": "arms reaching up, hands in air, stretching",
        "reaching_forward": "reaching forward, hands reaching out",
        "behind_head": "hands behind head, elbows out",
        "hugging_self": "hugging self, arms around body",
        "t_pose": "T-pose, arms spread wide",
    }
    
    SHOULDERS = {
        "relaxed": "relaxed shoulders",
        "hunched": "hunched shoulders, tense",
        "angled": "one shoulder higher, angled shoulders",
        "shrugged": "shrugging shoulders",
    }
    
    TORSO = {
        "facing_viewer": "torso facing viewer, front view",
        "turned_side": "torso turned to side, side profile",
        "turned_away": "back turned to viewer, back view",
        "arching": "arching back, chest out",
        "twisting": "twisting torso, dynamic pose",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "arms": (list(cls.ARMS.keys()),),
                "shoulders": (list(cls.SHOULDERS.keys()),),
                "torso": (list(cls.TORSO.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Pose Architect"

    def generate(self, arms, shoulders, torso):
        a = self.ARMS.get(arms, "")
        s = self.SHOULDERS.get(shoulders, "")
        t = self.TORSO.get(torso, "")
        return (f"{a}, {s}, {t}",)


class LowerBodyRig:
    """Controls legs, hips, and sitting/standing state"""
    
    LEGS = {
        "standing_straight": "standing straight, legs together",
        "legs_spread": "legs spread wide, open legs, spread eagle",
        "kneeling": "kneeling on ground, on knees",
        "sitting_chair": "sitting on chair, legs bent",
        "sitting_floor": "sitting on floor, legs crossed",
        "squatting": "squatting, slav squat, deep squat",
        "leg_lifted": "one leg lifted, standing on one leg",
        "kicking": "high kick, leg up",
        "lying_back": "lying on back, legs up",
    }
    
    HIPS = {
        "square": "hips square to camera",
        "popped": "one hip popped, weight on one leg",
        "thrusting": "hips thrusting forward",
        "tilted_back": "hips tilted back, presenting",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "legs": (list(cls.LEGS.keys()),),
                "hips": (list(cls.HIPS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Pose Architect"

    def generate(self, legs, hips):
        l = self.LEGS.get(legs, "")
        h = self.HIPS.get(hips, "")
        return (f"{l}, {h}",)


class HeadNeckRig:
    """Controls head direction and tilt"""
    
    LOOK = {
        "at_viewer": "looking at viewer, eye contact",
        "looking_up": "looking up, chin up",
        "looking_down": "looking down, chin tucked",
        "looking_away": "looking away, profile face",
        "looking_back": "looking back over shoulder",
        "eyes_closed": "eyes closed",
    }
    
    TILT = {
        "straight": "head straight",
        "tilted_left": "head tilted left, cute tilt",
        "tilted_right": "head tilted right, inquiring tilt",
        "thrown_back": "head thrown back, exposing neck",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "looking": (list(cls.LOOK.keys()),),
                "tilt": (list(cls.TILT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Pose Architect"

    def generate(self, looking, tilt):
        l = self.LOOK.get(looking, "")
        t = self.TILT.get(tilt, "")
        return (f"{l}, {t}",)


class HandPoseRig:
    """Detailed hand and finger pose control"""
    
    POSE = {
        "relaxed": "relaxed hands, open palms",
        "fist": "clenched fists, punching",
        "peace_sign": "peace sign, v sign, two fingers",
        "grasping": "grasping, holding object, claw hand",
        "pointing": "pointing finger, index finger",
        "shushing": "shushing gesture, finger on lips",
        "thumbs_up": "thumbs up, approving",
        "heart_shape": "heart hands, making heart shape",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "left_hand": (list(cls.POSE.keys()),),
                "right_hand": (list(cls.POSE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Pose Architect"

    def generate(self, left_hand, right_hand):
        l = self.POSE.get(left_hand, "")
        r = self.POSE.get(right_hand, "")
        return (f"left hand {l}, right hand {r}",)


class DynamicInteractionRig:
    """Poses involving interactions with others or environment"""
    
    ACTION = {
        "pulling_hair": "hand pulling hair, head pulled back",
        "choking": "hand on throat, choking, neck grasp",
        "pinning_wrists": "pinning wrists, wrists held down",
        "lifting_leg": "lifting partner's leg, leg on shoulder",
        "spanking_motion": "hand raised for spanking, striking motion",
        "carrying": "carrying partner, princess carry",
        "pushing_against_wall": "pushing against wall, pinned to wall",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "interaction": (list(cls.ACTION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Pose Architect"

    def generate(self, interaction):
        return (self.ACTION.get(interaction, ""),)


class PoseStringAssembler:
    """Combines all rig parts into a master pose instruction"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "head_rig": ("STRING", {"forceInput": True}),
                "upper_body": ("STRING", {"forceInput": True}),
                "lower_body": ("STRING", {"forceInput": True}),
            },
            "optional": {
                "hands": ("STRING", {"forceInput": True}),
                "interaction": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("full_pose_prompt",)
    FUNCTION = "assemble"
    CATEGORY = "Mason's Nodes/Pose Architect"

    def assemble(self, head_rig, upper_body, lower_body, hands="", interaction=""):
        parts = [head_rig, upper_body, lower_body]
        if hands: parts.append(hands)
        if interaction: parts.append(interaction)
        
        return (", ".join(parts),)


NODE_CLASS_MAPPINGS = {
    "UpperBodyRig": UpperBodyRig,
    "LowerBodyRig": LowerBodyRig,
    "HeadNeckRig": HeadNeckRig,
    "HandPoseRig": HandPoseRig,
    "DynamicInteractionRig": DynamicInteractionRig,
    "PoseStringAssembler": PoseStringAssembler,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UpperBodyRig": "🦴 Upper Body Rig",
    "LowerBodyRig": "🦴 Lower Body Rig",
    "HeadNeckRig": "🦴 Head/Neck Rig",
    "HandPoseRig": "✋ Hand Pose Rig",
    "DynamicInteractionRig": "🤼 Dynamic Interaction Rig",
    "PoseStringAssembler": "🦴 Pose String Assembler",
}
