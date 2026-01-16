"""
Mason Nodes - Anatomical Perfection
Ensure perfect anatomy and body details in your generations
"""

class AnatomicalPerfection:
    """Ensure anatomically correct and beautiful body proportions."""
    
    FACE_DETAILS = {
        "Perfect Face": "perfect face, symmetrical features, beautiful face, detailed facial features, flawless skin texture",
        "Model Face": "model face, high cheekbones, perfect nose, full lips, defined jawline",
        "Cute Face": "cute face, soft features, round cheeks, button nose, youthful",
        "Elegant Face": "elegant face, refined features, aristocratic, sophisticated",
        "Fierce Face": "fierce face, strong features, intense eyes, powerful expression",
        "Doll Face": "doll-like face, perfect symmetry, large eyes, small nose, porcelain",
    }
    
    EYE_DETAILS = {
        "Perfect Eyes": "perfect eyes, detailed iris, realistic eye reflections, beautiful eyelashes",
        "Expressive Eyes": "expressive eyes, soulful, emotional depth, detailed pupils",
        "Anime Eyes": "large anime eyes, sparkling, vibrant iris colors, detailed",
        "Sultry Eyes": "sultry bedroom eyes, half-lidded, seductive gaze, smoky",
        "Innocent Eyes": "innocent wide eyes, pure expression, bright, clear",
    }
    
    SKIN_DETAILS = {
        "Perfect Skin": "perfect skin texture, realistic pores, subsurface scattering, natural skin shine",
        "Porcelain Skin": "porcelain skin, flawless, smooth, pale and beautiful",
        "Glowing Skin": "glowing radiant skin, healthy, luminous, dewy",
        "Tanned Skin": "tanned skin, sun-kissed, warm tones, healthy glow",
        "Realistic Skin": "ultra realistic skin, visible pores, natural imperfections, photorealistic",
    }
    
    BODY_ANATOMY = {
        "Perfect Proportions": "perfect body proportions, anatomically correct, ideal figure",
        "Athletic Body": "athletic body, toned muscles, defined abs, fit physique",
        "Curvy Body": "curvy body, hourglass figure, wide hips, full bust, feminine",
        "Slim Body": "slim body, slender figure, graceful, elegant proportions",
        "Muscular Body": "muscular body, defined muscles, strong physique, powerful",
    }
    
    HAND_DETAILS = {
        "Perfect Hands": "perfect hands, correct finger count, detailed knuckles, natural pose",
        "Elegant Hands": "elegant hands, slender fingers, manicured nails, graceful",
        "Strong Hands": "strong hands, defined, capable, realistic",
    }
    
    HAIR_DETAILS = {
        "Perfect Hair": "perfect hair, individual strands visible, realistic hair texture, shiny",
        "Flowing Hair": "flowing hair, dynamic movement, silky strands, windswept",
        "Detailed Hair": "highly detailed hair, strand-level detail, realistic highlights",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "face_detail": (list(cls.FACE_DETAILS.keys()), {"default": "Perfect Face"}),
                "eye_detail": (list(cls.EYE_DETAILS.keys()), {"default": "Perfect Eyes"}),
                "skin_detail": (list(cls.SKIN_DETAILS.keys()), {"default": "Perfect Skin"}),
                "body_anatomy": (list(cls.BODY_ANATOMY.keys()), {"default": "Perfect Proportions"}),
                "hand_detail": (list(cls.HAND_DETAILS.keys()), {"default": "Perfect Hands"}),
                "hair_detail": (list(cls.HAIR_DETAILS.keys()), {"default": "Perfect Hair"}),
            },
            "optional": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("perfected_prompt",)
    FUNCTION = "perfect"
    CATEGORY = "Mason/Masterpiece"
    
    def perfect(self, face_detail, eye_detail, skin_detail, body_anatomy, hand_detail, hair_detail, base_prompt=""):
        parts = []
        if base_prompt.strip():
            parts.append(base_prompt.strip())
        
        parts.extend([
            self.FACE_DETAILS[face_detail],
            self.EYE_DETAILS[eye_detail],
            self.SKIN_DETAILS[skin_detail],
            self.BODY_ANATOMY[body_anatomy],
            self.HAND_DETAILS[hand_detail],
            self.HAIR_DETAILS[hair_detail],
        ])
        
        return (", ".join(parts),)


