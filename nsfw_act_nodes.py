"""
Mason's Advanced NSFW Act Nodes for ComfyUI
Specific and accurate sexual act controllers - SD 1.5 optimized
"""

class OralActPro:
    """Detailed control over oral sexual acts"""
    
    ACT_TYPE = {
        "blowjob": "blowjob, sucking dick, fellatio, cheek bulge, bobbing head",
        "deepthroat": "deepthroat, deep throat, gagging, choking, extreme deepthroat",
        "facefucking": "facefucking, rough oral, grabbing head, forcing head down",
        "cunnilingus": "cunnilingus, eating pussy, licking pussy, tongue fucking",
        "facesitting": "facesitting, sitting on face, smothering, ass on face",
        "rimming": "rimming, anilingus, licking ass, tongue in ass",
        "69_position": "69 position, mutual oral, simultaneous oral",
        "spit_roast_oral": "spitroast oral, double suck, two dicks",
    }
    
    INTENSITY = {
        "gentle": "gentle, sensual, slow, kissing",
        "enthusiastic": "enthusiastic, eager, messy, slobber",
        "rough": "rough, aggressive, forceful, intense",
        "deep": "balls deep, throat fucking, pushing limits",
    }
    
    CUM_PLACEMENT = {
        "none": "",
        "in_mouth": "cum in mouth, swallowing cum, mouth full of cum",
        "on_face": "cum on face, facial, cumshot, splattered",
        "on_tongue": "cum on tongue, showing cum, tongue out",
        "dripping": "cum dripping from mouth, messy face, leaking",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "act_type": (list(cls.ACT_TYPE.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
                "cum_placement": (list(cls.CUM_PLACEMENT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Acts"

    def generate(self, prompt, act_type, intensity, cum_placement):
        act = self.ACT_TYPE.get(act_type, "")
        inten = self.INTENSITY.get(intensity, "")
        cum = self.CUM_PLACEMENT.get(cum_placement, "")
        
        parts = [prompt, act, inten]
        if cum: parts.append(cum)
        
        positive = ", ".join([p for p in parts if p])
        negative = "bad anatomy, floating limbs, censored, mosaic, bar censor"
        
        return (positive, negative)


class PenetrationPro:
    """Detailed control over penetrative acts (Vaginal/Anal)"""
    
    POSITION = {
        "missionary": "missionary position, lying on back, legs spread, looking up, intimate sex",
        "doggy_style": "doggystyle, from behind, on all fours, arching back, ass up",
        "cowgirl": "cowgirl position, straddling, sitting on top, riding dick, bouncing",
        "reverse_cowgirl": "reverse cowgirl, riding reverse, back to camera, ass focus",
        "mating_press": "mating press, legs pinned back, legs over shoulders, deep penetration",
        "prone_bone": "prone bone, lying on stomach, flat on bed, fucking from behind",
        "spooning": "spooning sex, lying on side, intimate, romantic sex",
        "standing": "standing sex, pinned against wall, leg lifted, carrying sex",
        "piledriver": "piledriver position, legs straight up, deep fucking",
        "anal": "anal sex, anal penetration, ass fucking, sodomy",
    }
    
    DEPTH = {
        "insertion": "insertion, just the tip, penetrating",
        "shallow": "shallow penetration, teasing",
        "deep": "balls deep, fully inserted, burying hips",
        "stretching": "stretching, gaping, too big",
    }
    
    VIEW = {
        "side_view": "side view, profile view, cross section",
        "top_down": "top down view, looking down",
        "bottom_up": "bottom up view, worms eye view",
        "pov": "pov, point of view, looking down at body",
        "close_up": "close up on genitals, insertion shot, genital focus",
        "internal": "internal view, x-ray, cross-section, inside body",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "position": (list(cls.POSITION.keys()),),
                "depth": (list(cls.DEPTH.keys()),),
                "view": (list(cls.VIEW.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Acts"

    def generate(self, prompt, position, depth, view):
        pos = self.POSITION.get(position, "")
        dep = self.DEPTH.get(depth, "")
        v = self.VIEW.get(view, "")
        
        positive = f"{prompt}, {pos}, {dep}, {v}, nsfw, hard core"
        negative = "bad anatomy, fused bodies, extra legs, extra arms"
        
        return (positive, negative)


class GroupActionPro:
    """Control over group acts and multiple partners"""
    
    ACT_TYPE = {
        "threesome_ffm": "threesome, 2girls 1boy, FFM, two women one man, spitroast",
        "threesome_mmf": "threesome, 1girl 2boys, MMF, double penetration, gangbang lite",
        "gangbang": "gangbang, 1girl many boys, multiple men, surrounded, bukake",
        "orgy": "orgy, group sex, multiple couples, chaos, many people",
        "spitroast": "spitroast, double penetration, mouth and pussy, mouth and ass",
        "double_penetration": "double penetration, dp, two dicks one hole, vaginal and anal",
        "bukkake": "bukkake, covered in cum, multiple facials, cum bath",
    }
    
    FOCUS = {
        "center_subject": "focus on girl, focus on center subject, men in background",
        "all_action": "wide shot, showing everyone, group action",
        "detail_insert": "close up on penetration, detail shot",
        "cum_mess": "aftermath, cum mess, exhausted, messy",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "act_type": (list(cls.ACT_TYPE.keys()),),
                "focus": (list(cls.FOCUS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Acts"

    def generate(self, prompt, act_type, focus):
        act = self.ACT_TYPE.get(act_type, "")
        foc = self.FOCUS.get(focus, "")
        
        positive = f"{prompt}, {act}, {foc}"
        negative = "bad anatomy, fused people, missing limbs, too many limbs"
        
        return (positive, negative)


class PaizuriPro:
    """Specialized controller for Breast/Tit acts"""
    
    ACT = {
        "paizuri": "paizuri, titjob, titty fuck, fucking breasts, breast sex",
        "breast_smother": "breast smother, buried in breasts, face in tits",
        "sandwich": "sandwiching, squeezing breasts together, cleavage fuck",
        "lactation": "lactation, lactating, leaking milk, breast milk",
        "nipple_play": "nipple play, pinching nipples, pulling nipples, hard nipples",
        "oil_massage": "oil massage, oily breasts, slick breasts, shiny",
    }
    
    VIEW = {
        "pov": "pov titjob, looking down at tits",
        "side": "side view titjob, profile breast",
        "under": "from below, underboob view",
        "close": "extreme closeup breasts, nipple focus",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "act": (list(cls.ACT.keys()),),
                "view": (list(cls.VIEW.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Acts"

    def generate(self, prompt, act, view):
        a = self.ACT.get(act, "")
        v = self.VIEW.get(view, "")
        return (f"{prompt}, {a}, {v}", "small breasts, flat chest")


class FootFetishPro:
    """Detailed Foot Fetish Controller"""
    
    ACT = {
        "footjob": "footjob, foot sex, rubbing feet on dick",
        "worship": "foot worship, licking feet, kissing feet, bowing to feet",
        "trampling": "trampling, standing on chest, stepping on face",
        "facesitting_feet": "feet on face, soles on face, smelling feet",
        "posing": "showing feet, soles focus, toes spread, arch display",
    }
    
    FOCUS = {
        "soles": "soles focus, wrinkled soles, soft soles",
        "toes": "toes focus, sucking toes, toe ring",
        "arches": "high arches, foot arch focus",
        "heels": "heels focus, smooth heels",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "act": (list(cls.ACT.keys()),),
                "focus": (list(cls.FOCUS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Acts"

    def generate(self, prompt, act, focus):
        a = self.ACT.get(act, "")
        f = self.FOCUS.get(focus, "")
        return (f"{prompt}, {a}, {f}", "bad feet, extra toes, missing toes, ugly feet")


class HandJobPro:
    """Handjob and Fingering Controller"""
    
    ACT = {
        "handjob": "handjob, giving a handjob, stroking dick, jerking off",
        "fingering": "fingering, rubbing clit, fingers in pussy, pussy play",
        "double_hand": "two handed handjob, double hand twist",
        "spit_lube": "spitting on hand, lubrication, saliva string",
    }
    
    GRIP = {
        "tight": "tight grip, squeezing hard",
        "gentle": "gentle touch, teasing, barely touching",
        "tip_focus": "rubbing tip, focusing on head, massaging glans",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "act": (list(cls.ACT.keys()),),
                "grip": (list(cls.GRIP.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "generate"
    CATEGORY = "Mason's Nodes/NSFW Acts"

    def generate(self, prompt, act, grip):
        a = self.ACT.get(act, "")
        g = self.GRIP.get(grip, "")
        return (f"{prompt}, {a}, {g}", "bad hands, missing fingers, extra fingers")


NODE_CLASS_MAPPINGS = {
    "OralActPro": OralActPro,
    "PenetrationPro": PenetrationPro,
    "GroupActionPro": GroupActionPro,
    "PaizuriPro": PaizuriPro,
    "FootFetishPro": FootFetishPro,
    "HandJobPro": HandJobPro,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OralActPro": "😮 Oral Act Pro",
    "PenetrationPro": "👉 Penetration Pro",
    "GroupActionPro": "👯‍♀️ Group Action Pro",
    "PaizuriPro": "🍈 Paizuri/Titjob Pro",
    "FootFetishPro": "🦶 Foot Fetish Pro",
    "HandJobPro": "✋ Handjob/Fingering Pro",
}
