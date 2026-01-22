"""
Creative Helper Nodes - Unique functionality for better generations
"""

import random


class WildcardRandomizer:
    """Pick random items from custom lists for variety"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list_items": ("STRING", {"default": "blonde\nbrunette\nredhead\nblack hair\nsilver hair", "multiline": True}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "num_picks": ("INT", {"default": 1, "min": 1, "max": 5}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("random_pick",)
    FUNCTION = "randomize"
    CATEGORY = "Mason/Creative Helpers"

    def randomize(self, list_items, seed, num_picks):
        random.seed(seed)
        items = [i.strip() for i in list_items.split('\n') if i.strip()]
        if not items:
            return ("",)
        picks = random.sample(items, min(num_picks, len(items)))
        return (", ".join(picks),)


class EmotionBlender:
    """Mix two emotions together with adjustable blend"""
    
    EMOTIONS = ["happy", "sad", "angry", "surprised", "shy", "confident", "seductive", 
                "playful", "serious", "dreamy", "mischievous", "loving", "fierce", "peaceful"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "emotion_1": (cls.EMOTIONS,),
                "emotion_2": (cls.EMOTIONS,),
                "blend": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.1}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("blended_emotion",)
    FUNCTION = "blend"
    CATEGORY = "Mason/Creative Helpers"

    def blend(self, emotion_1, emotion_2, blend):
        if blend <= 0.2:
            return (f"{emotion_1} expression",)
        elif blend >= 0.8:
            return (f"{emotion_2} expression",)
        else:
            # Create a blended description
            e1_weight = int((1 - blend) * 100)
            e2_weight = int(blend * 100)
            return (f"expression mixing {emotion_1} and {emotion_2}, {e1_weight}% {emotion_1} {e2_weight}% {emotion_2}",)



class WeatherAtmosphere:
    """Add weather and atmospheric effects to scenes"""
    
    WEATHER = ["clear", "rain", "heavy rain", "snow", "fog", "mist", "storm", 
               "overcast", "partly cloudy", "haze", "steam", "smoke"]
    
    INTENSITY = ["subtle", "moderate", "heavy", "extreme"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "weather": (cls.WEATHER,),
                "intensity": (cls.INTENSITY,),
            },
            "optional": {
                "add_lighting_effects": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weather_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason/Creative Helpers"

    def apply(self, weather, intensity, add_lighting_effects=True):
        weather_fx = {
            "rain": "rain drops, wet surfaces, water droplets, reflections on wet ground",
            "heavy rain": "heavy rainfall, drenched, water streaming, puddles, rain streaks",
            "snow": "snowfall, snow particles, frost, cold atmosphere",
            "fog": "foggy atmosphere, misty, low visibility, ethereal",
            "mist": "light mist, soft atmosphere, dreamy haze",
            "storm": "stormy weather, dramatic clouds, wind effects, intense atmosphere",
            "steam": "steam rising, humid atmosphere, condensation",
            "smoke": "smoke particles, hazy, atmospheric smoke",
        }
        
        base = weather_fx.get(weather, weather)
        result = f"{intensity} {weather}" if weather else ""
        
        if base and weather in weather_fx:
            result = f"{result}, {base}"
        
        if add_lighting_effects and weather in ["rain", "heavy rain", "storm"]:
            result += ", dramatic lighting, moody atmosphere"
        elif add_lighting_effects and weather in ["fog", "mist"]:
            result += ", soft diffused lighting"
            
        return (result,)


class TimeOfDayLighting:
    """Realistic lighting presets based on time of day"""
    
    TIMES = ["golden hour sunrise", "morning", "midday", "afternoon", 
             "golden hour sunset", "blue hour", "dusk", "night", "midnight", "dawn"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "time_of_day": (cls.TIMES,),
            },
            "optional": {
                "indoor_outdoor": (["outdoor", "indoor with window", "indoor artificial"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lighting_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason/Creative Helpers"

    def apply(self, time_of_day, indoor_outdoor="outdoor"):
        lighting = {
            "golden hour sunrise": "warm golden sunlight, soft shadows, orange and pink hues, sunrise lighting",
            "morning": "bright natural morning light, fresh atmosphere, soft shadows",
            "midday": "bright overhead sunlight, harsh shadows, high contrast",
            "afternoon": "warm afternoon light, lengthening shadows, comfortable lighting",
            "golden hour sunset": "golden sunset light, warm orange glow, long shadows, beautiful warm lighting",
            "blue hour": "blue hour lighting, twilight, soft blue tones, magical atmosphere",
            "dusk": "dim dusk lighting, darkening sky, transitional lighting",
            "night": "night time, dark atmosphere, artificial lighting, city lights",
            "midnight": "deep night, very dark, moonlight only, mysterious",
            "dawn": "pre-sunrise light, soft awakening light, peaceful dawn",
        }
        
        result = lighting.get(time_of_day, time_of_day)
        
        if indoor_outdoor == "indoor with window":
            result = f"{result}, light streaming through window"
        elif indoor_outdoor == "indoor artificial":
            result = f"indoor lighting, artificial light, {time_of_day} visible through window"
            
        return (result,)


class CharacterConsistency:
    """Lock in character details for consistent multi-gen"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "character_name": ("STRING", {"default": "Character1"}),
                "physical_traits": ("STRING", {"default": "blonde hair, blue eyes, fair skin", "multiline": True}),
                "distinguishing_features": ("STRING", {"default": "small mole on left cheek", "multiline": True}),
            },
            "optional": {
                "body_type": ("STRING", {"default": ""}),
                "approximate_age": ("STRING", {"default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("character_prompt", "character_id",)
    FUNCTION = "lock"
    CATEGORY = "Mason/Creative Helpers"

    def lock(self, character_name, physical_traits, distinguishing_features, body_type="", approximate_age=""):
        parts = []
        if approximate_age:
            parts.append(approximate_age)
        if physical_traits:
            parts.append(physical_traits)
        if body_type:
            parts.append(body_type)
        if distinguishing_features:
            parts.append(distinguishing_features)
        
        prompt = ", ".join(parts)
        # Create a simple hash for character ID
        char_id = f"{character_name}_{hash(prompt) % 10000}"
        
        return (f"[{character_name}] {prompt}", char_id,)


class OutfitSwapper:
    """Keep same person, cycle through different outfits"""
    
    OUTFIT_PRESETS = {
        "Casual": "casual clothes, t-shirt, jeans, relaxed style",
        "Formal": "formal attire, elegant dress, sophisticated",
        "Business": "business attire, professional clothing, office wear",
        "Swimwear": "swimsuit, bikini, beach wear",
        "Athletic": "athletic wear, sports clothing, fitness outfit",
        "Evening": "evening gown, elegant dress, formal night wear",
        "Lingerie": "lingerie, intimate apparel, lace",
        "Sleepwear": "sleepwear, pajamas, comfortable night clothes",
        "None": "nude, naked, no clothes",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "outfit_type": (list(cls.OUTFIT_PRESETS.keys()),),
            },
            "optional": {
                "color_override": ("STRING", {"default": ""}),
                "custom_details": ("STRING", {"default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("outfit_prompt",)
    FUNCTION = "swap"
    CATEGORY = "Mason/Creative Helpers"

    def swap(self, outfit_type, color_override="", custom_details=""):
        base = self.OUTFIT_PRESETS.get(outfit_type, outfit_type)
        
        if color_override:
            base = f"{color_override} {base}"
        if custom_details:
            base = f"{base}, {custom_details}"
            
        return (base,)


class AngleRotator:
    """Generate same pose from different camera angles"""
    
    ANGLES = ["front view", "three quarter view left", "three quarter view right",
              "side view left", "side view right", "back view", 
              "from above", "from below", "dutch angle"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "camera_angle": (cls.ANGLES,),
            },
            "optional": {
                "distance": (["close up", "medium shot", "full body", "wide shot"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("angle_prompt",)
    FUNCTION = "rotate"
    CATEGORY = "Mason/Creative Helpers"

    def rotate(self, camera_angle, distance="medium shot"):
        return (f"{camera_angle}, {distance}",)


class CleanBackgroundMode:
    """Prompts optimized for easy background removal"""
    
    BG_TYPES = ["solid white", "solid gray", "solid black", "gradient", 
                "studio backdrop", "green screen", "simple neutral"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "background_type": (cls.BG_TYPES,),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("bg_prompt", "negative_add",)
    FUNCTION = "apply"
    CATEGORY = "Mason/Creative Helpers"

    def apply(self, background_type):
        bg_prompts = {
            "solid white": "pure white background, white backdrop, clean white studio",
            "solid gray": "neutral gray background, gray backdrop, studio gray",
            "solid black": "pure black background, black backdrop, dark studio",
            "gradient": "gradient background, smooth gradient backdrop",
            "studio backdrop": "professional studio background, clean backdrop",
            "green screen": "green screen background, chroma key green",
            "simple neutral": "simple clean background, minimal backdrop, neutral",
        }
        
        negative = "busy background, complex background, detailed background, cluttered"
        
        return (bg_prompts.get(background_type, background_type), negative,)


class LocationDetailer:
    """Add realistic details to basic locations"""
    
    LOCATIONS = ["bedroom", "bathroom", "living room", "kitchen", "office", 
                 "hotel room", "studio", "outdoor", "beach", "pool"]
    
    STYLES = ["luxury", "modern", "vintage", "messy", "clean", "minimalist", 
              "cozy", "professional", "romantic", "casual"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "location": (cls.LOCATIONS,),
                "style": (cls.STYLES,),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("location_prompt",)
    FUNCTION = "detail"
    CATEGORY = "Mason/Creative Helpers"

    def detail(self, location, style):
        details = {
            ("bedroom", "luxury"): "luxury bedroom, expensive bedding, high end furniture, elegant decor",
            ("bedroom", "modern"): "modern bedroom, contemporary furniture, clean lines, minimalist design",
            ("bedroom", "cozy"): "cozy bedroom, warm lighting, soft textures, comfortable atmosphere",
            ("bedroom", "romantic"): "romantic bedroom, rose petals, candles, intimate lighting",
            ("bathroom", "luxury"): "luxury bathroom, marble surfaces, elegant fixtures, spa-like",
            ("bathroom", "modern"): "modern bathroom, sleek design, contemporary fixtures",
            ("hotel room", "luxury"): "luxury hotel room, high end amenities, elegant decor, premium bedding",
        }
        
        # Try to get specific combo, fallback to generic
        result = details.get((location, style))
        if not result:
            result = f"{style} {location}, {style} decor, {style} atmosphere"
            
        return (result,)


# Node registration
NODE_CLASS_MAPPINGS = {
    "WildcardRandomizer": WildcardRandomizer,
    "EmotionBlender": EmotionBlender,
    "WeatherAtmosphere": WeatherAtmosphere,
    "TimeOfDayLighting": TimeOfDayLighting,
    "CharacterConsistency": CharacterConsistency,
    "OutfitSwapper": OutfitSwapper,
    "AngleRotator": AngleRotator,
    "CleanBackgroundMode": CleanBackgroundMode,
    "LocationDetailer": LocationDetailer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WildcardRandomizer": "🎲 Wildcard Randomizer",
    "EmotionBlender": "😊 Emotion Blender",
    "WeatherAtmosphere": "🌧️ Weather/Atmosphere",
    "TimeOfDayLighting": "🌅 Time of Day Lighting",
    "CharacterConsistency": "👤 Character Consistency",
    "OutfitSwapper": "👗 Outfit Swapper",
    "AngleRotator": "📐 Angle Rotator",
    "CleanBackgroundMode": "🎯 Clean Background Mode",
    "LocationDetailer": "🏠 Location Detailer",
}
