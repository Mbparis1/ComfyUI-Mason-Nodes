"""
Mason's Style Master Nodes for ComfyUI
Complete style control without needing LoRAs - SD 1.5 optimized
"""


class CinematicStyler:
    """Apply cinematic film styles through prompts alone"""
    
    STYLES = {
        "hollywood_blockbuster": "cinematic lighting, movie quality, blockbuster film look, dramatic lighting, high production value, film grain, anamorphic lens",
        "indie_film": "indie film aesthetic, natural lighting, authentic look, grainy, documentary style, intimate cinematography",
        "noir": "film noir style, high contrast, dramatic shadows, black and white tones, moody lighting, 1940s cinema",
        "sci_fi": "sci-fi movie lighting, futuristic, neon accents, cyberpunk influence, dramatic rim lighting",
        "romance": "romantic film lighting, soft glow, warm tones, dreamy atmosphere, golden hour, romantic cinematography",
        "thriller": "thriller movie look, tense atmosphere, cold tones, harsh shadows, unsettling lighting",
        "art_house": "art house cinema, stylized, unique framing, artistic composition, avant-garde",
        "70s_film": "1970s film look, warm color grading, film grain, vintage cinema, retro color palette",
        "80s_film": "1980s film aesthetic, neon colors, bold lighting, retro style, synthwave influence",
        "90s_film": "1990s film look, natural tones, slightly desaturated, gritty realism",
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
    RETURN_NAMES = ("cinematic_prompt",)
    FUNCTION = "stylize"
    CATEGORY = "Mason's Nodes/Style Master"

    def stylize(self, prompt, style):
        style_desc = self.STYLES.get(style, "")
        return (f"{prompt}, {style_desc}",)


class PhotographerStyle:
    """Emulate famous photographer styles through prompts"""
    
    PHOTOGRAPHERS = {
        "helmut_newton": "Helmut Newton style, high fashion, dramatic black and white, strong contrast, powerful poses, glamorous",
        "peter_lindbergh": "Peter Lindbergh style, natural beauty, minimal retouching, emotional portraits, black and white, authentic",
        "mario_testino": "Mario Testino style, vibrant colors, high energy, glamorous, celebrity portrait style",
        "annie_leibovitz": "Annie Leibovitz style, theatrical, conceptual portraits, dramatic lighting, storytelling",
        "terry_richardson": "Terry Richardson style, flash photography, raw, unfiltered, snapshot aesthetic",
        "david_lachapelle": "David LaChapelle style, surreal, hyper-colorful, pop art influence, fantastical",
        "rankin": "Rankin style, bold, graphic, high contrast, fashion forward",
        "richard_avedon": "Richard Avedon style, clean white background, emotional depth, stark simplicity",
        "playboy_classic": "classic Playboy photography style, glamorous lighting, artistic nude, tasteful, professional studio",
        "sports_illustrated": "Sports Illustrated Swimsuit style, beach setting, natural beauty, athletic, sun-kissed",
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
    RETURN_NAMES = ("styled_prompt",)
    FUNCTION = "apply_style"
    CATEGORY = "Mason's Nodes/Style Master"

    def apply_style(self, prompt, photographer):
        style = self.PHOTOGRAPHERS.get(photographer, "")
        return (f"{prompt}, {style}",)


class MoodController:
    """Control overall mood and atmosphere"""
    
    MOODS = {
        "romantic": "romantic mood, soft atmosphere, warm tones, intimate feeling, love in the air",
        "seductive": "seductive atmosphere, sultry mood, intimate lighting, sensual ambiance",
        "playful": "playful mood, fun atmosphere, bright energy, cheerful vibe",
        "mysterious": "mysterious mood, enigmatic atmosphere, shadows, intriguing",
        "powerful": "powerful mood, confident energy, strong presence, commanding",
        "innocent": "innocent mood, pure atmosphere, soft light, gentle",
        "wild": "wild mood, untamed energy, dynamic, passionate",
        "elegant": "elegant mood, sophisticated atmosphere, refined, graceful",
        "edgy": "edgy mood, bold atmosphere, unconventional, daring",
        "dreamy": "dreamy mood, ethereal atmosphere, soft focus, fantasy-like",
        "intense": "intense mood, focused energy, dramatic, passionate",
        "relaxed": "relaxed mood, calm atmosphere, peaceful, serene",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "mood": (list(cls.MOODS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("mood_prompt",)
    FUNCTION = "set_mood"
    CATEGORY = "Mason's Nodes/Style Master"

    def set_mood(self, prompt, mood):
        mood_desc = self.MOODS.get(mood, "")
        return (f"{prompt}, {mood_desc}",)


class ColorGrading:
    """Apply color grading effects through prompts"""
    
    GRADES = {
        "warm_golden": "warm color grading, golden tones, amber highlights, warm shadows",
        "cool_blue": "cool color grading, blue tones, cold highlights, teal shadows",
        "vintage_sepia": "vintage sepia tones, aged look, brown tints, nostalgic colors",
        "high_contrast_bw": "high contrast black and white, dramatic monochrome, deep blacks, bright whites",
        "soft_pastel": "soft pastel colors, muted tones, gentle hues, delicate palette",
        "vibrant_saturated": "vibrant colors, highly saturated, bold hues, punchy colors",
        "desaturated_muted": "desaturated colors, muted palette, subtle tones, understated",
        "teal_orange": "teal and orange color grading, cinematic colors, complementary tones",
        "neon_pop": "neon color pop, bright accent colors, vivid highlights",
        "earthy_natural": "earthy tones, natural colors, organic palette, nature-inspired",
        "cross_processed": "cross-processed look, unusual colors, film effect, experimental",
        "faded_film": "faded film look, lifted blacks, reduced contrast, vintage fade",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "grade": (list(cls.GRADES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("graded_prompt",)
    FUNCTION = "grade"
    CATEGORY = "Mason's Nodes/Style Master"

    def grade(self, prompt, grade):
        grade_desc = self.GRADES.get(grade, "")
        return (f"{prompt}, {grade_desc}",)


class WeatherAtmosphere:
    """Add weather and atmospheric effects"""
    
    WEATHER = {
        "sunny_clear": "sunny day, clear sky, bright sunlight, warm sun",
        "overcast": "overcast sky, soft diffused light, cloudy, even lighting",
        "golden_hour": "golden hour, magic hour lighting, warm sun low on horizon, long shadows",
        "blue_hour": "blue hour, twilight, cool blue light, dusk atmosphere",
        "rainy": "rainy weather, rain drops, wet surfaces, moody atmosphere, overcast",
        "foggy": "foggy atmosphere, mist, hazy, mysterious, soft visibility",
        "stormy": "stormy weather, dramatic clouds, intense atmosphere, lightning",
        "snowy": "snowy weather, falling snow, winter atmosphere, cold light",
        "sunset": "sunset lighting, orange and pink sky, warm dramatic light",
        "sunrise": "sunrise lighting, early morning light, fresh atmosphere, dawn",
        "night": "nighttime, dark atmosphere, artificial lighting, nocturnal",
        "moonlit": "moonlit night, soft lunar light, romantic darkness, silvery glow",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "weather": (list(cls.WEATHER.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weather_prompt",)
    FUNCTION = "set_weather"
    CATEGORY = "Mason's Nodes/Style Master"

    def set_weather(self, prompt, weather):
        weather_desc = self.WEATHER.get(weather, "")
        return (f"{prompt}, {weather_desc}",)


class EraDecadeStyle:
    """Apply era/decade specific aesthetics"""
    
    ERAS = {
        "1950s": "1950s style, vintage pin-up aesthetic, classic glamour, retro",
        "1960s": "1960s style, mod fashion, go-go aesthetic, swinging sixties",
        "1970s": "1970s style, disco era, bohemian, earth tones, vintage",
        "1980s": "1980s style, big hair, neon, bold makeup, MTV era aesthetic",
        "1990s": "1990s style, grunge influence, minimalist, supermodel era",
        "2000s": "2000s style, Y2K aesthetic, low rise, glossy, early digital era",
        "2010s": "2010s style, Instagram aesthetic, natural makeup, modern",
        "2020s": "2020s style, contemporary, current trends, modern aesthetic",
        "victorian": "Victorian era style, period clothing, historical, ornate",
        "art_deco": "Art Deco style, 1920s glamour, geometric patterns, jazz age",
        "retro_futurism": "retro futurism, vintage sci-fi aesthetic, space age",
        "timeless": "timeless style, classic beauty, age-defying elegance",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "era": (list(cls.ERAS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("era_prompt",)
    FUNCTION = "set_era"
    CATEGORY = "Mason's Nodes/Style Master"

    def set_era(self, prompt, era):
        era_desc = self.ERAS.get(era, "")
        return (f"{prompt}, {era_desc}",)


NODE_CLASS_MAPPINGS = {
    "CinematicStyler": CinematicStyler,
    "PhotographerStyle": PhotographerStyle,
    "MoodController": MoodController,
    "ColorGrading": ColorGrading,
    "WeatherAtmosphere": WeatherAtmosphere,
    "EraDecadeStyle": EraDecadeStyle,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CinematicStyler": "🎬 Cinematic Styler",
    "PhotographerStyle": "📸 Photographer Style",
    "MoodController": "🎭 Mood Controller",
    "ColorGrading": "🎨 Color Grading",
    "WeatherAtmosphere": "🌤️ Weather/Atmosphere",
    "EraDecadeStyle": "📅 Era/Decade Style",
}
