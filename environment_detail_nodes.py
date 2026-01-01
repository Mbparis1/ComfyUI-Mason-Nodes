"""
Mason's Environment & Atmosphere Detail Nodes for ComfyUI
Temperature, time of day, and age refinement - SD 1.5 optimized
"""


class TemperatureSweatController:
    """Controls temperature-related visual effects on the subject"""
    
    TEMPERATURE = {
        "cold": "cold environment, visible breath, pink cheeks and nose, shivering slightly",
        "cool": "cool environment, comfortable, slight chill",
        "neutral": "",
        "warm": "warm environment, relaxed, comfortable warmth",
        "hot": "hot environment, heavy sweating, flushed skin, overheated",
        "steamy": "steamy environment, condensation, sauna-like heat, glistening",
    }
    
    SWEAT_LEVELS = {
        "none": "",
        "light_glow": "light sheen on skin, subtle glow",
        "perspiring": "perspiring, sweat on forehead, damp skin",
        "heavy_sweat": "heavy sweating, sweat dripping, completely drenched in sweat",
        "post_workout": "post-workout sweat, athletic perspiration, exhausted and sweaty",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "temperature": (list(cls.TEMPERATURE.keys()),),
                "sweat_level": (list(cls.SWEAT_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("temp_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environment"

    def apply(self, prompt, temperature, sweat_level):
        parts = [prompt]
        if temperature != "neutral":
            parts.append(self.TEMPERATURE.get(temperature, ""))
        if sweat_level != "none":
            parts.append(self.SWEAT_LEVELS.get(sweat_level, ""))
        return (", ".join([p for p in parts if p]),)


class TimeOfDayLighting:
    """Specific time-of-day lighting conditions"""
    
    TIMES = {
        "dawn": "dawn lighting, early morning light, soft pink sky, first light",
        "morning": "morning light, fresh daylight, bright and clean, new day",
        "golden_hour_morning": "golden hour morning, warm early sunlight, long shadows",
        "midday": "midday sun, harsh overhead light, minimal shadows, bright",
        "afternoon": "afternoon light, warm sunlight, relaxed atmosphere",
        "golden_hour_evening": "golden hour evening, warm sunset glow, romantic lighting",
        "dusk": "dusk lighting, purple sky, fading light, twilight",
        "blue_hour": "blue hour, cool blue tones, magical atmosphere, post-sunset",
        "night": "night time, artificial lighting, dark environment, nighttime",
        "midnight": "midnight, low light, intimate darkness, late night",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "time_of_day": (list(cls.TIMES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("time_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environment"

    def apply(self, prompt, time_of_day):
        t = self.TIMES.get(time_of_day, "")
        if t:
            return (f"{prompt}, {t}",)
        return (prompt,)


class AgeAppearanceRefinement:
    """Fine control over perceived age and maturity"""
    
    AGE_RANGES = {
        "young_adult": "young adult, early twenties, youthful energy, fresh faced",
        "mid_twenties": "mid twenties, prime of youth, confident beauty",
        "late_twenties": "late twenties, mature beauty, refined features",
        "early_thirties": "early thirties, sophisticated, elegant maturity",
        "milf": "milf aesthetic, attractive mature woman, confident older woman",
        "cougar": "cougar aesthetic, sexy older woman, experienced beauty, distinguished",
    }
    
    MATURITY_CUES = {
        "youthful_skin": "youthful skin, no wrinkles, smooth complexion",
        "light_lines": "light expression lines, subtle maturity, lived-in beauty",
        "distinguished": "distinguished features, graceful aging, elegant lines",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "age_range": (list(cls.AGE_RANGES.keys()),),
                "maturity_cues": (list(cls.MATURITY_CUES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("age_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environment"

    def apply(self, prompt, age_range, maturity_cues):
        parts = [prompt]
        parts.append(self.AGE_RANGES.get(age_range, ""))
        parts.append(self.MATURITY_CUES.get(maturity_cues, ""))
        return (", ".join([p for p in parts if p]),)


class DynamicWeatherPro:
    """Advanced weather control system"""
    
    TYPE = {
        "clear": "clear skies, blue sky, sunny",
        "cloudy": "cloudy sky, overcast, grey clouds, gloomy",
        "rain": "raining, rainfall, wet ground, puddles, storm",
        "snow": "snowing, snowflakes, snow covered ground, winter",
        "storm": "thunderstorm, lightning, dark clouds, heavy rain",
        "fog": "foggy, mist, haze, low visibility",
        "windy": "windy, blowing wind, hair blowing, leaves blowing",
    }
    
    INTENSITY = {
        "light": "light, gentle, subtle",
        "moderate": "moderate, steady",
        "heavy": "heavy, intense, severe, extreme",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "weather_type": (list(cls.TYPE.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weather_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environment"

    def apply(self, prompt, weather_type, intensity):
        w = self.TYPE.get(weather_type, "")
        i = self.INTENSITY.get(intensity, "")
        
        # Simple combinator logic
        if intensity == "heavy":
            w = f"heavy {w}"
        elif intensity == "light":
            w = f"light {w}"
            
        return (f"{prompt}, {w}",)


NODE_CLASS_MAPPINGS = {
    "TemperatureSweatController": TemperatureSweatController,
    "TimeOfDayLighting": TimeOfDayLighting,
    "AgeAppearanceRefinement": AgeAppearanceRefinement,
    "DynamicWeatherPro": DynamicWeatherPro,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TemperatureSweatController": "🌡️ Temperature & Sweat Controller",
    "TimeOfDayLighting": "🌅 Time of Day Lighting",
    "AgeAppearanceRefinement": "👩 Age Appearance Refinement",
    "DynamicWeatherPro": "⛈️ Dynamic Weather Pro",
}
