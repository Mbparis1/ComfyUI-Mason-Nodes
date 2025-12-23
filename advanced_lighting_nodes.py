"""
Mason's Advanced Lighting Nodes for ComfyUI
Studio-quality lighting control through prompts - SD 1.5 optimized
"""


class ThreePointLightingSetup:
    """Professional three-point lighting: key, fill, and back lights"""
    
    KEY_LIGHTS = {
        "soft_large": "soft key light, large softbox, diffused main light, gentle shadows",
        "hard_small": "hard key light, small source, sharp shadows, focused light",
        "butterfly": "butterfly key light, overhead centered, beauty lighting",
        "rembrandt": "Rembrandt key light, 45 degree angle, triangle shadow on cheek",
        "split": "split key light, 90 degree angle, half-face illuminated"
    }
    
    FILL_LIGHTS = {
        "none": "no fill light, strong shadows, dramatic contrast",
        "subtle": "subtle fill light, deep shadows, moody, 4:1 ratio",
        "moderate": "moderate fill light, balanced shadows, 2:1 ratio",
        "strong": "strong fill light, minimal shadows, even lighting, 1.5:1 ratio"
    }
    
    BACK_LIGHTS = {
        "none": "",
        "rim": "rim light, edge lighting, highlighted outline, separation from background",
        "hair_light": "hair light, top back lighting, highlighted hair, glossy strands",
        "kicker": "kicker light, side back light, edge highlight, dimensional",
        "halo": "halo backlighting, glowing outline, angelic rim, strong separation"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "key_light": (list(cls.KEY_LIGHTS.keys()),),
                "fill_light": (list(cls.FILL_LIGHTS.keys()),),
                "back_light": (list(cls.BACK_LIGHTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lit_prompt",)
    FUNCTION = "setup_lighting"
    CATEGORY = "Mason's Nodes/Advanced Lighting"

    def setup_lighting(self, prompt, key_light, fill_light, back_light):
        key = self.KEY_LIGHTS.get(key_light, "")
        fill = self.FILL_LIGHTS.get(fill_light, "")
        back = self.BACK_LIGHTS.get(back_light, "")
        parts = [prompt, key, fill]
        if back:
            parts.append(back)
        return (", ".join(parts),)


class ShadowController:
    """Control shadow characteristics"""
    
    SHADOW_HARDNESS = {
        "none": "no shadows, flat lighting, shadowless, even illumination",
        "very_soft": "very soft shadows, highly diffused, gentle transitions",
        "soft": "soft shadows, diffused edges, gradual falloff",
        "medium": "medium shadows, defined but not harsh, natural look",
        "hard": "hard shadows, defined edges, dramatic, sharp transitions",
        "very_hard": "very hard shadows, razor edges, intense contrast, noir style"
    }
    
    SHADOW_DIRECTIONS = {
        "from_above": "shadows falling down, overhead light source, natural sun direction",
        "from_left": "shadows to the right, left-side lighting, directional",
        "from_right": "shadows to the left, right-side lighting, directional",
        "from_below": "shadows upward, underlighting, dramatic, horror style",
        "multiple": "multiple shadow directions, complex lighting, layered shadows"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "hardness": (list(cls.SHADOW_HARDNESS.keys()),),
                "direction": (list(cls.SHADOW_DIRECTIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("shadow_prompt",)
    FUNCTION = "set_shadows"
    CATEGORY = "Mason's Nodes/Advanced Lighting"

    def set_shadows(self, prompt, hardness, direction):
        hard = self.SHADOW_HARDNESS.get(hardness, "")
        direct = self.SHADOW_DIRECTIONS.get(direction, "")
        return (f"{prompt}, {hard}, {direct}",)


class HighlightController:
    """Control specular highlights and skin shine"""
    
    HIGHLIGHT_TYPES = {
        "matte": "matte skin, no highlights, non-reflective, flat finish",
        "subtle_sheen": "subtle skin sheen, healthy glow, minimal highlights",
        "natural": "natural highlights, realistic skin reflections, balanced shine",
        "dewy": "dewy skin, fresh appearance, moisture glow, luminous",
        "oiled": "oiled skin look, high shine, glistening, wet appearance",
        "wet_look": "wet skin, water droplets, high reflectivity, soaked appearance"
    }
    
    CATCHLIGHTS = {
        "none": "no eye catchlights",
        "subtle": "subtle eye catchlights, small reflections in eyes",
        "ring": "ring catchlights in eyes, circular reflections, ring light look",
        "window": "window catchlights, rectangular reflections in eyes",
        "multiple": "multiple catchlights, complex eye reflections, studio setup"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "highlights": (list(cls.HIGHLIGHT_TYPES.keys()),),
                "catchlights": (list(cls.CATCHLIGHTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("highlight_prompt",)
    FUNCTION = "set_highlights"
    CATEGORY = "Mason's Nodes/Advanced Lighting"

    def set_highlights(self, prompt, highlights, catchlights):
        high = self.HIGHLIGHT_TYPES.get(highlights, "")
        catch = self.CATCHLIGHTS.get(catchlights, "")
        return (f"{prompt}, {high}, {catch}",)


class ColorTemperatureController:
    """Control warm/cool color casts"""
    
    TEMPERATURES = {
        "very_cool": "very cool color temperature, blue tint, icy tones, 3000K look",
        "cool": "cool color temperature, slight blue, daylight balanced, 5000K",
        "neutral": "neutral color temperature, balanced white, accurate colors, 5500K",
        "warm": "warm color temperature, golden tones, orange tint, 3500K look",
        "very_warm": "very warm color temperature, deep golden, sunset tones, 2500K look",
        "mixed": "mixed color temperature, warm and cool contrast, color tension"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "temperature": (list(cls.TEMPERATURES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("temp_prompt",)
    FUNCTION = "set_temperature"
    CATEGORY = "Mason's Nodes/Advanced Lighting"

    def set_temperature(self, prompt, temperature):
        temp = self.TEMPERATURES.get(temperature, "")
        return (f"{prompt}, {temp}",)


class LightingRatioController:
    """Control key-to-fill lighting ratios"""
    
    RATIOS = {
        "1_to_1": "1:1 lighting ratio, flat even lighting, no shadow depth, beauty look",
        "2_to_1": "2:1 lighting ratio, subtle shadows, soft dimension, flattering",
        "3_to_1": "3:1 lighting ratio, natural shadows, classic portrait lighting",
        "4_to_1": "4:1 lighting ratio, defined shadows, dramatic but controlled",
        "8_to_1": "8:1 lighting ratio, deep shadows, moody, film noir influenced",
        "high_contrast": "high contrast lighting ratio, extreme shadows, dramatic, bold"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "ratio": (list(cls.RATIOS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ratio_prompt",)
    FUNCTION = "set_ratio"
    CATEGORY = "Mason's Nodes/Advanced Lighting"

    def set_ratio(self, prompt, ratio):
        rat = self.RATIOS.get(ratio, "")
        return (f"{prompt}, {rat}",)


class PracticalLightingAdder:
    """Add practical light sources: lamps, candles, screen glow"""
    
    PRACTICAL_LIGHTS = {
        "none": "",
        "table_lamp": "table lamp lighting, warm lamp glow, practical light source, cozy illumination",
        "candles": "candlelight, flickering candles, warm flame light, romantic glow",
        "fireplace": "fireplace light, fire glow, dancing flames, warm flickering light",
        "neon_signs": "neon sign lighting, colored neon glow, vibrant light, urban night",
        "screen_glow": "screen glow, computer light on face, blue screen illumination, tech lighting",
        "string_lights": "string light glow, fairy lights, twinkling bokeh, festive lighting",
        "window_light": "window light, natural light through window, dappled sunlight, soft rays",
        "car_headlights": "car headlight illumination, harsh direct beams, night scene lighting",
        "streetlamp": "streetlamp lighting, overhead night light, urban glow, night scene"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "practical_light": (list(cls.PRACTICAL_LIGHTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("practical_prompt",)
    FUNCTION = "add_practical"
    CATEGORY = "Mason's Nodes/Advanced Lighting"

    def add_practical(self, prompt, practical_light):
        prac = self.PRACTICAL_LIGHTS.get(practical_light, "")
        if prac:
            return (f"{prompt}, {prac}",)
        return (prompt,)


NODE_CLASS_MAPPINGS = {
    "ThreePointLightingSetup": ThreePointLightingSetup,
    "ShadowController": ShadowController,
    "HighlightController": HighlightController,
    "ColorTemperatureController": ColorTemperatureController,
    "LightingRatioController": LightingRatioController,
    "PracticalLightingAdder": PracticalLightingAdder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ThreePointLightingSetup": "💡 Three-Point Lighting",
    "ShadowController": "🌑 Shadow Controller",
    "HighlightController": "✨ Highlight Controller",
    "ColorTemperatureController": "🌡️ Color Temperature",
    "LightingRatioController": "⚖️ Lighting Ratio",
    "PracticalLightingAdder": "🕯️ Practical Lighting",
}
