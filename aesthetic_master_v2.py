class AestheticMasterV2:
    """
    The Ultimate Aesthetic Director for ComfyUI.
    Provides curated presets for Lighting, Atmosphere, Camera, and Composition.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "lighting": (["None", "Cinematic", "Volumetric", "Studio Softbox", "Neon Noir", "Golden Hour", "Rembrandt", "God Rays", "Bioluminescent"],),
                "atmosphere": (["None", "Foggy", "Dusty", "Clear", "Rainy", "Cyberpunk Haze", "Ethereal Glow", "Dark & Gritty"],),
                "camera": (["None", "Leica M6", "Sony A7RIV", "Canon 5D", "85mm Portrait", "35mm Street", "Macro 100mm", "Wide Angle 24mm"],),
                "composition": (["None", "Rule of Thirds", "Center Focus", "Symmetrical", "Low Angle", "High Angle", "Dutch Angle", "Bokeh Background"],),
                "grading": (["None", "Kodak Portra 400", "Fujifilm Velvia", "Bleach Bypass", "Technicolor", "Black & White High Contrast"],),
            },
            "optional": {
                "optional_prompt": ("STRING", {"multiline": True, "forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("aesthetic_prompt",)
    FUNCTION = "compose_aesthetics"
    CATEGORY = "Mason's Nodes/Aesthetics"

    def compose_aesthetics(self, lighting, atmosphere, camera, composition, grading, optional_prompt=""):
        parts = []
        
        # Helper to add valid parts
        def add_part(label, value):
            if value != "None":
                if label == "lighting":
                    parts.append(f"{value} lighting")
                elif label == "camera":
                    parts.append(f"shot on {value}")
                elif label == "grading":
                    parts.append(f"color graded {value}")
                else:
                    parts.append(value)

        add_part("lighting", lighting)
        add_part("atmosphere", atmosphere)
        add_part("camera", camera)
        add_part("composition", composition)
        add_part("grading", grading)

        aesthetic_string = ", ".join(parts)
        
        if optional_prompt:
            if aesthetic_string:
                return (f"{optional_prompt}, {aesthetic_string}",)
            return (optional_prompt,)
        
        return (aesthetic_string,)

NODE_CLASS_MAPPINGS = {
    "AestheticMasterV2": AestheticMasterV2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AestheticMasterV2": "🎨 Aesthetic Master V2"
}
