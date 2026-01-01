"""
Mason's Cinematic Nodes for ComfyUI
Hollywood-grade film effects and framing - SD 1.5 optimized
"""


class CinematicFraming:
    """Professional cinematic framing and composition"""
    
    ASPECT_RATIOS = {
        "widescreen_16_9": "widescreen 16:9 aspect ratio, cinematic frame",
        "cinemascope_2_35": "cinemascope 2.35:1 ultra-wide, epic scope, letterbox",
        "imax_1_43": "IMAX 1.43:1 tall frame, immersive vertical",
        "academy_4_3": "classic academy ratio 4:3, vintage cinema",
        "anamorphic": "anamorphic lens, horizontal lens flare, oval bokeh",
    }
    
    SHOTS = {
        "establishing": "establishing shot, wide view, setting the scene, landscape",
        "wide": "wide shot, full environment visible, context shot",
        "medium": "medium shot, waist up, conversational distance",
        "close_up": "close-up shot, face fills frame, emotional",
        "extreme_close": "extreme close-up, eyes only, intense detail",
        "over_shoulder": "over the shoulder shot, POV conversation",
        "low_angle_hero": "low angle hero shot, looking up, powerful",
        "high_angle_vulnerable": "high angle shot, looking down, vulnerable",
        "dutch_angle": "dutch angle, tilted camera, tension, unease",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "aspect_ratio": (list(cls.ASPECT_RATIOS.keys()),),
                "shot_type": (list(cls.SHOTS.keys()),),
                "depth_of_field": (["deep_focus", "shallow", "ultra_shallow", "tilt_shift"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("framing_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Cinematic"

    def apply(self, prompt, aspect_ratio, shot_type, depth_of_field):
        parts = [prompt]
        parts.append(self.ASPECT_RATIOS.get(aspect_ratio, ""))
        parts.append(self.SHOTS.get(shot_type, ""))
        
        dof_map = {
            "deep_focus": "deep focus, everything sharp, Gregg Toland style",
            "shallow": "shallow depth of field, soft background blur, bokeh",
            "ultra_shallow": "extremely shallow depth of field, razor thin focus plane",
            "tilt_shift": "tilt-shift effect, miniature look, selective focus",
        }
        parts.append(dof_map.get(depth_of_field, ""))
        
        return (", ".join([p for p in parts if p]),)


class FilmGrainPro:
    """Authentic film grain and analog effects"""
    
    FILM_STOCKS = {
        "kodak_portra": "Kodak Portra 400, warm skin tones, soft colors, portrait film",
        "kodak_ektar": "Kodak Ektar 100, vivid colors, high saturation, fine grain",
        "fuji_velvia": "Fuji Velvia, ultra-saturated, vivid greens and blues",
        "ilford_hp5": "Ilford HP5, black and white, classic grain, high contrast",
        "cinestill_800t": "CineStill 800T, tungsten balanced, halation, night photography",
        "kodak_vision3": "Kodak Vision3 500T, cinema film, Hollywood movie look",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "film_stock": (list(cls.FILM_STOCKS.keys()),),
                "grain_intensity": (["subtle", "medium", "heavy", "extreme"],),
                "era": (["modern", "1990s", "1980s", "1970s", "vintage"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("film_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Cinematic"

    def apply(self, prompt, film_stock, grain_intensity, era):
        parts = [prompt]
        parts.append(self.FILM_STOCKS.get(film_stock, ""))
        
        grain_map = {
            "subtle": "subtle film grain, fine texture",
            "medium": "visible film grain, authentic analog",
            "heavy": "heavy film grain, gritty texture, aged film",
            "extreme": "extreme grain, damaged film, lo-fi aesthetic",
        }
        parts.append(grain_map.get(grain_intensity, ""))
        
        era_map = {
            "1990s": "1990s film look, slightly faded, nostalgic",
            "1980s": "1980s film aesthetic, warm tones, soft glow",
            "1970s": "1970s cinema, desaturated, gritty realism",
            "vintage": "vintage film, aged colors, classic cinema",
        }
        if era != "modern":
            parts.append(era_map.get(era, ""))
        
        return (", ".join([p for p in parts if p]),)


class LensEffectsPro:
    """Professional lens effects and optical characteristics"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "lens_type": (["standard", "anamorphic", "fisheye", "telephoto", "macro", "tilt_shift"],),
                "flare": (["none", "subtle", "dramatic", "jj_abrams"],),
                "aberration": (["none", "chromatic", "vignette", "distortion"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lens_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Cinematic"

    def apply(self, prompt, lens_type, flare, aberration):
        parts = [prompt]
        
        lens_map = {
            "anamorphic": "anamorphic lens, oval bokeh, horizontal flare",
            "fisheye": "fisheye lens, extreme wide angle, barrel distortion",
            "telephoto": "telephoto lens, compressed perspective, flat background",
            "macro": "macro lens, extreme close-up, shallow focus",
            "tilt_shift": "tilt-shift lens, selective focus, miniature effect",
        }
        if lens_type != "standard":
            parts.append(lens_map.get(lens_type, ""))
        
        flare_map = {
            "subtle": "subtle lens flare, light bloom",
            "dramatic": "dramatic lens flare, light streaks, sun glare",
            "jj_abrams": "JJ Abrams style lens flare, multiple flares, sci-fi",
        }
        if flare != "none":
            parts.append(flare_map.get(flare, ""))
        
        aberration_map = {
            "chromatic": "chromatic aberration, color fringing, RGB split",
            "vignette": "heavy vignette, dark corners, tunnel vision",
            "distortion": "lens distortion, warped edges, vintage lens",
        }
        if aberration != "none":
            parts.append(aberration_map.get(aberration, ""))
        
        return (", ".join([p for p in parts if p]),)


class HollywoodColorGrade:
    """Iconic Hollywood movie color grades"""
    
    GRADES = {
        "teal_orange": "teal and orange color grade, Hollywood blockbuster, complementary colors",
        "matrix_green": "Matrix green tint, cyberpunk, digital rain aesthetic",
        "blade_runner": "Blade Runner 2049, neon orange and pink, dystopian",
        "mad_max": "Mad Max Fury Road, desaturated orange, apocalyptic",
        "john_wick": "John Wick color grade, high contrast, blue shadows",
        "pirates_caribbean": "Pirates of the Caribbean, warm golden, adventure tone",
        "saving_private_ryan": "Saving Private Ryan, desaturated, bleach bypass",
        "la_la_land": "La La Land, vivid saturated, dreamlike colors",
        "inception": "Inception, cool blue steel, architectural precision",
        "avatar": "Avatar, luminescent blue, bioluminescent glow",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "color_grade": (list(cls.GRADES.keys()),),
                "intensity": (["subtle", "standard", "strong"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("graded_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Cinematic"

    def apply(self, prompt, color_grade, intensity):
        parts = [prompt]
        parts.append(self.GRADES.get(color_grade, ""))
        
        if intensity == "subtle":
            parts.append("subtle color grading")
        elif intensity == "strong":
            parts.append("heavy color grading, stylized")
        
        return (", ".join([p for p in parts if p]),)


class DirectorToolkit:
    """Director-level scene composition and style"""
    
    DIRECTOR = {
        "nolan": "Christopher Nolan style, practical effects, IMAX, epic scale, temporal",
        "tarantino": "Quentin Tarantino style, dialogue heavy, low angles, trunk shot, stylized violence",
        "villeneuve": "Denis Villeneuve style, slow burn, vast landscapes, minimal dialogue, atmospheric",
        "fincher": "David Fincher style, muted colors, precise framing, rain, green tint",
        "spielberg": "Steven Spielberg style, magical realism, lens flare, adventure, wonder",
        "kubrick": "Stanley Kubrick style, symmetry, one-point perspective, cold, clinical",
        "snyder": "Zack Snyder style, speed ramping, desaturated, epic poses, high contrast",
        "anderson": "Wes Anderson style, centered, pastel colors, whimsical, symmetrical",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "director_style": (list(cls.DIRECTOR.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("director_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Cinematic"

    def apply(self, prompt, director_style):
        d = self.DIRECTOR.get(director_style, "")
        return (f"{prompt}, {d}",)


NODE_CLASS_MAPPINGS = {
    "CinematicFraming": CinematicFraming,
    "FilmGrainPro": FilmGrainPro,
    "LensEffectsPro": LensEffectsPro,
    "HollywoodColorGrade": HollywoodColorGrade,
    "DirectorToolkit": DirectorToolkit,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CinematicFraming": "🎬 Cinematic Framing",
    "FilmGrainPro": "🎞️ Film Grain Pro",
    "LensEffectsPro": "📷 Lens Effects Pro",
    "HollywoodColorGrade": "🎥 Hollywood Color Grade",
    "DirectorToolkit": "🧑‍🎨 Director Toolkit",
}
