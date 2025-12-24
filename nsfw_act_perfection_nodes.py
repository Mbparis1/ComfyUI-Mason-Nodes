"""
Mason's NSFW Act Perfection Nodes
The absolute peak of act-specific accuracy - SD 1.5 optimized
"""

class DeepThroatPerfection:
    """Perfects the deep throat blowjob act with all micro-details"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "depth": (["shallow", "medium", "deep", "balls_deep"],),
                "gag_reflex": (["none", "slight", "heavy_gagging", "drooling"],),
                "hand_interaction": (["none", "hand_on_back_of_head", "fingers_in_mouth", "double_handjob_combo"],),
                "throat_detail": ("BOOLEAN", {"default": True}),
                "eye_state": (["neutral", "watering_eyes", "rolled_back", "pleading_look"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("act_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Act Perfection"

    def apply(self, prompt, depth, gag_reflex, hand_interaction, throat_detail, eye_state):
        parts = [prompt, "deep throat blowjob"]
        
        # Depth
        depth_map = {
            "shallow": "tip only, oral focus",
            "medium": "taking half, mouth full",
            "deep": "deep penetration into throat, mouth wide open",
            "balls_deep": "extreme deepthroat, balls pressing against chin, full length in throat",
        }
        parts.append(depth_map[depth])
        
        # Gagging
        if gag_reflex == "slight":
            parts.append("slight gagging, heavy breathing")
        elif gag_reflex == "heavy_gagging":
            parts.append("intense gagging, throat reflex, struggling to breath")
        elif gag_reflex == "drooling":
            parts.append("messy drooling, saliva dripping from mouth, wet face")
            
        # Hands
        if hand_interaction == "hand_on_back_of_head":
            parts.append("hand on back of head, pushing down, dominant hand placement")
        elif hand_interaction == "fingers_in_mouth":
            parts.append("fingers in mouth beside penis, stretching mouth, messy")
        elif hand_interaction == "double_handjob_combo":
            parts.append("hand stroking base, double hand interaction")
            
        # Throat
        if throat_detail:
            parts.append("visible throat bulge, neck muscles straining, realistic swallowing")
            
        # Eyes
        eye_map = {
            "watering_eyes": "eyes watering, tears from gagging, glistening eyes",
            "rolled_back": "eyes rolling back in ecstasy, whites showing",
            "pleading_look": "looking up with pleading eyes, submissive gaze",
        }
        if eye_state != "neutral":
            parts.append(eye_map[eye_state])
            
        return (", ".join(parts),)

class GropingPerfection:
    """Perfects the act of groping and physical handling"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "target_area": (["breasts", "buttocks", "thighs", "waist"],),
                "grip_intensity": (["soft", "firm", "hard_squeeze", "rough_grabbing"],),
                "finger_placement": (["flat_palm", "fingertips_digging_in", "spreading"],),
                "skin_reaction": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("groping_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Act Perfection"

    def apply(self, prompt, target_area, grip_intensity, finger_placement, skin_reaction):
        parts = [prompt, f"groping {target_area}"]
        
        # Grip
        grip_map = {
            "soft": "gentle touch, palm on skin",
            "firm": "firm grip, holding securely",
            "hard_squeeze": "hard squeeze, fingers pressing deep",
            "rough_grabbing": "rough grabbing, aggressive handling, intense grip",
        }
        parts.append(grip_map[grip_intensity])
        
        # Fingers
        if finger_placement == "fingertips_digging_in":
            parts.append("fingertips digging into flesh, visible pressure points")
        elif finger_placement == "spreading":
            parts.append(f"fingers spreading the {target_area} apart, showcasing")
            
        # Skin
        if skin_reaction:
            parts.append("skin indentation, flesh being displaced, realistic physical contact, skin compression")
            
        return (", ".join(parts),)

class AnalPerfection:
    """Perfects anal penetration with anatomical accuracy"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "phase": (["insertion", "mid_thrust", "balls_pressing", "aftermath_gaping"],),
                "stretching": (["natural", "wide_stretching", "extreme_diameter", "gaping"],),
                "lubrication": (["dry_look", "wet_glistening", "messy_lube", "dripping"],),
                "sphincter_detail": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("anal_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Act Perfection"

    def apply(self, prompt, phase, stretching, lubrication, sphincter_detail):
        parts = [prompt, "anal sex"]
        
        # Phase
        phase_map = {
            "insertion": "initial insertion, stretching point, tight fit",
            "mid_thrust": "full penetration, rhythmic movement, high friction",
            "balls_pressing": "balls pressing against anus, full depth, extreme penetration",
            "aftermath_gaping": "freshly used, gaping anus, open and stretched, red and flushed",
        }
        parts.append(phase_map[phase])
        
        # Stretching
        stretch_map = {
            "wide_stretching": "wide stretching, skin taut, extreme diameter",
            "extreme_diameter": "extreme stretching, pushing limits, massive fit",
            "gaping": "gaping open, unable to close, circular stretch",
        }
        if stretching != "natural":
            parts.append(stretch_map[stretching])
            
        # Lube
        lube_map = {
            "wet_glistening": "wet glistening skin, light lubrication",
            "messy_lube": "messy lubricant, white streaks, heavy lube",
            "dripping": "lube dripping down, very wet and messy",
        }
        if lubrication != "dry_look":
            parts.append(lube_map[lubrication])
            
        # Detail
        if sphincter_detail:
            parts.append("detailed sphincter texture, wrinkled skin, realistic anatomical detail, reddened rim")
            
        return (", ".join(parts),)

class VaginalPerfection:
    """Perfects vaginal penetration and pussy play"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "depth": (["insertion", "mid", "deep_bottoming_out"],),
                "labia_state": (["closed", "spreading", "pulled_open", "swollen"],),
                "fluid_type": (["natural_moisture", "dripping_wet", "creampie_leakage", "foamy"],),
                "friction_visual": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("vaginal_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Act Perfection"

    def apply(self, prompt, depth, labia_state, fluid_type, friction_visual):
        parts = [prompt, "vaginal penetration"]
        
        # Depth
        depth_map = {
            "insertion": "initial entry, stretching opening",
            "mid": "rhythmic thrusting, wet friction",
            "deep_bottoming_out": "bottoming out, deep penetration, internal focus",
        }
        parts.append(depth_map[depth])
        
        # Labia
        labia_map = {
            "spreading": "labia spreading wide, showcasing entrance",
            "pulled_open": "fingers pulling labia open, extreme exposure",
            "swollen": "swollen labia, heavily aroused, engorged tissue",
        }
        if labia_state != "closed":
            parts.append(labia_map[labia_state])
            
        # Fluids
        fluid_map = {
            "dripping_wet": "dripping wet pussy, soaked, liquid trails",
            "creampie_leakage": "creampie leaking out, thick white fluid, messy",
            "foamy": "foamy white friction, air bubbles in lube, messy sex",
        }
        if fluid_type != "natural_moisture":
            parts.append(fluid_map[fluid_type])
            
        # Friction
        if friction_visual:
            parts.append("visible friction, skin flushing, wet sounds visual, intense contact")
            
        return (", ".join(parts),)

class ManualPlayPerfection:
    """Perfects fingering and handplay acts"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "act_type": (["fingering", "pussy_rubbing", "clit_play", "spreading_wide", "penis_stroking"],),
                "hand_count": (["single_hand", "both_hands"],),
                "digit_count": (["one_finger", "two_fingers", "three_fingers", "whole_fist"],),
                "moisture_level": (["damp", "soaked", "stringy_saliva", "messy_lube"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("manual_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Act Perfection"

    def apply(self, prompt, act_type, hand_count, digit_count, moisture_level):
        parts = [prompt]
        
        # Act
        act_map = {
            "fingering": "fingering pussy, fingers inside",
            "pussy_rubbing": "rubbing pussy, clitoral stimulation",
            "clit_play": "intense clit play, focused stimulation",
            "spreading_wide": "fingers spreading pussy wide, extreme exposure",
            "penis_stroking": "handjob, stroking penis, firm grip",
        }
        parts.append(act_map[act_type])
        
        # Digits
        if act_type in ["fingering", "spreading_wide"]:
            digit_map = {
                "one_finger": "one finger inside, tight",
                "two_fingers": "two fingers inside, stretching",
                "three_fingers": "three fingers inside, wide stretch",
                "whole_fist": "fisting, extreme penetration, huge stretching",
            }
            parts.append(digit_map[digit_count])
            
        # Moisture
        moisture_map = {
            "soaked": "completely soaked, dripping wet",
            "stringy_saliva": "stringy saliva, wet mouth-like moisture",
            "messy_lube": "messy lube, white streaks, ultra wet",
        }
        if moisture_level != "damp":
            parts.append(moisture_map[moisture_level])
            
        if hand_count == "both_hands":
            parts.append("using both hands, dual interaction")
            
        return (", ".join(parts),)

NODE_CLASS_MAPPINGS = {
    "DeepThroatPerfection": DeepThroatPerfection,
    "GropingPerfection": GropingPerfection,
    "AnalPerfection": AnalPerfection,
    "VaginalPerfection": VaginalPerfection,
    "ManualPlayPerfection": ManualPlayPerfection,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeepThroatPerfection": "👅 Deep Throat Perfection",
    "GropingPerfection": "🤲 Groping Perfection",
    "AnalPerfection": "🍑 Anal Perfection",
    "VaginalPerfection": "🌸 Vaginal Perfection",
    "ManualPlayPerfection": "🤚 Manual Play Perfection",
}
