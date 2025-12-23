"""
Mason's Outfit Descriptor Nodes for ComfyUI
Detailed clothing and fabric control - SD 1.5 optimized
"""

import random


class LingerieSelector:
    """Detailed lingerie types with materials"""
    
    LINGERIE_TYPES = {
        "lace_bra": "wearing lace bra, delicate lace cups, intricate lace pattern, feminine lingerie",
        "push_up_bra": "wearing push-up bra, enhanced cleavage, supportive cups, lifted bust",
        "bralette": "wearing bralette, soft bralette, unlined, natural shape, casual intimates",
        "corset": "wearing corset, laced corset, cinched waist, structured boning, vintage lingerie",
        "bustier": "wearing bustier, strapless support, structured bodice, glamour lingerie",
        "teddy": "wearing teddy, one-piece lingerie, bodysuit style, seamless design",
        "babydoll": "wearing babydoll lingerie, sheer overlay, flowing fabric, romantic style",
        "sports_bra": "wearing sports bra, athletic support, workout top, sporty style"
    }
    
    MATERIALS = {
        "silk": "silk material, smooth silk, luxurious silk, shiny silk fabric",
        "lace": "lace material, delicate lace, see-through lace, intricate lace pattern",
        "satin": "satin material, smooth satin, glossy satin, lustrous fabric",
        "cotton": "cotton material, soft cotton, comfortable cotton, breathable fabric",
        "mesh": "mesh material, sheer mesh, see-through mesh, transparent fabric",
        "velvet": "velvet material, soft velvet, luxurious velvet, rich texture"
    }
    
    COLORS = {
        "black": "black colored, classic black, dark black",
        "white": "white colored, pure white, crisp white",
        "red": "red colored, passionate red, deep red, crimson",
        "pink": "pink colored, soft pink, blush pink, feminine pink",
        "nude": "nude colored, skin tone, natural nude, flesh colored",
        "blue": "blue colored, navy blue, royal blue"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "lingerie_type": (list(cls.LINGERIE_TYPES.keys()),),
                "material": (list(cls.MATERIALS.keys()),),
                "color": (list(cls.COLORS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lingerie_prompt",)
    FUNCTION = "select"
    CATEGORY = "Mason's Nodes/Outfit"

    def select(self, prompt, lingerie_type, material, color):
        lingerie = self.LINGERIE_TYPES.get(lingerie_type, "")
        mat = self.MATERIALS.get(material, "")
        col = self.COLORS.get(color, "")
        return (f"{prompt}, {lingerie}, {mat}, {col}",)


class SwimwearSelector:
    """Bikini types, one-pieces, coverage levels"""
    
    SWIMWEAR_TYPES = {
        "string_bikini": "wearing string bikini, minimal coverage, tie sides, revealing swimwear",
        "triangle_bikini": "wearing triangle bikini, classic style, adjustable ties, standard coverage",
        "bandeau_bikini": "wearing bandeau bikini, strapless top, tube style, minimal straps",
        "high_waist_bikini": "wearing high-waisted bikini, retro style, vintage inspired, high-rise bottoms",
        "one_piece": "wearing one-piece swimsuit, full coverage, classic swimwear, connected top and bottom",
        "monokini": "wearing monokini, cutout swimsuit, revealing one-piece, connected design with cutouts",
        "thong_bikini": "wearing thong bikini, minimal back coverage, cheeky style, revealing bottom",
        "micro_bikini": "wearing micro bikini, extremely minimal coverage, tiny triangles, barely there"
    }
    
    PATTERNS = {
        "solid": "solid color, single color, no pattern",
        "tropical": "tropical print, palm leaves, exotic flowers, vacation pattern",
        "striped": "striped pattern, nautical stripes, classic stripes",
        "leopard": "leopard print, animal print, wild pattern",
        "floral": "floral pattern, flower print, feminine design"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "swimwear_type": (list(cls.SWIMWEAR_TYPES.keys()),),
                "pattern": (list(cls.PATTERNS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("swimwear_prompt",)
    FUNCTION = "select"
    CATEGORY = "Mason's Nodes/Outfit"

    def select(self, prompt, swimwear_type, pattern):
        swimwear = self.SWIMWEAR_TYPES.get(swimwear_type, "")
        pat = self.PATTERNS.get(pattern, "")
        return (f"{prompt}, {swimwear}, {pat}",)


class DressSelector:
    """Dress styles for various occasions"""
    
    DRESS_TYPES = {
        "cocktail_dress": "wearing cocktail dress, semi-formal dress, party dress, knee-length elegance",
        "evening_gown": "wearing evening gown, floor-length dress, formal gown, elegant full-length",
        "sundress": "wearing sundress, casual summer dress, light fabric, breezy style",
        "mini_dress": "wearing mini dress, short dress, above-knee hemline, flirty style",
        "bodycon": "wearing bodycon dress, tight-fitting dress, figure-hugging, form-fitting silhouette",
        "wrap_dress": "wearing wrap dress, crossover neckline, tied waist, flattering fit",
        "maxi_dress": "wearing maxi dress, ankle-length dress, flowing fabric, bohemian style",
        "slip_dress": "wearing slip dress, silky dress, minimalist, delicate straps, satin finish"
    }
    
    NECKLINES = {
        "v_neck": "v-neckline, plunging v, deep v-cut",
        "sweetheart": "sweetheart neckline, curved bust line, romantic neckline",
        "halter": "halter neckline, tied behind neck, bare shoulders",
        "off_shoulder": "off-shoulder neckline, bare shoulders, exposed collarbone",
        "strapless": "strapless, no straps, bare shoulders and arms",
        "high_neck": "high neckline, modest coverage, elegant"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "dress_type": (list(cls.DRESS_TYPES.keys()),),
                "neckline": (list(cls.NECKLINES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("dress_prompt",)
    FUNCTION = "select"
    CATEGORY = "Mason's Nodes/Outfit"

    def select(self, prompt, dress_type, neckline):
        dress = self.DRESS_TYPES.get(dress_type, "")
        neck = self.NECKLINES.get(neckline, "")
        return (f"{prompt}, {dress}, {neck}",)


class FootwearSelector:
    """Footwear including heels, boots, and stockings"""
    
    FOOTWEAR = {
        "barefoot": "barefoot, bare feet, no shoes, natural feet",
        "high_heels": "wearing high heels, stilettos, tall heels, elegant footwear",
        "platform_heels": "wearing platform heels, chunky heels, elevated platform",
        "ankle_boots": "wearing ankle boots, short boots, bootie style",
        "thigh_high_boots": "wearing thigh-high boots, over-knee boots, tall leather boots",
        "sandals": "wearing sandals, strappy sandals, open-toe footwear",
        "sneakers": "wearing sneakers, athletic shoes, casual footwear",
        "flats": "wearing flats, flat shoes, ballet flats, no heel"
    }
    
    STOCKINGS = {
        "none": "",
        "sheer_stockings": "wearing sheer stockings, transparent hosiery, see-through stockings",
        "fishnet": "wearing fishnet stockings, net pattern, mesh hosiery",
        "thigh_highs": "wearing thigh-high stockings, stay-up stockings, bare thigh visible",
        "pantyhose": "wearing pantyhose, full-length hosiery, sheer tights",
        "lace_top_stockings": "wearing lace-top stockings, decorative band, elegant hosiery"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "footwear": (list(cls.FOOTWEAR.keys()),),
                "stockings": (list(cls.STOCKINGS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("footwear_prompt",)
    FUNCTION = "select"
    CATEGORY = "Mason's Nodes/Outfit"

    def select(self, prompt, footwear, stockings):
        shoe = self.FOOTWEAR.get(footwear, "")
        stocking = self.STOCKINGS.get(stockings, "")
        if stocking:
            return (f"{prompt}, {shoe}, {stocking}",)
        return (f"{prompt}, {shoe}",)


class UnderwearController:
    """Underwear styles, colors, materials"""
    
    UNDERWEAR_STYLES = {
        "thong": "wearing thong, minimal back coverage, thin waistband",
        "g_string": "wearing g-string, string back, minimal coverage",
        "bikini_cut": "wearing bikini underwear, moderate coverage, classic style",
        "boyshorts": "wearing boyshorts, shorts-style underwear, full coverage",
        "high_waist_panties": "wearing high-waisted panties, retro style, tummy coverage",
        "lace_panties": "wearing lace panties, delicate lace, feminine style",
        "no_underwear": "no underwear, commando, nothing underneath"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "underwear_style": (list(cls.UNDERWEAR_STYLES.keys()),),
                "color": (["black", "white", "red", "pink", "nude", "blue", "purple"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("underwear_prompt",)
    FUNCTION = "select"
    CATEGORY = "Mason's Nodes/Outfit"

    def select(self, prompt, underwear_style, color):
        underwear = self.UNDERWEAR_STYLES.get(underwear_style, "")
        return (f"{prompt}, {underwear}, {color} colored",)


class ClothingStateController:
    """Control clothing condition: intact, disheveled, partially removed"""
    
    CLOTHING_STATES = {
        "pristine": "pristine clothing, perfectly fitted, neat and tidy, well-maintained outfit",
        "casual": "casually worn, relaxed fit, comfortable styling",
        "disheveled": "disheveled clothing, messy outfit, slightly undone, rumpled fabric",
        "partially_unbuttoned": "partially unbuttoned, open buttons, revealing peek, casual undone",
        "slipping_off": "clothing slipping off, falling straps, sliding fabric, coming undone",
        "partially_removed": "partially removed clothing, halfway off, in process of undressing",
        "pulled_aside": "clothing pulled aside, moved to reveal, displaced fabric",
        "torn": "torn clothing, ripped fabric, damaged outfit, tattered look"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "clothing_state": (list(cls.CLOTHING_STATES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("clothing_state_prompt",)
    FUNCTION = "set_state"
    CATEGORY = "Mason's Nodes/Outfit"

    def set_state(self, prompt, clothing_state):
        state = self.CLOTHING_STATES.get(clothing_state, "")
        return (f"{prompt}, {state}",)


class FabricDetailer:
    """Detailed fabric and material descriptions"""
    
    FABRICS = {
        "silk": "silk fabric, smooth silk, luxurious silk texture, lustrous sheen, flowing silk",
        "lace": "lace fabric, intricate lace pattern, delicate lacework, see-through lace, romantic lace",
        "leather": "leather material, genuine leather, smooth leather, shiny leather, supple leather",
        "latex": "latex material, shiny latex, tight latex, reflective surface, form-fitting latex",
        "velvet": "velvet fabric, soft velvet texture, plush velvet, rich velvet, luxurious velvet",
        "satin": "satin fabric, smooth satin, glossy satin finish, silky satin, lustrous satin",
        "cotton": "cotton fabric, soft cotton, breathable cotton, comfortable cotton",
        "mesh": "mesh fabric, sheer mesh, see-through mesh, transparent mesh, netted material",
        "chiffon": "chiffon fabric, sheer chiffon, flowing chiffon, lightweight chiffon, ethereal",
        "denim": "denim fabric, classic denim, blue jeans material, sturdy denim",
        "pvc": "PVC material, shiny PVC, vinyl look, glossy plastic-like material"
    }
    
    QUALITIES = {
        "shiny": "shiny finish, glossy surface, reflective material, high shine",
        "matte": "matte finish, non-reflective, soft surface, subtle texture",
        "textured": "textured fabric, detailed texture, tactile surface, dimensional",
        "sheer": "sheer fabric, see-through material, transparent, revealing",
        "opaque": "opaque fabric, non-transparent, solid coverage, full opacity"
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "fabric": (list(cls.FABRICS.keys()),),
                "quality": (list(cls.QUALITIES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("fabric_prompt",)
    FUNCTION = "detail"
    CATEGORY = "Mason's Nodes/Outfit"

    def detail(self, prompt, fabric, quality):
        fab = self.FABRICS.get(fabric, "")
        qual = self.QUALITIES.get(quality, "")
        return (f"{prompt}, {fab}, {qual}",)


NODE_CLASS_MAPPINGS = {
    "LingerieSelector": LingerieSelector,
    "SwimwearSelector": SwimwearSelector,
    "DressSelector": DressSelector,
    "FootwearSelector": FootwearSelector,
    "UnderwearController": UnderwearController,
    "ClothingStateController": ClothingStateController,
    "FabricDetailer": FabricDetailer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LingerieSelector": "🩱 Lingerie Selector",
    "SwimwearSelector": "👙 Swimwear Selector",
    "DressSelector": "👗 Dress Selector",
    "FootwearSelector": "👠 Footwear Selector",
    "UnderwearController": "🩲 Underwear Controller",
    "ClothingStateController": "👕 Clothing State Controller",
    "FabricDetailer": "🧵 Fabric Detailer",
}
