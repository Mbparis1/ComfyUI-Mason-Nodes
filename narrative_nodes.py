"""
Mason's Narrative Scenario Builder Nodes
Contextual prompts for situational storytelling - SD 1.5 optimized
"""

class ScenarioArchitect:
    """Builds a situational context for the scene"""
    
    SCENARIOS = {
        "secret_affair": "secret affair, clandestine meeting, hidden from view, forbidden romance, tension",
        "office_scandal": "office setting, forbidden workplace encounter, desk, professional environment, risk of discovery",
        "gym_encounter": "gym setting, locker room, post-workout tension, athletic environment, intimate encounter",
        "photographers_studio": "photography studio, professional shoot, model and photographer dynamic, studio lighting, artistic tension",
        "late_night_kitchen": "late night kitchen, quiet house, intimate midnight encounter, soft lighting",
        "hotel_room_luxury": "luxury hotel room, expensive setting, anonymous encounter, opulent decor",
        "outdoor_risk": "outdoor setting, public place, risk of discovery, hidden in the shadows, adventurous",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "scenario": (list(cls.SCENARIOS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scenario_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Narrative"

    def apply(self, prompt, scenario):
        s = self.SCENARIOS.get(scenario, "")
        return (f"{prompt}, {s}",)

class DialogueHintGen:
    """Inserts cues for vocalizations and dialogue hints into the prompt"""
    
    HINTS = {
        "stifled_moans": "stifled moans, quiet vocalizations, muffled sounds, intense silence",
        "heavy_panting": "heavy panting, audible breathing, gasping for air",
        "whispered_commands": "whispering in ear, intense verbal dynamic, vocal intimacy",
        "uninhibited_sounds": "loud vocalizations, uninhibited sounds, pleasure noises",
        "begging_tone": "begging expression, vocal submission, intense verbal dynamic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "hint": (list(cls.HINTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("dialogue_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Narrative"

    def apply(self, prompt, hint):
        h = self.HINTS.get(hint, "")
        return (f"{prompt}, {h}",)

NODE_CLASS_MAPPINGS = {
    "ScenarioArchitect": ScenarioArchitect,
    "DialogueHintGen": DialogueHintGen,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ScenarioArchitect": "📖 Scenario Architect",
    "DialogueHintGen": "💬 Dialogue Hint Gen",
}
