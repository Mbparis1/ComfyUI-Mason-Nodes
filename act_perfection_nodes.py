class ActPerfectionMaster:
    """
    Phase 11: Act Perfection Masters
    Specialized nodes for hyper-accurate and detailed generation of specific acts.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "act_type": (["Deep Throat", "Groping", "Anilingus", "Cunnilingus", "Paizuri"],),
                "intensity": (["Soft", "Passionate", "Hardcore", "Extreme"],),
                "camera_angle": (["POV", "Side View", "Top Down", "Close Up", "X-Ray"],),
                "anatomical_detail": (["Standard", "High Detail", "Anatomically Perfect"],),
            },
             "optional": {
                "subject_1": ("STRING", {"default": "woman", "multiline": False}),
                "subject_2": ("STRING", {"default": "man", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("act_prompt",)
    FUNCTION = "generate_act"
    CATEGORY = "Mason's Nodes/NSFW Acts"

    def generate_act(self, act_type, intensity, camera_angle, anatomical_detail, subject_1="woman", subject_2="man"):
        
        details = []
        
        # Base Act Definitions
        if act_type == "Deep Throat":
            base = f"fellatio, {subject_1} sucking {subject_2} penis, deep throat, gagging, choking, saliva strands, eyes rolling back, cheeks sucked in"
        elif act_type == "Groping":
             base = f"{subject_2} groping {subject_1}, hands on breasts, squeezing, fingers pressing into skin, skin indentation"
        elif act_type == "Anilingus":
             base = f"anilingus, {subject_2} licking {subject_1} anus, spread cheeks, tongue exposure"
        elif act_type == "Cunnilingus":
             base = f"cunnilingus, {subject_2} licking {subject_1} pussy, tongue inside, spread legs"
        elif act_type == "Paizuri":
             base = f"paizuri, titfuck, {subject_1} squeezing penis between breasts, nipples touching penis"
        else:
            base = f"{act_type}"

        details.append(base)

        # Intensity Modifiers
        if intensity == "Hardcore":
            details.append("sweaty skin, rough interaction, heavy breathing")
        elif intensity == "Extreme":
            details.append("extreme stretching, excessive fluids, messy face")

        # Camera
        details.append(f"view from {camera_angle}")

        # Anatomy
        if anatomical_detail == "Anatomically Perfect":
            details.append("highly detailed genitalia, detailed veins, perfect anatomy, 8k textures")

        return (", ".join(details),)

NODE_CLASS_MAPPINGS = {
    "ActPerfectionMaster": ActPerfectionMaster
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ActPerfectionMaster": "🔞 Act Perfection Master"
}
