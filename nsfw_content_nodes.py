"""
Mason's NSFW Content Nodes for ComfyUI
Explicit content control nodes - SD 1.5 optimized
Use responsibly and legally.
"""


class ExplicitPoseController:
    """Control explicit/sensual poses"""
    
    POSES = {
        # Standing poses
        "standing_seductive": "standing seductively, hip cocked, hand on hip, alluring stance",
        "standing_undressing": "standing while undressing, removing clothing, strip tease pose",
        "standing_back_arch": "standing with arched back, chest forward, sensual curve",
        "against_wall": "leaning against wall, seductive lean, provocative stance",
        
        # Sitting poses
        "sitting_spread": "sitting with legs apart, open posture, inviting",
        "sitting_straddle": "straddling, sitting straddle position, legs apart",
        "sitting_reclined": "sitting reclined back, leaning back, relaxed sensual",
        
        # Lying poses  
        "lying_back": "lying on back, supine position, looking up",
        "lying_side": "lying on side, side pose, curves emphasized",
        "lying_stomach": "lying on stomach, prone position, looking back",
        "lying_spread": "lying spread out, open pose, relaxed sprawl",
        
        # Kneeling poses
        "kneeling_upright": "kneeling upright, on knees, straight posture",
        "kneeling_forward": "kneeling leaning forward, on all fours, crawling pose",
        "kneeling_back_arch": "kneeling with arched back, presenting pose",
        
        # Dynamic poses
        "bending_over": "bending over, bent at waist, rear emphasized",
        "stretching": "stretching pose, body elongated, sensual stretch",
        "dancing": "sensual dancing, body in motion, fluid movement",
    }
    
    EMPHASIS = {
        "natural": "",
        "chest_emphasis": "chest emphasized, bust prominent, cleavage visible",
        "rear_emphasis": "rear emphasized, bottom prominent, curves highlighted",
        "legs_emphasis": "legs emphasized, long legs, legs spread",
        "full_body": "full body visible, entire figure shown, complete view",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "pose": (list(cls.POSES.keys()),),
                "emphasis": (list(cls.EMPHASIS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("pose_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Content"

    def apply(self, prompt, pose, emphasis):
        p = self.POSES.get(pose, "")
        e = self.EMPHASIS.get(emphasis, "")
        if e:
            return (f"{prompt}, {p}, {e}",)
        return (f"{prompt}, {p}",)


class ArousalExpressionController:
    """Control arousal and pleasure expressions"""
    
    EXPRESSIONS = {
        "neutral": "neutral expression, calm, relaxed face",
        "subtle_pleasure": "subtle pleasure, slight smile, content expression",
        "enjoying": "enjoying expression, pleased look, satisfied",
        "aroused": "aroused expression, flushed cheeks, parted lips",
        "passionate": "passionate expression, intense pleasure, ecstatic",
        "orgasmic": "orgasmic expression, peak pleasure, ecstasy face",
        "afterglow": "afterglow expression, satisfied, post-pleasure bliss",
        "teasing": "teasing expression, playful arousal, coy smile",
        "wanting": "wanting expression, desire in eyes, longing look",
    }
    
    DETAILS = {
        "none": "",
        "parted_lips": "parted lips, mouth slightly open",
        "biting_lip": "biting lip, lip bite, seductive",
        "closed_eyes": "eyes closed, pleasure, feeling good",
        "half_closed_eyes": "half-closed eyes, bedroom eyes, sultry",
        "flushed": "flushed cheeks, blushing, pink cheeks",
        "sweaty": "light sweat, perspiration, exertion",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "expression": (list(cls.EXPRESSIONS.keys()),),
                "detail": (list(cls.DETAILS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("expression_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Content"

    def apply(self, prompt, expression, detail):
        exp = self.EXPRESSIONS.get(expression, "")
        det = self.DETAILS.get(detail, "")
        if det:
            return (f"{prompt}, {exp}, {det}",)
        return (f"{prompt}, {exp}",)


class IntimateInteractionController:
    """Control intimate interactions between subjects"""
    
    INTERACTIONS = {
        "kissing_soft": "soft kissing, gentle kiss, tender lips meeting",
        "kissing_passionate": "passionate kissing, deep kiss, intense lip lock",
        "kissing_neck": "kissing neck, neck kisses, nibbling neck",
        "embracing_close": "close embrace, bodies pressed together, intimate hug",
        "embracing_from_behind": "embracing from behind, spooning standing, wrapped around",
        "caressing": "caressing, gentle touching, hands exploring",
        "grinding": "grinding together, bodies moving, rhythmic motion",
        "straddling": "straddling partner, sitting on lap, mounted position",
        "pinned": "pinned down, held in place, dominant position",
        "entangled": "bodies entangled, limbs intertwined, wrapped together",
    }
    
    INTENSITY = {
        "gentle": "gentle, soft, tender, loving",
        "moderate": "moderate intensity, balanced passion",
        "passionate": "passionate, intense, heated, fervent",
        "aggressive": "aggressive, rough, forceful, dominant",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "interaction": (list(cls.INTERACTIONS.keys()),),
                "intensity": (list(cls.INTENSITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("interaction_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Content"

    def apply(self, prompt, interaction, intensity):
        inter = self.INTERACTIONS.get(interaction, "")
        intense = self.INTENSITY.get(intensity, "")
        return (f"{prompt}, {inter}, {intense}",)


class BodyEmphasisController:
    """Emphasize specific body parts"""
    
    BODY_PARTS = {
        "breasts": "breasts, bust, chest, cleavage",
        "buttocks": "buttocks, rear, bottom, behind",
        "legs": "legs, thighs, long legs, shapely legs",
        "hips": "hips, wide hips, curved hips, hip bones",
        "waist": "waist, narrow waist, waistline, midriff",
        "stomach": "stomach, flat stomach, toned belly, abdomen",
        "back": "back, spine, shoulder blades, back muscles",
        "shoulders": "shoulders, collarbone, neck and shoulders",
        "full_figure": "full figure, entire body, complete form",
    }
    
    PRESENTATION = {
        "natural": "natural presentation, unposed",
        "highlighted": "highlighted, emphasized, prominent",
        "centered": "centered in frame, focal point, main focus",
        "close_up": "close-up view, detailed, zoomed in",
        "artistic": "artistic presentation, tasteful, aesthetic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "body_part": (list(cls.BODY_PARTS.keys()),),
                "presentation": (list(cls.PRESENTATION.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("emphasis_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Content"

    def apply(self, prompt, body_part, presentation):
        part = self.BODY_PARTS.get(body_part, "")
        pres = self.PRESENTATION.get(presentation, "")
        return (f"{prompt}, {part}, {pres}",)


class NudityController:
    """Control level and type of nudity"""
    
    NUDITY_LEVELS = {
        "implied": "implied nudity, suggestive, covered strategically",
        "partial_top": "topless, bare chest, no top, exposed breasts",
        "partial_bottom": "bottomless, no bottoms, exposed below waist",
        "full_frontal": "full frontal nudity, completely nude front, naked",
        "full_rear": "rear nudity, bare back and buttocks, naked from behind",
        "full_nude": "fully nude, completely naked, no clothing, bare skin",
    }
    
    COVERAGE = {
        "none": "",
        "hands_covering": "hands covering, self-covering, modest gesture",
        "hair_covering": "hair covering body, long hair draped, hair as cover",
        "fabric_draped": "fabric draped, sheet or cloth partially covering",
        "shadow_covered": "shadows covering, strategic shadows, artistic shadow",
        "back_to_camera": "back to camera, rear view, facing away",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "nudity_level": (list(cls.NUDITY_LEVELS.keys()),),
                "coverage": (list(cls.COVERAGE.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("nudity_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Content"

    def apply(self, prompt, nudity_level, coverage):
        level = self.NUDITY_LEVELS.get(nudity_level, "")
        cov = self.COVERAGE.get(coverage, "")
        if cov:
            return (f"{prompt}, {level}, {cov}",)
        return (f"{prompt}, {level}",)


class BreastDetailController:
    """Detailed breast appearance control"""
    
    SIZES = {
        "flat": "flat chest, no breasts",
        "small": "small breasts, A-cup, petite bust",
        "medium": "medium breasts, B-cup, modest bust",
        "large": "large breasts, C-cup, full bust",
        "very_large": "very large breasts, D-cup, heavy bust",
        "huge": "huge breasts, DD+ cup, massive bust",
    }
    
    SHAPES = {
        "natural": "natural breast shape, realistic",
        "perky": "perky breasts, upturned, firm",
        "round": "round breasts, spherical shape",
        "teardrop": "teardrop breasts, natural hang, pear shaped",
        "wide_set": "wide-set breasts, separated, spaced apart",
        "close_set": "close-set breasts, cleavage, together",
    }
    
    DETAILS = {
        "none": "",
        "nipples_visible": "visible nipples, erect nipples",
        "areola_visible": "visible areola, natural coloring",
        "cleavage": "deep cleavage, pushed together",
        "underboob": "underboob visible, breast underside",
        "sideboob": "sideboob visible, side of breast",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "size": (list(cls.SIZES.keys()),),
                "shape": (list(cls.SHAPES.keys()),),
                "detail": (list(cls.DETAILS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("breast_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Content"

    def apply(self, prompt, size, shape, detail):
        sz = self.SIZES.get(size, "")
        sh = self.SHAPES.get(shape, "")
        det = self.DETAILS.get(detail, "")
        parts = [prompt, sz, sh]
        if det:
            parts.append(det)
        return (", ".join([p for p in parts if p]),)


class ButtocksDetailController:
    """Detailed buttocks appearance control"""
    
    SIZES = {
        "small": "small butt, petite rear, compact",
        "medium": "medium butt, average rear, proportional",
        "large": "large butt, big rear, full bottom",
        "very_large": "very large butt, huge rear, voluptuous bottom",
        "athletic": "athletic butt, toned rear, muscular glutes",
    }
    
    SHAPES = {
        "round": "round butt, spherical, bubble butt",
        "heart": "heart-shaped butt, wide hips tapering",
        "square": "square butt, flat sided",
        "pear": "pear-shaped butt, wider at bottom",
        "perky": "perky butt, upturned, high and tight",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "size": (list(cls.SIZES.keys()),),
                "shape": (list(cls.SHAPES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("butt_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Content"

    def apply(self, prompt, size, shape):
        sz = self.SIZES.get(size, "")
        sh = self.SHAPES.get(shape, "")
        return (f"{prompt}, {sz}, {sh}",)


class SensualLightingController:
    """Lighting specifically for sensual/NSFW content"""
    
    LIGHTING_TYPES = {
        "soft_romantic": "soft romantic lighting, warm glow, intimate atmosphere",
        "candlelight": "candlelight, flickering warm light, romantic candles",
        "moonlight": "moonlight, blue silver glow, night lighting, nocturnal",
        "neon_bedroom": "neon lighting, pink and purple glow, moody bedroom",
        "silhouette": "silhouette lighting, backlit, figure outlined",
        "window_light": "window light, natural side lighting, soft shadows",
        "spotlight": "spotlight, focused light on body, dramatic contrast",
        "golden_hour": "golden hour light, warm sunset glow, bronze skin",
        "low_key": "low key lighting, mostly shadows, mysterious, noir",
        "high_key": "high key lighting, bright, soft, minimal shadows",
    }
    
    SHADOW_PLAY = {
        "none": "",
        "body_shadows": "shadows accentuating body curves, shadow definition",
        "face_shadows": "partial face in shadow, mysterious, alluring",
        "dramatic": "dramatic shadows, high contrast, chiaroscuro",
        "soft": "soft diffused shadows, gentle gradient, flattering",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "lighting": (list(cls.LIGHTING_TYPES.keys()),),
                "shadow_play": (list(cls.SHADOW_PLAY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lighting_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/NSFW Content"

    def apply(self, prompt, lighting, shadow_play):
        light = self.LIGHTING_TYPES.get(lighting, "")
        shadow = self.SHADOW_PLAY.get(shadow_play, "")
        if shadow:
            return (f"{prompt}, {light}, {shadow}",)
        return (f"{prompt}, {light}",)


NODE_CLASS_MAPPINGS = {
    "ExplicitPoseController": ExplicitPoseController,
    "ArousalExpressionController": ArousalExpressionController,
    "IntimateInteractionController": IntimateInteractionController,
    "BodyEmphasisController": BodyEmphasisController,
    "NudityController": NudityController,
    "BreastDetailController": BreastDetailController,
    "ButtocksDetailController": ButtocksDetailController,
    "SensualLightingController": SensualLightingController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExplicitPoseController": "🔞 Explicit Pose Controller",
    "ArousalExpressionController": "😩 Arousal Expression",
    "IntimateInteractionController": "💋 Intimate Interaction",
    "BodyEmphasisController": "👀 Body Emphasis",
    "NudityController": "🚿 Nudity Controller",
    "BreastDetailController": "🍒 Breast Detail",
    "ButtocksDetailController": "🍑 Buttocks Detail",
    "SensualLightingController": "🕯️ Sensual Lighting",
}
