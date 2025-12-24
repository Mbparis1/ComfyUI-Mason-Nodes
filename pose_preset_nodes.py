"""
Mason's Pose Preset Nodes for ComfyUI
Instant configuration for Pose Architect - huge library of predefined poses
"""

class PosePresetLoader:
    """Library of 50+ pre-configured poses for Pose Architect"""
    
    # Format: "Preset Name": (UpperBody, LowerBody, HeadNeck, HandPose)
    # Using values corresponding to the inputs in pose_architect_nodes.py
    PRESETS = {
        # --- Standing / Basic ---
        "Standing_Neutral": ("arms_down", "standing_straight", "looking_straight", "relaxed"),
        "Standing_CrossedArms": ("arms_crossed", "standing_straight", "looking_straight", "relaxed"),
        "Standing_HandsOnHips": ("hands_on_hips", "standing_wide", "head_tilt_left", "relaxed"),
        "T_Pose": ("t_pose_arms", "standing_straight", "looking_straight", "open_palm"),
        "A_Pose": ("arms_45_degrees", "standing_wide", "looking_straight", "relaxed"),
        
        # --- Sitting ---
        "Sitting_Chair": ("hands_in_lap", "sitting_chair", "looking_straight", "relaxed"),
        "Sitting_Floor_Crosslegged": ("hands_on_knees", "sitting_lotus", "looking_down", "relaxed"),
        "Sitting_W_Pose": ("hands_between_legs", "sitting_w_style", "looking_up", "relaxed"),
        "Squatting_Deep": ("hands_on_knees", "squatting_deep", "looking_straight", "relaxed"),
        
        # --- Kneeling / Crawling ---
        "Kneeling_Upright": ("hands_behind_back", "kneeling_upright", "looking_straight", "bound_wrists"),
        "All_Fours_Crawling": ("arms_reaching", "all_fours", "looking_forward", "open_palm"),
        "Doggystyle_Arch": ("arms_supporting", "all_fours", "looking_back", "gripping"),
        "Head_Down_Ass_Up": ("arms_down_head", "kneeling_bent_over", "face_pressed_down", "relaxed"),
        
        # --- Lying Down ---
        "Lying_Back_Spread": ("arms_above_head", "legs_spread_wide", "looking_up", "gripping_sheets"),
        "Lying_Stomach": ("arms_under_chin", "legs_straight", "looking_at_camera", "relaxed"),
        "Side_Lying": ("arm_under_head", "legs_curled", "looking_forward", "relaxed"),
        "Missionary_Receiver": ("wrapping_legs", "legs_spread_raised", "head_back", "gripping_shoulders"),
        
        # --- Action / Dynamic ---
        "Running": ("arms_pumping", "running_stride", "looking_forward", "fist"),
        "Jumping": ("arms_up_cheer", "jumping_tuck", "looking_up", "open_palm"),
        "Fighting_Stance": ("guard_up", "wide_stance", "looking_forward", "fist"),
        "Kicking": ("guard_up", "high_kick", "looking_forward", "fist"),
        
        # --- NSFW Specific ---
        "Cowgirl_Riding": ("hands_on_partner_chest", "straddling_squat", "looking_down_partner", "open_palm"),
        "Reverse_Cowgirl": ("hands_reaching_back", "straddling_squat", "looking_back", "open_palm"),
        "Mating_Press": ("arms_above_head", "legs_pressed_chest", "looking_up_ahegao", "gripping"),
        "Standing_Carry": ("wrapping_arms_neck", "legs_wrapped_waist", "looking_partner", "hugging"),
        "Spitroast_Middle": ("hands_holding_head", "all_fours", "mouth_open", "relaxed"),
        "Anal_Presentation": ("pulling_cheeks", "bent_over_standing", "looking_back", "pulling"),
        "Double_Peace_V": ("double_peace_sign", "kneeling_upright", "tongue_out", "peace_sign"),
        "Jack_O_Pose": ("arms_supporting", "legs_wide_bent", "looking_down_between_legs", "relaxed"),
        
        # --- Pinup / Model ---
        "Pinup_Bent_Over": ("hands_on_knees", "bent_over_standing", "looking_back_shoulder", "relaxed"),
        "Model_Turn": ("hand_on_hip", "crossed_legs_standing", "looking_back_shoulder", "relaxed"),
        "Selfie_High_Angle": ("holding_phone_high", "standing_straight", "looking_up_camera", "holding_object"),
        "Mirror_Selfie": ("holding_phone_mirror", "leaning_hip", "looking_mirror", "holding_object"),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PRESETS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("upper_body", "lower_body", "head_neck", "hand_pose")
    FUNCTION = "load_preset"
    CATEGORY = "Mason's Nodes/Automation"

    def load_preset(self, preset):
        return self.PRESETS.get(preset, ("arms_down", "standing_straight", "looking_straight", "relaxed"))


class PresetMixer:
    """Mixes two presets together. Note: This creates compound prompts like 'arms_down AND arms_up' which may require SD interpretation"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset_A": (list(PosePresetLoader.PRESETS.keys()),),
                "preset_B": (list(PosePresetLoader.PRESETS.keys()),),
                "mix_method": (["strict_blend", "append"],), # blend = (A:0.5), (B:0.5)
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("upper_body", "lower_body", "head_neck", "hand_pose")
    FUNCTION = "mix"
    CATEGORY = "Mason's Nodes/Automation"

    def mix(self, preset_A, preset_B, mix_method):
        pA = PosePresetLoader.PRESETS.get(preset_A)
        pB = PosePresetLoader.PRESETS.get(preset_B)
        
        results = []
        for i in range(4): # For each component
            if pA[i] == pB[i]:
                results.append(pA[i])
            else:
                if mix_method == "strict_blend":
                    results.append(f"({pA[i]}:0.5), ({pB[i]}:0.5)")
                else:
                    results.append(f"{pA[i]}, {pB[i]}")
                    
        return tuple(results)


NODE_CLASS_MAPPINGS = {
    "PosePresetLoader": PosePresetLoader,
    "PresetMixer": PresetMixer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PosePresetLoader": "🧘 Pose Preset Loader",
    "PresetMixer": "🔀 Preset Mixer",
}
