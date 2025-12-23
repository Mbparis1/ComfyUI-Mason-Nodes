"""
Mason's Model/Magazine Style Nodes for ComfyUI
Replicate specific publication aesthetics - LoRA replacement - SD 1.5 optimized
"""


class ModelAgencyStyle:
    """Replicate specific model agency/publication aesthetics"""
    
    STYLES = {
        "victorias_secret": (
            "victoria's secret style photography, VS angel aesthetic, "
            "glamorous beauty, bombshell look, perfect hair and makeup, "
            "sensual yet classy, runway model quality, high fashion lingerie"
        ),
        "sports_illustrated": (
            "sports illustrated swimsuit style, SI aesthetic, "
            "athletic beauty, beach photography, golden tan, "
            "healthy fit body, action sports, tropical location"
        ),
        "playboy_classic": (
            "playboy classic style, centerfold aesthetic, "
            "glamour photography, soft lighting, classic poses, "
            "tasteful nudity, pinup girl quality, vintage glamour"
        ),
        "playboy_modern": (
            "modern playboy style, contemporary glamour, "
            "artistic nude photography, editorial quality, "
            "sophisticated sensuality, magazine quality"
        ),
        "maxim": (
            "maxim magazine style, mens magazine aesthetic, "
            "sexy but commercial, provocative poses, "
            "high production value, nightlife vibe"
        ),
        "fhm": (
            "fhm magazine style, lad mag aesthetic, "
            "girl next door appeal, accessible sexy, "
            "fun and flirty, commercial appeal"
        ),
        "penthouse": (
            "penthouse style photography, sophisticated erotica, "
            "artistic explicit, high quality production, "
            "glamorous adult content, luxury aesthetic"
        ),
        "suicide_girls": (
            "suicide girls aesthetic, alternative beauty, "
            "tattoos and piercings, punk rock glamour, "
            "edgy sensuality, counterculture beauty"
        ),
        "met_art": (
            "met-art style, fine art nude, "
            "artistic nude photography, natural beauty, "
            "European aesthetic, gallery quality nude art"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.STYLES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("model_style_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Model Styles"

    def apply(self, prompt, style):
        s = self.STYLES.get(style, "")
        return (f"{prompt}, {s}",)


class MagazineCoverStyle:
    """Replicate magazine cover aesthetics"""
    
    MAGAZINES = {
        "vogue": (
            "vogue magazine style, high fashion editorial, "
            "anna wintour approved, couture aesthetic, "
            "avant-garde fashion, artistic editorial"
        ),
        "cosmopolitan": (
            "cosmopolitan magazine style, glamorous beauty, "
            "commercial appeal, accessible glamour, "
            "fun and flirty aesthetic, magazine cover quality"
        ),
        "elle": (
            "elle magazine style, european elegance, "
            "sophisticated fashion, chic aesthetic, "
            "refined beauty, editorial quality"
        ),
        "harpers_bazaar": (
            "harpers bazaar style, luxury fashion, "
            "artistic editorial, bold and dramatic, "
            "high fashion photography, avant-garde"
        ),
        "gq": (
            "gq magazine style, sophisticated masculine, "
            "refined and polished, upscale aesthetic, "
            "gentleman's quarterly quality"
        ),
        "vanity_fair": (
            "vanity fair style, celebrity glamour, "
            "hollywood aesthetic, dramatic lighting, "
            "portrait photography, iconic poses"
        ),
        "rolling_stone": (
            "rolling stone style, rock and roll aesthetic, "
            "edgy editorial, music industry vibe, "
            "artistic photography, cultural icons"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "magazine": (list(cls.MAGAZINES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("magazine_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Model Styles"

    def apply(self, prompt, magazine):
        m = self.MAGAZINES.get(magazine, "")
        return (f"{prompt}, {m}",)


class PhotographerStyleEmulator:
    """Emulate famous photographer styles"""
    
    PHOTOGRAPHERS = {
        "helmut_newton": (
            "helmut newton style photography, bold sensuality, "
            "high contrast black and white, powerful women, "
            "provocative elegance, fashion noir"
        ),
        "annie_leibovitz": (
            "annie leibovitz style, dramatic portraiture, "
            "cinematic lighting, celebrity quality, "
            "storytelling photography, iconic poses"
        ),
        "peter_lindbergh": (
            "peter lindbergh style, natural beauty, "
            "black and white authenticity, supermodel aesthetic, "
            "honest portraiture, timeless elegance"
        ),
        "mario_testino": (
            "mario testino style, glamorous fashion, "
            "vibrant colors, celebrity beauty, "
            "luxurious aesthetic, high fashion"
        ),
        "terry_richardson": (
            "terry richardson style, flash photography, "
            "raw and edgy, snapshot aesthetic, "
            "controversial glamour, direct flash"
        ),
        "david_lachapelle": (
            "david lachapelle style, surreal pop art, "
            "hyper colorful, fantastical scenes, "
            "celebrity portraiture, artistic excess"
        ),
        "richard_avedon": (
            "richard avedon style, high contrast, "
            "white background minimalism, pure portrait, "
            "movement in fashion, dynamic poses"
        ),
        "herb_ritts": (
            "herb ritts style, sculptural bodies, "
            "outdoor natural light, athletic beauty, "
            "male and female form, classic aesthetic"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "photographer": (list(cls.PHOTOGRAPHERS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("photographer_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Model Styles"

    def apply(self, prompt, photographer):
        p = self.PHOTOGRAPHERS.get(photographer, "")
        return (f"{prompt}, {p}",)


class DecadeAesthetic:
    """Replicate specific decade aesthetics in photography"""
    
    DECADES = {
        "1950s_pinup": (
            "1950s pinup style, vintage pin-up, "
            "marilyn monroe era, classic americana, "
            "retro glamour, rockabilly aesthetic"
        ),
        "1960s_mod": (
            "1960s mod style, swinging sixties, "
            "twiggy aesthetic, mod fashion, "
            "geometric patterns, space age"
        ),
        "1970s_disco": (
            "1970s disco era, studio 54 aesthetic, "
            "glam rock influence, earth tones, "
            "bohemian glamour, natural beauty"
        ),
        "1980s_glamour": (
            "1980s glamour style, big hair era, "
            "power dressing, neon colors, "
            "excess and opulence, dallas dynasty"
        ),
        "1990s_supermodel": (
            "1990s supermodel era, cindy crawford aesthetic, "
            "natural beauty, minimal makeup, "
            "heroin chic influence, grunge glamour"
        ),
        "2000s_y2k": (
            "2000s y2k aesthetic, early millennium, "
            "paris hilton era, low rise fashion, "
            "spray tan, frosted makeup"
        ),
        "2010s_instagram": (
            "2010s instagram aesthetic, contouring era, "
            "kardashian influence, selfie culture, "
            "filtered beauty, social media glamour"
        ),
        "2020s_natural": (
            "2020s natural beauty, clean girl aesthetic, "
            "minimal makeup, authentic beauty, "
            "sustainable fashion, effortless chic"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "decade": (list(cls.DECADES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("decade_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Model Styles"

    def apply(self, prompt, decade):
        d = self.DECADES.get(decade, "")
        return (f"{prompt}, {d}",)


NODE_CLASS_MAPPINGS = {
    "ModelAgencyStyle": ModelAgencyStyle,
    "MagazineCoverStyle": MagazineCoverStyle,
    "PhotographerStyleEmulator": PhotographerStyleEmulator,
    "DecadeAesthetic": DecadeAesthetic,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ModelAgencyStyle": "💃 Model Agency Style",
    "MagazineCoverStyle": "📰 Magazine Cover Style",
    "PhotographerStyleEmulator": "📸 Photographer Style",
    "DecadeAesthetic": "📅 Decade Aesthetic",
}
