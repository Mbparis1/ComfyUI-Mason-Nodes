"""
Mason's Narrative Scenario Building Nodes for ComfyUI
Create complex backstories and scenarios for generated content.
"""

class ContextBuilder:
    """Establish Scene Context and Backstory"""
    
    SCENARIO = {
        "caught_in_act": "caught in the act, surprised, secret discovered, hiding",
        "first_time": "first time, nervous, hesitant, inexperienced, shy",
        "public_risk": "public sex, risky place, quiet, trying not to be seen",
        "interview": "casting couch, interview, audition, nervous candidate",
        "massage": "massage parlor, oil massage, happy ending, towel",
        "gym_workout": "gym workout, yoga pants, sweaty, locker room",
        "office_late": "working late, office sex, desk, boss",
    }
    
    TIME = {
        "morning": "morning light, waking up, bed head, messy hair",
        "night": "night time, dark, lamps, atmospheric",
        "golden_hour": "sunset, golden hour, romantic lighting",
        "party": "party atmosphere, club lights, drunk, nightlife",
    }
    
    ATMOSPHERE = {
        "romantic": "romantic atmosphere, candles, rose petals, love",
        "seedy": "seedy motel, cheap hotel, dirty, gritty",
        "luxury": "luxury penthouse, expensive furniture, rich, high class",
        "clinical": "hospital, exam room, clinical, sterile, medical",
        "school": "classroom, locker room, school uniform, desks",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "scenario": (list(cls.SCENARIO.keys()),),
                "time": (list(cls.TIME.keys()),),
                "atmosphere": (list(cls.ATMOSPHERE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Narrative Scenarios"

    def generate(self, prompt, scenario, time, atmosphere):
        s = self.SCENARIO.get(scenario, "")
        t = self.TIME.get(time, "")
        a = self.ATMOSPHERE.get(atmosphere, "")
        
        positive = f"{prompt}, {s}, {t}, {a}"
        negative = "bad setting, conflicting atmosphere"
        
        return (positive, negative)


class RelationshipBuilder:
    """Define Dynamics Between Characters"""
    
    DYNAMIC = {
        "strangers": "strangers, first meeting, awkward, getting to know",
        "lovers": "deeply in love, romantic, familiar, passionate",
        "enemies": "hate sex, angry sex, rough, conflict",
        "teacher_student": "teacher and student, power dynamic, classroom",
        "boss_employee": "boss and employee, office, power abuse, coercion",
        "doctor_patient": "doctor and patient, medical exam, clinical",
        "step_siblings": "step siblings, taboo, home setting, family",
        "cheating": "cheating wife, affair, ntr, secret lover",
    }
    
    POWER = {
        "equal": "equal power, mutual consent, loving",
        "dominant_submissive": "dominant and submissive, power play, master slave",
        "forced": "forced, coercion, reluctant, resisting",
        "seduction": "seduction, teasing, tempting, trying to convince",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "dynamic": (list(cls.DYNAMIC.keys()),),
                "power_balance": (list(cls.POWER.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Narrative Scenarios"

    def generate(self, prompt, dynamic, power_balance):
        d = self.DYNAMIC.get(dynamic, "")
        p = self.POWER.get(power_balance, "")
        
        positive = f"{prompt}, {d}, {p}"
        negative = "bad anatomy, fused people"
        
        return (positive, negative)


class ScenarioStager:
    """Set the Scene with Props and Locations"""
    
    LOCATION = {
        "bedroom_messy": "messy bedroom, unmade bed, clothes on floor, lived in",
        "bedroom_luxury": "luxury bedroom, silk sheets, expensive hotel",
        "bathroom": "bathroom, shower, bathtub, tile floor, mirror",
        "kitchen": "kitchen counter, cooking, apron, messy kitchen",
        "living_room": "living room, couch, sofa, tv in background",
        "outdoors_nature": "forest, woods, nature, grass, trees",
        "outdoors_urban": "alley, city street, rooftop, brick wall",
        "car": "car interior, leather seats, cramped, roadside",
        "dungeon": "bdsm dungeon, chains, cage, dark room",
    }
    
    PROPS = {
        "none": "",
        "smartphone": "holding smartphone, taking selfie, recording",
        "toy": "sex toy, vibrator, dildo, holding toy",
        "condom": "holding condom, condom wrapper, safety",
        "money": "cash, money, payment, bills",
        "alcohol": "holding drink, wine glass, beer bottle, drunk",
        "camera": "holding camera, filming, tripod",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "location": (list(cls.LOCATION.keys()),),
                "props": (list(cls.PROPS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Narrative Scenarios"

    def generate(self, prompt, location, props):
        l = self.LOCATION.get(location, "")
        p = self.PROPS.get(props, "")
        
        positive = f"{prompt}, {l}, {p}"
        negative = "empty room, minimal background"
        
        return (positive, negative)


NODE_CLASS_MAPPINGS = {
    "ContextBuilder": ContextBuilder,
    "RelationshipBuilder": RelationshipBuilder,
    "ScenarioStager": ScenarioStager,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ContextBuilder": "📖 Context Builder",
    "RelationshipBuilder": "❤️ Relationship Builder",
    "ScenarioStager": "🎬 Scenario Stager",
}
