"""
Mason's Environmental FX Nodes for ComfyUI
Weather, magic, particles and atmospheric effects - SD 1.5 optimized
"""


class OceanEffectsPro:
    """Ocean, water, and nautical environmental effects"""
    
    OCEAN_STATES = {
        "calm": "calm ocean, still water, mirror-like surface, peaceful sea",
        "gentle_waves": "gentle waves, light swells, peaceful sailing",
        "rough_seas": "rough seas, large waves, whitecaps, stormy",
        "storm": "storm at sea, massive waves, lightning, dangerous waters",
        "maelstrom": "maelstrom, whirlpool, spinning vortex, supernatural",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "ocean_state": (list(cls.OCEAN_STATES.keys()),),
                "time_of_day": (["sunrise", "day", "sunset", "night", "moonlit"],),
                "weather": (["clear", "overcast", "foggy", "stormy", "mystical"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ocean_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environmental FX"

    def apply(self, prompt, ocean_state, time_of_day, weather):
        parts = [prompt]
        parts.append(self.OCEAN_STATES.get(ocean_state, ""))
        
        time_map = {
            "sunrise": "sunrise over ocean, golden light, dawn at sea",
            "day": "daylight, bright sun, clear visibility",
            "sunset": "sunset at sea, orange sky, romantic light",
            "night": "night ocean, dark waters, stars above",
            "moonlit": "moonlit ocean, silver light on water, ethereal",
        }
        parts.append(time_map.get(time_of_day, ""))
        
        weather_map = {
            "overcast": "overcast sky, gray clouds, diffused light",
            "foggy": "sea fog, mist, mysterious atmosphere",
            "stormy": "storm clouds, rain, lightning in distance",
            "mystical": "mystical atmosphere, supernatural glow, otherworldly",
        }
        if weather != "clear":
            parts.append(weather_map.get(weather, ""))
        
        return (", ".join([p for p in parts if p]),)


class FireMagicFX:
    """Fire, flames, and magical fire effects"""
    
    FIRE_TYPES = {
        "natural_fire": "natural fire, realistic flames, warm orange glow",
        "bonfire": "large bonfire, crackling flames, sparks flying",
        "torch": "burning torch, flickering flame, medieval lighting",
        "dragon_fire": "dragon fire, intense flames, supernatural heat",
        "hellfire": "hellfire, unnatural flames, demonic, green or blue fire",
        "phoenix_flames": "phoenix flames, golden fire, rebirth, purifying",
        "magical_fire": "magical fire, arcane flames, spell effects",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "fire_type": (list(cls.FIRE_TYPES.keys()),),
                "intensity": (["embers", "low", "medium", "raging", "inferno"],),
                "color": (["natural", "blue", "green", "purple", "white"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fire_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environmental FX"

    def apply(self, prompt, fire_type, intensity, color):
        parts = [prompt]
        parts.append(self.FIRE_TYPES.get(fire_type, ""))
        
        intensity_map = {
            "embers": "glowing embers, dying fire, red coals",
            "low": "low flames, gentle fire, controlled burn",
            "medium": "medium flames, steady fire, good heat",
            "raging": "raging fire, intense flames, spreading",
            "inferno": "massive inferno, all-consuming flames, devastating",
        }
        parts.append(intensity_map.get(intensity, ""))
        
        if color != "natural":
            parts.append(f"{color} flames, unnatural fire color, supernatural")
        
        return (", ".join([p for p in parts if p]),)


class ParticleAtmosphere:
    """Atmospheric particles and environmental details"""
    
    PARTICLES = {
        "dust_motes": "dust motes in light, floating particles, sunbeam dust",
        "fireflies": "fireflies, bioluminescent, magical forest",
        "snow": "falling snow, snowflakes, winter atmosphere",
        "rain": "rain falling, water droplets, wet atmosphere",
        "ash": "falling ash, volcanic, apocalyptic",
        "petals": "falling petals, flower blossoms, romantic",
        "sparks": "flying sparks, fire embers, forge atmosphere",
        "magic_particles": "magical particles, glowing motes, spell effects",
        "fog": "rolling fog, mist, mysterious atmosphere",
        "smoke": "drifting smoke, haze, atmospheric",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "particle_type": (list(cls.PARTICLES.keys()),),
                "density": (["sparse", "medium", "dense", "overwhelming"],),
                "lighting_interaction": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("atmosphere_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environmental FX"

    def apply(self, prompt, particle_type, density, lighting_interaction):
        parts = [prompt]
        parts.append(self.PARTICLES.get(particle_type, ""))
        
        density_map = {
            "sparse": "few particles, subtle atmosphere",
            "medium": "moderate particles, noticeable effect",
            "dense": "heavy particles, thick atmosphere",
            "overwhelming": "overwhelming particles, visibility reduced",
        }
        parts.append(density_map.get(density, ""))
        
        if lighting_interaction:
            parts.append("particles catching light, visible in light beams, volumetric lighting")
        
        return (", ".join([p for p in parts if p]),)


class MagicEffectsPro:
    """Magical effects and supernatural phenomena"""
    
    MAGIC_TYPES = {
        "arcane": "arcane magic, glowing runes, mystical energy, wizard spell",
        "elemental_fire": "fire magic, flames swirling, pyromancy",
        "elemental_ice": "ice magic, frost crystals, cryomancy",
        "elemental_lightning": "lightning magic, electric arcs, electromancy",
        "nature": "nature magic, vines, leaves, druidic power",
        "dark": "dark magic, shadows, corruption, necromancy",
        "light": "light magic, holy glow, divine power, radiance",
        "portal": "magical portal, swirling vortex, dimensional gate",
        "healing": "healing magic, golden glow, restoration, warmth",
        "summoning": "summoning circle, ritual magic, conjuration",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "magic_type": (list(cls.MAGIC_TYPES.keys()),),
                "intensity": (["subtle", "visible", "powerful", "overwhelming"],),
                "source": (["hands", "staff", "amulet", "ambient", "ground"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("magic_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Environmental FX"

    def apply(self, prompt, magic_type, intensity, source):
        parts = [prompt]
        parts.append(self.MAGIC_TYPES.get(magic_type, ""))
        
        intensity_map = {
            "subtle": "subtle magic effect, faint glow",
            "visible": "visible magic, clear magical energy",
            "powerful": "powerful magic, intense glow, crackling energy",
            "overwhelming": "overwhelming magical power, blinding light, reality warping",
        }
        parts.append(intensity_map.get(intensity, ""))
        
        source_map = {
            "hands": "magic emanating from hands, casting gesture",
            "staff": "magic flowing from staff, wizard's implement",
            "amulet": "magic from amulet, glowing pendant",
            "ambient": "ambient magic, environmental, surrounding",
            "ground": "magic circle on ground, floor runes",
        }
        parts.append(source_map.get(source, ""))
        
        return (", ".join([p for p in parts if p]),)


NODE_CLASS_MAPPINGS = {
    "OceanEffectsPro": OceanEffectsPro,
    "FireMagicFX": FireMagicFX,
    "ParticleAtmosphere": ParticleAtmosphere,
    "MagicEffectsPro": MagicEffectsPro,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OceanEffectsPro": "🌊 Ocean Effects Pro",
    "FireMagicFX": "🔥 Fire & Magic FX",
    "ParticleAtmosphere": "✨ Particle Atmosphere",
    "MagicEffectsPro": "🔮 Magic Effects Pro",
}
