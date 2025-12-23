"""
Mason's Environment Detail Nodes for ComfyUI
Replace scene/environment LoRAs with prompt engineering - SD 1.5 optimized
"""


class SurfaceController:
    """Control surface textures in scenes"""
    
    SURFACES = {
        "marble": "marble surface, polished marble, veined stone, luxurious marble",
        "wood": "wooden surface, wood grain, natural wood texture, timber",
        "concrete": "concrete surface, cement texture, industrial concrete",
        "metal": "metal surface, metallic texture, brushed metal, cold steel",
        "glass": "glass surface, transparent glass, reflective glass, clear",
        "fabric": "fabric surface, textile, cloth texture, soft material",
        "leather": "leather surface, leather texture, genuine leather, supple",
        "tile": "tile surface, ceramic tiles, bathroom tiles, mosaic",
        "brick": "brick surface, red brick, exposed brick wall, rustic",
        "sand": "sandy surface, beach sand, fine sand texture, grainy",
        "grass": "grass surface, green grass, lawn, soft grass",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "surface": (list(cls.SURFACES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("surface_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environment Detail"

    def apply(self, prompt, surface):
        sur = self.SURFACES.get(surface, "")
        return (f"{prompt}, {sur}",)


class ReflectionController:
    """Control reflections in scenes"""
    
    REFLECTIONS = {
        "none": "no reflections, matte surfaces, non-reflective",
        "subtle": "subtle reflections, slight mirror, faint reflection",
        "mirror": "mirror reflection, clear reflection, reflective surface",
        "water": "water reflection, rippling reflection, pool reflection",
        "glass": "glass reflection, window reflection, transparent reflection",
        "wet_floor": "wet floor reflection, puddle reflection, shiny wet surface",
        "chrome": "chrome reflection, metallic mirror, distorted reflection",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "reflection": (list(cls.REFLECTIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("reflection_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environment Detail"

    def apply(self, prompt, reflection):
        ref = self.REFLECTIONS.get(reflection, "")
        return (f"{prompt}, {ref}",)


class FogHazeController:
    """Control atmospheric fog and haze"""
    
    ATMOSPHERICS = {
        "clear": "clear atmosphere, no fog, sharp visibility, crisp air",
        "light_haze": "light haze, subtle atmospheric haze, soft atmosphere",
        "misty": "misty atmosphere, light mist, foggy, romantic fog",
        "fog": "fog, foggy environment, thick mist, low visibility",
        "heavy_fog": "heavy fog, dense fog, mysterious atmosphere, obscured",
        "smoke": "smoke in air, smoky atmosphere, haze from smoke",
        "dust": "dusty atmosphere, dust particles, hazy dust, desert dust",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "atmosphere": (list(cls.ATMOSPHERICS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fog_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environment Detail"

    def apply(self, prompt, atmosphere):
        atm = self.ATMOSPHERICS.get(atmosphere, "")
        return (f"{prompt}, {atm}",)


class ParticleController:
    """Control particles in the air"""
    
    PARTICLES = {
        "none": "",
        "dust_motes": "dust motes in air, floating particles, visible dust in light",
        "snow": "falling snow, snowflakes, winter snow, gentle snowfall",
        "rain": "rain, raindrops, falling rain, rainy weather",
        "sparkles": "sparkles in air, glitter, magical particles, fairy dust",
        "petals": "flower petals in air, falling petals, romantic petals",
        "leaves": "falling leaves, autumn leaves, floating leaves",
        "embers": "glowing embers, fire particles, floating sparks",
        "bubbles": "bubbles, soap bubbles, floating bubbles, iridescent",
        "confetti": "confetti, falling confetti, celebration particles",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "particle": (list(cls.PARTICLES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("particle_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environment Detail"

    def apply(self, prompt, particle):
        part = self.PARTICLES.get(particle, "")
        if part:
            return (f"{prompt}, {part}",)
        return (prompt,)


class TimeOfDayEnhancer:
    """Enhanced time of day control"""
    
    TIMES = {
        "dawn": "dawn light, early morning, pink sky, soft morning light, sunrise colors",
        "morning": "morning light, fresh daylight, bright morning, soft shadows",
        "midday": "midday sun, harsh overhead light, strong shadows, noon",
        "afternoon": "afternoon light, warm afternoon, angled sunlight, soft golden",
        "golden_hour": "golden hour, warm golden light, sunset glow, magic hour",
        "sunset": "sunset light, orange sky, dramatic sunset, evening colors",
        "blue_hour": "blue hour, twilight, deep blue sky, cool evening light",
        "dusk": "dusk, fading light, evening twilight, dark blue sky",
        "night": "night time, dark, moonlight, night scene, low light",
        "midnight": "midnight, deep night, very dark, starlit",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "time": (list(cls.TIMES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("time_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environment Detail"

    def apply(self, prompt, time):
        t = self.TIMES.get(time, "")
        return (f"{prompt}, {t}",)


class SeasonController:
    """Control seasonal appearance"""
    
    SEASONS = {
        "spring": "spring season, blooming flowers, fresh green, spring atmosphere, new growth",
        "summer": "summer season, bright sun, lush green, hot weather, summer vibes",
        "autumn": "autumn season, fall colors, orange leaves, warm tones, cozy autumn",
        "winter": "winter season, cold weather, bare trees, snow, winter atmosphere",
        "tropical": "tropical setting, palm trees, humid, tropical paradise",
        "desert": "desert environment, arid, sandy, hot and dry, desert landscape",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "season": (list(cls.SEASONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("season_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environment Detail"

    def apply(self, prompt, season):
        s = self.SEASONS.get(season, "")
        return (f"{prompt}, {s}",)


NODE_CLASS_MAPPINGS = {
    "SurfaceController": SurfaceController,
    "ReflectionController": ReflectionController,
    "FogHazeController": FogHazeController,
    "ParticleController": ParticleController,
    "TimeOfDayEnhancer": TimeOfDayEnhancer,
    "SeasonController": SeasonController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SurfaceController": "🧱 Surface Controller",
    "ReflectionController": "🪞 Reflection Controller",
    "FogHazeController": "🌫️ Fog/Haze Controller",
    "ParticleController": "✨ Particle Controller",
    "TimeOfDayEnhancer": "🌅 Time of Day Enhancer",
    "SeasonController": "🍂 Season Controller",
}
