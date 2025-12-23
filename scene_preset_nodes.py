"""
Mason's Scene Preset Nodes for ComfyUI
Quick environment/scene setups - SD 1.5 optimized
"""


class BedroomSceneBuilder:
    """Build bedroom scene descriptions"""
    
    BEDROOM_TYPES = {
        "modern": "modern bedroom, contemporary design, clean lines, minimalist furniture",
        "luxury": "luxury bedroom, opulent, expensive furniture, high-end decor, silk sheets",
        "cozy": "cozy bedroom, warm lighting, comfortable bed, soft blankets, inviting",
        "romantic": "romantic bedroom, rose petals, candles, soft lighting, intimate atmosphere",
        "hotel": "hotel room, professional bedding, neutral decor, clean hotel bedroom",
        "bohemian": "bohemian bedroom, eclectic decor, colorful textiles, artistic",
        "minimalist": "minimalist bedroom, sparse furniture, clean, simple, zen",
        "vintage": "vintage bedroom, antique furniture, classic style, retro decor",
    }
    
    BED_TYPES = {
        "king": "king size bed, large bed, spacious",
        "queen": "queen size bed, medium bed",
        "canopy": "canopy bed, four poster bed, draped fabric",
        "platform": "platform bed, modern low bed, sleek design",
        "round": "round bed, circular bed, unique design",
    }
    
    LIGHTING = {
        "natural": "natural daylight, window light, soft sunlight",
        "morning": "morning light, sunrise glow, fresh daylight",
        "evening": "evening light, warm sunset tones, golden hour",
        "night": "night time, dark room, dim lighting",
        "candlelit": "candlelit, candle light, warm flickering glow, romantic",
        "neon": "neon lighting, colored neon glow, moody",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "bedroom_type": (list(cls.BEDROOM_TYPES.keys()),),
                "bed_type": (list(cls.BED_TYPES.keys()),),
                "lighting": (list(cls.LIGHTING.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Scene Presets"

    def build(self, prompt, bedroom_type, bed_type, lighting):
        bedroom = self.BEDROOM_TYPES.get(bedroom_type, "")
        bed = self.BED_TYPES.get(bed_type, "")
        light = self.LIGHTING.get(lighting, "")
        return (f"{prompt}, {bedroom}, {bed}, {light}",)


class PoolsideSceneBuilder:
    """Build poolside/water scene descriptions"""
    
    POOL_TYPES = {
        "luxury_pool": "luxury swimming pool, infinity pool, resort pool, crystal clear water",
        "backyard_pool": "backyard pool, residential pool, private pool",
        "hotel_pool": "hotel pool, resort pool, lounge chairs, tropical setting",
        "indoor_pool": "indoor pool, indoor swimming pool, glass ceiling, modern",
        "natural_pool": "natural pool, lagoon, natural water, tropical paradise",
        "rooftop_pool": "rooftop pool, city skyline, urban pool, penthouse",
    }
    
    ELEMENTS = {
        "lounge_chairs": "lounge chairs, sun loungers, poolside furniture",
        "tropical_plants": "tropical plants, palm trees, lush greenery",
        "umbrellas": "beach umbrellas, sun shade, colorful umbrellas",
        "bar": "pool bar, tiki bar, drinks, cocktails",
        "waterfall": "waterfall feature, cascading water, water feature",
    }
    
    TIME = {
        "sunny_day": "bright sunny day, clear blue sky, golden sunlight",
        "sunset": "sunset, golden hour, orange sky, warm light",
        "night": "night time, pool lights, underwater lighting, stars",
        "overcast": "overcast sky, soft diffused light, cloudy",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "pool_type": (list(cls.POOL_TYPES.keys()),),
                "elements": (list(cls.ELEMENTS.keys()),),
                "time": (list(cls.TIME.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Scene Presets"

    def build(self, prompt, pool_type, elements, time):
        pool = self.POOL_TYPES.get(pool_type, "")
        elem = self.ELEMENTS.get(elements, "")
        t = self.TIME.get(time, "")
        return (f"{prompt}, {pool}, {elem}, {t}",)


class StudioSceneBuilder:
    """Build photography studio scene descriptions"""
    
    STUDIO_TYPES = {
        "professional": "professional photography studio, studio lighting, controlled environment",
        "glamour": "glamour photo studio, fashion photography setup, high-end",
        "boudoir": "boudoir studio, intimate setting, soft fabrics, romantic props",
        "fashion": "fashion photography studio, runway style, editorial setup",
        "portrait": "portrait studio, simple backdrop, focused lighting",
        "art": "art studio, creative space, artistic environment, props",
    }
    
    BACKDROPS = {
        "white": "white backdrop, clean white background, seamless white",
        "black": "black backdrop, dark background, dramatic black",
        "gray": "gray backdrop, neutral gray background, studio gray",
        "colored": "colored backdrop, vibrant background color",
        "gradient": "gradient backdrop, smooth color transition background",
        "textured": "textured backdrop, fabric texture, artistic background",
    }
    
    PROPS = {
        "none": "",
        "stool": "studio stool, posing stool, simple seat",
        "bed": "studio bed, white sheets, boudoir prop",
        "chair": "elegant chair, posing chair, decorative seat",
        "mirror": "large mirror, reflective surface, mirror prop",
        "fabrics": "flowing fabrics, silk drapes, sheer curtains",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "studio_type": (list(cls.STUDIO_TYPES.keys()),),
                "backdrop": (list(cls.BACKDROPS.keys()),),
                "props": (list(cls.PROPS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Scene Presets"

    def build(self, prompt, studio_type, backdrop, props):
        studio = self.STUDIO_TYPES.get(studio_type, "")
        back = self.BACKDROPS.get(backdrop, "")
        prop = self.PROPS.get(props, "")
        if prop:
            return (f"{prompt}, {studio}, {back}, {prop}",)
        return (f"{prompt}, {studio}, {back}",)


class OutdoorSceneBuilder:
    """Build outdoor scene descriptions"""
    
    LOCATIONS = {
        "beach": "beach, sandy beach, ocean waves, seaside, coastal",
        "forest": "forest, woodland, trees, natural setting, green foliage",
        "garden": "garden, flower garden, blooming flowers, landscaped",
        "park": "park, public park, green grass, trees, natural light",
        "urban": "urban setting, city street, buildings, metropolitan",
        "desert": "desert, sand dunes, arid landscape, golden sand",
        "mountain": "mountain, mountain backdrop, peaks, scenic view",
        "field": "open field, meadow, tall grass, wildflowers",
        "rooftop": "rooftop, city view, urban rooftop, skyline background",
    }
    
    WEATHER = {
        "sunny": "sunny day, bright sunlight, clear sky, warm",
        "cloudy": "cloudy day, overcast, soft light, diffused",
        "golden_hour": "golden hour, sunset light, warm golden tones",
        "blue_hour": "blue hour, twilight, cool blue tones, dusk",
        "rainy": "rainy, rain, wet surfaces, dramatic weather",
        "foggy": "foggy, misty, atmospheric fog, mysterious",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "location": (list(cls.LOCATIONS.keys()),),
                "weather": (list(cls.WEATHER.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Scene Presets"

    def build(self, prompt, location, weather):
        loc = self.LOCATIONS.get(location, "")
        weath = self.WEATHER.get(weather, "")
        return (f"{prompt}, {loc}, {weath}",)


class BathroomSceneBuilder:
    """Build bathroom scene descriptions"""
    
    BATHROOM_TYPES = {
        "luxury_spa": "luxury spa bathroom, marble surfaces, high-end fixtures, elegant",
        "modern": "modern bathroom, contemporary design, clean lines, sleek fixtures",
        "vintage": "vintage bathroom, clawfoot tub, classic tiles, retro style",
        "hotel": "hotel bathroom, pristine white, professional, clean",
        "minimalist": "minimalist bathroom, simple design, clean, zen-like",
    }
    
    FEATURES = {
        "bathtub": "bathtub, soaking tub, bath, bubble bath",
        "shower": "shower, glass shower, rainfall shower, steam",
        "jacuzzi": "jacuzzi, hot tub, whirlpool bath, bubbling water",
        "vanity": "vanity mirror, bathroom mirror, makeup area",
    }
    
    AMBIANCE = {
        "steam": "steam, steamy bathroom, warm mist, humid",
        "candlelit": "candlelit, candles, romantic lighting, warm glow",
        "bright": "bright lighting, well-lit, clean bright bathroom",
        "moody": "moody lighting, dim, atmospheric, shadows",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "bathroom_type": (list(cls.BATHROOM_TYPES.keys()),),
                "feature": (list(cls.FEATURES.keys()),),
                "ambiance": (list(cls.AMBIANCE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Scene Presets"

    def build(self, prompt, bathroom_type, feature, ambiance):
        bath = self.BATHROOM_TYPES.get(bathroom_type, "")
        feat = self.FEATURES.get(feature, "")
        amb = self.AMBIANCE.get(ambiance, "")
        return (f"{prompt}, {bath}, {feat}, {amb}",)


NODE_CLASS_MAPPINGS = {
    "BedroomSceneBuilder": BedroomSceneBuilder,
    "PoolsideSceneBuilder": PoolsideSceneBuilder,
    "StudioSceneBuilder": StudioSceneBuilder,
    "OutdoorSceneBuilder": OutdoorSceneBuilder,
    "BathroomSceneBuilder": BathroomSceneBuilder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BedroomSceneBuilder": "🛏️ Bedroom Scene Builder",
    "PoolsideSceneBuilder": "🏊 Poolside Scene Builder",
    "StudioSceneBuilder": "📸 Studio Scene Builder",
    "OutdoorSceneBuilder": "🌳 Outdoor Scene Builder",
    "BathroomSceneBuilder": "🛁 Bathroom Scene Builder",
}
