"""
Mason's NSFW LoRA Emulator Nodes for ComfyUI
Specialized LoRA replacements for NSFW content - SD 1.5 optimized
"""

class NSFWBodyPartsLoRA:
    """Emulates detailed body part LoRAs (Breasts/Butt) with shape control"""
    
    BREAST_SHAPES = {
        "natural": "natural breasts, natural shape, anatomical",
        "round": "round breasts, perfect globes, fake boobs, implants",
        "perky": "perky breasts, gravity defying, uplifted",
        "heavy": "heavy breasts, sagging naturally, large aerola",
        "teardrop": "teardrop shaped breasts, natural hang",
        "huge": "huge breasts, gigantic tits, hyper breasts",
    }
    
    BUTT_SHAPES = {
        "heart": "heart shaped ass, heart shaped butt, wide hips",
        "bubble": "bubble butt, round ass, perky butt",
        "plump": "plump ass, thick ass, big booty, fat ass",
        "athletic": "athletic toned butt, firm ass, muscular glutes",
        "wide": "wide hips, huge ass, dump truck ass",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "breast_shape": (list(cls.BREAST_SHAPES.keys()),),
                "breast_size": (["small", "medium", "large", "huge", "gigantic", "hyper"],),
                "butt_shape": (list(cls.BUTT_SHAPES.keys()),),
                "butt_size": (["small", "medium", "large", "huge", "gigantic"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/NSFW LoRA Emulators"

    def emulate(self, prompt, breast_shape, breast_size, butt_shape, butt_size):
        bs = self.BREAST_SHAPES.get(breast_shape, "")
        bts = self.BUTT_SHAPES.get(butt_shape, "")
        
        parts = []
        if prompt: parts.append(prompt)
        
        # Breasts
        parts.append(f"{breast_size} breasts")
        parts.append(bs)
        
        # Butt
        parts.append(f"{butt_size} butt")
        parts.append(bts)
        
        positive = ", ".join(parts)
        negative = "bad anatomy, asymmetrical breasts, deformed nipples, missing nipples, flat ass, flat chest"
        
        return (positive, negative)


class NSFWSkinTextureLoRA:
    """Emulates skin texture, sweat, oil, and veins LoRAs"""
    
    SKIN_CONDITION = {
        "oily": "oily skin, shiny skin, glistening skin, wet skin",
        "sweaty": "sweaty skin, perspiration, sweat drops, glistening sweat",
        "drenched": "drenched in sweat, heavy sweating, soaking wet skin",
        "veiny": "veiny skin, visible veins, translucent skin, pale skin with veins",
        "flushed": "flushed skin, red skin, blushing, aroused skin tone",
        "detailed": "highly detailed skin texture, pores, skin grain",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "skin_texture": (list(cls.SKIN_CONDITION.keys()),),
                "intensity": (["subtle", "moderate", "intense", "extreme"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/NSFW LoRA Emulators"

    def emulate(self, prompt, skin_texture, intensity):
        tex = self.SKIN_CONDITION.get(skin_texture, "")
        
        mod = ""
        if intensity == "subtle": mod = "slightly"
        elif intensity == "intense": mod = "very"
        elif intensity == "extreme": mod = "extremely, hyper"
        
        positive = f"{prompt}, {mod} {tex}"
        negative = "plastic skin, smooth skin, dry skin, matte skin"
        
        return (positive, negative)


class NSFWArousalLoRA:
    """Emulates arousal expressions and bodily signs LoRAs"""
    
    EXPRESSIONS = {
        "ahegao": "ahegao face, tongue out, eyes rolled back, crossed eyes, drooling",
        "orgasm": "orgasm face, pleasure face, screaming in pleasure, ecstatic expression",
        "biting_lip": "biting lip, sultry expression, biting lower lip",
        "halying": "heavy breathing, panting, mouth open, sweat on face",
        "lewd_smile": "lewd smile, naughty smile, seductive smile, smirk",
        "glazed_eyes": "glazed eyes, heart pupils, dilated pupils, lustful gaze",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "expression": (list(cls.EXPRESSIONS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/NSFW LoRA Emulators"

    def emulate(self, prompt, expression):
        exp = self.EXPRESSIONS.get(expression, "")
        positive = f"{prompt}, {exp}"
        negative = "bored, neutral expression, calm, asleep"
        return (positive, negative)


class NSFWFluidsLoRA:
    """Emulates bodily fluids (cum, squirt, etc.) LoRAs"""
    
    FLUID_TYPE = {
        "cum_facial": "cum on face, cumshot, facial, semen on face, bukake",
        "cum_body": "cum on body, cum on breasts, cum on stomach, covered in cum",
        "cum_mouth": "cum in mouth, swallowing cum, leaking cum",
        "creampie": "creampie, leaking pussy, cum dripping, overflowing",
        "squirting": "squirting, gushing fluids, wet pussy, soaking wet",
        "drool": "drooling, saliva string, spit",
    }
    
    AMOUNT = {
        "little": "little bit, small amount",
        "moderate": "moderate amount",
        "lot": "lots of, excessive amount, covered in",
        "extreme": "extreme amount, buckets of, mess",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "fluid_type": (list(cls.FLUID_TYPE.keys()),),
                "amount": (list(cls.AMOUNT.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/NSFW LoRA Emulators"

    def emulate(self, prompt, fluid_type, amount):
        ft = self.FLUID_TYPE.get(fluid_type, "")
        amt = self.AMOUNT.get(amount, "")
        
        positive = f"{prompt}, {amt} {ft}, realistic fluids, thick fluids"
        negative = "dry, clean, no mess"
        return (positive, negative)


class NSFWPosesLoRA:
    """Emulates Sex Position LoRAs"""
    
    POSITIONS = {
        "doggy_style": (
            "doggystyle, from behind, on all fours, arching back, "
            "looking back, ass up"
        ),
        "missionary": (
            "missionary position, lying on back, legs spread, "
            "looking up, intimate"
        ),
        "cowgirl": (
            "cowgirl position, straddling, sitting on top, "
            "bouncing, riding"
        ),
        "reverse_cowgirl": (
            "reverse cowgirl, riding reverse, back to camera, "
            "looking back"
        ),
        "standing": (
            "standing sex, pinned against wall, leg lifted, "
            "carrying, bending over"
        ),
        "anal_focus": (
            "anal sex, gaping, spreading cheeks, "
            "view from behind, intricate detail"
        ),
        "fellatio": (
            "blowjob, giving head, sucking dick, deepthroat, "
            "looking up, eye contact"
        ),
        "cunnilingus": (
            "cunnilingus, eating pussy, licking, "
            "legs spread wide, receiving oral"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "position": (list(cls.POSITIONS.keys()),),
                "view": (["default", "from_behind", "from_front", "from_side", "from_above", "from_below", "pov"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/NSFW LoRA Emulators"

    def emulate(self, prompt, position, view):
        pos = self.POSITIONS.get(position, "")
        
        view_prompt = ""
        if view != "default":
            view_prompt = f"{view.replace('_', ' ')} view"
            
        positive = f"{prompt}, {pos}, {view_prompt}, nsfw, hard core"
        negative = "bad anatomy, impossible pose, floating limbs, censored, mosaic"
        return (positive, negative)


class NSFWFetishWearLoRA:
    """Emulates Fetish Clothing LoRAs"""
    
    OUTFIT = {
        "latex_catsuit": "latex catsuit, shiny latex, tight latex, fetish wear",
        "fishnets": "fishnet stockings, fishnet bodystocking, ripped fishnets",
        "shibari": "shibari rope, rope bondage, kinbaku, tied up, intricate knots",
        "micro_bikini": "micro bikini, sling bikini, dental floss bikini, barely covered",
        "harness": "leather harness, body harness, strapped",
        "latex_nurse": "latex nurse outfit, fetish nurse, medical fetish",
        "maid": "french maid outfit, latex maid, sexy maid apron",
        "sheer_lingerie": "sheer lingerie, see-through, transparent, lace",
    }
    
    STATE = {
        "worn_perfect": "perfectly worn, fitted",
        "torn": "torn clothes, ripped fabric, damaged",
        "undressing": "undressing, peeling off, half removed",
        "falling_off": "falling off, wardrobe malfunction, accidentally exposure",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "outfit": (list(cls.OUTFIT.keys()),),
                "state": (list(cls.STATE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/NSFW LoRA Emulators"

    def emulate(self, prompt, outfit, state):
        out = self.OUTFIT.get(outfit, "")
        st = self.STATE.get(state, "")
        
        positive = f"{prompt}, {out}, {st}, fetish esthetic"
        negative = "casual clothes, loose clothes, modest"
        return (positive, negative)


NODE_CLASS_MAPPINGS = {
    "NSFWBodyPartsLoRA": NSFWBodyPartsLoRA,
    "NSFWSkinTextureLoRA": NSFWSkinTextureLoRA,
    "NSFWArousalLoRA": NSFWArousalLoRA,
    "NSFWFluidsLoRA": NSFWFluidsLoRA,
    "NSFWPosesLoRA": NSFWPosesLoRA,
    "NSFWFetishWearLoRA": NSFWFetishWearLoRA,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NSFWBodyPartsLoRA": "🍒 NSFW Body Parts (LoRA Emulator)",
    "NSFWSkinTextureLoRA": "💦 NSFW Skin/Sweat (LoRA Emulator)",
    "NSFWArousalLoRA": "🥵 NSFW Arousal/Face (LoRA Emulator)",
    "NSFWFluidsLoRA": "🧴 NSFW Fluids (LoRA Emulator)",
    "NSFWPosesLoRA": "🧘 NSFW Poses (LoRA Emulator)",
    "NSFWFetishWearLoRA": "⛓️ NSFW Fetish Wear (LoRA Emulator)",
}
