"""
Mason's Extreme NSFW Mechanics Nodes
The highest level of detail for NSFW creation - SD 1.5 optimized
"""

class ExtremeFluidDynamics:
    """Advanced fluid control: volume, viscosity, and splatter logic"""
    
    FLUID_TYPES = {
        "thick_creamy": "thick creamy fluid, viscous white liquid, heavy coating, opaque",
        "watery_translucent": "watery translucent fluid, clear liquid, thin coating, glistening",
        "heavy_volume": "massive volume of fluid, flooding the scene, overflowing, abundant liquid",
        "messy_splatter": "wide splatter pattern, liquid droplets everywhere, messy coating, scattered",
        "slow_drip": "thick slow drips, viscous trailing, long liquid strands, dripping slowly",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "fluid_style": (list(cls.FLUID_TYPES.keys()),),
                "volume": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.1}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fluid_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Extreme NSFW"

    def apply(self, prompt, fluid_style, volume):
        f = self.FLUID_TYPES.get(fluid_style, "")
        if volume > 2.0:
            f = f"extreme {f}, covered in fluid, drenched"
        elif volume < 0.5:
            f = f"traces of {f}, light coating"
        return (f"{prompt}, {f}",)

class AnatomicalDetailMax:
    """Precision control over specific body part reactions"""
    
    REACTIONS = {
        "heavy_flushing": "intense skin flushing, deep red hue on chest and genitals, heat visible",
        "extreme_dilation": "extreme dilation, wide open, stretched to limit, gaping",
        "swelling_arousal": "visible swelling, engorged tissue, throbbing, heavily aroused",
        "vein_definition": "visible veins on skin, engorged blood vessels, extreme arousal",
        "texture_goosebumps": "goosebumps on skin, textured skin surface, shivering from pleasure",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "reaction": (list(cls.REACTIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("reaction_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Extreme NSFW"

    def apply(self, prompt, reaction):
        r = self.REACTIONS.get(reaction, "")
        return (f"{prompt}, {r}",)

class EnvironmentArousal:
    """Environmental cues of a sexual encounter"""
    
    CUES = {
        "messy_sheets": "rumpled bed sheets, messy blanket, bed in disarray, signs of struggle",
        "discarded_clothing": "discarded underwear on floor, messy pile of clothes, scattered attire",
        "wet_stains": "wet stains on surface, damp spots, liquid marks on bed",
        "steamy_mirror": "steamy mirror, condensation on walls, fogged glass, hot room",
        "disheveled_furniture": "disheveled furniture, moved pillows, room in chaos",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "cue": (list(cls.CUES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("env_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Extreme NSFW"

    def apply(self, prompt, cue):
        c = self.CUES.get(cue, "")
        return (f"{prompt}, {c}",)

class IntensityDriver:
    """Driving the intensity of the generation through gritty details"""
    
    DRIVERS = {
        "raw_passion": "raw passion, animalistic intensity, extreme desire, eyes locked",
        "physical_exhaustion": "gasping for air, physically exhausted, eyes unfocused, sweat dripping",
        "rough_mechanics": "rough movement, aggressive contact, intense friction, visible strain",
        "vulnerable_moment": "vulnerable expression, overwhelmed by pleasure, surrender",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "driver": (list(cls.DRIVERS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("intensity_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Extreme NSFW"

    def apply(self, prompt, driver):
        d = self.DRIVERS.get(driver, "")
        return (f"{prompt}, {d}",)

class PhysiologicalReactionMax:
    """Enhanced Body Reactions and Reflexes"""
    
    REFLEX = {
        "toes_curling": "curling toes, flexed feet, arching feet, extreme tension",
        "back_arching": "back arching, lifting hips, spine curvature, hyperextension",
        "muscle_spasm": "muscle spasms, twitching thighs, involuntary shaking, tremors",
        "knuckle_gripping": "white knuckle grip, gripping sheets, clawing, holding on tight",
        "neck_straining": "neck muscles straining, head thrown back, exposed neck",
    }
    
    STATE = {
        "climax": "orgasm face, climax, release, eyes rolled back, mouth open",
        "edge": "edging, holding back, desperate, frustrated arousal",
        "exhaustion": "limp body, collapsed, rubber legs, heavy breathing",
        "overstimulation": "overstimulated, sensitive, twitching, too much",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "reflex": (list(cls.REFLEX.keys()),),
                "state": (list(cls.STATE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Extreme NSFW"

    def generate(self, prompt, reflex, state):
        r = self.REFLEX.get(reflex, "")
        s = self.STATE.get(state, "")
        
        positive = f"{prompt}, {r}, {s}"
        negative = "bored, stiff, motionless"
        
        return (positive, negative)

class AftermathPro:
    """Detailed Post-Act Scenarios"""
    
    CONDITION = {
        "creampie_leak": "leaking creampie, overflow, dripping down thighs, mess",
        "sweat_drenched": "hair matted with sweat, shiny skin, bodies stuck together",
        "makeup_ruined": "ruined makeup, mascara running, smeared lipstick, messy face",
        "red_marks": "red hand prints, slap marks, friction burns, marking",
        "sleepy_cuddle": "aftercare, cuddling, spooning, sleeping, satisfied",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "condition": (list(cls.CONDITION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("aftermath_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Extreme NSFW"

    def generate(self, prompt, condition):
        c = self.CONDITION.get(condition, "")
        return (f"{prompt}, {c}",)

class InternalSensationPro:
    """Visualizing Internal Sensations"""
    
    SENSATION = {
        "stuffed": "stuffed belly, belly bulge, full belly, stretched stomach",
        "deep_impact": "cervix penetration, barely deep, too deep, wincing",
        "filling": "filling up, internal pressure, inflated",
        "pulsating": "throbbing, pulsating, milking, squeezing",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "sensation": (list(cls.SENSATION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("sensation_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/Extreme NSFW"

    def generate(self, prompt, sensation):
        s = self.SENSATION.get(sensation, "")
        return (f"{prompt}, {s}",)

NODE_CLASS_MAPPINGS = {
    "ExtremeFluidDynamics": ExtremeFluidDynamics,
    "AnatomicalDetailMax": AnatomicalDetailMax,
    "EnvironmentArousal": EnvironmentArousal,
    "IntensityDriver": IntensityDriver,
    "PhysiologicalReactionMax": PhysiologicalReactionMax,
    "AftermathPro": AftermathPro,
    "InternalSensationPro": InternalSensationPro,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExtremeFluidDynamics": "🌊 Extreme Fluid Dynamics",
    "AnatomicalDetailMax": "🍑 Anatomical Detail Max",
    "EnvironmentArousal": "🛏️ Environment Arousal",
    "IntensityDriver": "⚡ Intensity Driver",
    "PhysiologicalReactionMax": "🥵 Physiological Reaction Max",
    "AftermathPro": "🏁 Aftermath Pro",
    "InternalSensationPro": "🧘 Internal Sensation Pro",
}
