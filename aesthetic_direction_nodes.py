"""
Mason's Aesthetic Direction Nodes for ComfyUI
Advanced control over cinematography, lighting, color grading, and composition.
"""

class CinematographerPro:
    """Advanced Camera, Lens, and Film Stock Control"""
    
    CAMERAS = {
        "digital_cinema": "Arri Alexa, Red DSMC2, digital cinema quality, pristine sensor",
        "film_classic": "35mm film, film grain, analog aesthetic, Kodak Portra 400",
        "imax": "IMAX format, 70mm film, extreme resolution, epic scale",
        "vintage": "8mm vintage film, Super 8, nostalgic look, light leaks",
        "dslr": "high-end DSLR, Canon R5, Sony A7RIV, sharp digital photo",
        "smartphone": "iPhone photography, computational photography aesthetic",
    }
    
    LENSES = {
        "wide_angle": "16mm wide angle lens, expansive view, slight distortion",
        "standard": "35mm prime lens, street photography look, natural field of view",
        "portrait": "85mm portrait lens, flattering perspective, compression",
        "telephoto": "200mm telephoto lens, background compression, distant subject",
        "macro": "100mm macro lens, extreme close-up, microscopic detail",
        "fisheye": "fisheye lens, extreme distortion, circular field of view",
    }
    
    APERTURE = {
        "f1.2_creamy": "f/1.2 aperture, razor thin depth of field, creamy bokeh, dreamy background",
        "f1.8_portrait": "f/1.8 aperture, shallow depth of field, blurred background, subject separation",
        "f2.8_standard": "f/2.8 aperture, natural bokeh, balanced depth of field",
        "f8_sharp": "f/8 aperture, deep depth of field, sharp background, everything in focus",
        "f16_landscape": "f/16 aperture, hyperfocal distance, maximum sharpness throughout",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "camera": (list(cls.CAMERAS.keys()),),
                "lens": (list(cls.LENSES.keys()),),
                "aperture": (list(cls.APERTURE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Aesthetic Direction"

    def generate(self, prompt, camera, lens, aperture):
        cam = self.CAMERAS.get(camera, "")
        len_val = self.LENSES.get(lens, "")
        apt = self.APERTURE.get(aperture, "")
        
        positive = f"{prompt}, {cam}, {len_val}, {apt}"
        negative = "bad camera, low quality image, blurry, out of focus"
        
        return (positive, negative)


class LightingDirectorPro:
    """Professional Studio and Natural Lighting Control"""
    
    SETUP = {
        "rembrandt": "Rembrandt lighting, chiaroscuro, triangle rule, dramatic portrait lighting",
        "butterfly": "butterfly lighting, paramount lighting, glamour lighting, shadow under nose",
        "split": "split lighting, distinct light and dark sides, dramatic contrast",
        "rim_light": "rim light, backlighting, halo effect, edge lighting, subject separation",
        "three_point": "three-point lighting system, key light, fill light, back light, studio standard",
        "softbox": "large softbox, diffused light, soft shadows, wrap-around light",
    }
    
    ENVIRONMENT = {
        "golden_hour": "golden hour, warm sunlight, long shadows, magic hour, sunset glow",
        "blue_hour": "blue hour, twilight, cool tones, before sunrise, cinematic blue",
        "midday": "harsh midday sun, high contrast, hard shadows, bright daylight",
        "overcast": "overcast sky, giant softbox, diffused daylight, even lighting",
        "moonlight": "moonlight, night scene, cool blue tones, darkness, low key",
        "neon_city": "neon signs, cyberpunk lighting, colorful light sources, city glow",
    }
    
    ATMOSPHERE = {
        "clear": "clear air, sharp visibility, no haze",
        "volumetric_fog": "volumetric fog, god rays, light shafts, misty atmosphere",
        "haze": "atmospheric haze, depth cues, aerial perspective",
        "dusty": "dust particles, floating dust, textured air, dirty atmosphere",
        "smoke": "smoke haze, cinematic atmosphere, mysterious fog",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "setup": (list(cls.SETUP.keys()),),
                "environment": (list(cls.ENVIRONMENT.keys()),),
                "atmosphere": (list(cls.ATMOSPHERE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Aesthetic Direction"

    def generate(self, prompt, setup, environment, atmosphere):
        s = self.SETUP.get(setup, "")
        e = self.ENVIRONMENT.get(environment, "")
        a = self.ATMOSPHERE.get(atmosphere, "")
        
        positive = f"{prompt}, {s}, {e}, {a}"
        negative = "flat lighting, boring lighting, washed out, overexposed, underexposed"
        
        return (positive, negative)


class ColorGradingMaster:
    """Cinema Quality Color Grading"""
    
    LOOK = {
        "teal_orange": "teal and orange color grading, hollywood blockbuster look, complementary colors",
        "matrix_green": "matrix green tint, sickly green atmosphere, sci-fi dystopia",
        "bleach_bypass": "bleach bypass, high contrast, desaturated, silver retention, gritty war movie",
        "technicolor": "Technicolor, vibrant red, saturated primary colors, vintage color film",
        "noir_bw": "film noir, black and white, high contrast, dramatic shadows, silver gelatin",
        "pastel_dream": "pastel color grading, soft pinks and blues, wes anderson style, dreamy",
        "vintage_polaroid": "vintage polaroid, faded blacks, color shift, instant film look",
        "cyberpunk": "cyberpunk color palette, neon pink and blue, deep blacks, high saturation",
    }
    
    MOOD = {
        "neutral": "neutral color balance, accurate colors",
        "warm": "warm color temperature, cozy, nostalgic, inviting",
        "cool": "cool color temperature, detached, clinical, melancholic",
        "vibrant": "high saturation, vibrant colors, energetic, lively",
        "muted": "muted tone, desaturated, somber, serious",
        "dark": "dark mood, low key, ominous, mysterious",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "look": (list(cls.LOOK.keys()),),
                "mood": (list(cls.MOOD.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("positive_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Aesthetic Direction"

    def apply(self, prompt, look, mood):
        l = self.LOOK.get(look, "")
        m = self.MOOD.get(mood, "")
        return (f"{prompt}, {l}, {m}",)


class CompositionMaster:
    """Advanced Framing and Composition Rules"""
    
    FRAMING = {
        "wide_shot": "wide shot, establishing shot, environment focus",
        "medium_shot": "medium shot, waist up, standard portrait",
        "close_up": "close up, face focus, emotional impact",
        "extreme_close_up": "extreme close up, detail focus, macro view",
        "full_body": "full body shot, head to toe, showing outfit",
        "cowboy_shot": "cowboy shot, knees up, american shot",
    }
    
    ANGLE = {
        "eye_level": "eye level shot, neutral angle",
        "low_angle": "low angle shot, looking up at subject, heroic, dominant",
        "high_angle": "high angle shot, looking down at subject, vulnerable, submissive",
        "birds_eye": "bird's eye view, top down, god's eye view, overhead shot",
        "dutch_angle": "dutch angle, tilted camera, dynamic tension, unease",
        "over_shoulder": "over the shoulder shot, conversational angle, subjective view",
    }
    
    RULE = {
        "rule_of_thirds": "rule of thirds, off-center composition, balanced",
        "center_frame": "center frame, symmetrical composition, wes anderson style",
        "golden_ratio": "golden ratio composition, perfect proportions, fibonacci spiral",
        "leading_lines": "leading lines, vanishing point, depth perspective",
        "negative_space": "heavy negative space, isolated subject, minimalist composition",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "framing": (list(cls.FRAMING.keys()),),
                "angle": (list(cls.ANGLE.keys()),),
                "rule": (list(cls.RULE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Aesthetic Direction"

    def generate(self, prompt, framing, angle, rule):
        f = self.FRAMING.get(framing, "")
        a = self.ANGLE.get(angle, "")
        r = self.RULE.get(rule, "")
        
        positive = f"{prompt}, {f}, {a}, {r}"
        negative = "bad composition, bad framing, cut off head, awkward framing"
        
        return (positive, negative)


NODE_CLASS_MAPPINGS = {
    "CinematographerPro": CinematographerPro,
    "LightingDirectorPro": LightingDirectorPro,
    "ColorGradingMaster": ColorGradingMaster,
    "CompositionMaster": CompositionMaster,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CinematographerPro": "🎥 Cinematographer Pro",
    "LightingDirectorPro": "💡 Lighting Director Pro",
    "ColorGradingMaster": "🎨 Color Grading Master",
    "CompositionMaster": "📐 Composition Master",
}
