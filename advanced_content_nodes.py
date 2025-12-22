"""
Mason's Advanced Content Nodes for ComfyUI
Multi-subject, interactions, and transitions
"""

import random


class MultiSubjectManager:
    """Handle 2+ people with distinct descriptions"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject1": ("STRING", {"default": "blonde woman", "multiline": True}),
                "subject2": ("STRING", {"default": "brunette woman", "multiline": True}),
                "relationship": (["side by side", "facing each other", "one behind other", "embracing", "interacting"],),
                "focus": (["both equal", "focus subject1", "focus subject2"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("multi_prompt",)
    FUNCTION = "manage"
    CATEGORY = "Mason's Nodes/Advanced Content"

    def manage(self, subject1, subject2, relationship, focus):
        focus_mods = {
            "both equal": "two women, both equally prominent",
            "focus subject1": f"focus on {subject1}, {subject2} in background",
            "focus subject2": f"focus on {subject2}, {subject1} in background",
        }
        
        prompt = f"{subject1} and {subject2}, {relationship}, {focus_mods[focus]}"
        return (prompt,)


class InteractionPoses:
    """Pre-built poses for couples/interactions"""
    
    INTERACTIONS = {
        "standing_together": "two people standing close together, side by side, shoulders touching",
        "facing_each_other": "two people facing each other, eye contact, intimate distance",
        "back_to_back": "two people back to back, standing confidently",
        "one_behind": "one person standing behind the other, arms around waist",
        "embracing": "two people embracing, hugging, close contact",
        "holding_hands": "two people holding hands, connected, intimate moment",
        "dancing": "two people dancing together, close embrace, romantic",
        "kissing": "two people kissing, intimate moment, romantic embrace",
        "sitting_together": "two people sitting close together, casual intimacy",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "interaction": (list(cls.INTERACTIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("interaction_prompt",)
    FUNCTION = "pose"
    CATEGORY = "Mason's Nodes/Advanced Content"

    def pose(self, prompt, interaction):
        pose_desc = self.INTERACTIONS.get(interaction, "")
        return (f"{prompt}, {pose_desc}",)


class WardrobeTransition:
    """Gradual clothing changes across frames"""
    
    TRANSITIONS = {
        "dressed_to_bikini": ["fully dressed casual", "removing outer layer", "in underwear", "in bikini top", "in bikini"],
        "formal_to_casual": ["formal dress", "loosening dress", "dress falling", "casual clothing", "relaxed attire"],
        "dressed_to_lingerie": ["fully dressed", "unbuttoning", "shirt open", "revealing lingerie", "lingerie only"],
        "workout_to_shower": ["workout clothes", "removing top", "sports bra only", "undressing", "towel wrapped"],
        "adding_layers": ["minimal clothing", "adding top", "adding bottom", "accessorizing", "fully styled"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject": ("STRING", {"default": "beautiful woman", "multiline": True}),
                "transition": (list(cls.TRANSITIONS.keys()),),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 10}),
                "total_frames": ("INT", {"default": 5, "min": 2, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("wardrobe_prompt",)
    FUNCTION = "transition"
    CATEGORY = "Mason's Nodes/Advanced Content"

    def transition(self, subject, transition, frame_number, total_frames):
        stages = self.TRANSITIONS.get(transition, ["dressed"])
        idx = min(int(frame_number * len(stages) / total_frames), len(stages) - 1)
        clothing = stages[idx]
        return (f"{subject}, {clothing}",)


class EnvironmentBlender:
    """Smooth transitions between settings"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject": ("STRING", {"default": "", "multiline": True}),
                "start_environment": ("STRING", {"default": "indoor bedroom"}),
                "end_environment": ("STRING", {"default": "outdoor beach"}),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 10}),
                "total_frames": ("INT", {"default": 5, "min": 2, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("blended_prompt",)
    FUNCTION = "blend"
    CATEGORY = "Mason's Nodes/Advanced Content"

    def blend(self, subject, start_environment, end_environment, frame_number, total_frames):
        progress = frame_number / max(total_frames - 1, 1)
        
        if progress < 0.3:
            env = start_environment
        elif progress < 0.7:
            env = f"transitioning from {start_environment} to {end_environment}"
        else:
            env = end_environment
        
        return (f"{subject}, {env}",)


class TimeOfDayShifter:
    """Progress lighting from day to night"""
    
    TIMES = {
        "dawn_to_noon": ["dawn, early morning light", "morning, golden light", "late morning", "midday, bright sun", "noon, overhead sun"],
        "noon_to_dusk": ["noon, bright light", "afternoon, warm light", "late afternoon, golden hour", "sunset, orange sky", "dusk, purple sky"],
        "dusk_to_night": ["dusk, dim light", "twilight, blue hour", "early night", "night, dark", "midnight, darkness"],
        "night_to_dawn": ["night, dark", "pre-dawn, hint of light", "early dawn", "dawn breaking", "sunrise, golden light"],
        "golden_hour": ["approaching golden hour", "early golden hour", "peak golden hour", "late golden hour", "after golden hour"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "time_progression": (list(cls.TIMES.keys()),),
                "frame_number": ("INT", {"default": 0, "min": 0, "max": 10}),
                "total_frames": ("INT", {"default": 5, "min": 2, "max": 10}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("timed_prompt",)
    FUNCTION = "shift"
    CATEGORY = "Mason's Nodes/Advanced Content"

    def shift(self, prompt, time_progression, frame_number, total_frames):
        stages = self.TIMES.get(time_progression, ["day"])
        idx = min(int(frame_number * len(stages) / total_frames), len(stages) - 1)
        time_desc = stages[idx]
        return (f"{prompt}, {time_desc}",)


class HairStyler:
    """Control hair style and color"""
    
    STYLES = {
        "long_straight": "long straight hair, flowing hair, silky hair",
        "long_wavy": "long wavy hair, flowing waves, voluminous hair",
        "long_curly": "long curly hair, bouncy curls, voluminous curls",
        "medium_straight": "medium length straight hair, shoulder length",
        "short_bob": "short bob haircut, chin length hair",
        "pixie": "pixie cut, very short hair, cropped hair",
        "ponytail": "hair in ponytail, tied back hair",
        "bun": "hair in bun, updo hairstyle",
        "braids": "braided hair, braids",
        "messy": "messy hair, tousled hair, bedhead",
    }
    
    COLORS = {
        "blonde": "blonde hair, golden hair",
        "brunette": "brown hair, brunette",
        "black": "black hair, dark hair",
        "red": "red hair, ginger, auburn",
        "platinum": "platinum blonde, silver hair",
        "pink": "pink hair, dyed pink",
        "blue": "blue hair, dyed blue",
        "ombre": "ombre hair, gradient color",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.STYLES.keys()),),
                "color": (list(cls.COLORS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("hair_prompt",)
    FUNCTION = "style"
    CATEGORY = "Mason's Nodes/Advanced Content"

    def style(self, prompt, style, color):
        style_desc = self.STYLES.get(style, "")
        color_desc = self.COLORS.get(color, "")
        return (f"{prompt}, {color_desc}, {style_desc}",)


NODE_CLASS_MAPPINGS = {
    "MultiSubjectManager": MultiSubjectManager,
    "InteractionPoses": InteractionPoses,
    "WardrobeTransition": WardrobeTransition,
    "EnvironmentBlender": EnvironmentBlender,
    "TimeOfDayShifter": TimeOfDayShifter,
    "HairStyler": HairStyler,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MultiSubjectManager": "👥 Multi-Subject Manager",
    "InteractionPoses": "💑 Interaction Poses",
    "WardrobeTransition": "👙 Wardrobe Transition",
    "EnvironmentBlender": "🌅 Environment Blender",
    "TimeOfDayShifter": "🌙 Time of Day Shifter",
    "HairStyler": "💇 Hair Styler",
}
