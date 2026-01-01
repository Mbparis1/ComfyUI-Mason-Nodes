"""
Mason's Niche Fetish Nodes for ComfyUI
Specialized body part focus and clothing destruction - SD 1.5 optimized
"""


class FootFocusPro:
    """Specialized node for foot-focused content"""
    
    FOOT_TYPES = {
        "bare_natural": "bare feet, natural toes, clean feet, realistic feet",
        "painted_toes": "painted toenails, pedicured feet, glossy nail polish",
        "wet_feet": "wet feet, water droplets on toes, glistening feet",
        "dirty_feet": "dirty soles, dusty feet, natural wear",
        "stockinged": "feet in stockings, nylon-covered toes, sheer fabric on feet",
    }
    
    FOCUS_TYPES = {
        "soles": "focus on soles, wrinkled soles, arch of foot visible",
        "toes": "focus on toes, individual toes detailed, toe spread",
        "arches": "high arches, elegant foot shape, curved instep",
        "full_foot": "full foot visible, ankle to toes, complete foot view",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "foot_type": (list(cls.FOOT_TYPES.keys()),),
                "focus": (list(cls.FOCUS_TYPES.keys()),),
                "action": (["resting", "pointed", "flexed", "dangling", "footjob"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("foot_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Niche"

    def apply(self, prompt, foot_type, focus, action):
        parts = [prompt]
        parts.append(self.FOOT_TYPES.get(foot_type, ""))
        parts.append(self.FOCUS_TYPES.get(focus, ""))
        
        action_map = {
            "resting": "feet resting, relaxed position",
            "pointed": "pointed toes, ballet feet, elegant stretch",
            "flexed": "flexed feet, toes pulled back, stretched soles",
            "dangling": "feet dangling, shoes half off, teasing",
            "footjob": "feet wrapped around shaft, toes gripping, foot stimulation",
        }
        parts.append(action_map.get(action, ""))
        
        return (", ".join([p for p in parts if p]),)


class BodyPartWorship:
    """Specialized focus on specific body parts"""
    
    BODY_PARTS = {
        "armpit": "armpits exposed, arms raised, underarm visible, smooth armpits",
        "navel": "navel visible, belly button focus, toned stomach, midriff",
        "neck": "neck exposed, elegant neck, throat visible, collarbone",
        "back": "back exposed, spine visible, shoulder blades, bare back",
        "inner_thigh": "inner thighs visible, soft thigh skin, gap between thighs",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "body_part": (list(cls.BODY_PARTS.keys()),),
                "skin_detail": (["smooth", "glistening", "sweaty", "goosebumps"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("worship_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Niche"

    def apply(self, prompt, body_part, skin_detail):
        parts = [prompt]
        parts.append(self.BODY_PARTS.get(body_part, ""))
        
        skin_map = {
            "smooth": "smooth skin texture, flawless",
            "glistening": "glistening skin, light reflecting on skin",
            "sweaty": "sweaty skin, perspiration, moist skin",
            "goosebumps": "goosebumps on skin, raised texture, cold or aroused",
        }
        parts.append(skin_map.get(skin_detail, ""))
        
        return (", ".join([p for p in parts if p]),)


class ClothingDestruction:
    """Controls for torn, ripped, and removed clothing"""
    
    DESTRUCTION_LEVELS = {
        "intact": "",
        "disheveled": "disheveled clothing, messy attire, clothes askew",
        "partially_torn": "partially torn clothing, ripped fabric, exposed skin through tears",
        "heavily_torn": "heavily torn clothing, shredded fabric, barely covering",
        "stripped": "clothes being removed, undressing, clothing pulled off",
        "aftermath": "clothes on floor, discarded clothing nearby, just removed",
    }
    
    GARMENT_FOCUS = {
        "shirt": "torn shirt, ripped top, buttons popped",
        "pants": "torn pants, ripped jeans, fabric shredded at thighs",
        "dress": "torn dress, ripped gown, fabric falling away",
        "underwear": "torn underwear, ripped panties, destroyed lingerie",
        "stockings": "torn stockings, ripped nylons, runs in fabric",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "destruction_level": (list(cls.DESTRUCTION_LEVELS.keys()),),
                "garment": (list(cls.GARMENT_FOCUS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("destruction_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Niche"

    def apply(self, prompt, destruction_level, garment):
        parts = [prompt]
        if destruction_level != "intact":
            parts.append(self.DESTRUCTION_LEVELS.get(destruction_level, ""))
            parts.append(self.GARMENT_FOCUS.get(garment, ""))
        return (", ".join([p for p in parts if p]),)


class FetishMaterialMaster:
    """Specialized rendering for fetish materials"""
    
    MATERIAL = {
        "latex": "latex, latex clothing, high gloss rubber, tightness, reflective",
        "pvc": "pvc, vinyl outfit, plastic shine, synthetic fabric",
        "leather": "leather, black leather, textured leather, studded leather",
        "nylon": "nylon, sheer fabric, pantyhose, denier, silky",
        "spandex": "spandex, lycra, gym wear, shiny fabric, stretching",
    }
    
    QUALITY = {
        "matte": "matte finish, dull",
        "satin": "satin finish, soft sheeen",
        "glossy": "glossy, wet look, shiny",
        "mirror": "mirror polish, high reflection, chrome finish",
        "oiled": "oiled surface, slick, lubricant",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "material": (list(cls.MATERIAL.keys()),),
                "quality": (list(cls.QUALITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("material_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Niche"

    def apply(self, prompt, material, quality):
        m = self.MATERIAL.get(material, "")
        q = self.QUALITY.get(quality, "")
        return (f"{prompt}, {m}, {q}",)


class ArmpitFetishSpecialist:
    """Specific controls for armpit content"""
    
    POSE = {
        "arms_up": "arms raised high, exposing armpits, stretching arms",
        "behind_head": "hands behind head, elbows back, armpits open",
        "wiping_sweat": "wiping sweat from forehead, arm lifted",
        "presenting": "presenting armpit close to camera, close up",
    }
    
    DETAIL = {
        "smooth": "smooth armpits, shaved, clean skin",
        "stubble": "stubble, slight hair growth, shadow",
        "hairy": "natural armpit hair, hairy armpits, unshaven",
        "sweaty": "sweaty armpits, wet patch, glistening sweat",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "pose": (list(cls.POSE.keys()),),
                "detail": (list(cls.DETAIL.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("armpit_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Niche"

    def apply(self, prompt, pose, detail):
        p = self.POSE.get(pose, "")
        d = self.DETAIL.get(detail, "")
        return (f"{prompt}, {p}, {d}",)


NODE_CLASS_MAPPINGS = {
    "FootFocusPro": FootFocusPro,
    "BodyPartWorship": BodyPartWorship,
    "ClothingDestruction": ClothingDestruction,
    "FetishMaterialMaster": FetishMaterialMaster,
    "ArmpitFetishSpecialist": ArmpitFetishSpecialist,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FootFocusPro": "🦶 Foot Focus Pro",
    "BodyPartWorship": "💋 Body Part Worship",
    "ClothingDestruction": "👔 Clothing Destruction",
    "FetishMaterialMaster": "🖤 Fetish Material Master",
    "ArmpitFetishSpecialist": "💪 Armpit Specialist",
}
