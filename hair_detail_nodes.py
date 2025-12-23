"""
Mason's Hair Detail Nodes for ComfyUI
Replace hair LoRAs with prompt engineering - SD 1.5 optimized
"""


class HairTextureController:
    """Control hair texture and quality"""
    
    TEXTURES = {
        "silky": "silky hair, smooth hair, glossy strands, healthy shine, salon-quality",
        "sleek": "sleek hair, straight and smooth, polished look, no flyaways",
        "soft": "soft hair, touchable hair, gentle texture, flowing",
        "coarse": "coarse hair, thick strands, textured hair, strong hair",
        "frizzy": "frizzy hair, textured frizz, wild hair, untamed",
        "curly_defined": "defined curls, springy curls, bouncy ringlets",
        "wavy_loose": "loose waves, beachy waves, relaxed waves",
        "natural": "natural hair texture, authentic hair, realistic strands",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "texture": (list(cls.TEXTURES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("hair_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Hair Detail"

    def apply(self, prompt, texture):
        tex = self.TEXTURES.get(texture, "")
        return (f"{prompt}, {tex}",)


class HairVolumeController:
    """Control hair volume and body"""
    
    VOLUMES = {
        "flat": "flat hair, limp hair, no volume, straight down",
        "natural": "natural volume, normal body, healthy fullness",
        "voluminous": "voluminous hair, full body, bouncy, lifted roots",
        "big_hair": "big hair, huge volume, dramatic fullness, statement hair",
        "teased": "teased hair, backcombed, retro volume, height at crown",
        "fluffy": "fluffy hair, soft volume, airy texture, cloud-like",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "volume": (list(cls.VOLUMES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("volume_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Hair Detail"

    def apply(self, prompt, volume):
        vol = self.VOLUMES.get(volume, "")
        return (f"{prompt}, {vol}",)


class HairHighlightController:
    """Control hair highlights and color effects"""
    
    HIGHLIGHTS = {
        "none": "solid hair color, single tone, uniform color",
        "subtle": "subtle highlights, natural dimension, sun-kissed streaks",
        "balayage": "balayage highlights, hand-painted color, gradient effect",
        "chunky": "chunky highlights, bold streaks, visible contrast",
        "babylights": "babylights, fine delicate highlights, natural look",
        "lowlights": "lowlights, darker strands, added depth, dimension",
        "roots": "dark roots, grown out color, intentional roots showing",
    }
    
    SHINE = {
        "matte": "matte hair, non-shiny, natural finish",
        "natural": "natural hair shine, healthy sheen",
        "glossy": "glossy hair, high shine, reflective, mirror-like",
        "wet_look": "wet look hair, slicked, gelled appearance",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "highlights": (list(cls.HIGHLIGHTS.keys()),),
                "shine": (list(cls.SHINE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("highlight_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Hair Detail"

    def apply(self, prompt, highlights, shine):
        high = self.HIGHLIGHTS.get(highlights, "")
        sh = self.SHINE.get(shine, "")
        return (f"{prompt}, {high}, {sh}",)


class HairMovementController:
    """Control hair movement and flow"""
    
    MOVEMENTS = {
        "static": "static hair, still, no movement, perfectly placed",
        "slight": "slight hair movement, gentle sway, soft motion",
        "windblown": "windblown hair, wind in hair, flowing movement, dynamic",
        "wild": "wild hair movement, chaotic flow, dramatic wind effect",
        "floating": "floating hair, weightless, underwater-like movement",
        "swinging": "swinging hair, mid-motion, action shot, movement blur",
        "tousled": "tousled hair, messy movement, bedroom hair, disheveled",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "movement": (list(cls.MOVEMENTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("movement_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Hair Detail"

    def apply(self, prompt, movement):
        mov = self.MOVEMENTS.get(movement, "")
        return (f"{prompt}, {mov}",)


class BangsController:
    """Control bang styles in detail"""
    
    BANG_STYLES = {
        "none": "no bangs, forehead visible, hair swept back",
        "straight": "straight bangs, blunt cut bangs, full fringe",
        "side_swept": "side swept bangs, diagonal fringe, swept to side",
        "curtain": "curtain bangs, parted fringe, face-framing bangs",
        "wispy": "wispy bangs, thin delicate bangs, soft fringe",
        "choppy": "choppy bangs, textured bangs, modern fringe",
        "baby_bangs": "baby bangs, micro bangs, short fringe",
        "long_side": "long side bangs, eye-covering, sweeping fringe",
        "see_through": "see-through bangs, Korean style, thin transparent bangs",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "bang_style": (list(cls.BANG_STYLES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("bangs_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Hair Detail"

    def apply(self, prompt, bang_style):
        bangs = self.BANG_STYLES.get(bang_style, "")
        return (f"{prompt}, {bangs}",)


class HairAccessoryAdder:
    """Add hair accessories"""
    
    ACCESSORIES = {
        "none": "",
        "hairpin": "hairpin, decorative hair clip, hair accessory",
        "headband": "headband, hair band, head accessory",
        "ribbon": "ribbon in hair, hair ribbon, bow",
        "flowers": "flowers in hair, floral hair accessory, natural decoration",
        "tiara": "tiara, crown, princess headpiece, sparkling tiara",
        "clips": "hair clips, decorative clips, barrettes",
        "scrunchie": "scrunchie, fabric hair tie, retro accessory",
        "jeweled": "jeweled hair accessory, crystal hairpiece, sparkly",
        "feathers": "feathers in hair, feather accessory, bohemian",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "accessory": (list(cls.ACCESSORIES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("accessory_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Hair Detail"

    def apply(self, prompt, accessory):
        acc = self.ACCESSORIES.get(accessory, "")
        if acc:
            return (f"{prompt}, {acc}",)
        return (prompt,)


NODE_CLASS_MAPPINGS = {
    "HairTextureController": HairTextureController,
    "HairVolumeController": HairVolumeController,
    "HairHighlightController": HairHighlightController,
    "HairMovementController": HairMovementController,
    "BangsController": BangsController,
    "HairAccessoryAdder": HairAccessoryAdder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HairTextureController": "💇 Hair Texture Controller",
    "HairVolumeController": "💨 Hair Volume Controller",
    "HairHighlightController": "✨ Hair Highlight Controller",
    "HairMovementController": "🌬️ Hair Movement Controller",
    "BangsController": "✂️ Bangs Controller",
    "HairAccessoryAdder": "🎀 Hair Accessory Adder",
}
