"""
Mason Nodes - Anime & Cartoon Character Selector
Extensive database of popular anime/cartoon characters with detailed prompts
"""

class AnimeCharacterSelector:
    """Select from 150+ popular anime/cartoon characters with perfect prompts."""
    
    # Comprehensive character database with detailed appearance prompts
    CHARACTERS = {
        # === NARUTO ===
        "Naruto Uzumaki": "naruto uzumaki, spiky blonde hair, blue eyes, whisker marks on cheeks, orange and black jacket, hidden leaf headband, ninja, determined expression",
        "Sasuke Uchiha": "sasuke uchiha, black spiky hair, dark eyes, pale skin, blue high-collar shirt, uchiha clan symbol, handsome, serious expression",
        "Sakura Haruno": "sakura haruno, pink hair, green eyes, red outfit, hidden leaf headband, beautiful, determined expression",
        "Hinata Hyuga": "hinata hyuga, dark blue hair, lavender byakugan eyes, pale skin, shy expression, beautiful, ninja outfit",
        "Kakashi Hatake": "kakashi hatake, silver spiky hair, mask covering lower face, one sharingan eye, jonin vest, cool demeanor",
        "Itachi Uchiha": "itachi uchiha, long black hair in ponytail, red sharingan eyes, akatsuki cloak, facial lines, handsome, calm expression",
        
        # === ONE PIECE ===
        "Monkey D. Luffy": "monkey d luffy, black messy hair, straw hat, scar under left eye, red vest, blue shorts, cheerful grin, muscular",
        "Roronoa Zoro": "roronoa zoro, green short hair, three earrings on left ear, three swords, green haramaki, muscular, serious expression, scar over left eye",
        "Nami": "nami one piece, orange wavy hair, brown eyes, curvy figure, blue tattoo on left arm, bikini top, beautiful, confident smile",
        "Nico Robin": "nico robin, black hair with bangs, blue eyes, tall slender figure, purple outfit, elegant, mysterious smile",
        "Boa Hancock": "boa hancock, long black hair, blue eyes, extremely beautiful, snake earrings, revealing chinese dress, arrogant expression",
        
        # === DRAGON BALL ===
        "Goku": "son goku, spiky black hair, muscular build, orange gi with blue undershirt, serious battle expression, saiyan warrior",
        "Vegeta": "vegeta, black flame-shaped hair, widow's peak, muscular, blue spandex, white gloves, proud arrogant expression",
        "Bulma": "bulma dragon ball, blue hair, blue eyes, beautiful, scientist, fashionable outfit, confident smile",
        "Android 18": "android 18, blonde bob haircut, blue eyes, beautiful, blue denim jacket, black undershirt, calm expression",
        "Gohan": "adult gohan, black spiky hair, glasses, muscular, purple gi, kind expression",
        
        # === MY HERO ACADEMIA ===
        "Izuku Midoriya": "izuku midoriya deku, green curly hair, freckles, green eyes, u.a. uniform, determined expression",
        "Katsuki Bakugo": "katsuki bakugo, spiky ash blonde hair, red eyes, angry expression, u.a. hero costume, explosive personality",
        "Ochaco Uraraka": "ochaco uraraka, brown bob haircut, pink cheeks, brown eyes, cute, u.a. uniform, cheerful",
        "Shoto Todoroki": "shoto todoroki, half white half red hair, heterochromia eyes, burn scar on left eye, handsome, calm expression",
        "Momo Yaoyorozu": "momo yaoyorozu, long black hair in ponytail, tall, beautiful, mature figure, elegant, u.a. uniform",
        
        # === DEMON SLAYER ===
        "Tanjiro Kamado": "tanjiro kamado, burgundy hair with black tips, scar on forehead, kind eyes, checkered haori, demon slayer uniform, earrings",
        "Nezuko Kamado": "nezuko kamado, long black hair with orange tips, pink eyes, bamboo mouthpiece, pink kimono, demon girl, beautiful",
        "Zenitsu Agatsuma": "zenitsu agatsuma, blonde hair, yellow haori, scared expression, demon slayer uniform",
        "Inosuke Hashibira": "inosuke hashibira, blue hair, boar mask, muscular shirtless, dual swords, wild",
        "Shinobu Kocho": "shinobu kocho, black hair with purple tips in butterfly style, purple eyes, smile, butterfly haori, beautiful",
        "Mitsuri Kanroji": "mitsuri kanroji, pink and green gradient hair, green eyes, busty figure, revealing demon slayer uniform, love pillar",
        
        # === ATTACK ON TITAN ===
        "Eren Yeager": "eren yeager, brown hair, green eyes, survey corps uniform, determined angry expression",
        "Mikasa Ackerman": "mikasa ackerman, short black hair, grey eyes, red scarf, survey corps uniform, beautiful, stoic expression",
        "Levi Ackerman": "levi ackerman, black undercut hair, grey eyes, short stature, survey corps cravat, handsome, bored expression",
        "Historia Reiss": "historia reiss, long blonde hair, blue eyes, petite, beautiful, queen outfit or survey corps uniform",
        "Annie Leonhart": "annie leonhart, blonde hair in bun, blue eyes, hooked nose, cold expression, military uniform",
        
        # === JUJUTSU KAISEN ===
        "Yuji Itadori": "yuji itadori, pink spiky hair, brown eyes, athletic build, jujutsu high uniform, cheerful but serious",
        "Megumi Fushiguro": "megumi fushiguro, black spiky hair, dark eyes, handsome, jujutsu high uniform, serious expression",
        "Nobara Kugisaki": "nobara kugisaki, orange bob hair, confident smirk, jujutsu high uniform, beautiful, fierce",
        "Gojo Satoru": "gojo satoru, white spiky hair, bright blue six eyes, black blindfold around eyes, tall, handsome, cocky smile, black outfit",
        "Maki Zenin": "maki zenin, green ponytail, glasses, athletic figure, jujutsu sorcerer outfit, confident",
        
        # === CHAINSAW MAN ===
        "Denji": "denji chainsaw man, messy blonde hair, shark teeth smile, shirtless with chainsaws coming from head and arms",
        "Power": "power chainsaw man, long blonde hair, red horns, red eyes, sharp teeth, blood fiend, insane expression, beautiful",
        "Makima": "makima chainsaw man, auburn hair in braids, yellow spiral eyes, white shirt, black tie, mysterious smile, beautiful, control devil",
        "Aki Hayakawa": "aki hayakawa, black hair in topknot, blue eyes, handsome, suit, serious expression, devil hunter",
        
        # === BLEACH ===
        "Ichigo Kurosaki": "ichigo kurosaki, orange spiky hair, brown eyes, shinigami black robes, large sword, determined expression",
        "Rukia Kuchiki": "rukia kuchiki, short black hair, violet eyes, petite, shinigami robes, beautiful, noble bearing",
        "Orihime Inoue": "orihime inoue, long orange hair, brown eyes, busty figure, hairpins, school uniform, sweet smile",
        "Rangiku Matsumoto": "rangiku matsumoto, wavy blonde hair, blue eyes, very busty figure, shinigami robes, beauty mark, flirty",
        "Yoruichi Shihoin": "yoruichi shihoin, purple hair in ponytail, dark skin, golden eyes, athletic figure, confident, beautiful",
        
        # === STUDIO GHIBLI ===
        "Chihiro (Spirited Away)": "chihiro spirited away, brown hair in ponytail, brown eyes, young girl, white and pink outfit, brave expression",
        "Howl": "howl moving castle, blonde hair, blue eyes, handsome, flashy wizard outfit, earring, mysterious smile",
        "Sophie": "young sophie moving castle, brunette hair, plain dress, beautiful, gentle expression",
        "San (Princess Mononoke)": "san princess mononoke, black hair, face paint, wolf girl, fierce, wild beauty, fur cape",
        "Nausicaa": "nausicaa, auburn short hair, blue eyes, flight suit, brave, beautiful, princess of the valley",
        
        # === FATE SERIES ===
        "Saber (Artoria)": "saber artoria pendragon, blonde hair in bun, green eyes, blue armored dress, ahoge, regal beauty, serious expression",
        "Rin Tohsaka": "rin tohsaka, black twin tails, aqua eyes, red outfit, tsundere expression, beautiful",
        "Sakura Matou": "sakura matou fate, long purple hair, violet eyes, gentle expression, beautiful, school uniform",
        "Jeanne d'Arc": "jeanne d'arc fate, long blonde hair in braid, violet eyes, armor and flag, holy maiden, beautiful",
        "Scathach": "scathach fate, long purple hair, red eyes, bodysuit, warrior queen, beautiful, confident",
        
        # === EVANGELION ===
        "Rei Ayanami": "rei ayanami, short blue hair, red eyes, pale skin, plugsuit, emotionless expression, mysterious beauty",
        "Asuka Langley": "asuka langley soryu, orange long hair, blue eyes, red plugsuit, tsundere, beautiful, confident",
        "Misato Katsuragi": "misato katsuragi, purple hair, brown eyes, red jacket, cross necklace, mature beauty, confident",
        
        # === SWORD ART ONLINE ===
        "Kirito": "kirito sword art online, black hair, black eyes, black coat, dual swords, handsome, serious",
        "Asuna": "asuna yuuki, long orange-chestnut hair, hazel eyes, white and red outfit, rapier, beautiful, kind smile",
        "Sinon": "sinon sword art online, short teal hair, blue eyes, sniper rifle, cool beauty, confident",
        
        # === RE:ZERO ===
        "Rem": "rem re:zero, short blue hair covering one eye, blue eyes, maid outfit, beautiful, devoted expression",
        "Ram": "ram re:zero, short pink hair, pink eyes, maid outfit, beautiful, confident smirk",
        "Emilia": "emilia re:zero, long silver hair, purple eyes, white and purple outfit, elf ears, beautiful, gentle",
        
        # === KONOSUBA ===
        "Aqua": "aqua konosuba, long blue hair, blue eyes, blue outfit, goddess, beautiful, crying or smug expression",
        "Megumin": "megumin konosuba, short black hair, red eyes, witch hat, eyepatch, crimson demon outfit, cute, dramatic",
        "Darkness": "darkness konosuba, long blonde hair, blue eyes, crusader armor, busty figure, masochistic expression",
        
        # === QUINTESSENTIAL QUINTUPLETS ===
        "Miku Nakano": "miku nakano, long pink hair with headphones, blue eyes, shy expression, school uniform, beautiful",
        "Nino Nakano": "nino nakano, long pink hair with ribbon, blue eyes, tsundere, school uniform, beautiful",
        "Itsuki Nakano": "itsuki nakano, long pink hair with star hairclips, blue eyes, eating, school uniform, cute",
        
        # === OSHI NO KO ===
        "Ai Hoshino": "ai hoshino, long purple hair, star pupils in eyes, idol outfit, beautiful, fake smile, mysterious",
        "Aqua Hoshino": "aqua hoshino oshi no ko, dark hair, dark blue star eye, handsome, actor, serious expression",
        "Ruby Hoshino": "ruby hoshino, blonde hair, pink star eyes, idol outfit, cute, energetic smile",
        "Kana Arima": "kana arima, red hair in twin tails, tsundere expression, actress, cute, competitive",
        
        # === SPY X FAMILY ===
        "Yor Forger": "yor forger, long black hair, red eyes, assassin dress or housewife outfit, beautiful, elegant but deadly",
        "Loid Forger": "loid forger twilight, blonde hair, blue eyes, handsome, spy suit, cool composed expression",
        "Anya Forger": "anya forger, pink hair with hair ornaments, green eyes, child, school uniform, smug heh expression, cute",
        
        # === POKEMON ===
        "Misty": "misty pokemon, orange hair in side ponytail, green eyes, yellow crop top, suspenders, shorts, beautiful trainer",
        "May": "may pokemon, brown hair with bandana, blue eyes, red outfit, beautiful coordinator",
        "Dawn": "dawn pokemon, blue hair, blue eyes, pink outfit, beautiful coordinator",
        "Cynthia": "cynthia pokemon champion, long blonde hair, grey eyes, black outfit, beautiful, mysterious aura",
        "Serena (Pokemon)": "serena pokemon, honey blonde hair, blue eyes, pink outfit, beautiful performer",
        
        # === DISNEY/WESTERN ANIMATION ===
        "Elsa": "elsa frozen, platinum blonde braid, blue eyes, ice dress, ice powers, beautiful queen, elegant",
        "Rapunzel": "rapunzel tangled, very long blonde hair, green eyes, purple dress, beautiful princess, cheerful",
        "Jasmine": "princess jasmine aladdin, long black hair, brown eyes, teal outfit, arabian princess, beautiful",
        "Ariel": "ariel little mermaid, red hair, blue eyes, mermaid tail, beautiful, curious expression",
        "Belle": "belle beauty and the beast, brown hair in ponytail, brown eyes, yellow ball gown, beautiful, bookish",
        "Moana": "moana disney, long wavy black hair, brown eyes, polynesian features, red outfit, brave, beautiful",
        
        # === AVATAR/KORRA ===
        "Azula": "azula avatar, black hair in topknot, golden eyes, fire nation armor, beautiful, cruel smirk, blue fire",
        "Katara": "katara avatar, brown hair with loopies, blue eyes, water tribe blue outfit, waterbender, beautiful",
        "Korra": "korra avatar, brown hair bob, blue eyes, muscular, water tribe outfit, strong, beautiful",
        "Asami Sato": "asami sato legend of korra, long black hair, green eyes, elegant, red lipstick, makeup, beautiful, wealthy",
        
        # === CYBERPUNK EDGERUNNERS ===
        "Lucy (Edgerunners)": "lucy cyberpunk edgerunners, white hair bob, netrunner suit, futuristic, beautiful, mysterious",
        "Rebecca (Edgerunners)": "rebecca cyberpunk edgerunners, pink pigtails, petite, cybernetic enhancements, cute but deadly",
        
        # === MISCELLANEOUS POPULAR ===
        "Zero Two": "zero two darling in the franxx, long pink hair, red horns, teal eyes, red pilot suit, beautiful, playful smile",
        "Hatsune Miku": "hatsune miku vocaloid, long teal twin tails, teal eyes, black and teal outfit, digital idol, beautiful",
        "Tohru (Dragon Maid)": "tohru kobayashi dragon maid, blonde hair, dragon horns and tail, maid outfit, busty, cute, in love expression",
        "Violet Evergarden": "violet evergarden, blonde hair with ribbon, blue eyes, mechanical arms, white dress, beautiful, doll-like, emotionless",
        "Toga Himiko": "toga himiko my hero academia, blonde hair in messy buns, yellow eyes, crazy yandere smile, sailor uniform, knives",
        "Ryuko Matoi": "ryuko matoi kill la kill, black hair with red streak, blue eyes, senketsu sailor uniform, scissor blade, fierce",
        "Satsuki Kiryuin": "satsuki kiryuin, long black hair, thick eyebrows, regal posture, white junketsu outfit, beautiful, overwhelming presence",
        "Erza Scarlet": "erza scarlet fairy tail, long scarlet red hair, brown eyes, armor, beautiful, fierce warrior",
        "Lucy Heartfilia": "lucy heartfilia fairy tail, blonde hair in side ponytail, brown eyes, busty figure, celestial spirits mage, beautiful",
        "Nami (Re:Zero)": "nami one piece, orange hair, brown eyes, curvy, navigator, bikini top, confident",
        "Albedo (Overlord)": "albedo overlord, long black hair, golden eyes, horns and wings, white dress, succubus, beautiful, yandere for ainz",
        "Shalltear Bloodfallen": "shalltear bloodfallen, silver hair, red eyes, gothic lolita vampire, pale, beautiful, crimson dress",
        "Esdeath": "esdeath akame ga kill, long blue hair, blue eyes, general uniform, ice powers, beautiful, sadistic smile",
        "Akame": "akame akame ga kill, long black hair, red eyes, black sailor outfit, murasame sword, beautiful assassin",
        "Kurisu Makise": "kurisu makise steins gate, long auburn hair, violet eyes, lab coat, tsundere genius, beautiful",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        characters = sorted(cls.CHARACTERS.keys())
        return {
            "required": {
                "character": (characters, {"default": characters[0]}),
                "add_quality_tags": ("BOOLEAN", {"default": True}),
                "art_style": (["default", "anime", "realistic anime", "semi-realistic", "high detail"], {"default": "anime"}),
                "clothing": (["default/canon", "nude", "lingerie", "bikini", "topless", "bottomless", "see-through", "micro bikini", "naked apron", "body paint only", "custom"], {"default": "default/canon"}),
            },
            "optional": {
                "custom_additions": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "character_name")
    FUNCTION = "generate"
    CATEGORY = "Mason/Characters"
    
    def generate(self, character, add_quality_tags, art_style, clothing, custom_additions=""):
        prompt = self.CHARACTERS.get(character, character)
        
        # Add style prefix
        styles = {
            "default": "",
            "anime": "anime style, ",
            "realistic anime": "realistic anime style, detailed, ",
            "semi-realistic": "semi-realistic, detailed anime, ",
            "high detail": "highly detailed, intricate, masterpiece, "
        }
        prompt = styles.get(art_style, "") + prompt
        
        # Handle clothing/NSFW options
        clothing_prompts = {
            "default/canon": "",
            "nude": ", completely nude, naked, bare skin, nipples, pussy, uncensored",
            "lingerie": ", wearing sexy lingerie, lace bra and panties, seductive",
            "bikini": ", wearing bikini, swimsuit, beach",
            "topless": ", topless, bare breasts, nipples, no shirt",
            "bottomless": ", bottomless, no pants, no panties, exposed pussy",
            "see-through": ", wearing see-through clothing, visible nipples, transparent fabric",
            "micro bikini": ", wearing micro bikini, barely covered, string bikini, exposed skin",
            "naked apron": ", wearing only an apron, naked apron, bare ass, sideboob",
            "body paint only": ", body paint only, painted skin, no actual clothes, artistic nudity",
            "custom": ""
        }
        prompt += clothing_prompts.get(clothing, "")
        
        # Add quality tags
        if add_quality_tags:
            prompt += ", masterpiece, best quality, highly detailed, beautiful, high resolution"
        
        # Add custom additions
        if custom_additions.strip():
            prompt += f", {custom_additions.strip()}"
        
        return (prompt, character)


class AnimeSeriesSelector:
    """Quick selector by anime series, then character."""
    
    SERIES_CHARACTERS = {
        "Naruto": ["Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", "Hinata Hyuga", "Kakashi Hatake", "Itachi Uchiha"],
        "One Piece": ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Nico Robin", "Boa Hancock"],
        "Dragon Ball": ["Goku", "Vegeta", "Bulma", "Android 18", "Gohan"],
        "My Hero Academia": ["Izuku Midoriya", "Katsuki Bakugo", "Ochaco Uraraka", "Shoto Todoroki", "Momo Yaoyorozu"],
        "Demon Slayer": ["Tanjiro Kamado", "Nezuko Kamado", "Zenitsu Agatsuma", "Inosuke Hashibira", "Shinobu Kocho", "Mitsuri Kanroji"],
        "Attack on Titan": ["Eren Yeager", "Mikasa Ackerman", "Levi Ackerman", "Historia Reiss", "Annie Leonhart"],
        "Jujutsu Kaisen": ["Yuji Itadori", "Megumi Fushiguro", "Nobara Kugisaki", "Gojo Satoru", "Maki Zenin"],
        "Spy x Family": ["Yor Forger", "Loid Forger", "Anya Forger"],
        "Pokemon": ["Misty", "May", "Dawn", "Cynthia", "Serena (Pokemon)"],
        "Fate Series": ["Saber (Artoria)", "Rin Tohsaka", "Sakura Matou", "Jeanne d'Arc", "Scathach"],
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "series": (sorted(cls.SERIES_CHARACTERS.keys()), {"default": "Naruto"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("characters_list",)
    FUNCTION = "list_characters"
    CATEGORY = "Mason/Characters"
    
    def list_characters(self, series):
        chars = self.SERIES_CHARACTERS.get(series, [])
        return (", ".join(chars),)


NODE_CLASS_MAPPINGS = {
    "MasonAnimeCharacterSelector": AnimeCharacterSelector,
    "MasonAnimeSeriesSelector": AnimeSeriesSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonAnimeCharacterSelector": "🎌 Anime Character Selector",
    "MasonAnimeSeriesSelector": "📺 Anime Series Browser",
}
