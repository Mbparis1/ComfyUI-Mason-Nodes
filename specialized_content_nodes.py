"""
Mason's Specialized Content Nodes for ComfyUI
Textures, effects, accessories - Optimized for SD 1.5
"""


class PerspectiveController:
    """Force specific camera angles - SD 1.5 keywords"""
    
    PERSPECTIVES = {
        "worms_eye": "worms eye view, looking up, low angle, from below, upward perspective",
        "birds_eye": "birds eye view, looking down, aerial view, from above, overhead shot",
        "eye_level": "eye level, straight on, neutral angle, direct view",
        "dutch_angle": "dutch angle, tilted frame, dynamic angle, canted shot",
        "over_shoulder": "over the shoulder shot, from behind subject, looking at scene",
        "pov": "pov, point of view, first person perspective, subjective shot",
        "extreme_closeup": "extreme close-up, macro shot, tight framing, detail shot",
        "wide_establishing": "wide shot, establishing shot, full scene visible, environmental",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "perspective": (list(cls.PERSPECTIVES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("perspective_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Specialized"

    def apply(self, prompt, perspective):
        persp_desc = self.PERSPECTIVES.get(perspective, "")
        return (f"{prompt}, {persp_desc}",)


class JewelryAccessoryBuilder:
    """Detailed accessory prompts - SD 1.5 optimized"""
    
    JEWELRY = {
        "necklace": "wearing necklace, pendant, chain around neck",
        "choker": "wearing choker, tight necklace, collar necklace",
        "earrings": "wearing earrings, ear jewelry, decorated ears",
        "bracelet": "wearing bracelet, wrist jewelry, arm band",
        "rings": "wearing rings, finger jewelry, ring on finger",
        "anklet": "wearing anklet, ankle bracelet, foot jewelry",
        "belly_chain": "wearing belly chain, waist chain, body jewelry",
        "hair_accessories": "hair accessories, hair pins, decorative hair clips",
        "tiara": "wearing tiara, crown, head jewelry",
    }
    
    MATERIALS = {
        "gold": "gold jewelry, golden, shiny gold",
        "silver": "silver jewelry, sterling, metallic silver",
        "diamond": "diamond jewelry, sparkling diamonds, gem-encrusted",
        "pearl": "pearl jewelry, white pearls, iridescent pearls",
        "simple": "simple jewelry, minimalist, understated",
        "ornate": "ornate jewelry, elaborate, detailed craftsmanship",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "jewelry_type": (list(cls.JEWELRY.keys()),),
                "material": (list(cls.MATERIALS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("accessorized_prompt",)
    FUNCTION = "accessorize"
    CATEGORY = "Mason's Nodes/Specialized"

    def accessorize(self, prompt, jewelry_type, material):
        jewelry = self.JEWELRY.get(jewelry_type, "")
        mat = self.MATERIALS.get(material, "")
        return (f"{prompt}, {jewelry}, {mat}",)


class TattooPlacement:
    """Add tattoo descriptions with placement - SD 1.5"""
    
    PLACEMENTS = {
        "shoulder": "tattoo on shoulder, shoulder tattoo",
        "lower_back": "lower back tattoo, tramp stamp",
        "arm_sleeve": "arm sleeve tattoo, full sleeve",
        "forearm": "forearm tattoo, lower arm tattoo",
        "thigh": "thigh tattoo, upper leg tattoo",
        "chest": "chest tattoo, sternum tattoo",
        "neck": "neck tattoo, behind ear tattoo",
        "ankle": "ankle tattoo, foot tattoo",
        "ribcage": "ribcage tattoo, side tattoo",
        "hip": "hip tattoo, bikini line tattoo",
    }
    
    STYLES = {
        "tribal": "tribal tattoo, black ink, geometric patterns",
        "floral": "floral tattoo, flower design, botanical",
        "script": "script tattoo, lettering, text tattoo",
        "small_minimal": "small minimalist tattoo, tiny tattoo",
        "full_color": "colorful tattoo, full color ink",
        "blackwork": "blackwork tattoo, solid black design",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "placement": (list(cls.PLACEMENTS.keys()),),
                "style": (list(cls.STYLES.keys()),),
                "has_tattoo": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("tattoo_prompt",)
    FUNCTION = "place"
    CATEGORY = "Mason's Nodes/Specialized"

    def place(self, prompt, placement, style, has_tattoo):
        if not has_tattoo:
            return (f"{prompt}, no tattoos, clean skin",)
        
        place_desc = self.PLACEMENTS.get(placement, "")
        style_desc = self.STYLES.get(style, "")
        return (f"{prompt}, {place_desc}, {style_desc}",)


class WetSweatEffect:
    """Realistic moisture effects - SD 1.5 keywords"""
    
    EFFECTS = {
        "dry": "dry skin, matte skin, no moisture",
        "slight_sheen": "slight skin sheen, healthy glow, subtle shine",
        "light_sweat": "light sweat, glistening skin, post-workout glow",
        "sweaty": "sweaty, perspiration, beads of sweat, wet skin",
        "wet_water": "wet skin, water droplets, just out of water, dripping wet",
        "oiled": "oiled skin, body oil, shiny oiled, glistening oil",
        "after_shower": "fresh from shower, wet hair, damp skin, towel",
        "rain_wet": "rain-soaked, raindrops on skin, caught in rain",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "effect": (list(cls.EFFECTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("wet_prompt",)
    FUNCTION = "apply_effect"
    CATEGORY = "Mason's Nodes/Specialized"

    def apply_effect(self, prompt, effect):
        effect_desc = self.EFFECTS.get(effect, "")
        return (f"{prompt}, {effect_desc}",)


class TextureController:
    """Specific material textures - SD 1.5 optimized"""
    
    TEXTURES = {
        "leather": "leather texture, leather material, smooth leather, shiny leather",
        "silk": "silk fabric, silky smooth, flowing silk, luxurious silk",
        "lace": "lace fabric, lace texture, delicate lace, intricate lace pattern",
        "satin": "satin fabric, shiny satin, smooth satin, glossy material",
        "velvet": "velvet fabric, soft velvet, rich velvet texture",
        "cotton": "cotton fabric, soft cotton, natural cotton",
        "latex": "latex material, shiny latex, tight latex, glossy rubber",
        "sheer": "sheer fabric, see-through, transparent material, gauzy",
        "denim": "denim fabric, jeans material, blue denim",
        "mesh": "mesh fabric, net material, fishnet, open weave",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "texture": (list(cls.TEXTURES.keys()),),
                "for_clothing": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("textured_prompt",)
    FUNCTION = "add_texture"
    CATEGORY = "Mason's Nodes/Specialized"

    def add_texture(self, prompt, texture, for_clothing):
        tex_desc = self.TEXTURES.get(texture, "")
        if for_clothing:
            tex_desc = f"wearing {tex_desc} clothing"
        return (f"{prompt}, {tex_desc}",)


class BreathingAnimation:
    """Subtle chest/body movement cycle - SD 1.5 animation frames"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 20}),
                "breath_cycle_frames": ("INT", {"default": 8, "min": 4, "max": 16}),
                "intensity": (["subtle", "moderate", "deep"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("breathing_prompt",)
    FUNCTION = "breathe"
    CATEGORY = "Mason's Nodes/Specialized"

    def breathe(self, prompt, frame_number, breath_cycle_frames, intensity):
        import math
        
        # Create sine wave for breathing
        phase = (frame_number % breath_cycle_frames) / breath_cycle_frames * 2 * math.pi
        breath_val = math.sin(phase)  # -1 to 1
        
        intensity_map = {"subtle": 0.3, "moderate": 0.6, "deep": 1.0}
        mult = intensity_map.get(intensity, 0.5)
        
        if breath_val > 0.3 * mult:
            breath_desc = "inhaling, chest expanded, breathing in"
        elif breath_val < -0.3 * mult:
            breath_desc = "exhaling, chest relaxed, breathing out"
        else:
            breath_desc = "natural breath, neutral chest position"
        
        return (f"{prompt}, {breath_desc}",)


NODE_CLASS_MAPPINGS = {
    "PerspectiveController": PerspectiveController,
    "JewelryAccessoryBuilder": JewelryAccessoryBuilder,
    "TattooPlacement": TattooPlacement,
    "WetSweatEffect": WetSweatEffect,
    "TextureController": TextureController,
    "BreathingAnimation": BreathingAnimation,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PerspectiveController": "📐 Perspective Controller",
    "JewelryAccessoryBuilder": "💎 Jewelry Builder",
    "TattooPlacement": "🎨 Tattoo Placement",
    "WetSweatEffect": "💧 Wet/Sweat Effect",
    "TextureController": "🧵 Texture Controller",
    "BreathingAnimation": "🫁 Breathing Animation",
}
