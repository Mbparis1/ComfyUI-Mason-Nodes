"""
Mason's Smart Prompt Engineering Nodes for ComfyUI
Optimized for SD 1.5 - Prompt weight balancing and enhancement
"""


class PromptWeightBalancer:
    """Auto-adjust (keyword:weight) syntax for SD 1.5"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "emphasis_keyword": ("STRING", {"default": ""}),
                "emphasis_strength": (["subtle (1.1)", "medium (1.2)", "strong (1.3)", "very strong (1.4)"],),
                "de_emphasis_keyword": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weighted_prompt",)
    FUNCTION = "balance"
    CATEGORY = "Mason's Nodes/Smart Prompts"

    def balance(self, prompt, emphasis_keyword, emphasis_strength, de_emphasis_keyword):
        weights = {"subtle (1.1)": 1.1, "medium (1.2)": 1.2, "strong (1.3)": 1.3, "very strong (1.4)": 1.4}
        weight = weights.get(emphasis_strength, 1.2)
        
        result = prompt
        
        # Add emphasis using SD 1.5 syntax (keyword:weight)
        if emphasis_keyword.strip():
            result += f", ({emphasis_keyword}:{weight})"
        
        # De-emphasize using lower weight
        if de_emphasis_keyword.strip():
            result += f", ({de_emphasis_keyword}:0.7)"
        
        return (result,)


class SynonymSuggester:
    """Offer alternative words for variety - SD 1.5 optimized keywords"""
    
    SYNONYMS = {
        "beautiful": ["gorgeous", "stunning", "attractive", "pretty", "lovely"],
        "sexy": ["seductive", "alluring", "sensual", "provocative", "enticing"],
        "young": ["youthful", "fresh-faced", "vibrant", "energetic"],
        "woman": ["lady", "female", "girl", "model"],
        "nude": ["naked", "unclothed", "bare", "exposed"],
        "realistic": ["photorealistic", "lifelike", "natural", "authentic"],
        "detailed": ["intricate", "elaborate", "high-detail", "fine details"],
        "lighting": ["illumination", "light", "lit", "lighting setup"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "keyword": (list(cls.SYNONYMS.keys()),),
                "seed": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("synonym", "all_options")
    FUNCTION = "suggest"
    CATEGORY = "Mason's Nodes/Smart Prompts"

    def suggest(self, keyword, seed):
        import random
        random.seed(seed)
        options = self.SYNONYMS.get(keyword, [keyword])
        chosen = random.choice(options)
        all_opts = ", ".join(options)
        return (chosen, all_opts)


class PromptTranslator:
    """Convert casual text to SD 1.5 prompt-optimized keywords"""
    
    TRANSLATIONS = {
        "good looking": "attractive, beautiful, aesthetically pleasing",
        "hot": "sexy, attractive, alluring, seductive",
        "skinny": "slim, slender, thin, lean body",
        "thick": "curvy, voluptuous, full-figured",
        "fit": "athletic, toned, muscular, fit body",
        "old": "mature, older, aged",
        "pretty face": "beautiful face, attractive features, symmetrical face",
        "nice body": "attractive body, well-proportioned, appealing physique",
        "big boobs": "large breasts, ample bust, full chest",
        "nice butt": "shapely posterior, round buttocks, attractive rear",
        "long legs": "long legs, leggy, elongated legs",
        "good skin": "flawless skin, smooth skin, clear complexion",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "casual_text": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("optimized_prompt",)
    FUNCTION = "translate"
    CATEGORY = "Mason's Nodes/Smart Prompts"

    def translate(self, casual_text):
        result = casual_text.lower()
        for casual, optimized in self.TRANSLATIONS.items():
            if casual in result:
                result = result.replace(casual, optimized)
        return (result,)


class NegativeMirror:
    """Auto-generate negatives from positives for SD 1.5"""
    
    MIRRORS = {
        "detailed": "low detail, blurry, unfocused",
        "realistic": "unrealistic, fake, artificial, cartoon",
        "beautiful": "ugly, unattractive, deformed",
        "young": "old, aged, wrinkled",
        "clear skin": "acne, blemishes, skin imperfections",
        "sharp": "blurry, soft, out of focus",
        "high quality": "low quality, bad quality, poor quality",
        "symmetrical": "asymmetrical, uneven, lopsided",
        "natural": "unnatural, artificial, fake",
        "professional": "amateur, unprofessional",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "positive_prompt": ("STRING", {"default": "", "multiline": True}),
                "add_standard_negatives": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "mirror"
    CATEGORY = "Mason's Nodes/Smart Prompts"

    def mirror(self, positive_prompt, add_standard_negatives):
        negatives = []
        pos_lower = positive_prompt.lower()
        
        for positive, negative in self.MIRRORS.items():
            if positive in pos_lower:
                negatives.append(negative)
        
        if add_standard_negatives:
            negatives.extend([
                "bad anatomy", "bad hands", "extra fingers", "missing fingers",
                "deformed", "mutated", "disfigured", "blurry", "bad quality"
            ])
        
        return (", ".join(negatives),)


NODE_CLASS_MAPPINGS = {
    "PromptWeightBalancer": PromptWeightBalancer,
    "SynonymSuggester": SynonymSuggester,
    "PromptTranslator": PromptTranslator,
    "NegativeMirror": NegativeMirror,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptWeightBalancer": "⚖️ Prompt Weight Balancer",
    "SynonymSuggester": "📖 Synonym Suggester",
    "PromptTranslator": "🔄 Prompt Translator",
    "NegativeMirror": "🪞 Negative Mirror",
}
