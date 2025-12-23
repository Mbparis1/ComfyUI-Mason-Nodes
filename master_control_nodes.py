"""
Mason's Master Control Nodes for ComfyUI
All-in-one comprehensive nodes - No LoRAs needed
"""


class EyeDetailMaster:
    """Complete eye control - replaces need for eye LoRAs"""
    
    COLORS = {
        "blue": "blue eyes, bright blue irises, sapphire eyes",
        "green": "green eyes, emerald irises, jade green eyes",
        "brown": "brown eyes, warm brown irises, chocolate eyes",
        "hazel": "hazel eyes, mixed green-brown irises",
        "gray": "gray eyes, silver-gray irises, stormy eyes",
        "amber": "amber eyes, golden-brown irises, honey eyes",
        "violet": "violet eyes, purple irises, amethyst eyes",
        "heterochromia": "heterochromia, two different colored eyes, unique eyes",
    }
    
    EXPRESSIONS = {
        "neutral": "neutral eye expression, calm gaze",
        "seductive": "seductive eyes, bedroom eyes, alluring gaze, half-lidded",
        "intense": "intense gaze, piercing eyes, focused look",
        "playful": "playful eyes, sparkling, mischievous look",
        "sultry": "sultry eyes, smoky look, sensual gaze",
        "innocent": "innocent eyes, wide-eyed, doe eyes",
        "confident": "confident eyes, direct gaze, self-assured look",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "eye_color": (list(cls.COLORS.keys()),),
                "expression": (list(cls.EXPRESSIONS.keys()),),
                "add_detail": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("eye_detailed_prompt",)
    FUNCTION = "detail_eyes"
    CATEGORY = "Mason's Nodes/Master Control"

    def detail_eyes(self, prompt, eye_color, expression, add_detail):
        color_desc = self.COLORS.get(eye_color, "")
        expr_desc = self.EXPRESSIONS.get(expression, "")
        
        detail = ""
        if add_detail:
            detail = ", highly detailed eyes, realistic eye texture, sharp eye detail, catchlights, realistic iris detail"
        
        return (f"{prompt}, {color_desc}, {expr_desc}{detail}",)


class BodyDetailMaster:
    """Complete body control - replaces need for body LoRAs"""
    
    BUILDS = {
        "slim": "slim body, slender figure, lean, thin",
        "athletic": "athletic body, toned, fit, muscular definition, six pack abs",
        "curvy": "curvy body, hourglass figure, wide hips, ample curves",
        "petite": "petite body, small frame, delicate build",
        "voluptuous": "voluptuous body, full figure, generous proportions, ample bust, wide hips",
        "muscular": "muscular body, strong build, defined muscles, powerful physique",
        "average": "average body, normal proportions, natural build",
    }
    
    SKIN_QUALITY = {
        "flawless": "flawless skin, perfect skin, smooth skin, no blemishes",
        "natural": "natural skin, realistic skin texture, subtle imperfections, pores visible",
        "tanned": "tanned skin, sun-kissed, bronzed, golden tan",
        "pale": "pale skin, fair complexion, porcelain skin",
        "freckled": "freckled skin, cute freckles, natural freckles",
        "oiled": "oiled skin, glistening, shiny skin, body oil",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "body_build": (list(cls.BUILDS.keys()),),
                "skin_quality": (list(cls.SKIN_QUALITY.keys()),),
                "add_anatomy_fix": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("body_prompt",)
    FUNCTION = "detail_body"
    CATEGORY = "Mason's Nodes/Master Control"

    def detail_body(self, prompt, body_build, skin_quality, add_anatomy_fix):
        build = self.BUILDS.get(body_build, "")
        skin = self.SKIN_QUALITY.get(skin_quality, "")
        
        anatomy = ""
        if add_anatomy_fix:
            anatomy = ", anatomically correct, proper proportions, correct anatomy"
        
        return (f"{prompt}, {build}, {skin}{anatomy}",)


class QualityMasterNode:
    """Ultimate quality enhancement - replaces all quality LoRAs"""
    
    QUALITY_LEVELS = {
        "ultra": "masterpiece, best quality, ultra detailed, 8k uhd, professional photography, award winning, extremely detailed, photorealistic, hyperrealistic, sharp focus, intricate details, studio quality",
        "high": "masterpiece, best quality, highly detailed, 8k, professional photo, sharp focus, detailed",
        "good": "high quality, detailed, sharp focus, good lighting",
        "balanced": "good quality, balanced detail, clear image",
        "fast": "decent quality, clear, focused",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "quality": (list(cls.QUALITY_LEVELS.keys()),),
                "add_negative_prevention": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("enhanced_prompt", "auto_negative")
    FUNCTION = "enhance"
    CATEGORY = "Mason's Nodes/Master Control"

    def enhance(self, prompt, quality, add_negative_prevention):
        quality_tags = self.QUALITY_LEVELS.get(quality, "")
        enhanced = f"{prompt}, {quality_tags}"
        
        if add_negative_prevention:
            negative = "bad quality, low quality, worst quality, blurry, out of focus, bad anatomy, bad hands, extra fingers, missing fingers, deformed, disfigured, mutation, ugly, duplicate, morbid, mutilated, poorly drawn face, poorly drawn hands, extra limbs, fused fingers, too many fingers, long neck, malformed limbs, missing arms, missing legs, extra arms, extra legs, distorted, amateur, jpeg artifacts, watermark, signature, text"
        else:
            negative = ""
        
        return (enhanced, negative)


class CompleteCharacterBuilder:
    """All-in-one character creation - no LoRAs needed"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "gender": (["female", "male"],),
                "age_range": (["18-22", "23-28", "29-35", "36-45", "46-55"],),
                "ethnicity": ([
                    "caucasian", "asian_east", "asian_southeast", "japanese", "korean", "chinese",
                    "latina", "african", "african_american", "indian", "middle_eastern", "arabic",
                    "mediterranean", "scandinavian", "slavic", "mixed_asian", "mixed_latina", "mixed_african"
                ],),
                "face_shape": (["oval", "round", "square", "heart", "oblong", "diamond"],),
                "body_type": (["slim", "athletic", "curvy", "petite", "voluptuous", "hourglass", "pear", "average"],),
                "hair_color": (["blonde", "platinum_blonde", "strawberry_blonde", "brunette", "light_brown", "black", "red", "auburn", "ginger", "silver", "ombre", "balayage", "pink", "purple", "blue"],),
                "hair_style": (["long_straight", "long_wavy", "long_curly", "medium_straight", "medium_wavy", "medium_curly", "short_pixie", "short_bob", "lob", "ponytail", "high_ponytail", "braids", "bun", "messy_bun", "updo", "half_up", "pigtails", "bangs_straight", "bangs_curtain"],),
                "hair_length": (["very_long", "long", "medium", "short", "pixie", "buzz"],),
                "eye_color": (["blue", "light_blue", "green", "emerald", "brown", "dark_brown", "hazel", "gray", "amber", "violet"],),
                "breast_size": (["flat", "small", "medium", "large", "very_large", "huge"],),
                "height": (["petite_short", "average", "tall", "very_tall"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("character_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Master Control"

    def build(self, gender, age_range, ethnicity, face_shape, body_type, hair_color, hair_style, hair_length, eye_color, breast_size, height):
        age_map = {
            "18-22": "young adult, early twenties, youthful",
            "23-28": "mid twenties, young woman, prime age",
            "29-35": "late twenties to early thirties, mature beauty",
            "36-45": "mature, sophisticated, confident",
            "46-55": "middle aged, distinguished, experienced beauty",
        }
        
        ethnicity_map = {
            "caucasian": "caucasian, european features, fair skin",
            "asian_east": "east asian, asian features, smooth skin",
            "asian_southeast": "southeast asian, thai or filipino features",
            "japanese": "japanese, japanese features, delicate features",
            "korean": "korean, korean features, porcelain skin",
            "chinese": "chinese, chinese features, refined features",
            "latina": "latina, hispanic features, olive skin",
            "african": "african, dark skin, african features",
            "african_american": "african american, dark skin, american features",
            "indian": "indian, south asian features, brown skin",
            "middle_eastern": "middle eastern, arabic features, olive skin",
            "arabic": "arabic, arabian features, exotic beauty",
            "mediterranean": "mediterranean, greek or italian features, olive skin",
            "scandinavian": "scandinavian, nordic features, pale skin, high cheekbones",
            "slavic": "slavic, eastern european features, high cheekbones",
            "mixed_asian": "mixed asian, eurasian features, exotic blend",
            "mixed_latina": "mixed latina, multiracial, latin blend",
            "mixed_african": "mixed african, multiracial, diverse heritage",
        }
        
        face_map = {
            "oval": "oval face shape, balanced proportions",
            "round": "round face, soft features, full cheeks",
            "square": "square face, strong jaw, angular features",
            "heart": "heart shaped face, wide forehead, pointed chin",
            "oblong": "oblong face, long face, elegant proportions",
            "diamond": "diamond face shape, prominent cheekbones",
        }
        
        body_map = {
            "slim": "slim body, slender",
            "athletic": "athletic body, toned, fit, muscular definition",
            "curvy": "curvy body, hourglass figure",
            "petite": "petite, small frame",
            "voluptuous": "voluptuous, full figure",
            "hourglass": "hourglass figure, balanced bust and hips, narrow waist",
            "pear": "pear shaped body, wider hips than bust",
            "average": "average build, natural body",
        }
        
        breast_map = {
            "flat": "flat chest, no breasts",
            "small": "small breasts, perky, A-cup",
            "medium": "medium breasts, natural, B-cup",
            "large": "large breasts, ample bust, C-cup to D-cup",
            "very_large": "very large breasts, huge bust, DD-cup",
            "huge": "huge breasts, massive bust, extremely large",
        }
        
        height_map = {
            "petite_short": "petite height, short, under 5 feet 2 inches",
            "average": "average height, 5 feet 4 to 5 feet 7",
            "tall": "tall, 5 feet 8 to 5 feet 11, long legs",
            "very_tall": "very tall, over 6 feet, model height, statuesque",
        }
        
        hair_style_map = {
            "long_straight": "long straight hair, sleek",
            "long_wavy": "long wavy hair, flowing waves",
            "long_curly": "long curly hair, ringlets",
            "medium_straight": "medium length straight hair",
            "medium_wavy": "medium length wavy hair",
            "medium_curly": "medium length curly hair",
            "short_pixie": "pixie cut, short cropped",
            "short_bob": "bob haircut, chin length",
            "lob": "lob haircut, long bob, shoulder length",
            "ponytail": "ponytail, pulled back",
            "high_ponytail": "high ponytail, sporty",
            "braids": "braided hair, intricate braids",
            "bun": "hair in bun, neat updo",
            "messy_bun": "messy bun, casual updo",
            "updo": "elegant updo, formal hairstyle",
            "half_up": "half up half down hairstyle",
            "pigtails": "pigtails, twin tails",
            "bangs_straight": "straight bangs, fringe",
            "bangs_curtain": "curtain bangs, parted fringe",
        }
        
        hair_length_map = {
            "very_long": "very long hair, past waist",
            "long": "long hair, past shoulders",
            "medium": "medium length hair, shoulder length",
            "short": "short hair, above shoulders",
            "pixie": "pixie length, very short",
            "buzz": "buzz cut, nearly shaved",
        }
        
        parts = [
            f"beautiful {gender}",
            age_map.get(age_range, ""),
            ethnicity_map.get(ethnicity, ""),
            face_map.get(face_shape, ""),
            body_map.get(body_type, ""),
            height_map.get(height, ""),
            f"{hair_color} hair",
            hair_length_map.get(hair_length, ""),
            hair_style_map.get(hair_style, ""),
            f"{eye_color} eyes",
            breast_map.get(breast_size, ""),
            "detailed face, beautiful features, photorealistic"
        ]
        
        return (", ".join([p for p in parts if p]),)


class ScenePresetMaster:
    """Complete scene presets - instant professional setups"""
    
    PRESETS = {
        "boudoir_bedroom": "in a luxurious boudoir bedroom, silk sheets, soft ambient lighting, intimate setting, romantic atmosphere, candles, elegant furniture",
        "professional_studio": "in a professional photo studio, clean backdrop, studio lighting, professional photography setup, controlled lighting",
        "beach_sunset": "on a tropical beach at sunset, golden hour lighting, ocean waves, palm trees, warm colors, paradise setting",
        "bathroom_luxury": "in a luxurious bathroom, marble surfaces, bathtub, soft lighting, steam, elegant fixtures",
        "pool_day": "by a beautiful pool, sunny day, clear water, poolside, outdoor setting, summer vibes",
        "gym_fitness": "in a modern gym, fitness setting, workout environment, athletic atmosphere",
        "office_professional": "in a modern office, professional setting, desk, business environment",
        "outdoor_nature": "outdoors in nature, natural setting, trees, sunlight, fresh air",
        "nightclub_party": "in a nightclub, party atmosphere, neon lights, dancing, energetic",
        "hotel_room": "in an elegant hotel room, luxurious bed, ambient lighting, travel setting",
        "shower_wet": "in a shower, water droplets, wet skin, steam, bathroom",
        "car_interior": "inside a luxury car, leather seats, automotive setting",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subject": ("STRING", {"default": "", "multiline": True}),
                "scene": (list(cls.PRESETS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_prompt",)
    FUNCTION = "apply_scene"
    CATEGORY = "Mason's Nodes/Master Control"

    def apply_scene(self, subject, scene):
        scene_desc = self.PRESETS.get(scene, "")
        return (f"{subject}, {scene_desc}",)


class UltimatePoseMaster:
    """Complete pose library - every pose imaginable"""
    
    POSES = {
        # Standing poses
        "standing_confident": "standing confidently, hands on hips, power pose, strong stance",
        "standing_casual": "standing casually, relaxed pose, natural stance",
        "standing_sexy": "standing seductively, hip cocked, alluring pose, one hand on hip",
        "standing_back_view": "standing with back to camera, looking over shoulder, back view",
        "standing_contrapposto": "standing in contrapposto, classical pose, weight on one leg, artistic stance",
        "standing_tiptoe": "standing on tiptoes, elongated figure, ballet stance",
        "standing_leaning": "leaning against wall, casual lean, relaxed stance",
        
        # Sitting poses
        "sitting_elegant": "sitting elegantly, legs crossed, refined posture",
        "sitting_casual": "sitting casually, relaxed, natural pose",
        "sitting_floor": "sitting on floor, legs extended, ground level",
        "sitting_knees_up": "sitting with knees pulled up, hugging knees",
        "sitting_lotus": "sitting in lotus position, cross-legged, meditation pose",
        "sitting_straddle": "sitting with legs straddled, wide seated position",
        "sitting_side_saddle": "sitting side saddle, legs to one side, elegant",
        
        # Lying poses
        "lying_on_back": "lying on back, supine position, looking up",
        "lying_on_side": "lying on side, propped on elbow, side view",
        "lying_on_stomach": "lying on stomach, prone position, looking at camera",
        "lying_sensual": "lying sensually, seductive pose, stretched out",
        "lying_fetal": "lying in fetal position, curled up, vulnerable",
        "lying_spread_eagle": "lying spread eagle, arms and legs extended, open position",
        
        # Kneeling poses
        "kneeling_upright": "kneeling upright, straight posture",
        "kneeling_sitting_back": "kneeling sitting back on heels",
        "on_all_fours": "on all fours, hands and knees position, arched back",
        "kneeling_one_knee": "kneeling on one knee, proposal pose, gallant",
        
        # Action poses
        "walking_toward": "walking toward camera, mid-stride, approaching",
        "dancing": "dancing, dynamic pose, movement, graceful",
        "stretching": "stretching, arms raised, full body stretch",
        "bending_over": "bending over, bent at waist, rear view prominence",
        "running": "running pose, mid-stride, athletic motion, dynamic",
        "jumping": "jumping pose, airborne, dynamic leap, energetic",
        
        # Intimate poses
        "covering_modestly": "covering modestly, hands covering, demure",
        "arms_above_head": "arms raised above head, exposed, vulnerable",
        "touching_self": "hands on body, self-touch, sensual",
        "spread_pose": "spread pose, open position, inviting",
        "arched_back": "arched back, curved spine, sensual arch",
        "hip_thrust": "hips thrust forward, provocative stance, curved posture",
        
        # Yoga poses
        "yoga_downward_dog": "downward dog pose, yoga position, inverted V, flexible",
        "yoga_warrior": "warrior pose, yoga stance, strong legs, arms extended",
        "yoga_cobra": "cobra pose, yoga position, raised upper body, floor stretch",
        "yoga_child_pose": "child's pose, yoga position, kneeling forward fold, resting",
        "yoga_tree": "tree pose, yoga stance, one foot on thigh, balanced",
        "yoga_bridge": "bridge pose, yoga position, hips raised, back arch",
        
        # Sports poses
        "tennis_serve": "tennis serve pose, athletic stance, arm raised, sports motion",
        "golf_swing": "golf swing pose, mid-swing, athletic rotation",
        "swimming": "swimming pose, freestyle stroke, athletic motion",
        "volleyball_spike": "volleyball spike pose, jumping attack, athletic",
        "surfing": "surfing pose, board stance, balanced, athletic",
        
        # Modeling poses
        "model_runway": "runway model pose, walking stride, confident, high fashion",
        "model_editorial": "editorial pose, high fashion, artistic, magazine style",
        "model_catalog": "catalog pose, commercial, approachable, product focused",
        "model_glamour": "glamour pose, alluring, sensual, beauty focused",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "pose": (list(cls.POSES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("posed_prompt",)
    FUNCTION = "pose"
    CATEGORY = "Mason's Nodes/Master Control"

    def pose(self, prompt, pose):
        pose_desc = self.POSES.get(pose, "")
        return (f"{prompt}, {pose_desc}",)


NODE_CLASS_MAPPINGS = {
    "EyeDetailMaster": EyeDetailMaster,
    "BodyDetailMaster": BodyDetailMaster,
    "QualityMasterNode": QualityMasterNode,
    "CompleteCharacterBuilder": CompleteCharacterBuilder,
    "ScenePresetMaster": ScenePresetMaster,
    "UltimatePoseMaster": UltimatePoseMaster,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EyeDetailMaster": "👁️ Eye Detail Master",
    "BodyDetailMaster": "💪 Body Detail Master",
    "QualityMasterNode": "⭐ Quality Master",
    "CompleteCharacterBuilder": "👤 Complete Character Builder",
    "ScenePresetMaster": "🎬 Scene Preset Master",
    "UltimatePoseMaster": "🧘 Ultimate Pose Master",
}
