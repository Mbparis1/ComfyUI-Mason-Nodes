"""
Mason's Architecture Nodes for ComfyUI
Buildings, structures, and architectural elements - SD 1.5 optimized
"""


class HistoricalArchitecture:
    """Historical and period architecture"""
    
    STYLES = {
        "medieval_castle": "medieval castle, stone walls, towers, drawbridge, fortress",
        "gothic_cathedral": "gothic cathedral, flying buttresses, stained glass, spires",
        "roman_temple": "Roman temple, columns, marble, classical architecture",
        "greek_ruins": "ancient Greek ruins, Parthenon style, Doric columns, weathered",
        "egyptian_pyramid": "Egyptian pyramid, ancient, desert, massive stone",
        "japanese_temple": "Japanese temple, pagoda, wood construction, zen garden",
        "victorian_mansion": "Victorian mansion, ornate, multiple stories, gothic elements",
        "tudor_house": "Tudor house, half-timbered, English style, historical",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.STYLES.keys()),),
                "state": (["pristine", "weathered", "ruins", "restored"],),
                "time_of_day": (["day", "sunset", "night", "moonlit"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("architecture_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Architecture"

    def apply(self, prompt, style, state, time_of_day):
        parts = [prompt]
        parts.append(self.STYLES.get(style, ""))
        
        state_map = {
            "pristine": "well-maintained, perfect condition",
            "weathered": "weathered by time, aged, patina of history",
            "ruins": "ancient ruins, crumbling, overgrown, forgotten",
            "restored": "carefully restored, historical preservation",
        }
        parts.append(state_map.get(state, ""))
        
        time_map = {
            "sunset": "sunset lighting, golden hour, warm glow",
            "night": "night time, artificial lighting, dramatic",
            "moonlit": "moonlit, silver light, mysterious atmosphere",
        }
        if time_of_day != "day":
            parts.append(time_map.get(time_of_day, ""))
        
        return (", ".join([p for p in parts if p]),)


class ModernArchitecture:
    """Modern and contemporary architecture"""
    
    STYLES = {
        "skyscraper": "modern skyscraper, glass and steel, towering, urban",
        "brutalist": "brutalist architecture, raw concrete, massive, imposing",
        "minimalist": "minimalist design, clean lines, open space, simple",
        "art_deco": "Art Deco building, geometric patterns, 1920s glamour",
        "industrial": "industrial architecture, exposed pipes, warehouse style",
        "futuristic": "futuristic architecture, sleek curves, sci-fi, advanced",
        "sustainable": "eco-friendly building, green roof, solar panels, natural",
        "deconstructivist": "deconstructivist architecture, angular, fragmented, Gehry-style",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.STYLES.keys()),),
                "setting": (["urban", "suburban", "isolated", "waterfront"],),
                "lighting": (["daylight", "night_lit", "neon", "dramatic"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("modern_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Architecture"

    def apply(self, prompt, style, setting, lighting):
        parts = [prompt]
        parts.append(self.STYLES.get(style, ""))
        
        setting_map = {
            "urban": "urban setting, city environment, busy",
            "suburban": "suburban location, residential area, quiet",
            "isolated": "isolated location, alone in landscape, dramatic",
            "waterfront": "waterfront property, water reflection, scenic",
        }
        parts.append(setting_map.get(setting, ""))
        
        lighting_map = {
            "night_lit": "illuminated at night, interior lights glowing",
            "neon": "neon lighting, cyberpunk atmosphere, colorful",
            "dramatic": "dramatic lighting, high contrast, cinematic",
        }
        if lighting != "daylight":
            parts.append(lighting_map.get(lighting, ""))
        
        return (", ".join([p for p in parts if p]),)


class FantasyArchitecture:
    """Fantasy and otherworldly architecture"""
    
    STYLES = {
        "elven_palace": "elven palace, organic curves, natural integration, ethereal",
        "dwarven_hall": "dwarven hall, underground, massive stone, carved pillars",
        "dark_fortress": "dark fortress, menacing, black stone, evil stronghold",
        "cloud_castle": "castle in clouds, floating, heavenly, impossible",
        "underwater_palace": "underwater palace, aquatic, coral and pearl, mermaid kingdom",
        "tree_city": "city in giant trees, platforms and bridges, nature magic",
        "crystal_tower": "crystal tower, magical, glowing, wizard's domain",
        "necromancer_lair": "necromancer's lair, bones and skulls, dark magic, death",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.STYLES.keys()),),
                "magical_element": (["none", "glowing", "enchanted", "cursed", "ancient"],),
                "scale": (["normal", "massive", "impossible", "miniature"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fantasy_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Architecture"

    def apply(self, prompt, style, magical_element, scale):
        parts = [prompt]
        parts.append(self.STYLES.get(style, ""))
        
        magic_map = {
            "glowing": "magical glow, luminescent, radiating power",
            "enchanted": "enchanted structure, protective magic, blessed",
            "cursed": "cursed building, dark energy, forbidden place",
            "ancient": "ancient magic, primordial power, timeless enchantment",
        }
        if magical_element != "none":
            parts.append(magic_map.get(magical_element, ""))
        
        scale_map = {
            "massive": "massive scale, impossibly large, dwarfing surroundings",
            "impossible": "impossible architecture, defying physics, M.C. Escher-like",
            "miniature": "miniature, dollhouse scale, tiny but detailed",
        }
        if scale != "normal":
            parts.append(scale_map.get(scale, ""))
        
        return (", ".join([p for p in parts if p]),)


NODE_CLASS_MAPPINGS = {
    "HistoricalArchitecture": HistoricalArchitecture,
    "ModernArchitecture": ModernArchitecture,
    "FantasyArchitecture": FantasyArchitecture,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HistoricalArchitecture": "🏰 Historical Architecture",
    "ModernArchitecture": "🏢 Modern Architecture",
    "FantasyArchitecture": "🏯 Fantasy Architecture",
}
