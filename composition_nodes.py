"""
Mason's Composition Nodes for ComfyUI
Professional photographic composition control - SD 1.5 optimized
"""


class RuleOfThirdsPositioner:
    """Subject placement using rule of thirds"""
    
    POSITIONS = {
        "center": "subject in center, centered composition, middle of frame",
        "left_third": "subject on left third, left side of frame, off-center left",
        "right_third": "subject on right third, right side of frame, off-center right",
        "upper_third": "subject in upper third, top of frame, elevated position",
        "lower_third": "subject in lower third, bottom of frame, grounded position",
        "upper_left": "subject in upper left intersection, rule of thirds, power point",
        "upper_right": "subject in upper right intersection, rule of thirds, power point",
        "lower_left": "subject in lower left intersection, rule of thirds, power point",
        "lower_right": "subject in lower right intersection, rule of thirds, power point"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "position": (list(cls.POSITIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("positioned_prompt",)
    FUNCTION = "position"
    CATEGORY = "Mason's Nodes/Composition"

    def position(self, prompt, position):
        pos_desc = self.POSITIONS.get(position, "")
        return (f"{prompt}, {pos_desc}",)


class FramingController:
    """Control shot framing and cropping"""
    
    FRAMINGS = {
        "extreme_close_up": "extreme close-up, ECU, face fills frame, intimate detail, macro view",
        "close_up": "close-up shot, CU, head and shoulders, facial detail, tight framing",
        "medium_close_up": "medium close-up, MCU, chest and up, upper body focus",
        "medium_shot": "medium shot, MS, waist up, half body visible, standard framing",
        "medium_long": "medium long shot, MLS, knees up, three-quarter body",
        "full_body": "full body shot, head to toe, entire figure visible, complete body",
        "long_shot": "long shot, LS, full body with environment, establishing context",
        "extreme_long_shot": "extreme long shot, ELS, subject small in frame, vast environment"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "framing": (list(cls.FRAMINGS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("framed_prompt",)
    FUNCTION = "frame"
    CATEGORY = "Mason's Nodes/Composition"

    def frame(self, prompt, framing):
        frame_desc = self.FRAMINGS.get(framing, "")
        return (f"{prompt}, {frame_desc}",)


class NegativeSpaceController:
    """Control empty space around subject"""
    
    NEGATIVE_SPACE = {
        "minimal": "tight framing, minimal negative space, subject fills frame, no empty areas",
        "balanced": "balanced composition, moderate negative space, breathing room",
        "spacious": "spacious framing, ample negative space, airy composition, room to breathe",
        "dramatic_left": "negative space on left, subject right, asymmetrical balance",
        "dramatic_right": "negative space on right, subject left, asymmetrical balance",
        "headroom": "headroom above subject, space above head, vertical breathing room",
        "lead_room": "lead room in front of subject, directional space, movement room"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "space": (list(cls.NEGATIVE_SPACE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("spaced_prompt",)
    FUNCTION = "set_space"
    CATEGORY = "Mason's Nodes/Composition"

    def set_space(self, prompt, space):
        space_desc = self.NEGATIVE_SPACE.get(space, "")
        return (f"{prompt}, {space_desc}",)


class SubjectProminenceController:
    """How dominant subject is in frame"""
    
    PROMINENCE_LEVELS = {
        "dominant": "subject dominant in frame, commanding presence, fills majority of image",
        "prominent": "subject prominent, clearly the focus, main visual element",
        "balanced": "balanced prominence, subject and environment equal, contextual shot",
        "environmental": "environmental portrait, subject within context, setting emphasized",
        "subtle": "subject subtle in frame, understated presence, environment focused"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "prominence": (list(cls.PROMINENCE_LEVELS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prominence_prompt",)
    FUNCTION = "set_prominence"
    CATEGORY = "Mason's Nodes/Composition"

    def set_prominence(self, prompt, prominence):
        prom_desc = self.PROMINENCE_LEVELS.get(prominence, "")
        return (f"{prompt}, {prom_desc}",)


class ForegroundElementsAdder:
    """Add foreground blur/elements for depth"""
    
    FOREGROUND_ELEMENTS = {
        "none": "",
        "blurred_foliage": "blurred foreground foliage, out of focus leaves, bokeh plants",
        "blurred_flowers": "blurred foreground flowers, soft petals in front, floral bokeh",
        "blurred_curtain": "blurred sheer curtain in foreground, fabric foreground blur",
        "water_droplets": "water droplets in foreground, bokeh droplets, rain blur",
        "light_flares": "foreground lens flare, light streaks, optical effects",
        "frame_within_frame": "frame within frame, doorway framing, window framing, natural frame",
        "soft_bokeh": "soft foreground bokeh, colorful blur, abstract foreground"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "foreground": (list(cls.FOREGROUND_ELEMENTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("foreground_prompt",)
    FUNCTION = "add_foreground"
    CATEGORY = "Mason's Nodes/Composition"

    def add_foreground(self, prompt, foreground):
        fg_desc = self.FOREGROUND_ELEMENTS.get(foreground, "")
        if fg_desc:
            return (f"{prompt}, {fg_desc}",)
        return (prompt,)


class BackgroundComplexityController:
    """Control background from simple to complex"""
    
    BACKGROUNDS = {
        "solid": "solid color background, plain backdrop, uniform background, simple",
        "gradient": "gradient background, smooth color transition, faded backdrop",
        "simple_studio": "simple studio backdrop, clean background, professional minimal",
        "blurred_simple": "simple blurred background, soft out of focus backdrop, minimal detail",
        "moderate_detail": "moderately detailed background, some environmental context",
        "rich_environment": "rich environmental background, detailed setting, contextual depth",
        "complex_scene": "complex background scene, intricate environment, many details",
        "busy_urban": "busy urban background, city backdrop, architectural detail"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "complexity": (list(cls.BACKGROUNDS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("background_prompt",)
    FUNCTION = "set_background"
    CATEGORY = "Mason's Nodes/Composition"

    def set_background(self, prompt, complexity):
        bg_desc = self.BACKGROUNDS.get(complexity, "")
        return (f"{prompt}, {bg_desc}",)


NODE_CLASS_MAPPINGS = {
    "RuleOfThirdsPositioner": RuleOfThirdsPositioner,
    "FramingController": FramingController,
    "NegativeSpaceController": NegativeSpaceController,
    "SubjectProminenceController": SubjectProminenceController,
    "ForegroundElementsAdder": ForegroundElementsAdder,
    "BackgroundComplexityController": BackgroundComplexityController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RuleOfThirdsPositioner": "📐 Rule of Thirds Positioner",
    "FramingController": "🖼️ Framing Controller",
    "NegativeSpaceController": "⬜ Negative Space Controller",
    "SubjectProminenceController": "👤 Subject Prominence",
    "ForegroundElementsAdder": "🌿 Foreground Elements",
    "BackgroundComplexityController": "🏙️ Background Complexity",
}
