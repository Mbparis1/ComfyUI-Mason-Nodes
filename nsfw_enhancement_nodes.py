"""
Mason Nodes - NSFW Enhancement Nodes
Comprehensive NSFW action, pose, style, and anatomical detail nodes
For maximum control over adult content generation
"""

class MasonNSFWActionSelector:
    """Select from a variety of NSFW actions and scenarios."""
    
    ACTIONS = {
        # ============================================
        # SOLO ACTIONS
        # ============================================
        "Solo - Sensual Pose": "sensual pose, seductive expression, bedroom eyes, alluring, teasing, soft lighting",
        "Solo - Self Touch": "touching self, hands on body, sensual self-caress, pleasuring, eyes closed in pleasure",
        "Solo - Masturbation": "masturbating, fingers on genitals, self-pleasure, orgasmic expression, moaning",
        "Solo - Toy Play": "using toy, vibrator, dildo, pleasuring self with toy, ecstatic expression",
        "Solo - Strip Tease": "stripping, removing clothes, undressing, teasing strip, playful expression",
        "Solo - Spread Pose": "spreading legs, legs apart, exposed, presenting, inviting pose",
        "Solo - Bent Over": "bent over, from behind view, presenting rear, arched back, looking back",
        "Solo - On Knees": "on knees, kneeling, submissive pose, looking up, waiting",
        "Solo - Lying Down": "lying on bed, reclined, relaxed nude pose, comfortable, inviting",
        "Solo - Standing Nude": "standing nude, full body visible, confident pose, proud",
        
        # ============================================
        # COUPLE ACTIONS - ORAL
        # ============================================
        "Oral - Giving BJ": "giving blowjob, oral sex, mouth on penis, sucking, on knees, looking up at partner",
        "Oral - BJ Close-up": "blowjob close-up, penis in mouth, oral sex detail, lips wrapped around shaft",
        "Oral - Deepthroat": "deepthroat, taking fully in mouth, gagging slightly, determined expression",
        "Oral - Licking": "licking penis, tongue on shaft, teasing with tongue, playful oral",
        "Oral - Receiving Cunnilingus": "receiving oral, partner between legs, cunnilingus, ecstatic expression, arched back",
        "Oral - 69 Position": "69 position, mutual oral sex, simultaneous pleasuring, tangled bodies",
        
        # ============================================
        # COUPLE ACTIONS - INTERCOURSE
        # ============================================
        "Sex - Missionary": "missionary position, man on top, face to face, intimate, legs wrapped around",
        "Sex - Cowgirl": "cowgirl position, woman on top, riding, bouncing, dominant female",
        "Sex - Reverse Cowgirl": "reverse cowgirl, woman on top facing away, rear visible, riding",
        "Sex - Doggy Style": "doggy style, from behind, bent over, hands gripping hips, arched back",
        "Sex - Standing": "standing sex, against wall, lifted, passionate, desperate",
        "Sex - Spooning": "spooning sex, lying side by side, intimate, gentle, romantic",
        "Sex - Prone Bone": "prone bone position, lying flat on stomach, from behind, pressing down",
        "Sex - Legs Up": "legs up missionary, ankles on shoulders, deep penetration, intense",
        "Sex - From Behind Standing": "bent over standing, from behind, gripping furniture, intense thrusting",
        
        # ============================================
        # COUPLE ACTIONS - ANAL
        # ============================================
        "Anal - Penetration": "anal sex, anal penetration, from behind, tight, intense expression",
        "Anal - Reverse Cowgirl": "anal reverse cowgirl, riding anally, bouncing, intense",
        
        # ============================================
        # GROUP ACTIONS
        # ============================================
        "Threesome - MMF": "threesome mmf, two men one woman, double attention, overwhelmed with pleasure",
        "Threesome - FFM": "threesome ffm, two women one man, both women pleasuring, sharing",
        "Threesome - Spitroast": "spitroast, oral and vaginal simultaneously, airtight, overwhelmed",
        "Gangbang": "gangbang, multiple partners, surrounded, center of attention",
        
        # ============================================
        # SPECIFIC SCENARIOS
        # ============================================
        "Titjob": "titjob, paizuri, breast sex, penis between breasts, pushing breasts together",
        "Handjob": "giving handjob, hand on penis, stroking, jerking off partner",
        "Footjob": "footjob, feet on penis, using feet to pleasure, skilled foot technique",
        "Facial - Receiving": "receiving facial, cum on face, eyes closed, mouth open, satisfied",
        "Creampie": "creampie, internal cumshot, cum dripping out, freshly filled",
        "Cum on Body": "cum on body, cum on breasts, cum on stomach, messy finish",
        "Squirting": "squirting, female ejaculation, intense orgasm, wet explosion",
        "Ahegao": "ahegao, fucked silly expression, eyes rolling, tongue out, drooling, overwhelmed",
        
        # ============================================
        # BDSM / KINK
        # ============================================
        "BDSM - Bondage": "bondage, tied up, rope bondage, shibari, restrained, helpless",
        "BDSM - Blindfolded": "blindfolded, sensory deprivation, anticipation, heightened senses",
        "BDSM - Collar and Leash": "wearing collar, leash attached, pet play, submissive, controlled",
        "BDSM - Spanking": "being spanked, red marks on butt, punishment, discipline",
        "BDSM - Dominant Pose": "dominant pose, dominating partner, in control, powerful stance",
        "BDSM - Submissive Pose": "submissive pose, kneeling, head down, obedient, awaiting command",
        
        # ============================================
        # SETTINGS
        # ============================================
        "Setting - Bedroom": "in bedroom, on bed, silk sheets, intimate setting, warm lighting",
        "Setting - Shower": "in shower, wet, water running, steam, slippery, pressed against tiles",
        "Setting - Office": "in office, on desk, professional clothes torn, forbidden affair",
        "Setting - Outdoors": "outdoors, public risk, nature setting, exhibitionism, thrill of being caught",
        "Setting - Pool": "by pool, wet swimsuit, dripping water, summer heat, pool edge",
    }
    
    INTENSITY = {
        "Soft/Sensual": "soft lighting, romantic mood, gentle, loving, sensual, tasteful",
        "Passionate": "passionate, intense desire, hungry for each other, burning passion",
        "Rough/Aggressive": "rough sex, aggressive, hair pulling, intense thrusting, primal",
        "Extreme": "extreme, hardcore, intense, overwhelming, relentless, exhausted from pleasure",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "action": (sorted(cls.ACTIONS.keys()), {"default": "Solo - Sensual Pose"}),
                "intensity": (list(cls.INTENSITY.keys()), {"default": "Passionate"}),
            },
            "optional": {
                "custom_details": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("action_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason/NSFW"
    
    def generate(self, action, intensity, custom_details=""):
        parts = []
        parts.append(self.ACTIONS[action])
        parts.append(self.INTENSITY[intensity])
        
        if custom_details and custom_details.strip():
            parts.append(custom_details.strip())
        
        return (", ".join(parts),)


class MasonNSFWAnatomyEnhancer:
    """Enhance anatomical detail and accuracy for NSFW content."""
    
    BODY_FOCUS = {
        "Full Body": "full nude body, entire figure visible, head to toe",
        "Upper Body": "upper body focus, breasts visible, face and torso",
        "Lower Body": "lower body focus, hips and below, genital area visible",
        "Face/Expression": "face focus, expression of pleasure, detailed face",
        "Breasts Focus": "breast focus, detailed breasts, nipples visible, cleavage",
        "Butt Focus": "butt focus, rear view, detailed buttocks, ass",
        "Genital Focus": "genital focus, detailed genitalia, anatomically correct",
        "Full Spread": "fully spread, everything visible, completely exposed",
    }
    
    BREAST_DESC = {
        "None/Custom": "",
        "Small Natural": "small natural breasts, perky, petite bust, a-cup, delicate",
        "Medium Natural": "medium natural breasts, perfect handful, c-cup, feminine",
        "Large Natural": "large natural breasts, big bust, d-cup, heavy, bouncing",
        "Very Large Natural": "very large natural breasts, huge bust, dd-cup, massive, heavy",
        "Small Perky": "small perky breasts, firm, youthful, pointy nipples",
        "Large Enhanced": "large enhanced breasts, round, firm, augmented, fake tits",
        "Athletic": "athletic build, toned, smaller breasts, fit body, muscular",
    }
    
    BODY_TYPE = {
        "None/Custom": "",
        "Petite": "petite body, small frame, tiny, delicate, slender",
        "Slim": "slim body, slender, thin, model-like, elegant",
        "Athletic": "athletic body, toned, fit, muscular definition, abs",
        "Curvy": "curvy body, hourglass figure, wide hips, thick thighs",
        "Voluptuous": "voluptuous body, very curvy, thick, full figured, big curves",
        "BBW": "bbw, plus size, thick, heavy, chubby, full body",
        "Muscular": "muscular body, defined muscles, fitness model, strong",
    }
    
    SKIN_DETAIL = {
        "Standard": "detailed skin, realistic skin texture",
        "Oiled": "oiled skin, glistening, shiny, wet look, glossy body",
        "Sweaty": "sweaty skin, glistening with sweat, post-workout, exertion",
        "Wet": "wet skin, water droplets, just showered, dripping",
        "Tanned": "tanned skin, sun-kissed, tan lines visible, bronzed",
        "Pale": "pale porcelain skin, fair, alabaster, creamy white",
        "Freckled": "freckled skin, natural freckles, cute spots",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "body_focus": (list(cls.BODY_FOCUS.keys()), {"default": "Full Body"}),
                "breast_type": (list(cls.BREAST_DESC.keys()), {"default": "None/Custom"}),
                "body_type": (list(cls.BODY_TYPE.keys()), {"default": "None/Custom"}),
                "skin_detail": (list(cls.SKIN_DETAIL.keys()), {"default": "Standard"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("anatomy_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason/NSFW"
    
    def generate(self, body_focus, breast_type, body_type, skin_detail):
        parts = []
        parts.append(self.BODY_FOCUS[body_focus])
        
        if self.BREAST_DESC[breast_type]:
            parts.append(self.BREAST_DESC[breast_type])
        if self.BODY_TYPE[body_type]:
            parts.append(self.BODY_TYPE[body_type])
        
        parts.append(self.SKIN_DETAIL[skin_detail])
        parts.append("anatomically correct, realistic anatomy, perfect proportions")
        
        return (", ".join(filter(None, parts)),)


class MasonNSFWExpressionSelector:
    """Select facial expressions for NSFW content."""
    
    EXPRESSIONS = {
        "Seductive": "seductive expression, bedroom eyes, sultry look, inviting, flirty gaze",
        "Innocent": "innocent expression, doe eyes, naive look, pure, first time nervousness",
        "Pleasured": "pleasured expression, eyes half-closed, parted lips, enjoying, feeling good",
        "Orgasmic": "orgasmic expression, eyes rolling back, mouth open, intense pleasure, climaxing",
        "Ahegao": "ahegao face, fucked silly, tongue out, eyes rolled up, drooling, mind broken",
        "Shy/Embarrassed": "shy expression, blushing, embarrassed, looking away, bashful",
        "Dominant": "dominant expression, in control, commanding, powerful, intimidating",
        "Submissive": "submissive expression, obedient, docile, eager to please, devoted",
        "Lustful": "lustful expression, hungry for more, desperate need, craving",
        "Surprised": "surprised expression, caught off guard, shocked, unexpected pleasure",
        "Playful": "playful expression, teasing smile, mischievous, fun-loving, naughty",
        "Intense": "intense expression, focused, determined, passionate concentration",
        "Exhausted": "exhausted expression, spent, satisfied, post-orgasm glow, tired bliss",
        "Begging": "begging expression, pleading eyes, wanting more, desperate",
        "Smirking": "smirking expression, knowing smile, confident, proud, satisfied smirk",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "expression": (list(cls.EXPRESSIONS.keys()), {"default": "Seductive"}),
            },
            "optional": {
                "add_eye_detail": ("BOOLEAN", {"default": True}),
                "add_lip_detail": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("expression_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason/NSFW"
    
    def generate(self, expression, add_eye_detail=True, add_lip_detail=True):
        parts = [self.EXPRESSIONS[expression]]
        
        if add_eye_detail:
            parts.append("detailed expressive eyes, eye contact, gaze")
        if add_lip_detail:
            parts.append("detailed lips, glossy lips, slightly parted")
        
        return (", ".join(parts),)


class MasonNSFWStylePreset:
    """Apply NSFW-specific style presets for different aesthetics."""
    
    STYLES = {
        "Amateur/POV": "amateur style, pov shot, first person view, realistic, homemade feel, authentic",
        "Professional Studio": "professional photography, studio lighting, polished, high production value",
        "Glamour/Boudoir": "boudoir photography, glamour shot, elegant sensual, classy nude, artistic",
        "Hardcore": "hardcore explicit, intense, raw, visceral, graphic detail",
        "Softcore Tease": "softcore, teasing, suggestive, implied, artistic nude, tasteful",
        "Vintage Pin-up": "vintage pin-up style, retro, classic, 1950s aesthetic, playful",
        "Japanese AV": "japanese av style, jav aesthetic, censored mosaic optional, idol style",
        "Hentai/Anime": "hentai style, anime aesthetic, 2d art, colorful, exaggerated",
        "CGI/3D Render": "3d render, cgi, detailed textures, realistic 3d, digital art",
        "Oil Painting": "oil painting style, artistic nude, classical, museum quality",
        "Photography": "dslr photography, raw photo, realistic lighting, candid",
        "Fantasy": "fantasy setting, magical, ethereal, otherworldly sensuality",
        "Cyberpunk": "cyberpunk aesthetic, neon lights, futuristic, tech elements, dark urban",
        "Gothic": "gothic aesthetic, dark romantic, dramatic, moody, vampire vibes",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "style": (list(cls.STYLES.keys()), {"default": "Professional Studio"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("style_prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason/NSFW"
    
    def generate(self, style):
        return (self.STYLES[style],)


class MasonNSFWQualityBooster:
    """Boost quality specifically for NSFW content generation."""
    
    QUALITY_LEVELS = {
        "Maximum Explicit": "masterpiece, best quality, ultra detailed, 8k uhd, photorealistic, explicit, NSFW, uncensored, anatomically perfect, realistic genitalia, detailed skin texture, perfect anatomy, accurate proportions, professional adult photography, sharp focus, intricate details",
        "High Quality NSFW": "best quality, highly detailed, NSFW, explicit, uncensored, anatomically correct, realistic, detailed, 4k, sharp, professional",
        "Artistic Nude": "masterpiece, artistic nude, beautiful, elegant, tasteful, museum quality, professional lighting, perfect anatomy, aesthetic",
        "Realistic Adult": "photorealistic, raw photo, NSFW, adult content, realistic skin, natural lighting, authentic, candid, amateur style",
        "Anime Hentai": "masterpiece, best quality, hentai, anime style, detailed, vibrant colors, explicit, uncensored hentai, nsfw anime",
    }
    
    NSFW_NEGATIVE = "censored, mosaic, blur on genitals, bar censor, light rays, convenient censoring, covered genitals, hidden parts, sfw, child, underage, minor, deformed, bad anatomy, extra limbs, missing limbs, mutated, ugly, blurry, low quality"
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "quality_level": (list(cls.QUALITY_LEVELS.keys()), {"default": "Maximum Explicit"}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("quality_prompt", "nsfw_negative")
    FUNCTION = "generate"
    CATEGORY = "Mason/NSFW"
    
    def generate(self, quality_level):
        return (self.QUALITY_LEVELS[quality_level], self.NSFW_NEGATIVE)


NODE_CLASS_MAPPINGS = {
    "MasonNSFWActionSelector": MasonNSFWActionSelector,
    "MasonNSFWAnatomyEnhancer": MasonNSFWAnatomyEnhancer,
    "MasonNSFWExpressionSelector": MasonNSFWExpressionSelector,
    "MasonNSFWStylePreset": MasonNSFWStylePreset,
    "MasonNSFWQualityBooster": MasonNSFWQualityBooster,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonNSFWActionSelector": "🔥 NSFW Action Selector (60+ Actions)",
    "MasonNSFWAnatomyEnhancer": "💪 NSFW Anatomy Enhancer",
    "MasonNSFWExpressionSelector": "😈 NSFW Expression Selector",
    "MasonNSFWStylePreset": "🎨 NSFW Style Preset",
    "MasonNSFWQualityBooster": "⚡ NSFW Quality Booster",
}
