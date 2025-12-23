"""
Mason's Accessory & Detail Nodes for ComfyUI  
Often overlooked details that make images more realistic - SD 1.5 optimized
"""


class JewelryController:
    """Control jewelry beyond earrings"""
    
    NECKLACES = {
        "none": "",
        "choker": "choker necklace, tight necklace, fitted around neck",
        "pendant": "pendant necklace, hanging charm, long chain",
        "pearl_strand": "pearl necklace, string of pearls, classic pearls",
        "chain": "chain necklace, gold chain, silver chain",
        "statement": "statement necklace, large decorative, bold jewelry",
        "layered": "layered necklaces, multiple chains, stacked necklaces",
    }
    
    RINGS = {
        "none": "",
        "engagement": "engagement ring, diamond ring, sparkling gem",
        "wedding_band": "wedding band, simple band, married",
        "fashion": "fashion ring, decorative ring, statement ring",
        "multiple": "multiple rings, stacked rings, rings on several fingers",
    }
    
    BRACELETS = {
        "none": "",
        "bangle": "bangle bracelet, rigid bracelet, wrist bangle",
        "chain": "chain bracelet, delicate chain, wrist chain",
        "cuff": "cuff bracelet, wide cuff, statement wrist",
        "beaded": "beaded bracelet, bead strand, bohemian bracelet",
        "watch": "luxury watch, wristwatch, elegant timepiece",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "necklace": (list(cls.NECKLACES.keys()),),
                "ring": (list(cls.RINGS.keys()),),
                "bracelet": (list(cls.BRACELETS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("jewelry_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Accessories"

    def apply(self, prompt, necklace, ring, bracelet):
        parts = [prompt]
        n = self.NECKLACES.get(necklace, "")
        r = self.RINGS.get(ring, "")
        b = self.BRACELETS.get(bracelet, "")
        if n: parts.append(n)
        if r: parts.append(r)
        if b: parts.append(b)
        return (", ".join(parts),)


class NailController:
    """Control nail/manicure appearance"""
    
    NAIL_LENGTH = {
        "short": "short nails, natural length nails, trimmed nails",
        "medium": "medium length nails, moderate nail length",
        "long": "long nails, extended nails, lengthy nails",
        "very_long": "very long nails, stiletto length, extreme length",
    }
    
    NAIL_SHAPE = {
        "natural": "natural nail shape, rounded tips",
        "square": "square nails, flat tips, squared off",
        "almond": "almond shaped nails, tapered, elegant shape",
        "stiletto": "stiletto nails, pointed tips, sharp nails",
        "coffin": "coffin nails, ballerina shape, tapered square",
    }
    
    NAIL_STYLE = {
        "bare": "bare nails, no polish, natural nails",
        "clear": "clear nail polish, shiny natural, glossy",
        "french": "french manicure, white tips, classic french",
        "red": "red nail polish, classic red nails, bold red",
        "pink": "pink nail polish, soft pink nails, feminine",
        "dark": "dark nail polish, black nails, deep color",
        "glitter": "glitter nails, sparkly polish, shimmering nails",
        "art": "nail art, decorated nails, intricate nail design",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "length": (list(cls.NAIL_LENGTH.keys()),),
                "shape": (list(cls.NAIL_SHAPE.keys()),),
                "style": (list(cls.NAIL_STYLE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("nail_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Accessories"

    def apply(self, prompt, length, shape, style):
        l = self.NAIL_LENGTH.get(length, "")
        sh = self.NAIL_SHAPE.get(shape, "")
        st = self.NAIL_STYLE.get(style, "")
        return (f"{prompt}, {l}, {sh}, {st}",)


class GlassesController:
    """Control eyewear"""
    
    GLASSES = {
        "none": "",
        "reading": "reading glasses, small frames, intellectual",
        "fashion": "fashion glasses, stylish frames, designer eyewear",
        "cat_eye": "cat eye glasses, retro frames, vintage style",
        "round": "round glasses, circular frames, hipster glasses",
        "aviator": "aviator glasses, pilot style, classic aviators",
        "oversized": "oversized glasses, large frames, statement eyewear",
        "rimless": "rimless glasses, frameless, subtle eyewear",
    }
    
    SUNGLASSES = {
        "none": "",
        "aviator": "aviator sunglasses, pilot shades, mirrored lenses",
        "wayfarer": "wayfarer sunglasses, classic shape, ray-ban style",
        "cat_eye": "cat eye sunglasses, retro shades, feminine",
        "oversized": "oversized sunglasses, large shades, celebrity style",
        "sport": "sport sunglasses, athletic shades, wraparound",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "glasses": (list(cls.GLASSES.keys()),),
                "sunglasses": (list(cls.SUNGLASSES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("glasses_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Accessories"

    def apply(self, prompt, glasses, sunglasses):
        g = self.GLASSES.get(glasses, "")
        s = self.SUNGLASSES.get(sunglasses, "")
        parts = [prompt]
        if g: parts.append(g)
        if s: parts.append(s)
        return (", ".join(parts),)


class HeadwearController:
    """Control hats and headwear"""
    
    HEADWEAR = {
        "none": "",
        "baseball_cap": "baseball cap, sports cap, casual hat",
        "beanie": "beanie, knit cap, winter hat",
        "sun_hat": "sun hat, wide brim hat, summer hat",
        "fedora": "fedora hat, classic fedora, stylish hat",
        "beret": "beret, french beret, artistic hat",
        "headband": "headband, hair band, sporty headband",
        "bandana": "bandana, head wrap, tied bandana",
        "crown": "crown, tiara, royal headpiece",
        "flower_crown": "flower crown, floral headpiece, bohemian crown",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "headwear": (list(cls.HEADWEAR.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("headwear_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Accessories"

    def apply(self, prompt, headwear):
        h = self.HEADWEAR.get(headwear, "")
        if h:
            return (f"{prompt}, {h}",)
        return (prompt,)


class BodyPiercingController:
    """Control body piercings"""
    
    PIERCINGS = {
        "none": "",
        "nose_stud": "nose stud, small nose piercing, nostril piercing",
        "nose_ring": "nose ring, hoop nose piercing, septum ring",
        "lip": "lip piercing, lip ring, labret piercing",
        "eyebrow": "eyebrow piercing, brow ring",
        "tongue": "tongue piercing, tongue stud",
        "navel": "navel piercing, belly button ring, belly piercing",
        "nipple": "nipple piercings, nipple rings",
        "multiple_ear": "multiple ear piercings, many earrings, decorated ears",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "piercing": (list(cls.PIERCINGS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("piercing_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Accessories"

    def apply(self, prompt, piercing):
        p = self.PIERCINGS.get(piercing, "")
        if p:
            return (f"{prompt}, {p}",)
        return (prompt,)


class HandFootFixer:
    """Specialized fixer for hands and feet - the most problematic areas"""
    
    HAND_FIXES = {
        "basic": (
            "anatomically correct hands, proper hand anatomy, "
            "five fingers per hand, correct finger count"
        ),
        "detailed": (
            "anatomically correct hands, proper hand anatomy, "
            "five fingers per hand, correct finger count, "
            "detailed hands, realistic hands, natural hand pose, "
            "proper thumb placement, correct finger proportions"
        ),
        "hidden": (
            "hands hidden, hands not visible, hands behind back, "
            "hands out of frame, no hands shown"
        ),
    }
    
    FOOT_FIXES = {
        "basic": "anatomically correct feet, proper foot anatomy, five toes",
        "detailed": (
            "anatomically correct feet, proper foot anatomy, "
            "five toes per foot, realistic feet, natural toe proportions, "
            "detailed feet, correct foot shape"
        ),
        "hidden": "feet not visible, feet out of frame, feet hidden",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "hand_fix": (list(cls.HAND_FIXES.keys()),),
                "foot_fix": (list(cls.FOOT_FIXES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "fix"
    CATEGORY = "Mason's Nodes/Accessories"

    def fix(self, prompt, hand_fix, foot_fix):
        h = self.HAND_FIXES.get(hand_fix, "")
        f = self.FOOT_FIXES.get(foot_fix, "")
        
        pos = f"{prompt}, {h}, {f}"
        
        neg = (
            "bad hands, wrong hands, deformed hands, mutated hands, "
            "extra fingers, missing fingers, fused fingers, too many fingers, "
            "bad feet, wrong feet, deformed feet, extra toes, missing toes"
        )
        
        return (pos, neg)


NODE_CLASS_MAPPINGS = {
    "JewelryController": JewelryController,
    "NailController": NailController,
    "GlassesController": GlassesController,
    "HeadwearController": HeadwearController,
    "BodyPiercingController": BodyPiercingController,
    "HandFootFixer": HandFootFixer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JewelryController": "💍 Jewelry Controller",
    "NailController": "💅 Nail Controller",
    "GlassesController": "👓 Glasses Controller",
    "HeadwearController": "🎩 Headwear Controller",
    "BodyPiercingController": "📍 Body Piercing",
    "HandFootFixer": "🤚 Hand/Foot Fixer",
}
