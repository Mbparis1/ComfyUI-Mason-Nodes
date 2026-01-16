"""
Mason Nodes - Famous Artist Styles
Apply the styles of famous artists and art movements to your generations
"""

class FamousArtistStyle:
    """Apply famous artist styles to your images."""
    
    ARTISTS = {
        # Classic Masters
        "Leonardo da Vinci": "in the style of Leonardo da Vinci, renaissance, sfumato technique, soft shadows, mysterious atmosphere, Mona Lisa style",
        "Michelangelo": "in the style of Michelangelo, renaissance, sculptural forms, dramatic anatomy, Sistine Chapel style",
        "Rembrandt": "in the style of Rembrandt, chiaroscuro, dramatic lighting, golden age Dutch painting, rich shadows",
        "Caravaggio": "in the style of Caravaggio, tenebrism, dramatic contrast, theatrical lighting, baroque",
        "Vermeer": "in the style of Vermeer, soft natural light, domestic scenes, pearl-like luminosity, Dutch Golden Age",
        "Van Gogh": "in the style of Van Gogh, bold brushstrokes, vibrant colors, expressive, post-impressionist, starry night style",
        "Monet": "in the style of Monet, impressionist, soft light, water reflections, pastel colors, dreamy atmosphere",
        "Klimt": "in the style of Gustav Klimt, art nouveau, gold leaf, decorative patterns, The Kiss style, ornamental",
        "Mucha": "in the style of Alphonse Mucha, art nouveau, decorative, flowing lines, elegant women, ornate borders",
        
        # Modern Masters
        "Salvador Dali": "in the style of Salvador Dali, surrealist, melting forms, dreamlike, bizarre landscapes",
        "Picasso": "in the style of Picasso, cubist, geometric forms, abstract faces, bold colors",
        "Andy Warhol": "in the style of Andy Warhol, pop art, bold colors, high contrast, screen print style",
        "Frida Kahlo": "in the style of Frida Kahlo, surrealist, vibrant colors, symbolic, Mexican folk art influences",
        "Georgia O'Keeffe": "in the style of Georgia O'Keeffe, large flowers, desert landscapes, bold organic forms",
        
        # Contemporary/Digital
        "H.R. Giger": "in the style of H.R. Giger, biomechanical, dark surrealism, alien aesthetic, industrial organic",
        "Frank Frazetta": "in the style of Frank Frazetta, fantasy art, muscular figures, dynamic action, dramatic lighting",
        "Boris Vallejo": "in the style of Boris Vallejo, fantasy art, heroic figures, vibrant colors, mythological",
        "Luis Royo": "in the style of Luis Royo, dark fantasy, sensual, gothic, detailed armor and weapons",
        "Hajime Sorayama": "in the style of Hajime Sorayama, chrome robots, sexy gynoids, hyper-realistic metal, airbrush",
        
        # Anime/Manga Artists
        "Makoto Shinkai": "in the style of Makoto Shinkai, beautiful skies, lens flares, photorealistic anime backgrounds",
        "Studio Ghibli": "in the style of Studio Ghibli, Hayao Miyazaki, warm colors, detailed backgrounds, whimsical",
        "CLAMP": "in the style of CLAMP, elegant long limbs, flowing hair, bishonen, shoujo aesthetic",
        "Yusuke Murata": "in the style of Yusuke Murata, dynamic action, detailed muscles, One Punch Man style",
        "Akira Toriyama": "in the style of Akira Toriyama, Dragon Ball, clean lines, dynamic poses",
        
        # Concept Artists
        "Craig Mullins": "in the style of Craig Mullins, digital painting, atmospheric, cinematic, concept art",
        "Syd Mead": "in the style of Syd Mead, futuristic, sleek design, sci-fi vehicles, Blade Runner",
        "Feng Zhu": "in the style of Feng Zhu, concept art, sci-fi environments, detailed worldbuilding",
        "Artgerm": "in the style of Artgerm, Stanley Lau, beautiful faces, comic book, vibrant colors",
        "Ross Tran": "in the style of Ross Tran, digital art, dynamic lighting, beautiful portraits",
        "WLOP": "in the style of WLOP, ethereal, beautiful women, soft lighting, fantasy, ghostblade",
        "Sakimichan": "in the style of Sakimichan, semi-realistic, beautiful characters, polished, vibrant",
    }
    
    ART_MOVEMENTS = {
        "Renaissance": "renaissance style, classical composition, realistic proportions, religious themes, sfumato",
        "Baroque": "baroque style, dramatic, ornate, rich colors, strong contrast, dynamic composition",
        "Impressionism": "impressionist style, visible brushstrokes, emphasis on light, outdoor scenes, pastel palette",
        "Art Nouveau": "art nouveau style, organic curves, nature motifs, decorative, flowing lines",
        "Art Deco": "art deco style, geometric shapes, bold colors, glamorous, 1920s aesthetic",
        "Surrealism": "surrealist style, dreamlike, bizarre juxtapositions, subconscious imagery",
        "Pop Art": "pop art style, bold colors, commercial imagery, high contrast, comic style",
        "Cyberpunk": "cyberpunk style, neon lights, high tech low life, rain, dystopian future",
        "Steampunk": "steampunk style, Victorian era, brass and copper, gears, steam-powered machinery",
        "Vaporwave": "vaporwave aesthetic, retro 80s, pastel colors, glitch art, nostalgic",
        "Ukiyo-e": "ukiyo-e style, Japanese woodblock print, flat colors, bold outlines, waves",
        "Gothic": "gothic style, dark atmosphere, ornate architecture, mysterious, medieval",
        "Romanticism": "romanticism style, emotional, sublime nature, dramatic landscapes",
        "Rococo": "rococo style, ornate, pastel colors, playful themes, elegant",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        artists = ["None"] + sorted(cls.ARTISTS.keys())
        movements = ["None"] + sorted(cls.ART_MOVEMENTS.keys())
        return {
            "required": {
                "artist": (artists, {"default": "None"}),
                "art_movement": (movements, {"default": "None"}),
                "style_strength": (["subtle", "moderate", "strong"], {"default": "moderate"}),
            },
            "optional": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("styled_prompt",)
    FUNCTION = "apply_style"
    CATEGORY = "Mason/Masterpiece"
    
    def apply_style(self, artist, art_movement, style_strength, base_prompt=""):
        parts = []
        
        if base_prompt.strip():
            parts.append(base_prompt.strip())
        
        strength_prefix = {
            "subtle": "slightly inspired by ",
            "moderate": "",
            "strong": "heavily in "
        }
        prefix = strength_prefix[style_strength]
        
        if artist != "None":
            style_text = self.ARTISTS[artist]
            if prefix:
                style_text = prefix + style_text
            parts.append(style_text)
        
        if art_movement != "None":
            movement_text = self.ART_MOVEMENTS[art_movement]
            if prefix:
                movement_text = prefix + movement_text
            parts.append(movement_text)
        
        return (", ".join(parts),)


class CinematicColorGrading:
    """Apply cinematic color grading looks to your images."""
    
    GRADES = {
        "Teal & Orange": "teal and orange color grading, cinematic, complementary colors, blockbuster look",
        "Bleach Bypass": "bleach bypass look, desaturated, high contrast, gritty, film noir",
        "Cross Process": "cross processed colors, unusual color shifts, vintage, artistic",
        "Golden Hour": "golden hour color grading, warm orange tones, soft shadows, romantic",
        "Blue Hour": "blue hour grading, cool blue tones, twilight mood, serene",
        "Noir": "film noir grading, black and white, high contrast, dramatic shadows, 1940s",
        "Vintage Film": "vintage film look, faded colors, film grain, retro, 70s aesthetic",
        "Cyberpunk Neon": "cyberpunk color grading, neon pink and blue, high saturation, futuristic",
        "Matrix Green": "matrix style grading, green tint, digital rain aesthetic, cyber",
        "Blade Runner": "blade runner color grading, blue and orange neons, rainy, dystopian",
        "Wes Anderson": "wes anderson style, pastel colors, symmetrical, quirky, nostalgic",
        "Michael Bay": "michael bay style, golden warm tones, sunset, epic, explosive",
        "David Fincher": "david fincher style, desaturated, green-yellow tint, dark, moody",
        "Zack Snyder": "zack snyder style, desaturated, muted colors, dramatic, 300 style",
        "Euphoria": "euphoria tv style, vibrant neons, purple and pink, party atmosphere, glitter",
        "Stranger Things": "stranger things style, warm 80s colors, nostalgic, supernatural glow",
        "Natural": "natural color grading, true to life colors, balanced exposure",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "color_grade": (list(cls.GRADES.keys()), {"default": "Teal & Orange"}),
            },
            "optional": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("graded_prompt",)
    FUNCTION = "apply_grade"
    CATEGORY = "Mason/Masterpiece"
    
    def apply_grade(self, color_grade, base_prompt=""):
        parts = []
        if base_prompt.strip():
            parts.append(base_prompt.strip())
        parts.append(self.GRADES[color_grade])
        return (", ".join(parts),)


class ProfessionalLighting:
    """Professional photography and cinema lighting setups."""
    
    SETUPS = {
        # Studio Lighting
        "Rembrandt": "Rembrandt lighting, triangle of light on cheek, dramatic, portrait classic",
        "Rembrandt Portrait": "Rembrandt lighting, triangle of light on cheek, dramatic, portrait classic, studio portrait",
        "Butterfly": "butterfly lighting, shadow under nose, glamour, beauty photography",
        "Loop": "loop lighting, soft shadow from nose, flattering, portrait",
        "Split": "split lighting, half face lit, dramatic, moody, artistic",
        "Broad": "broad lighting, lit side toward camera, flattering, wider face",
        "Short": "short lighting, lit side away from camera, slimming, dramatic",
        
        # Natural Lighting
        "Golden Hour": "golden hour sunlight, warm directional light, long shadows, romantic",
        "Blue Hour": "blue hour lighting, cool ambient light, twilight, serene",
        "Overcast": "overcast soft light, diffused, no harsh shadows, even illumination",
        "Dappled": "dappled sunlight through trees, natural patterns, forest light",
        "Backlit Silhouette": "backlit, silhouette, rim light, dramatic contrast",
        "Window Light": "natural window light, soft, directional, indoor portrait",
        
        # Cinematic Lighting
        "Three Point": "three point lighting setup, key fill and back light, professional",
        "High Key": "high key lighting, minimal shadows, bright, airy, cheerful",
        "Low Key": "low key lighting, dominant shadows, moody, dramatic, mysterious",
        "Chiaroscuro": "chiaroscuro lighting, strong contrast, renaissance, dramatic",
        "Noir": "film noir lighting, harsh shadows, venetian blinds effect, mysterious",
        
        # Creative Lighting
        "Neon Glow": "neon lighting, colorful glow, cyberpunk, night club",
        "Ring Light": "ring light, even face illumination, catchlights, beauty",
        "Colored Gel": "colored gel lighting, creative colors, artistic, fashion",
        "Practical Lights": "practical lighting, lamps candles in scene, cozy, atmospheric",
        "Volumetric": "volumetric lighting, god rays, light beams, atmospheric, dramatic",
        "Rim Light": "strong rim lighting, glowing edges, separation from background",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "lighting_setup": (list(cls.SETUPS.keys()), {"default": "Rembrandt"}),
            },
            "optional": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lit_prompt",)
    FUNCTION = "apply_lighting"
    CATEGORY = "Mason/Masterpiece"
    
    def apply_lighting(self, lighting_setup, base_prompt=""):
        parts = []
        if base_prompt.strip():
            parts.append(base_prompt.strip())
        parts.append(self.SETUPS[lighting_setup])
        return (", ".join(parts),)


class CompositionGuide:
    """Apply professional composition techniques."""
    
    COMPOSITIONS = {
        "Rule of Thirds": "rule of thirds composition, subject off-center, balanced",
        "Golden Ratio": "golden ratio composition, fibonacci spiral, harmonious",
        "Centered": "centered composition, symmetrical, balanced, powerful",
        "Leading Lines": "leading lines composition, lines drawing eye to subject",
        "Framing": "natural framing, subject framed by elements, focused",
        "Negative Space": "negative space composition, minimalist, breathing room",
        "Diagonal": "diagonal composition, dynamic, movement, energy",
        "Triangle": "triangular composition, stable, classical, three points",
        "S-Curve": "s-curve composition, flowing, elegant, eye movement",
        "Fill Frame": "fill the frame, close crop, intimate, detailed",
        "Symmetry": "symmetrical composition, mirror balance, architectural",
        "Asymmetry": "asymmetrical balance, dynamic tension, interesting",
        "Layers": "layered composition, foreground midground background, depth",
        "Pattern Break": "pattern with focal point break, attention grabbing",
        "Portrait Close-Up": "close-up portrait composition, face focus, intimate framing",
    }
    
    PERSPECTIVES = {
        "Eye Level": "eye level perspective, natural, relatable",
        "Low Angle": "low angle shot, looking up, powerful, heroic",
        "High Angle": "high angle shot, looking down, vulnerable, overview",
        "Dutch Angle": "dutch angle, tilted frame, tension, unease",
        "Bird's Eye": "bird's eye view, directly above, map-like",
        "Worm's Eye": "worm's eye view, extreme low angle, dramatic",
        "Over Shoulder": "over the shoulder shot, connection, conversation",
        "POV": "point of view shot, first person perspective, immersive",
        "shallow": "shallow depth of field, background blur, subject isolation",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "composition": (list(cls.COMPOSITIONS.keys()), {"default": "Rule of Thirds"}),
                "perspective": (list(cls.PERSPECTIVES.keys()), {"default": "Eye Level"}),
            },
            "optional": {
                "base_prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("composed_prompt",)
    FUNCTION = "apply_composition"
    CATEGORY = "Mason/Masterpiece"
    
    def apply_composition(self, composition, perspective, base_prompt=""):
        parts = []
        if base_prompt.strip():
            parts.append(base_prompt.strip())
        parts.append(self.COMPOSITIONS[composition])
        parts.append(self.PERSPECTIVES[perspective])
        return (", ".join(parts),)


NODE_CLASS_MAPPINGS = {
    "MasonFamousArtistStyle": FamousArtistStyle,
    "MasonCinematicColorGrading": CinematicColorGrading,
    "MasonProfessionalLighting": ProfessionalLighting,
    "MasonCompositionGuide": CompositionGuide,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonFamousArtistStyle": "🎨 Famous Artist Style",
    "MasonCinematicColorGrading": "🎬 Cinematic Color Grading",
    "MasonProfessionalLighting": "💡 Professional Lighting",
    "MasonCompositionGuide": "📐 Composition Guide",
}
