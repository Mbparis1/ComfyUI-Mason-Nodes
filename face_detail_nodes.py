"""
Mason's Face Detail Nodes for ComfyUI
Replace face LoRAs with prompt engineering - SD 1.5 optimized
"""


class FacialStructureController:
    """Control facial bone structure"""
    
    CHEEKBONES = {
        "flat": "flat cheekbones, soft facial structure, round face",
        "subtle": "subtle cheekbones, gentle definition",
        "defined": "defined cheekbones, visible bone structure, sculpted",
        "high": "high cheekbones, prominent cheekbones, model features",
        "extreme": "extremely high cheekbones, sharp bone structure, striking",
    }
    
    JAW = {
        "soft": "soft jawline, rounded jaw, gentle chin",
        "natural": "natural jawline, normal jaw definition",
        "defined": "defined jawline, clear jaw angle, strong jaw",
        "angular": "angular jawline, sharp jaw, chiseled",
        "square": "square jaw, strong square jawline",
    }
    
    CHIN = {
        "round": "round chin, soft chin, curved",
        "pointed": "pointed chin, v-shaped, delicate",
        "square": "square chin, strong chin, defined",
        "cleft": "cleft chin, dimpled chin, chin cleft",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "cheekbones": (list(cls.CHEEKBONES.keys()),),
                "jaw": (list(cls.JAW.keys()),),
                "chin": (list(cls.CHIN.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("face_structure_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Face Detail"

    def apply(self, prompt, cheekbones, jaw, chin):
        ch = self.CHEEKBONES.get(cheekbones, "")
        j = self.JAW.get(jaw, "")
        c = self.CHIN.get(chin, "")
        return (f"{prompt}, {ch}, {j}, {c}",)


class NoseController:
    """Control nose shape and size"""
    
    SHAPES = {
        "button": "button nose, small cute nose, petite nose",
        "upturned": "upturned nose, turned up nose, celestial nose",
        "straight": "straight nose, Greek nose, refined bridge",
        "roman": "Roman nose, aquiline nose, prominent bridge",
        "snub": "snub nose, short nose, turned up tip",
        "wide": "wide nose, broad nose, wide nostrils",
        "narrow": "narrow nose, thin nose, slender bridge",
    }
    
    SIZE = {
        "small": "small nose, petite nose",
        "medium": "medium nose, proportional nose",
        "large": "large nose, prominent nose",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "shape": (list(cls.SHAPES.keys()),),
                "size": (list(cls.SIZE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("nose_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Face Detail"

    def apply(self, prompt, shape, size):
        sh = self.SHAPES.get(shape, "")
        sz = self.SIZE.get(size, "")
        return (f"{prompt}, {sh}, {sz}",)


class LipShapeController:
    """Control lip shape in detail"""
    
    SHAPES = {
        "thin": "thin lips, narrow lips, delicate mouth",
        "medium": "medium lips, balanced lips, natural fullness",
        "full": "full lips, plump lips, lush lips",
        "very_full": "very full lips, pillowy lips, extremely plump",
        "heart": "heart-shaped lips, defined cupid's bow, romantic lips",
        "wide": "wide lips, broad smile, generous mouth",
    }
    
    CUPIDS_BOW = {
        "subtle": "subtle cupid's bow, gentle lip peaks",
        "defined": "defined cupid's bow, clear lip peaks, classic shape",
        "sharp": "sharp cupid's bow, dramatic peaks, striking lips",
        "rounded": "rounded cupid's bow, soft peak, smooth curve",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "shape": (list(cls.SHAPES.keys()),),
                "cupids_bow": (list(cls.CUPIDS_BOW.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lip_shape_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Face Detail"

    def apply(self, prompt, shape, cupids_bow):
        sh = self.SHAPES.get(shape, "")
        cb = self.CUPIDS_BOW.get(cupids_bow, "")
        return (f"{prompt}, {sh}, {cb}",)


class EyeShapeController:
    """Control eye shape in detail"""
    
    SHAPES = {
        "almond": "almond eyes, almond-shaped eyes, classic eye shape",
        "round": "round eyes, wide eyes, doe eyes, innocent look",
        "hooded": "hooded eyes, heavy lid, mysterious look",
        "upturned": "upturned eyes, cat eyes, lifted outer corner",
        "downturned": "downturned eyes, droopy eyes, sad look",
        "monolid": "monolid eyes, single eyelid, Asian eye shape",
        "deep_set": "deep-set eyes, sunken eyes, intense gaze",
        "protruding": "protruding eyes, prominent eyes, prominent eye",
    }
    
    SIZE = {
        "small": "small eyes, petite eyes",
        "medium": "medium eyes, proportional eyes",
        "large": "large eyes, big eyes, prominent eyes",
        "very_large": "very large eyes, huge eyes, anime-like",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "shape": (list(cls.SHAPES.keys()),),
                "size": (list(cls.SIZE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("eye_shape_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Face Detail"

    def apply(self, prompt, shape, size):
        sh = self.SHAPES.get(shape, "")
        sz = self.SIZE.get(size, "")
        return (f"{prompt}, {sh}, {sz}",)


class EyebrowShapeController:
    """Control eyebrow shape and style"""
    
    SHAPES = {
        "natural": "natural eyebrows, ungroomed brows, authentic shape",
        "arched": "arched eyebrows, high arch, dramatic brows",
        "straight": "straight eyebrows, horizontal brows, Korean style",
        "curved": "curved eyebrows, soft arch, gentle curve",
        "angular": "angular eyebrows, sharp angle, defined peak",
        "rounded": "rounded eyebrows, soft rounded shape",
        "s_shaped": "s-shaped eyebrows, wavy brows, unique shape",
    }
    
    THICKNESS = {
        "thin": "thin eyebrows, pencil brows, refined",
        "medium": "medium eyebrows, balanced thickness",
        "thick": "thick eyebrows, bold brows, full brows",
        "bushy": "bushy eyebrows, natural thick, untamed brows",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "shape": (list(cls.SHAPES.keys()),),
                "thickness": (list(cls.THICKNESS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("eyebrow_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Face Detail"

    def apply(self, prompt, shape, thickness):
        sh = self.SHAPES.get(shape, "")
        th = self.THICKNESS.get(thickness, "")
        return (f"{prompt}, {sh}, {th}",)


class EarController:
    """Control ear appearance and accessories"""
    
    VISIBILITY = {
        "hidden": "ears hidden, hair covering ears",
        "partially_visible": "ears partially visible, hair tucked behind",
        "visible": "ears visible, ears showing, exposed ears",
    }
    
    EARRINGS = {
        "none": "",
        "studs": "stud earrings, small earrings, simple studs",
        "hoops": "hoop earrings, circular earrings, hoops",
        "dangles": "dangle earrings, drop earrings, hanging earrings",
        "chandelier": "chandelier earrings, elaborate earrings, statement earrings",
        "ear_cuff": "ear cuff, ear jewelry, cuff earring",
        "multiple": "multiple ear piercings, several earrings",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "visibility": (list(cls.VISIBILITY.keys()),),
                "earrings": (list(cls.EARRINGS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ear_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Face Detail"

    def apply(self, prompt, visibility, earrings):
        vis = self.VISIBILITY.get(visibility, "")
        ear = self.EARRINGS.get(earrings, "")
        if ear:
            return (f"{prompt}, {vis}, {ear}",)
        return (f"{prompt}, {vis}",)


class DimpleController:
    """Control dimple appearance"""
    
    DIMPLES = {
        "none": "no dimples, smooth cheeks",
        "cheek_subtle": "subtle cheek dimples, faint dimples when smiling",
        "cheek_visible": "visible cheek dimples, cute dimples, dimpled smile",
        "deep_cheek": "deep cheek dimples, prominent dimples, distinctive",
        "chin": "chin dimple, cleft chin, dimpled chin",
        "both": "cheek and chin dimples, multiple dimples, very cute",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "dimple_type": (list(cls.DIMPLES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("dimple_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Face Detail"

    def apply(self, prompt, dimple_type):
        dim = self.DIMPLES.get(dimple_type, "")
        return (f"{prompt}, {dim}",)


NODE_CLASS_MAPPINGS = {
    "FacialStructureController": FacialStructureController,
    "NoseController": NoseController,
    "LipShapeController": LipShapeController,
    "EyeShapeController": EyeShapeController,
    "EyebrowShapeController": EyebrowShapeController,
    "EarController": EarController,
    "DimpleController": DimpleController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FacialStructureController": "🦴 Facial Structure",
    "NoseController": "👃 Nose Controller",
    "LipShapeController": "👄 Lip Shape Controller",
    "EyeShapeController": "👁️ Eye Shape Controller",
    "EyebrowShapeController": "🤨 Eyebrow Shape",
    "EarController": "👂 Ear Controller",
    "DimpleController": "😊 Dimple Controller",
}
