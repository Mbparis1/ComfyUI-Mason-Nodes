"""
Mason Nodes - Celebrity & Real Person Selector
Extensive database of celebrities with detailed appearance prompts
"""

class CelebritySelector:
    """Select from 100+ celebrities with accurate appearance prompts."""
    
    # Comprehensive celebrity database with detailed appearance prompts
    CELEBRITIES = {
        # === ACTORS - FEMALE ===
        "Scarlett Johansson": "scarlett johansson, blonde wavy hair, green eyes, full lips, hourglass figure, beautiful actress, elegant, hollywood star",
        "Margot Robbie": "margot robbie, blonde hair, blue eyes, beautiful smile, australian actress, stunning figure, flawless skin, hollywood beauty",
        "Gal Gadot": "gal gadot, long dark brown hair, brown eyes, tall athletic figure, israeli beauty, wonder woman actress, elegant",
        "Ana de Armas": "ana de armas, brunette hair, hazel eyes, cuban beauty, stunning face, full lips, beautiful actress",
        "Sydney Sweeney": "sydney sweeney, blonde hair, blue eyes, curvy figure, beautiful, young actress, euphoria star",
        "Zendaya": "zendaya, brown skin, curly brown hair, tall slender, beautiful, fashion icon, actress",
        "Emma Watson": "emma watson, brunette hair, brown eyes, elegant beauty, british actress, refined features, beautiful",
        "Jennifer Lawrence": "jennifer lawrence, blonde hair, blue eyes, beautiful american actress, natural beauty, expressive",
        "Alexandra Daddario": "alexandra daddario, long dark hair, striking blue eyes, beautiful actress, stunning features",
        "Elizabeth Olsen": "elizabeth olsen, strawberry blonde hair, blue eyes, beautiful, elegant actress, expressive eyes",
        "Natalie Portman": "natalie portman, brunette hair, brown eyes, petite elegant, beautiful actress, refined features",
        "Anne Hathaway": "anne hathaway, dark brown hair, brown eyes, beautiful smile, tall, elegant actress",
        "Blake Lively": "blake lively, long blonde hair, blue eyes, tall statuesque, gorgeous, fashion icon",
        "Emilia Clarke": "emilia clarke, dark brown hair, green eyes, expressive face, british actress, beautiful smile",
        "Megan Fox": "megan fox, long black hair, blue eyes, full lips, stunning figure, iconic beauty",
        "Jessica Alba": "jessica alba, brown hair, brown eyes, latina beauty, stunning figure, flawless skin",
        "Jennifer Aniston": "jennifer aniston, blonde hair, blue eyes, beautiful smile, timeless beauty, fit figure",
        "Angelina Jolie": "angelina jolie, dark brown hair, blue eyes, full lips, high cheekbones, iconic beauty",
        "Kate Upton": "kate upton, blonde hair, blue eyes, curvy figure, model, all american beauty",
        "Emily Ratajkowski": "emily ratajkowski, brunette hair, brown eyes, stunning figure, model, beautiful face",
        
        # === ACTORS - MALE ===
        "Chris Hemsworth": "chris hemsworth, blonde hair, blue eyes, muscular build, handsome, australian actor, thor",
        "Henry Cavill": "henry cavill, dark hair, blue eyes, chiseled jaw, muscular, british actor, handsome",
        "Ryan Gosling": "ryan gosling, blonde hair, blue eyes, handsome, charming smile, hollywood actor",
        "Jason Momoa": "jason momoa, long dark hair, brown eyes, muscular, tattoos, hawaiian, rugged handsome",
        "Timothee Chalamet": "timothee chalamet, curly brown hair, green eyes, youthful handsome, slim, artistic",
        "Tom Holland": "tom holland, brown hair, brown eyes, youthful, british actor, fit, spider-man",
        "Zac Efron": "zac efron, brown hair, blue eyes, muscular, all american, handsome smile",
        "Leonardo DiCaprio": "leonardo dicaprio, blonde hair, blue eyes, classic handsome, hollywood star",
        "Brad Pitt": "brad pitt, blonde hair, blue eyes, chiseled features, hollywood icon, handsome",
        "Chris Evans": "chris evans, brown hair, blue eyes, muscular, all american, captain america, handsome",
        
        # === MUSICIANS - FEMALE ===
        "Taylor Swift": "taylor swift, blonde hair, blue eyes, tall slender, beautiful singer, elegant style",
        "Ariana Grande": "ariana grande, long brown ponytail, brown eyes, petite, beautiful singer, signature style",
        "Beyonce": "beyonce, blonde hair, brown eyes, curves, powerful beauty, queen, iconic singer",
        "Rihanna": "rihanna, dark skin, various hairstyles, stunning beauty, fashion icon, barbadian singer",
        "Dua Lipa": "dua lipa, long dark hair, striking features, british albanian singer, model looks, beautiful",
        "Selena Gomez": "selena gomez, brown hair, brown eyes, latina beauty, singer, beautiful smile",
        "Billie Eilish": "billie eilish, distinctive eyes, various hair colors, unique style, young singer",
        "Lady Gaga": "lady gaga, blonde hair, striking features, artistic, iconic singer, expressive",
        "Katy Perry": "katy perry, dark hair, blue eyes, curvy, beautiful singer, playful expression",
        "Miley Cyrus": "miley cyrus, various hairstyles, blue eyes, slender, bold expression, singer",
        "Shakira": "shakira, blonde wavy hair, colombian beauty, dancer figure, beautiful singer",
        "Jennifer Lopez": "jennifer lopez, brown hair, brown eyes, latina beauty, toned figure, iconic singer",
        "Nicki Minaj": "nicki minaj, various colorful wigs, curves, bold makeup, rapper, striking",
        "Cardi B": "cardi b, various hairstyles, curvy figure, bold makeup, rapper, expressive",
        "Doja Cat": "doja cat, various hairstyles, unique style, beautiful singer, expressive eyes",
        
        # === MUSICIANS - MALE ===
        "Harry Styles": "harry styles, curly brown hair, green eyes, british singer, stylish, handsome",
        "The Weeknd": "the weeknd, dark hair, canadian singer, stylish, handsome, artistic",
        "Post Malone": "post malone, tattoos, unique look, singer, distinctive style",
        "Justin Bieber": "justin bieber, brown hair, singer, stylish, canadian, youthful",
        "Bruno Mars": "bruno mars, curly black hair, hawaiian puerto rican, singer, stylish, charismatic",
        
        # === MODELS ===
        "Kendall Jenner": "kendall jenner, dark hair, tall slender, supermodel, beautiful, high fashion",
        "Gigi Hadid": "gigi hadid, blonde hair, blue eyes, supermodel, beautiful, california girl",
        "Bella Hadid": "bella hadid, dark hair, striking features, supermodel, high fashion, beautiful",
        "Adriana Lima": "adriana lima, dark hair, blue eyes, brazilian supermodel, stunning beauty, angel",
        "Cara Delevingne": "cara delevingne, blonde hair, thick eyebrows, british model, striking features",
        "Barbara Palvin": "barbara palvin, brunette, blue eyes, hungarian model, sweet face, beautiful",
        "Hailey Bieber": "hailey bieber, blonde hair, model, stylish, beautiful, fit",
        "Alexis Ren": "alexis ren, blonde hair, blue eyes, fitness model, toned, beautiful smile",
        
        # === KOREAN CELEBRITIES ===
        "Jisoo (BLACKPINK)": "jisoo blackpink, long black hair, korean beauty, singer, elegant, beautiful smile",
        "Jennie (BLACKPINK)": "jennie blackpink, various hairstyles, korean singer, charismatic, beautiful",
        "Rose (BLACKPINK)": "rose blackpink, blonde hair, korean australian singer, slender, beautiful",
        "Lisa (BLACKPINK)": "lisa blackpink, thai korean singer, dancer, beautiful, stylish",
        "IU": "iu korean singer, brown hair, cute face, beautiful, actress, elegant",
        "Tzuyu (TWICE)": "tzuyu twice, long dark hair, taiwanese beauty, tall, stunning, singer",
        "Irene (Red Velvet)": "irene red velvet, dark hair, korean beauty, leader, stunning visuals",
        "V (BTS)": "v bts kim taehyung, handsome korean singer, various hairstyles, artistic",
        "Jungkook (BTS)": "jungkook bts, dark hair, korean singer, handsome, muscular, youthful",
        "Jimin (BTS)": "jimin bts, various hair colors, korean singer, dancer, handsome, expressive",
        
        # === JAPANESE CELEBRITIES ===
        "Satomi Ishihara": "satomi ishihara, japanese actress, long dark hair, beautiful smile, elegant",
        "Yui Aragaki": "yui aragaki, japanese actress, cute face, beautiful, natural beauty",
        "Suzu Hirose": "suzu hirose, japanese actress, young beautiful, natural features",
        
        # === INFLUENCERS & INTERNET PERSONALITIES ===
        "Kim Kardashian": "kim kardashian, dark hair, brown eyes, curvy figure, iconic, glamorous makeup",
        "Kylie Jenner": "kylie jenner, various hair colors, full lips, curvy, businesswoman, glamorous",
        "Addison Rae": "addison rae, brunette hair, tiktok star, beautiful smile, all american",
        "Pokimane": "pokimane, dark hair, moroccan canadian, streamer, natural beauty, cute",
        "Valkyrae": "valkyrae, dark hair, filipina american, streamer, beautiful, gaming",
        
        # === ATHLETES ===
        "Paige Spiranac": "paige spiranac, blonde hair, blue eyes, golfer, athletic, beautiful smile",
        "Alex Morgan": "alex morgan, brunette hair, athletic, soccer player, beautiful, fit",
        "Simone Biles": "simone biles, dark skin, gymnast, athletic, powerful, beautiful",
        "Serena Williams": "serena williams, dark skin, athletic, tennis player, powerful, beautiful",
        
        # === CLASSIC ICONS ===
        "Marilyn Monroe": "marilyn monroe, platinum blonde hair, iconic beauty, red lips, vintage glamour",
        "Audrey Hepburn": "audrey hepburn, dark hair, elegant, classic beauty, timeless style, refined",
        "Elizabeth Taylor": "elizabeth taylor, dark hair, violet eyes, classic hollywood beauty, glamorous",
        "Grace Kelly": "grace kelly, blonde hair, blue eyes, elegant, princess of monaco, refined beauty",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        celebrities = sorted(cls.CELEBRITIES.keys())
        return {
            "required": {
                "celebrity": (celebrities, {"default": celebrities[0]}),
                "add_quality_tags": ("BOOLEAN", {"default": True}),
                "style": (["photorealistic", "artistic portrait", "glamour", "casual", "professional"], {"default": "photorealistic"}),
                "clothing": (["default", "nude", "lingerie", "bikini", "topless", "bottomless", "see-through", "wet t-shirt", "boudoir", "custom"], {"default": "default"}),
            },
            "optional": {
                "custom_additions": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "celebrity_name")
    FUNCTION = "generate"
    CATEGORY = "Mason/Characters"
    
    def generate(self, celebrity, add_quality_tags, style, clothing, custom_additions=""):
        prompt = self.CELEBRITIES.get(celebrity, celebrity)
        
        # Add style prefix
        styles = {
            "photorealistic": "photorealistic, 8k uhd, realistic photo, ",
            "artistic portrait": "artistic portrait, painterly, ",
            "glamour": "glamour photography, studio lighting, ",
            "casual": "candid photo, natural lighting, ",
            "professional": "professional photoshoot, studio lighting, "
        }
        prompt = styles.get(style, "") + prompt
        
        # Handle clothing/NSFW options
        clothing_prompts = {
            "default": "",
            "nude": ", completely nude, naked, bare skin, nipples, pussy, full frontal nudity, uncensored",
            "lingerie": ", wearing sexy lingerie, lace bra and panties, seductive pose, bedroom",
            "bikini": ", wearing bikini, swimsuit, beach, wet skin",
            "topless": ", topless, bare breasts, nipples visible, no top",
            "bottomless": ", bottomless, no pants, no panties, exposed pussy",
            "see-through": ", wearing see-through dress, visible nipples, transparent fabric, no bra",
            "wet t-shirt": ", wet t-shirt, soaked fabric, visible nipples, clinging to body",
            "boudoir": ", boudoir photoshoot, intimate, sexy pose, bedroom setting, sensual",
            "custom": ""
        }
        prompt += clothing_prompts.get(clothing, "")
        
        # Add quality tags
        if add_quality_tags:
            prompt += ", masterpiece, best quality, highly detailed, sharp focus, professional photography"
        
        # Add custom additions
        if custom_additions.strip():
            prompt += f", {custom_additions.strip()}"
        
        return (prompt, celebrity)


class CelebrityCategorySelector:
    """Browse celebrities by category."""
    
    CATEGORIES = {
        "Actresses": [
            "Scarlett Johansson", "Margot Robbie", "Gal Gadot", "Ana de Armas",
            "Sydney Sweeney", "Zendaya", "Emma Watson", "Alexandra Daddario",
            "Elizabeth Olsen", "Megan Fox"
        ],
        "Musicians": [
            "Taylor Swift", "Ariana Grande", "Beyonce", "Rihanna", "Dua Lipa",
            "Selena Gomez", "Lady Gaga", "Shakira", "Jennifer Lopez"
        ],
        "Models": [
            "Kendall Jenner", "Gigi Hadid", "Bella Hadid", "Adriana Lima",
            "Barbara Palvin", "Cara Delevingne", "Alexis Ren"
        ],
        "K-Pop Stars": [
            "Jisoo (BLACKPINK)", "Jennie (BLACKPINK)", "Rose (BLACKPINK)",
            "Lisa (BLACKPINK)", "IU", "Tzuyu (TWICE)", "Irene (Red Velvet)"
        ],
        "Male Actors": [
            "Chris Hemsworth", "Henry Cavill", "Ryan Gosling", "Jason Momoa",
            "Timothee Chalamet", "Tom Holland", "Zac Efron"
        ],
        "Influencers": [
            "Kim Kardashian", "Kylie Jenner", "Addison Rae", "Pokimane"
        ],
        "Classic Icons": [
            "Marilyn Monroe", "Audrey Hepburn", "Elizabeth Taylor", "Grace Kelly"
        ]
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "category": (sorted(cls.CATEGORIES.keys()), {"default": "Actresses"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("celebrities_in_category",)
    FUNCTION = "list_celebrities"
    CATEGORY = "Mason/Characters"
    
    def list_celebrities(self, category):
        celebs = self.CATEGORIES.get(category, [])
        return (", ".join(celebs),)


# Combined all-in-one selector
class CharacterMasterSelector:
    """One node to select from ALL characters - anime, cartoon, and celebrity."""
    
    @classmethod
    def INPUT_TYPES(cls):
        # Combine all characters
        all_chars = {}
        all_chars.update({f"[ANIME] {k}": v for k, v in AnimeCharacterSelector.CHARACTERS.items()} if hasattr(AnimeCharacterSelector, 'CHARACTERS') else {})
        all_chars.update({f"[CELEB] {k}": v for k, v in CelebritySelector.CELEBRITIES.items()})
        
        return {
            "required": {
                "character": (sorted(all_chars.keys()), {"default": sorted(all_chars.keys())[0]}),
                "add_quality": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate"
    CATEGORY = "Mason/Characters"
    
    def generate(self, character, add_quality):
        # Get from appropriate database
        if character.startswith("[ANIME]"):
            name = character.replace("[ANIME] ", "")
            from .anime_character_nodes import AnimeCharacterSelector
            prompt = AnimeCharacterSelector.CHARACTERS.get(name, name)
        else:
            name = character.replace("[CELEB] ", "")
            prompt = CelebritySelector.CELEBRITIES.get(name, name)
        
        if add_quality:
            prompt += ", masterpiece, best quality, highly detailed"
        
        return (prompt,)


NODE_CLASS_MAPPINGS = {
    "MasonCelebritySelector": CelebritySelector,
    "MasonCelebrityCategorySelector": CelebrityCategorySelector,
    "MasonCharacterMasterSelector": CharacterMasterSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonCelebritySelector": "⭐ Celebrity Selector",
    "MasonCelebrityCategorySelector": "📂 Celebrity Categories",
    "MasonCharacterMasterSelector": "👤 Master Character Selector (All)",
}
