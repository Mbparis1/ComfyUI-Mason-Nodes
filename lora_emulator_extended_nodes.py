"""
Mason's Extended LoRA Emulator Nodes for ComfyUI
More specialized LoRA replacements - SD 1.5 optimized
"""


class HairLoRA:
    """Emulates hair-specific LoRAs"""
    
    HAIR_STYLES = {
        "silky_smooth": (
            "silky smooth hair, glossy hair, healthy shiny hair, "
            "luxurious hair, salon quality hair, perfect hair, "
            "flowing hair, gorgeous hair"
        ),
        "volumous": (
            "voluminous hair, big hair, full body hair, "
            "bouncy hair, thick luscious hair, "
            "abundant hair, lots of volume"
        ),
        "natural_textured": (
            "natural hair texture, authentic hair, realistic hair strands, "
            "individual hairs visible, natural movement, "
            "realistic hair detail, flyaway hairs"
        ),
        "wet_look": (
            "wet hair, dripping wet hair, slicked back wet hair, "
            "water droplets in hair, just out of shower hair, "
            "glistening wet strands"
        ),
        "windblown": (
            "windblown hair, hair flowing in wind, dynamic hair movement, "
            "wind-swept hair, hair in motion, dramatic hair"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "style": (list(cls.HAIR_STYLES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, style):
        s = self.HAIR_STYLES.get(style, "")
        neg = "bad hair, messy unkempt hair, balding, hair loss, flat hair"
        return (f"{prompt}, {s}", neg)


class LightingLoRA:
    """Emulates professional lighting LoRAs"""
    
    LIGHTING = {
        "studio_professional": (
            "professional studio lighting, three-point lighting setup, "
            "key light, fill light, rim light, studio flash, "
            "commercial photography lighting, perfect exposure"
        ),
        "golden_hour": (
            "golden hour lighting, warm sunset light, golden sunlight, "
            "magic hour, warm ambient glow, sun low in sky, "
            "golden warm tones, beautiful natural light"
        ),
        "dramatic_chiaroscuro": (
            "dramatic chiaroscuro lighting, strong contrast, "
            "deep shadows, rembrandt lighting, renaissance lighting, "
            "single light source, dramatic mood"
        ),
        "soft_beauty": (
            "soft beauty lighting, diffused light, beauty dish, "
            "clamshell lighting, wraparound light, "
            "flattering soft shadows, beauty photography"
        ),
        "neon_cyberpunk": (
            "neon lighting, colorful neon glow, pink and blue neon, "
            "cyberpunk lighting, RGB lighting, nightclub atmosphere, "
            "colored light on skin, vibrant artificial light"
        ),
        "natural_window": (
            "natural window light, soft side lighting, "
            "window light portrait, diffused daylight, "
            "soft natural shadows, indoor natural light"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "lighting": (list(cls.LIGHTING.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, lighting):
        l = self.LIGHTING.get(lighting, "")
        neg = "bad lighting, harsh shadows, overexposed, underexposed, flat lighting"
        return (f"{prompt}, {l}", neg)


class BackgroundLoRA:
    """Emulates background/environment LoRAs"""
    
    BACKGROUNDS = {
        "studio_white": (
            "pure white background, white studio backdrop, "
            "clean white seamless, high key background, "
            "professional white studio"
        ),
        "studio_black": (
            "black background, dark studio backdrop, "
            "pure black seamless, low key background, "
            "dramatic dark background"
        ),
        "bokeh_lights": (
            "bokeh lights background, city lights bokeh, "
            "colorful bokeh circles, dreamy blurred lights, "
            "out of focus light orbs"
        ),
        "luxury_interior": (
            "luxury interior background, expensive room, "
            "high-end decor, marble floors, chandeliers, "
            "mansion interior, wealthy aesthetic"
        ),
        "nature_outdoor": (
            "beautiful nature background, outdoor setting, "
            "lush greenery, natural environment, "
            "scenic backdrop, forest or meadow"
        ),
        "beach_tropical": (
            "tropical beach background, palm trees, "
            "white sand beach, turquoise water, "
            "paradise setting, ocean backdrop"
        ),
        "urban_city": (
            "urban cityscape background, city streets, "
            "metropolitan backdrop, skyscrapers, "
            "city environment, urban setting"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "background": (list(cls.BACKGROUNDS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, background):
        b = self.BACKGROUNDS.get(background, "")
        neg = "ugly background, messy background, distracting background"
        return (f"{prompt}, {b}", neg)


class PoseLoRA:
    """Emulates pose/action LoRAs"""
    
    POSES = {
        "model_runway": (
            "runway model pose, fashion model stance, "
            "confident pose, high fashion posing, "
            "editorial pose, professional model"
        ),
        "sensual_recline": (
            "sensual reclining pose, lying seductively, "
            "alluring position, inviting pose, "
            "relaxed sensual, bedroom pose"
        ),
        "athletic_action": (
            "athletic action pose, dynamic movement, "
            "sports pose, active stance, "
            "powerful pose, in motion"
        ),
        "elegant_portrait": (
            "elegant portrait pose, graceful position, "
            "classic portrait stance, refined pose, "
            "sophisticated positioning"
        ),
        "candid_natural": (
            "candid natural pose, unposed look, "
            "authentic moment, natural positioning, "
            "caught in the moment, spontaneous"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "pose": (list(cls.POSES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, pose):
        p = self.POSES.get(pose, "")
        neg = "bad pose, awkward pose, unnatural position, stiff pose"
        return (f"{prompt}, {p}", neg)


class MakeupLoRA:
    """Emulates makeup/beauty LoRAs"""
    
    MAKEUP = {
        "natural_no_makeup": (
            "natural beauty, no makeup look, bare face, "
            "minimal cosmetics, fresh-faced, "
            "clean natural skin, effortless beauty"
        ),
        "subtle_everyday": (
            "subtle everyday makeup, light makeup, "
            "natural looking makeup, minimal makeup, "
            "soft enhancement, understated"
        ),
        "glamour_full": (
            "full glamour makeup, professional makeup, "
            "contoured face, highlighted cheekbones, "
            "defined eyes, perfect lipstick, "
            "magazine ready makeup"
        ),
        "smoky_sultry": (
            "smoky eye makeup, sultry dark eyes, "
            "dramatic eye shadow, smudged liner, "
            "seductive makeup, nighttime glam"
        ),
        "bold_editorial": (
            "bold editorial makeup, avant-garde cosmetics, "
            "artistic makeup, high fashion makeup, "
            "creative makeup, statement look"
        ),
        "pin_up_vintage": (
            "vintage pin-up makeup, red lipstick, "
            "winged eyeliner, classic beauty, "
            "1950s makeup style, retro glamour"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "makeup": (list(cls.MAKEUP.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, makeup):
        m = self.MAKEUP.get(makeup, "")
        neg = "bad makeup, smeared makeup, cakey makeup, clown makeup"
        return (f"{prompt}, {m}", neg)


class ClothingLoRA:
    """Emulates clothing/fashion LoRAs"""
    
    CLOTHING = {
        "lingerie_luxury": (
            "luxury lingerie, expensive intimate wear, "
            "designer lingerie, high-end bra and panties, "
            "silk and lace lingerie, agent provocateur style"
        ),
        "bikini_swimwear": (
            "sexy bikini, swimwear model, "
            "designer swimsuit, beach ready, "
            "bronzed skin bikini, summer vibes"
        ),
        "elegant_dress": (
            "elegant evening dress, designer gown, "
            "formal dress, sophisticated attire, "
            "red carpet worthy, high fashion dress"
        ),
        "casual_chic": (
            "casual chic outfit, stylish casual wear, "
            "effortlessly stylish, trendy casual, "
            "instagram fashion, street style"
        ),
        "athletic_wear": (
            "athletic wear, sports outfit, "
            "workout clothes, yoga pants, sports bra, "
            "fitness model attire, activewear"
        ),
        "latex_leather": (
            "latex outfit, shiny latex clothing, "
            "leather attire, fetish fashion, "
            "tight leather pants, dominatrix style"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "clothing": (list(cls.CLOTHING.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, clothing):
        c = self.CLOTHING.get(clothing, "")
        neg = "bad clothing, torn clothes, wrinkled clothes, cheap looking"
        return (f"{prompt}, {c}", neg)


class AgeAppearanceLoRA:
    """Emulates age/appearance LoRAs"""
    
    APPEARANCES = {
        "youthful_fresh": (
            "youthful appearance, young adult, fresh faced, "
            "vibrant and young, early twenties look, "
            "youthful energy, young and beautiful"
        ),
        "mature_elegant": (
            "mature elegance, sophisticated adult, "
            "refined beauty, mature but stunning, "
            "aged gracefully, distinguished beauty"
        ),
        "milf_aesthetic": (
            "milf aesthetic, attractive mature woman, "
            "confident older woman, experienced beauty, "
            "sexy mature, hot mom aesthetic"
        ),
        "girl_next_door": (
            "girl next door look, approachable beauty, "
            "natural wholesome look, friendly attractive, "
            "accessible beauty, relatable pretty"
        ),
        "exotic_unique": (
            "exotic beauty, unique features, "
            "striking unusual beauty, distinctive look, "
            "memorable face, unconventional attractive"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "appearance": (list(cls.APPEARANCES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_addition")
    FUNCTION = "emulate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate(self, prompt, appearance):
        a = self.APPEARANCES.get(appearance, "")
        neg = "ugly, unattractive, bad looking"
        return (f"{prompt}, {a}", neg)


class UltimateLoRAEmulator:
    """
    The ULTIMATE LoRA replacement - Combines ALL effects in one mega-node
    This single node can replace an entire LoRA stack
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
            },
            "optional": {
                # Realism
                "photorealism": (["off", "subtle", "strong", "ultimate"],),
                "detail_level": (["off", "light", "high", "extreme"],),
                
                # Subject
                "skin_quality": (["off", "natural", "flawless", "hyperreal"],),
                "face_style": (["off", "natural", "model", "ethereal"],),
                "eye_style": (["off", "captivating", "detailed", "sultry"],),
                "hair_style": (["off", "silky", "volumous", "natural"],),
                
                # Body/Pose
                "body_type": (["off", "slim", "athletic", "curvy", "voluptuous"],),
                "pose_style": (["off", "elegant", "sensual", "candid"],),
                
                # Style
                "lighting": (["off", "studio", "golden_hour", "dramatic", "soft"],),
                "makeup": (["off", "natural", "glamour", "smoky"],),
                "glamour": (["off", "soft", "high_fashion", "boudoir"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("mega_positive_prompt", "mega_negative_prompt")
    FUNCTION = "emulate_ultimate"
    CATEGORY = "Mason's Nodes/LoRA Emulators"

    def emulate_ultimate(self, prompt, 
                         photorealism="off", detail_level="off",
                         skin_quality="off", face_style="off", 
                         eye_style="off", hair_style="off",
                         body_type="off", pose_style="off",
                         lighting="off", makeup="off", glamour="off"):
        
        pos_parts = [prompt]
        neg_parts = []
        
        # === REALISM ===
        if photorealism != "off":
            realism_prompts = {
                "subtle": "photorealistic, realistic",
                "strong": "photorealistic, hyperrealistic, ultra realistic, 8k uhd",
                "ultimate": (
                    "photorealistic, hyperrealistic, ultra realistic photograph, "
                    "indistinguishable from photo, professional photography, "
                    "8k uhd, raw photo, subsurface scattering"
                ),
            }
            pos_parts.append(realism_prompts.get(photorealism, ""))
            neg_parts.append("cartoon, anime, illustration, 3d render")
        
        if detail_level != "off":
            detail_prompts = {
                "light": "detailed, sharp focus",
                "high": "highly detailed, intricate details, sharp",
                "extreme": "extremely detailed, hyper detailed, intricate details, masterpiece",
            }
            pos_parts.append(detail_prompts.get(detail_level, ""))
            neg_parts.append("blurry, low quality")
        
        # === SUBJECT ===
        if skin_quality != "off":
            skin_prompts = {
                "natural": "natural skin, realistic skin texture",
                "flawless": "flawless skin, perfect skin, smooth",
                "hyperreal": "hyperrealistic skin, visible pores, subsurface scattering",
            }
            pos_parts.append(skin_prompts.get(skin_quality, ""))
            neg_parts.append("bad skin, plastic skin")
        
        if face_style != "off":
            face_prompts = {
                "natural": "beautiful face, natural beauty, symmetrical",
                "model": "model face, perfect features, high cheekbones, striking",
                "ethereal": "ethereal beauty, angelic face, delicate features",
            }
            pos_parts.append(face_prompts.get(face_style, ""))
            neg_parts.append("ugly face, deformed face")
        
        if eye_style != "off":
            eye_prompts = {
                "captivating": "captivating eyes, mesmerizing gaze, beautiful eyes",
                "detailed": "highly detailed eyes, realistic iris, catchlights",
                "sultry": "sultry eyes, bedroom eyes, seductive gaze",
            }
            pos_parts.append(eye_prompts.get(eye_style, ""))
            neg_parts.append("bad eyes, crossed eyes")
        
        if hair_style != "off":
            hair_prompts = {
                "silky": "silky smooth hair, glossy healthy hair, beautiful hair",
                "volumous": "voluminous hair, full body hair, thick luscious",
                "natural": "natural hair texture, realistic hair strands, flyaways",
            }
            pos_parts.append(hair_prompts.get(hair_style, ""))
            neg_parts.append("bad hair")
        
        # === BODY/POSE ===
        if body_type != "off":
            body_prompts = {
                "slim": "slim fit body, slender figure, thin waist",
                "athletic": "athletic body, toned muscles, fit physique",
                "curvy": "curvy body, hourglass figure, wide hips",
                "voluptuous": "voluptuous body, full figure, generous curves",
            }
            pos_parts.append(body_prompts.get(body_type, ""))
            neg_parts.append("bad anatomy, deformed")
        
        if pose_style != "off":
            pose_prompts = {
                "elegant": "elegant pose, graceful position, refined",
                "sensual": "sensual pose, alluring position, seductive",
                "candid": "candid natural pose, authentic moment",
            }
            pos_parts.append(pose_prompts.get(pose_style, ""))
            neg_parts.append("awkward pose, stiff")
        
        # === STYLE ===
        if lighting != "off":
            light_prompts = {
                "studio": "professional studio lighting, three-point lighting",
                "golden_hour": "golden hour lighting, warm sunset glow",
                "dramatic": "dramatic lighting, chiaroscuro, high contrast",
                "soft": "soft beauty lighting, diffused, flattering",
            }
            pos_parts.append(light_prompts.get(lighting, ""))
            neg_parts.append("bad lighting")
        
        if makeup != "off":
            makeup_prompts = {
                "natural": "natural makeup, minimal cosmetics, fresh",
                "glamour": "glamour makeup, professional cosmetics, contoured",
                "smoky": "smoky eye makeup, sultry dark eyes, dramatic",
            }
            pos_parts.append(makeup_prompts.get(makeup, ""))
            neg_parts.append("bad makeup")
        
        if glamour != "off":
            glamour_prompts = {
                "soft": "glamour photography, soft lighting, beauty shot",
                "high_fashion": "high fashion photography, editorial, vogue style",
                "boudoir": "boudoir photography, intimate lighting, romantic",
            }
            pos_parts.append(glamour_prompts.get(glamour, ""))
            neg_parts.append("amateur, poorly lit")
        
        # Combine everything
        positive = ", ".join([p for p in pos_parts if p])
        negative = ", ".join(list(set([n for n in neg_parts if n])))  # Remove duplicates
        
        if not negative:
            negative = "low quality, bad anatomy, blurry"
        
        return (positive, negative)


NODE_CLASS_MAPPINGS = {
    "HairLoRA": HairLoRA,
    "LightingLoRA": LightingLoRA,
    "BackgroundLoRA": BackgroundLoRA,
    "PoseLoRA": PoseLoRA,
    "MakeupLoRA": MakeupLoRA,
    "ClothingLoRA": ClothingLoRA,
    "AgeAppearanceLoRA": AgeAppearanceLoRA,
    "UltimateLoRAEmulator": UltimateLoRAEmulator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HairLoRA": "💇 Hair (LoRA Emulator)",
    "LightingLoRA": "💡 Lighting (LoRA Emulator)",
    "BackgroundLoRA": "🖼️ Background (LoRA Emulator)",
    "PoseLoRA": "🕺 Pose (LoRA Emulator)",
    "MakeupLoRA": "💄 Makeup (LoRA Emulator)",
    "ClothingLoRA": "👗 Clothing (LoRA Emulator)",
    "AgeAppearanceLoRA": "👤 Age/Appearance (LoRA Emulator)",
    "UltimateLoRAEmulator": "🌟 ULTIMATE LoRA Emulator (ALL-IN-ONE)",
}