class DetailEnhancer:
    """Add specific detail enhancements to any prompt."""
    
    ENHANCEMENTS = {
        # Texture Details
        "Fabric Details": "detailed fabric texture, realistic cloth folds, textile quality visible",
        "Metal Details": "detailed metal surfaces, realistic reflections, chrome shine, metallic",
        "Jewelry Details": "detailed jewelry, sparkling gems, intricate metalwork, luxury",
        "Leather Details": "detailed leather texture, realistic grain, quality material",
        "Lace Details": "intricate lace details, delicate patterns, transparency",
        
        # Environmental Details
        "Water Effects": "realistic water, reflections, ripples, wet surfaces, droplets",
        "Fire Effects": "realistic fire, flames, embers, warm glow, dynamic",
        "Smoke Effects": "atmospheric smoke, wisps, volumetric, mysterious",
        "Rain Effects": "rain drops, wet surfaces, reflections, atmospheric",
        "Snow Effects": "snow particles, frost, cold atmosphere, winter",
        
        # Light Details
        "Light Rays": "god rays, volumetric light beams, atmospheric lighting",
        "Lens Flare": "artistic lens flare, light artifacts, cinematic",
        "Bokeh": "beautiful bokeh, blurred background lights, depth of field",
        "Sparkles": "sparkles and glitter, magical particles, shimmering",
        "Glow": "soft glow effect, ethereal, dreamy atmosphere",
        
        # Surface Details
        "Sweat/Wet Skin": "glistening skin, sweat droplets, wet look, shiny",
        "Makeup Details": "detailed makeup, perfect application, beauty",
        "Tattoo Details": "detailed tattoos, crisp lines, artistic ink",
        "Scars/Marks": "realistic scars, beauty marks, character details",
        
        # Technical Details
        "8K Resolution": "8k uhd, ultra high resolution, extreme detail",
        "Sharp Focus": "razor sharp focus, crisp details, no blur",
        "Film Grain": "subtle film grain, cinematic texture, analog feel",
        "HDR": "HDR, high dynamic range, detailed highlights and shadows",
        "skin": "detailed skin texture, realistic pores, natural skin detail",
        "True": "enhanced quality, detailed rendering, high fidelity",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        enhancements = list(cls.ENHANCEMENTS.keys())
        return {
            "required": {
                "enhancement_1": (["None"] + enhancements, {"default": "8K Resolution"}),
                "enhancement_2": (["None"] + enhancements, {"default": "Sharp Focus"}),
                "enhancement_3": (["None"] + enhancements, {"default": "None"}),
            },
            "optional": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("enhanced_prompt",)
    FUNCTION = "enhance"
    CATEGORY = "Mason/Masterpiece"
    
    def enhance(self, enhancement_1, enhancement_2, enhancement_3, base_prompt=""):
        parts = []
        if base_prompt.strip():
            parts.append(base_prompt.strip())
        
        for enh in [enhancement_1, enhancement_2, enhancement_3]:
            if enh != "None":
                parts.append(self.ENHANCEMENTS[enh])
        
        return (", ".join(parts),)


class PoseSelector:
    """Select from a variety of poses for your subject."""
    
    POSES = {
        # Standing Poses
        "Standing Confident": "standing confidently, hands on hips, powerful stance",
        "Standing Elegant": "standing elegantly, graceful posture, refined",
        "Standing Relaxed": "standing relaxed, natural pose, casual",
        "Standing Leaning": "leaning against wall, casual, relaxed pose",
        "Standing Arms Crossed": "standing with arms crossed, confident, assertive",
        
        # Sitting Poses
        "Sitting Elegant": "sitting elegantly, crossed legs, refined posture",
        "Sitting Casual": "sitting casually, relaxed, comfortable",
        "Sitting On Floor": "sitting on floor, artistic pose, informal",
        "Sitting On Edge": "sitting on edge, dynamic, interesting angle",
        
        # Lying Poses
        "Lying On Back": "lying on back, relaxed, sensual pose",
        "Lying On Side": "lying on side, curved silhouette, elegant",
        "Lying On Stomach": "lying on stomach, playful, looking at camera",
        "Reclining": "reclining gracefully, classical pose, artistic",
        
        # Action Poses
        "Walking": "walking, dynamic motion, captured movement",
        "Running": "running, dynamic action, motion blur, energetic",
        "Dancing": "dancing, graceful movement, artistic pose",
        "Jumping": "jumping, airborne, dynamic energy, joyful",
        "Fighting Stance": "fighting stance, martial arts, powerful",
        
        # Expressive Poses
        "Arms Raised": "arms raised above head, triumphant, open",
        "Hands In Hair": "hands running through hair, sensual, relaxed",
        "Looking Over Shoulder": "looking over shoulder, mysterious, alluring",
        "Hugging Self": "arms hugging self, intimate, vulnerable",
        "Stretching": "stretching, athletic, graceful movement",
        
        # Artistic Poses
        "Classical Venus": "Venus pose, classical sculpture, timeless beauty",
        "Contraposto": "contraposto pose, one hip raised, classical",
        "Odalisque": "odalisque reclining pose, artistic, classical",
        "Fashion Pose": "high fashion pose, editorial, strong angles",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pose": (list(cls.POSES.keys()), {"default": "Standing Confident"}),
            },
            "optional": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("posed_prompt",)
    FUNCTION = "apply_pose"
    CATEGORY = "Mason/Masterpiece"
    
    def apply_pose(self, pose, base_prompt=""):
        parts = []
        if base_prompt.strip():
            parts.append(base_prompt.strip())
        parts.append(self.POSES[pose])
        return (", ".join(parts),)


class EnvironmentBuilder:
    """Build detailed environment and background settings."""
    
    INDOOR = {
        "Luxury Bedroom": "luxury bedroom, silk sheets, dim lighting, romantic atmosphere, expensive decor",
        "Modern Apartment": "modern apartment, minimalist design, large windows, city view",
        "Victorian Room": "Victorian era room, ornate furniture, rich fabrics, antique",
        "Japanese Room": "traditional Japanese room, tatami mats, shoji screens, zen",
        "Nightclub": "nightclub interior, neon lights, dance floor, party atmosphere",
        "Art Gallery": "art gallery, white walls, spotlights, modern art",
        "Library": "classic library, wooden shelves, leather chairs, warm lighting",
        "Bathroom Luxury": "luxury bathroom, marble, rainfall shower, spa atmosphere",
        "Kitchen Modern": "modern kitchen, stainless steel, bright, clean design",
        "Studio": "photography studio, professional lighting, seamless background",
    }
    
    OUTDOOR = {
        "Beach Sunset": "tropical beach at sunset, golden light, waves, palm trees",
        "Beach Day": "sunny beach, blue water, white sand, clear sky",
        "Forest": "enchanted forest, dappled sunlight, trees, magical atmosphere",
        "Mountain": "mountain landscape, snow peaks, dramatic vista, epic",
        "City Street": "city street, urban environment, buildings, street lights",
        "Garden": "beautiful garden, flowers blooming, nature, peaceful",
        "Rooftop": "rooftop at night, city lights below, urban skyline",
        "Desert": "desert landscape, sand dunes, golden light, vast",
        "Waterfall": "waterfall setting, mist, lush vegetation, tropical",
        "Cherry Blossoms": "cherry blossom garden, pink petals falling, Japanese spring",
    }
    
    FANTASY = {
        "Castle": "fantasy castle, magical, medieval architecture, grand",
        "Space Station": "space station interior, sci-fi, windows to stars",
        "Underwater": "underwater scene, bubbles, fish, coral, aquatic",
        "Cloud Palace": "palace in clouds, ethereal, heavenly, divine",
        "Cyberpunk City": "cyberpunk city, neon signs, rain, futuristic dystopia",
        "Magical Forest": "magical forest, glowing plants, fairy lights, mystical",
        "Dragon Lair": "dragon's lair, treasure, dramatic lighting, epic fantasy",
        "Alien World": "alien planet, strange vegetation, multiple moons, exotic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        indoor = ["None"] + [f"Indoor: {k}" for k in cls.INDOOR.keys()]
        outdoor = ["None"] + [f"Outdoor: {k}" for k in cls.OUTDOOR.keys()]
        fantasy = ["None"] + [f"Fantasy: {k}" for k in cls.FANTASY.keys()]
        all_envs = indoor + outdoor + fantasy
        
        return {
            "required": {
                "environment": (all_envs, {"default": "Indoor: Studio"}),
                "time_of_day": (["Day", "Golden Hour", "Sunset", "Blue Hour", "Night", "Midnight"], {"default": "Day"}),
                "weather": (["Clear", "Cloudy", "Rainy", "Foggy", "Snowy", "Stormy"], {"default": "Clear"}),
            },
            "optional": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("environment_prompt",)
    FUNCTION = "build_environment"
    CATEGORY = "Mason/Masterpiece"
    
    def build_environment(self, environment, time_of_day, weather, base_prompt=""):
        parts = []
        if base_prompt.strip():
            parts.append(base_prompt.strip())
        
        if environment != "None":
            if environment.startswith("Indoor: "):
                key = environment.replace("Indoor: ", "")
                parts.append(self.INDOOR.get(key, ""))
            elif environment.startswith("Outdoor: "):
                key = environment.replace("Outdoor: ", "")
                parts.append(self.OUTDOOR.get(key, ""))
            elif environment.startswith("Fantasy: "):
                key = environment.replace("Fantasy: ", "")
                parts.append(self.FANTASY.get(key, ""))
        
        time_prompts = {
            "Day": "daytime, bright natural light",
            "Golden Hour": "golden hour, warm sunlight, long shadows",
            "Sunset": "sunset, orange and pink sky, dramatic lighting",
            "Blue Hour": "blue hour, twilight, cool tones",
            "Night": "nighttime, artificial lights, dark atmosphere",
            "Midnight": "midnight, very dark, minimal light, mysterious",
        }
        parts.append(time_prompts.get(time_of_day, ""))
        
        weather_prompts = {
            "Clear": "clear sky",
            "Cloudy": "cloudy sky, overcast, diffused light",
            "Rainy": "rainy weather, wet surfaces, reflections",
            "Foggy": "foggy atmosphere, misty, mysterious",
            "Snowy": "snowy weather, falling snow, winter",
            "Stormy": "stormy weather, dramatic clouds, lightning",
        }
        parts.append(weather_prompts.get(weather, ""))
        
        return (", ".join(filter(None, parts)),)


NODE_CLASS_MAPPINGS = {
    "MasonAnatomicalPerfection": AnatomicalPerfection,
    "MasonDetailEnhancer": DetailEnhancer,
    "MasonPoseSelector": PoseSelector,
    "MasonEnvironmentBuilder": EnvironmentBuilder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonAnatomicalPerfection": "🧬 Anatomical Perfection",
    "MasonDetailEnhancer": "✨ Detail Enhancer",
    "MasonPoseSelector": "🕺 Pose Selector",
    "MasonEnvironmentBuilder": "🌍 Environment Builder",
}
