"""
Mason's Advanced Control Nodes for ComfyUI
Multi-person, ethnicity mixing, weather, camera angles, templates
SD 1.5 optimized
"""


class MultiPersonSceneBuilder:
    """Build scenes with multiple people"""
    
    PERSON_COUNT = {
        "two": "two people, couple, pair",
        "three": "three people, trio, threesome",
        "four": "four people, group of four",
        "group": "group of people, several people, crowd",
    }
    
    ARRANGEMENT = {
        "side_by_side": "standing side by side, next to each other",
        "facing": "facing each other, looking at each other",
        "one_behind": "one person behind the other, staggered",
        "embracing": "embracing, holding each other, close together",
        "scattered": "scattered arrangement, natural grouping",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "person_count": (list(cls.PERSON_COUNT.keys()),),
                "arrangement": (list(cls.ARRANGEMENT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Advanced Control"

    def build(self, prompt, person_count, arrangement):
        pc = self.PERSON_COUNT.get(person_count, "")
        arr = self.ARRANGEMENT.get(arrangement, "")
        return (f"{prompt}, {pc}, {arr}",)


class EthnicityMixer:
    """Create unique mixed ethnicity appearances"""
    
    ETHNICITIES = {
        "european": "european features, caucasian",
        "east_asian": "east asian features, asian",
        "south_asian": "south asian features, indian subcontinent",
        "african": "african features, black, dark skin",
        "latin": "latin features, hispanic",
        "middle_eastern": "middle eastern features, arab",
        "pacific_islander": "pacific islander features, polynesian",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "primary_ethnicity": (list(cls.ETHNICITIES.keys()),),
                "secondary_ethnicity": (["none"] + list(cls.ETHNICITIES.keys()),),
                "mix_ratio": (["primary_dominant", "balanced", "secondary_dominant"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ethnicity_prompt",)
    FUNCTION = "mix"
    CATEGORY = "Mason's Nodes/Advanced Control"

    def mix(self, prompt, primary_ethnicity, secondary_ethnicity, mix_ratio):
        primary = self.ETHNICITIES.get(primary_ethnicity, "")
        
        if secondary_ethnicity == "none":
            return (f"{prompt}, {primary}",)
        
        secondary = self.ETHNICITIES.get(secondary_ethnicity, "")
        
        if mix_ratio == "primary_dominant":
            return (f"{prompt}, {primary}, hint of {secondary}, mixed ethnicity",)
        elif mix_ratio == "balanced":
            return (f"{prompt}, mixed {primary} and {secondary}, mixed race, unique features",)
        else:  # secondary_dominant
            return (f"{prompt}, {secondary}, hint of {primary}, mixed ethnicity",)


class WeatherEffectsController:
    """Add weather effects to the scene"""
    
    WEATHER = {
        "none": "",
        "rain_light": "light rain, drizzle, rain drops, wet conditions",
        "rain_heavy": "heavy rain, pouring rain, rain soaked, drenched",
        "snow": "snow falling, snowflakes, winter snow, snowy",
        "fog": "fog, misty, hazy atmosphere, foggy conditions",
        "wind": "windy, hair blowing, clothes moving, wind effect",
        "sunny": "bright sun, sunny day, sunlight, clear sky",
        "overcast": "overcast sky, cloudy, diffused light, gray sky",
        "storm": "stormy weather, dramatic clouds, threatening sky",
    }
    
    SUBJECT_EFFECT = {
        "dry": "",
        "slightly_wet": "slightly wet, damp, moisture on skin",
        "wet": "wet, water on skin, wet hair, dripping",
        "wind_affected": "wind-blown hair, clothes moving, windswept",
        "cold": "cold, visible breath, pink cheeks from cold",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "weather": (list(cls.WEATHER.keys()),),
                "subject_effect": (list(cls.SUBJECT_EFFECT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weather_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Advanced Control"

    def apply(self, prompt, weather, subject_effect):
        w = self.WEATHER.get(weather, "")
        s = self.SUBJECT_EFFECT.get(subject_effect, "")
        parts = [prompt]
        if w: parts.append(w)
        if s: parts.append(s)
        return (", ".join(parts),)


class CameraAngleController:
    """Specific camera angles and perspectives"""
    
    ANGLES = {
        "eye_level": "eye level shot, straight on, neutral angle",
        "low_angle": "low angle shot, looking up, heroic angle, from below",
        "high_angle": "high angle shot, looking down, from above",
        "birds_eye": "birds eye view, top down, overhead shot",
        "worms_eye": "worms eye view, extreme low angle, ground level",
        "dutch_angle": "dutch angle, tilted camera, canted angle, dynamic tilt",
        "pov": "pov shot, point of view, first person perspective",
        "over_shoulder": "over the shoulder shot, behind subject",
    }
    
    DISTANCE = {
        "extreme_close": "extreme close-up, ECU, macro, very tight",
        "close_up": "close-up shot, face fills frame, tight shot",
        "medium_close": "medium close-up, head and shoulders",
        "medium": "medium shot, waist up, mid shot",
        "medium_long": "medium long shot, knees up, american shot",
        "full_body": "full body shot, entire body visible, long shot",
        "wide": "wide shot, full figure with environment, establishing",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "angle": (list(cls.ANGLES.keys()),),
                "distance": (list(cls.DISTANCE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("camera_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Advanced Control"

    def apply(self, prompt, angle, distance):
        a = self.ANGLES.get(angle, "")
        d = self.DISTANCE.get(distance, "")
        return (f"{prompt}, {a}, {d}",)


class PromptTemplateStarter:
    """Pre-built prompt templates to start with"""
    
    TEMPLATES = {
        "portrait_beauty": (
            "beautiful woman, portrait photography, professional headshot, "
            "studio lighting, sharp focus, detailed face, high quality"
        ),
        "full_body_glamour": (
            "beautiful woman, full body shot, glamour photography, "
            "professional lighting, elegant pose, high quality, detailed"
        ),
        "boudoir_intimate": (
            "beautiful woman, boudoir photography, intimate setting, "
            "soft lighting, sensual pose, bedroom, romantic atmosphere"
        ),
        "beach_swimwear": (
            "beautiful woman, beach photography, swimwear, bikini, "
            "tropical setting, sunny, golden tan, summer vibes"
        ),
        "fashion_editorial": (
            "fashion model, editorial photography, high fashion, "
            "designer clothing, dramatic lighting, vogue style, magazine quality"
        ),
        "artistic_nude": (
            "artistic nude, fine art photography, tasteful, "
            "museum quality, classical pose, artistic lighting"
        ),
        "fitness_athletic": (
            "fit woman, athletic body, fitness photography, "
            "activewear, gym setting or outdoors, healthy, toned"
        ),
        "casual_lifestyle": (
            "beautiful woman, casual lifestyle photography, "
            "everyday setting, natural pose, relaxed, authentic"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template": (list(cls.TEMPLATES.keys()),),
                "additional_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("starter_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Advanced Control"

    def generate(self, template, additional_prompt):
        t = self.TEMPLATES.get(template, "")
        if additional_prompt:
            return (f"{t}, {additional_prompt}",)
        return (t,)


class ComprehensiveNegativeBuilder:
    """Build comprehensive negative prompts for best results"""
    
    CATEGORIES = {
        "anatomy": (
            "bad anatomy, wrong anatomy, deformed body, mutated, "
            "extra limbs, missing limbs, floating limbs, disconnected limbs"
        ),
        "face": (
            "deformed face, ugly face, bad face, asymmetric face, "
            "bad eyes, crossed eyes, deformed eyes"
        ),
        "hands": (
            "bad hands, deformed hands, extra fingers, missing fingers, "
            "fused fingers, too many fingers, wrong finger count"
        ),
        "quality": (
            "low quality, worst quality, jpeg artifacts, blurry, "
            "pixelated, noisy, grainy"
        ),
        "style": (
            "cartoon, anime, illustration, painting, drawing, sketch, "
            "3d render, cgi, fake"
        ),
        "artifacts": (
            "watermark, signature, text, logo, banner, username, "
            "border, frame"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "existing_negative": ("STRING", {"default": "", "multiline": True}),
                "include_anatomy": ("BOOLEAN", {"default": True}),
                "include_face": ("BOOLEAN", {"default": True}),
                "include_hands": ("BOOLEAN", {"default": True}),
                "include_quality": ("BOOLEAN", {"default": True}),
                "include_style": ("BOOLEAN", {"default": False}),
                "include_artifacts": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("comprehensive_negative",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Advanced Control"

    def build(self, existing_negative, include_anatomy, include_face, 
              include_hands, include_quality, include_style, include_artifacts):
        parts = []
        if existing_negative:
            parts.append(existing_negative)
        if include_anatomy:
            parts.append(self.CATEGORIES["anatomy"])
        if include_face:
            parts.append(self.CATEGORIES["face"])
        if include_hands:
            parts.append(self.CATEGORIES["hands"])
        if include_quality:
            parts.append(self.CATEGORIES["quality"])
        if include_style:
            parts.append(self.CATEGORIES["style"])
        if include_artifacts:
            parts.append(self.CATEGORIES["artifacts"])
        
        return (", ".join(parts),)


NODE_CLASS_MAPPINGS = {
    "MultiPersonSceneBuilder": MultiPersonSceneBuilder,
    "EthnicityMixer": EthnicityMixer,
    "WeatherEffectsController": WeatherEffectsController,
    "CameraAngleController": CameraAngleController,
    "PromptTemplateStarter": PromptTemplateStarter,
    "ComprehensiveNegativeBuilder": ComprehensiveNegativeBuilder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MultiPersonSceneBuilder": "👥 Multi-Person Scene",
    "EthnicityMixer": "🌍 Ethnicity Mixer",
    "WeatherEffectsController": "🌧️ Weather Effects",
    "CameraAngleController": "📐 Camera Angle Controller",
    "PromptTemplateStarter": "📝 Prompt Template Starter",
    "ComprehensiveNegativeBuilder": "🚫 Comprehensive Negative Builder",
}
