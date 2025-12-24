"""
Mason's AI Aesthetic Director Nodes
Translating moods and vibes into prompt logic - SD 1.5 optimized
"""

class AestheticMoodDirector:
    """Translates high-level moods into complex lighting and atmosphere prompts"""
    
    MOODS = {
        "classic_noir": "classic film noir style, dramatic shadows, harsh lighting, high contrast, cinematic atmosphere, 1940s aesthetic",
        "cyberpunk_neon": "cyberpunk aesthetic, vibrant neon lighting, pink and blue color palette, rain-slicked surfaces, futuristic atmosphere",
        "golden_hour_glamour": "golden hour lighting, warm sunlight, soft glow, romantic atmosphere, sunset tones, beautiful lens flare",
        "moody_boudoir": "moody boudoir lighting, soft shadows, intimate atmosphere, low key lighting, warm candlelight, sensual",
        "vibrant_fashion": "vibrant fashion photography, bright colors, saturated tones, high fashion lighting, clean and sharp",
        "ethereal_dream": "ethereal dream-like quality, soft focus, morning mist, hazy atmosphere, pastel colors, soft diffused light",
        "gritty_realism": "gritty realism, raw texture, natural lighting, candid atmosphere, unpolished, realistic film grain",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "mood": (list(cls.MOODS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("mood_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Aesthetics"

    def apply(self, prompt, mood):
        m = self.MOODS.get(mood, "")
        return (f"{prompt}, {m}",)

class CinematicColorGrader:
    """Applies specific color grading styles to the prompt"""
    
    STYLES = {
        "teal_and_orange": "teal and orange color grade, cinematic color palette, professional movie look",
        "vintage_sepia": "vintage sepia tones, warm nostalgic colors, old photograph aesthetic",
        "monochrome_master": "masterful monochrome, black and white photography, rich greyscale, high contrast",
        "pastel_soft": "soft pastel color palette, gentle tones, airy and light aesthetic",
        "earthy_natural": "earthy natural tones, muted colors, organic palette, realistic lighting",
        "high_key_white": "high key lighting, bright and airy, white dominant palette, clean aesthetic",
        "low_key_dark": "low key lighting, dark and moody, deep shadows, dramatic atmosphere",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "grading": (list(cls.STYLES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("graded_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Aesthetics"

    def apply(self, prompt, grading):
        g = self.STYLES.get(grading, "")
        return (f"{prompt}, {g}",)

NODE_CLASS_MAPPINGS = {
    "AestheticMoodDirector": AestheticMoodDirector,
    "CinematicColorGrader": CinematicColorGrader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AestheticMoodDirector": "🎭 Aesthetic Mood Director",
    "CinematicColorGrader": "🎨 Cinematic Color Grader",
}
