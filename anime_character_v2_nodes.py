"""
Mason Nodes - Anime & Cartoon Character Selector V2
Massive database of 300+ characters from anime, cartoons, and animation
With highly detailed prompts for accurate character recreation
"""

class AnimeCharacterSelectorV2:
    """Select from 300+ anime and cartoon characters with ultra-detailed prompts."""
    
    CHARACTERS = {
        # ============================================
        # NARUTO SERIES
        # ============================================
        "Naruto Uzumaki": "naruto uzumaki, young man, spiky bright blonde hair, ocean blue eyes, three whisker marks on each cheek, orange and black tracksuit jacket with white collar, hidden leaf village headband on forehead, tanned skin, determined confident expression, ninja, athletic build",
        "Naruto (Sage Mode)": "naruto uzumaki sage mode, blonde spiky hair, orange pigmentation around eyes, yellow toad-like eyes with horizontal pupils, orange sage coat, scroll on back, powerful aura",
        "Sasuke Uchiha": "sasuke uchiha, young man, spiky black hair with blue tint styled back, dark onyx eyes, pale fair skin, handsome sharp features, high-collar blue shirt, uchiha clan crest on back, stoic serious expression, lean muscular build",
        "Sasuke (Rinnegan)": "sasuke uchiha adult, long black hair covering left eye, purple rinnegan in left eye, red sharingan in right eye, black cloak, mature handsome face, missing left arm",
        "Sakura Haruno": "sakura haruno, young woman, bright pink short hair with bangs, large green eyes, fair skin, red qipao dress sleeveless, forehead protector as headband, petite figure, determined expression",
        "Sakura (Adult)": "sakura haruno adult, pink hair shoulder length, green eyes, diamond seal on forehead, red sleeveless top, black shorts, medical ninja, mature beautiful woman",
        "Hinata Hyuga": "hinata hyuga, young woman, long dark indigo blue hair with hime cut bangs, pale lavender byakugan eyes, no pupils, very pale porcelain skin, shy gentle expression, lavender and cream jacket, petite curvy figure, beautiful",
        "Kakashi Hatake": "kakashi hatake, adult man, gravity-defying silver white spiky hair, black mask covering lower face, one visible dark eye, hidden leaf headband covering left sharingan eye, jonin vest green, mysterious cool demeanor, lean muscular",
        "Itachi Uchiha": "itachi uchiha, young adult man, long black hair in low ponytail, red mangekyo sharingan eyes, pronounced tear troughs under eyes, handsome stoic face, akatsuki black cloak with red clouds, forehead protector with slash",
        "Tsunade": "tsunade senju, adult woman, long straight blonde hair in two low ponytails, honey brown eyes, purple diamond seal on forehead, very large bust, green haori jacket, grey kimono-style blouse, beautiful mature woman, hokage",
        "Jiraiya": "jiraiya, older adult man, long spiky white hair in ponytail, red face paint lines from eyes to chin, headband with horns, green short kimono, mesh armor, large muscular build, perverted sage",
        "Temari": "temari, young woman, blonde hair in four spiky ponytails, teal green eyes, tanned skin, black battle kimono, giant iron fan weapon, confident fierce expression, athletic figure",
        "Ino Yamanaka": "ino yamanaka, young woman, long platinum blonde hair in high ponytail with bangs covering right eye, blue eyes, purple crop top and skirt, beautiful slender figure, confident",
        
        # ============================================
        # ONE PIECE
        # ============================================
        "Monkey D. Luffy": "monkey d luffy, young man, short messy black hair, round black eyes, scar under left eye, straw hat with red band, red open vest showing chest, blue shorts, sandals, big cheerful grin showing teeth, athletic rubber body",
        "Luffy (Gear 5)": "luffy gear 5, white hair and clothes, laughing expression, rubber sun god nika form, cartoon-like appearance, white flame-like hair, joyful powerful aura",
        "Roronoa Zoro": "roronoa zoro, young man, short moss green hair, three gold earrings on left ear, scar over left closed eye, three swords style, green haramaki waist sash, open dark green coat, extremely muscular, serious fierce expression",
        "Zoro (Post-Timeskip)": "roronoa zoro post timeskip, green hair, scar over left eye now closed, one eye, muscular, green robe open chest, three swords, bandana sometimes on head",
        "Nami": "nami one piece, young woman, long wavy orange hair, large brown eyes, blue tattoo pinwheel and tangerine on left upper arm, very curvy hourglass figure, large bust, bikini top and jeans, log pose on wrist, beautiful navigator",
        "Nico Robin": "nico robin, adult woman, long straight black hair with bangs, blue eyes, tall slender elegant figure, purple or black dress, cowgirl hat sometimes, mature intelligent beauty, calm mysterious smile, archaeologist",
        "Boa Hancock": "boa hancock, adult woman, very long straight black hair past waist, large blue eyes, earrings, extremely beautiful face, arrogant expression, snake earrings, very tall, extremely curvaceous figure, qipao-style dress, pirate empress, love-love fruit powers",
        "Nefertari Vivi": "nefertari vivi, young woman, long wavy light blue hair, brown eyes, slender figure, princess of alabasta, dancer outfit or royal dress, kind gentle expression",
        "Yamato": "yamato one piece, young woman, long white hair with cyan streaks, turquoise eyes, oni horns red and white, very tall muscular, sideboob revealing outfit, carries large kanabo club, wants to be like oden",
        "Perona": "perona one piece, young woman, long light pink hair in twin tails, red eyes, gothic lolita black and red dress, crown, umbrella, cute creepy gothic style, ghost princess",
        
        # ============================================
        # DRAGON BALL SERIES
        # ============================================
        "Goku": "son goku, adult man, wild spiky black hair, black eyes, muscular athletic build, orange martial arts gi with blue undershirt, blue wristbands and boots, kind determined expression, saiyan warrior",
        "Goku (Super Saiyan)": "goku super saiyan, golden spiky hair standing up, teal green eyes, golden aura, orange gi, extremely muscular, powerful fierce expression",
        "Goku (Ultra Instinct)": "goku ultra instinct, silver white spiky hair, silver eyes, calm serene expression, shirtless or damaged gi, divine silver aura",
        "Vegeta": "vegeta, adult man, black flame-shaped spiky hair with widow's peak, black eyes, shorter stature but extremely muscular, blue spandex bodysuit, white gloves and boots, proud arrogant scowl, saiyan prince",
        "Vegeta (Super Saiyan Blue)": "vegeta super saiyan blue, blue spiky hair, blue aura, blue eyes, muscular, saiyan battle armor or blue gi",
        "Bulma": "bulma briefs, adult woman, short or long blue hair (varies), blue eyes, genius scientist, fashionable outfits, beautiful curvy figure, capsule corp heiress, confident smart expression",
        "Android 18": "android 18, adult woman, shoulder-length blonde hair, icy blue eyes, beautiful cold expression, striped long-sleeve shirt and vest, jeans and boots, slender athletic figure, cyborg",
        "Chi-Chi": "chi chi dragon ball, adult woman, black hair in bun, black eyes, chinese-style dress, housewife, former martial artist, goku's wife, beautiful but fierce temper",
        "Videl": "videl satan, young woman, short black hair or long in pigtails, blue eyes, athletic figure, white t-shirt and shorts, tomboy martial artist, determined expression",
        "Caulifla": "caulifla dragon ball super, young woman, spiky black hair swept back, black eyes, pink tube top showing midriff, purple baggy pants, confident cocky expression, saiyan from universe 6",
        "Kale": "kale dragon ball super, young woman, black hair in ponytail, black eyes, shy expression normally, red top and skirt, saiyan from universe 6, legendary super saiyan form",
        "Kefla": "kefla, fusion of caulifla and kale, wild spiky black and green hair, fierce expression, red and green outfit, extremely powerful, muscular feminine build",
        
        # ============================================  
        # MY HERO ACADEMIA
        # ============================================
        "Izuku Midoriya": "izuku midoriya deku, young man, messy curly dark green hair, large green eyes with white pupils, freckles on cheeks, u.a. high school uniform or green hero costume, athletic build, determined kind expression, one for all quirk",
        "Katsuki Bakugo": "katsuki bakugo, young man, spiky ash blonde hair, sharp red eyes, aggressive angry expression, black tanktop, muscular build, explosion quirk, hero costume with grenade gauntlets",
        "Shoto Todoroki": "shoto todoroki, young man, split hair half white half red, heterochromia left eye turquoise right eye grey, burn scar over left eye, handsome stoic expression, tall lean muscular, ice and fire quirk, hero costume half white half blue",
        "Ochaco Uraraka": "ochaco uraraka uravity, young woman, short brown bob hair, rosy pink permanent blush on cheeks, brown eyes, cute round face, pink and black hero suit, petite curvy figure, cheerful bubbly expression",
        "Momo Yaoyorozu": "momo yaoyorozu creati, young woman, long black hair in spiky ponytail, onyx eyes tall statuesque figure, very curvaceous, red leotard hero costume revealing for quirk use, mature elegant beauty, intelligent expression",
        "Tsuyu Asui": "tsuyu asui froppy, young woman, long dark green hair, very large round black eyes, wide mouth frog-like, green and black wetsuit hero costume, petite, frog quirk, calm expression",
        "Mina Ashido": "mina ashido pinky, young woman, short fluffy pink hair, black sclera with yellow irises, pink skin, athletic dancer body, purple and turquoise hero costume, cheerful energetic, acid quirk",
        "Kyoka Jiro": "kyoka jiro earphone jack, young woman, short dark purple hair in asymmetric cut, dark purple eyes, earphone jack earlobes, black choker, punk rock aesthetic, slender figure, cool reserved expression",
        "Nejire Hado": "nejire hado, young woman, long periwinkle blue hair in spirals, bright blue eyes, cheerful curious expression, blue hero costume, curvaceous figure, wave quirk, big three member",
        "Mirko": "mirko rumi usagiyama, adult woman, long white hair, dark skin, red eyes, rabbit ears, extremely muscular athletic body, white and purple leotard hero costume, fierce confident expression, rabbit hero",
        "Mt. Lady": "mt lady yu takeyama, adult woman, long creamy blonde hair in two tails, purple eyes, very curvaceous voluptuous figure, purple and cream skintight hero costume with horned mask, flirty attention-seeking",
        "Midnight": "midnight nemuri kayama, adult woman, long wild dark blue hair, blue eyes, very curvaceous mature body, revealing cream and purple dominatrix-style hero costume, handcuffs, seductive expression",
        
        # ============================================
        # DEMON SLAYER
        # ============================================
        "Tanjiro Kamado": "tanjiro kamado, young man, burgundy hair with black tips in ponytail, red eyes, kind determined expression, scar on forehead checkered pattern from fire, checkered green and black haori over demon slayer uniform, hanafuda earrings",
        "Nezuko Kamado": "nezuko kamado, young woman, long black hair with orange tips, pink eyes, bamboo muzzle in mouth, pink kimono with hemp leaf pattern, demon girl, petite beautiful, pink ribbon in hair, long nails",
        "Zenitsu Agatsuma": "zenitsu agatsuma, young man, short blonde hair, scared anxious expression normally, yellow and orange gradient haori, demon slayer uniform, cowardly but powerful when sleeping",
        "Inosuke Hashibira": "inosuke hashibira, young man, feminine beautiful face, black to blue gradient hair, blue eyes, usually wears boar head mask, shirtless showing muscular torso, dual serrated nichirin blades, wild personality",
        "Kanao Tsuyuri": "kanao tsuyuri, young woman, black hair in ponytail with butterfly pin, large purple eyes, stoic expression, demon slayer uniform with pink-lined white cape, beautiful, flower breathing",
        "Shinobu Kocho": "shinobu kocho, young woman, black hair with purple tips styled in yakai-maki, large purple gradient eyes, constant gentle smile, butterfly wing haori, petite slender, insect hashira, poison specialist",
        "Mitsuri Kanroji": "mitsuri kanroji, young woman, very long pink to green gradient braided hair, large green eyes, beauty mark under left eye, extremely curvaceous busty figure, revealing demon slayer uniform with skirt, love hashira, love breathing",
        "Daki": "daki demon slayer, young woman, long white hair with lime green tips, pink magenta eyes with kanji, extremely beautiful, revealing oiran outfit, sash weapons, upper rank demon",
        "Tamayo": "tamayo demon slayer, adult woman, dark brown hair in bun, pale skin, purple eyes, traditional purple kimono, elegant mature beauty, demon doctor, kind expression",
        
        # ============================================
        # ATTACK ON TITAN
        # ============================================
        "Eren Yeager": "eren yeager, young man, medium length brown hair, intense green eyes, determined angry expression, survey corps uniform with green cape, athletic build, later has long hair tied back",
        "Eren (Founding Titan)": "eren yeager founding titan form, extremely long dark hair, glowing eyes, colossal skeletal titan form, apocalyptic",
        "Mikasa Ackerman": "mikasa ackerman, young woman, short chin-length black hair, grey eyes, red scarf around neck always, survey corps uniform, lean muscular athletic, stoic protective expression, beautiful asian features",
        "Levi Ackerman": "levi ackerman, adult man, black undercut hair, sharp narrow grey eyes, short stature but extremely muscular, survey corps uniform with white cravat, bored or angry expression, humanity's strongest",
        "Historia Reiss": "historia reiss, young woman, long blonde hair, large blue eyes with eyebrows, small petite figure, survey corps uniform or royal dress, beautiful angelic appearance, queen of the walls",
        "Annie Leonhart": "annie leonhart, young woman, blonde hair in bun with bangs, hooked nose, blue eyes, cold emotionless expression, military police uniform, athletic stocky build, female titan shifter",
        "Hange Zoe": "hange zoe, adult person, messy brown hair in ponytail, glasses over brown eyes, survey corps uniform, eccentric excited expression, titan researcher",
        "Sasha Blouse": "sasha blouse, young woman, long reddish brown hair in ponytail, light brown eyes, survey corps uniform, often eating, cheerful expression, nicknamed potato girl",
        "Pieck Finger": "pieck finger, young woman, long messy black hair, tired sleepy black eyes, bags under eyes, marleyan military uniform or casual, slender, cart titan shifter",
        
        # ============================================
        # JUJUTSU KAISEN
        # ============================================
        "Yuji Itadori": "yuji itadori, young man, short spiky pink hair with undercut, brown eyes, athletic muscular build, jujutsu high uniform black with red hood, cheerful but serious when fighting, sukuna's vessel",
        "Megumi Fushiguro": "megumi fushiguro, young man, spiky black hair, dark blue eyes, handsome stoic expression, jujutsu high uniform, lean build, summons shikigami, ten shadows technique",
        "Nobara Kugisaki": "nobara kugisaki, young woman, orange ginger bob hair, fierce brown eyes, confident brash expression, jujutsu high uniform with skirt, hammer and nails weapon, beautiful fierce",
        "Gojo Satoru": "gojo satoru, adult man, spiky white hair, covered eyes with black blindfold normally, when revealed has bright crystalline blue six eyes, extremely tall, handsome, black high-collar uniform, cocky arrogant smile, strongest sorcerer",
        "Maki Zenin": "maki zenin, young woman, dark green hair in ponytail, green eyes behind glasses, athletic muscular figure, jujutsu sorcerer outfit, cursed tools specialist, confident aggressive expression",
        "Mei Mei": "mei mei jujutsu kaisen, adult woman, long light grey hair in braid, grey eyes, mature curvaceous figure, elegant black dress or sorcerer outfit, money-oriented, beautiful calm expression",
        "Miwa Kasumi": "miwa kasumi, young woman, short light blue hair, blue eyes, kyoto jujutsu high uniform, simple sword, sweet kind expression, ordinary but determined",
        "Tsukumo Yuki": "yuki tsukumo, adult woman, long blonde hair, laid back expression, casual clothes often motorcycle gear, special grade sorcerer, tall athletic",
        
        # ============================================
        # CHAINSAW MAN
        # ============================================
        "Denji": "denji chainsaw man, young man, messy dirty blonde hair, sharp shark-like teeth, scrawny initially, chainsaw coming from head and arms in devil form, wild desperate expression, poor devil hunter",
        "Power": "power chainsaw man, young woman, long messy blonde hair, small red horns, red eyes, sharp fanged teeth, blood fiend, white dress shirt often bloody, chaotic insane expression, beautiful but feral, flat chest she lies about",
        "Makima": "makima chainsaw man, adult woman, long auburn reddish brown hair in braids, yellow-ringed eyes with spiral pattern, white dress shirt, black tie, black pants, beautiful cold calculating expression, control devil, mysterious smile",
        "Aki Hayakawa": "aki hayakawa, young adult man, black hair in short ponytail with bangs, blue eyes, handsome serious expression, suit and tie, devil hunter, fox devil contract",
        "Himeno": "himeno chainsaw man, adult woman, short black hair, eyepatch over right eye, cigarette often, suit, mature beauty, devil hunter, ghost devil contract",
        "Reze": "reze chainsaw man, young woman, short dark purple hair, green eyes, cute innocent appearance normally, bomb devil hybrid, white shirt and dark skirt, beautiful mysterious",
        "Kobeni Higashiyama": "kobeni higashiyama, young woman, short dark brown hair, anxious terrified expression usually, suit, petite, surprisingly skilled despite cowardice",
        "Quanxi": "quanxi chainsaw man, adult woman, white hair in ponytail, eyepatch, chinese dress style outfit, extremely muscular athletic, crossbow devil, stoic expression, surrounded by girlfriends",
        
        # ============================================
        # BLEACH
        # ============================================
        "Ichigo Kurosaki": "ichigo kurosaki, young man, spiky bright orange hair, brown eyes, scowling default expression, shinigami black robes or school uniform, tall muscular, massive zanpakuto sword, soul reaper",
        "Rukia Kuchiki": "rukia kuchiki, young woman, short black hair with strand between eyes, violet eyes, petite short stature, shinigami black robes or simple dress, noble bearing, beautiful, ice zanpakuto",
        "Orihime Inoue": "orihime inoue, young woman, long burnt orange hair with hairpins, large grey eyes, very busty curvaceous figure, school uniform or casual, kind gentle expression, healing powers",
        "Rangiku Matsumoto": "rangiku matsumoto, adult woman, long wavy strawberry blonde hair, blue eyes, beauty mark under right eye, extremely busty voluptuous figure, shinigami robes worn loosely showing cleavage, flirty playful expression, lieutenant",
        "Yoruichi Shihoin": "yoruichi shihoin, adult woman, long purple hair in ponytail, dark skin, golden cat-like eyes, athletic toned figure, orange jacket or black bodysuit, confident teasing expression, flash goddess, can transform into black cat",
        "Nel Tu": "nelliel tu odelschwanck, adult woman, long wavy sea green hair, hazel eyes, skull mask fragment on head, red line across face, very curvaceous, arrancar outfit or torn, former espada, kind",
        "Tier Harribel": "tier harribel, adult woman, short blonde hair, dark skin, green eyes, lower face covered by high collar jacket, very busty, arrancar white outfit minimal, serious stoic, third espada",
        "Nemu Kurotsuchi": "nemu kurotsuchi, young woman, long black hair in braid, green eyes, emotionless expression, modified shinigami uniform short, petite but developed figure, artificial soul",

        # ============================================
        # STUDIO GHIBLI
        # ============================================
        "Chihiro (Spirited Away)": "chihiro spirited away, young girl, brown hair in ponytail with purple hair tie, brown eyes, simple green striped shirt and pink shorts, brave determined expression, bathhouse worker outfit later",
        "Haku": "haku spirited away, young man, straight dark green-black hair bob cut, green eyes, white and blue spirit outfit, handsome mysterious, can transform into white dragon",
        "San (Mononoke)": "san princess mononoke, young woman, wild short black hair, blue triangle face paint, wolf girl, blue eyes fierce and feral, white fur cape and dress, spear and dagger, raised by wolves",
        "Howl": "howl howls moving castle, young man, long blonde hair (or other colors through magic), blue eyes, handsome ethereal, flashy colorful outfits with jewelry, wizard, can turn into bird monster",
        "Sophie": "sophie hatter, young woman, silver-grey or brown hair depending on curse state, beautiful simple features, simple dress, hat maker, brave kind heart",
        "Kiki": "kiki delivery service, young girl, short black hair with red ribbon, black witch dress, witch in training, flying on broomstick with cat jiji, cheerful determined",
        "Nausicaa": "nausicaa valley of wind, young woman, short auburn hair, blue eyes, blue flight suit, brave warrior princess, loves ohmu and insects, toxic jungle explorer",
        "Sheeta": "sheeta laputa castle in sky, young girl, long black hair in braids, blue eyes, simple village dress, princess of laputa, gentle brave, crystal necklace",
        
        # ============================================
        # FATE SERIES
        # ============================================
        "Saber (Artoria)": "saber artoria pendragon, young woman, blonde hair in bun with ahoge strand, bright green eyes, blue and silver battle dress with armor, regal beautiful, serious noble expression, excalibur sword, king arthur",
        "Saber Alter": "saber alter artoria, pale skin, yellow eyes, black armor and dress, corrupted dark version, cold cruel expression, dark excalibur",
        "Rin Tohsaka": "rin tohsaka fate, young woman, long black hair in twin tails with red ribbons, aqua blue eyes, red turtleneck and black skirt, thigh high boots, beautiful tsundere expression, magus",
        "Sakura Matou": "sakura matou fate, young woman, long purple hair with red ribbon, violet eyes, gentle shy expression, school uniform or purple dress, dark backstory, beautiful tragic",
        "Jeanne d'Arc": "jeanne d'arc fate, young woman, very long blonde braid, violet eyes, silver armor with blue details, flag and sword, holy maiden, beautiful noble righteous expression",
        "Medusa/Rider": "medusa rider fate, tall woman, very long purple hair past knees, blindfold over eyes normally, purple eyes when shown, black revealing outfit, nail weapons on chains, tall slender, gorgon",
        "Scathach": "scathach fate, adult woman, long purple hair, red eyes, red bodysuit skintight, dual spears, warrior queen, beautiful cold expression, celtic lancer, immortal",
        "Ishtar (Rin)": "ishtar fate, woman with rin tohsaka's appearance, black twin tails with gold accessories, red eyes, floating on boat, revealing goddess outfit red and gold, babylonian goddess",
        "Tamamo no Mae": "tamamo no mae fate, woman, long pink hair, yellow fox eyes, fox ears and tail, japanese style miko outfit blue and white, cute flirty expression, divine spirit fox wife",
        "Nero Claudius": "nero claudius fate, young woman, blonde hair with rose ornaments, green eyes, red revealing emperor dress, vain proud expression, artist emperor, beautiful",
        
        # ============================================
        # EVANGELION
        # ============================================
        "Rei Ayanami": "rei ayanami evangelion, young woman, short light blue hair, red eyes, extremely pale skin, emotionless blank expression, white plugsuit or school uniform, mysterious, eva pilot",
        "Asuka Langley": "asuka langley soryu, young woman, long red-orange hair with neural connectors, blue eyes fierce expression, red plugsuit, tsundere attitude, confident arrogant, german eva pilot",
        "Misato Katsuragi": "misato katsuragi, adult woman, long purple hair, brown eyes, nerv uniform or casual, red jacket, cross necklace, mature beauty, often drinking beer, operations director",
        "Mari Makinami": "mari makinami illustrious, young woman, long brown hair in twintails, glasses, green eyes, pink plugsuit, cheerful eccentric, loves piloting eva, busty figure",
        
        # ============================================
        # RE:ZERO
        # ============================================
        "Rem": "rem re:zero, young woman, short sky blue hair covering right eye, blue left eye, maid outfit black and white with headpiece, demon sister, beautiful devoted expression, morning star flail weapon",
        "Ram": "ram re:zero, young woman, short pink hair covering right eye, pink left eye, maid outfit black and white, demon sister, confident smirk, rem's twin, lost horn",
        "Emilia": "emilia re:zero, young woman, long silver white hair with flower hairpin, purple eyes, elf ears, white and purple dress with cape, half-elf, beautiful gentle kind expression, ice magic",
        "Beatrice": "beatrice re:zero, young girl appearance, blonde drill twintails, blue eyes, pink and white gothic lolita dress, tsundere librarian, ancient spirit, powerful magic",
        "Echidna": "echidna re:zero, young woman, long white hair, black eyes, black funeral dress, witch of greed, mysterious smirk, loves knowledge, tea party host",
        
        # ============================================
        # KONOSUBA
        # ============================================
        "Aqua": "aqua konosuba, young woman, long light blue hair with ring accessory, blue eyes, detached sleeves white and blue, short blue skirt, goddess of water, useless crying or smug expression, beautiful but dumb",
        "Megumin": "megumin konosuba, young girl, short brown/black hair, red eyes, crimson demon, witch hat and cape, red and black outfit, eyepatch, explosion magic only, dramatic chunibyo pose",
        "Darkness": "darkness lalatina konosuba, young woman, long blonde hair, blue eyes, silver crusader armor, very busty figure, masochistic expression when hit, noble crusader, horrible accuracy",
        "Wiz": "wiz konosuba, adult woman, long brown hair, purple eyes, large bust, purple dress, lich shopkeeper, kind gentle despite being undead, often swindled by vanir",
        "Yunyun": "yunyun konosuba, young girl, black hair in twin tails, red eyes, crimson demon outfit similar to megumin, lonely no friends, rival to megumin developed figure",
        
        # ============================================
        # DISNEY ANIMATION
        # ============================================
        "Elsa": "elsa frozen, young woman, platinum blonde hair in long braid, large blue eyes, pale skin, ice blue dress with cape, ice queen powers, elegant regal beautiful, let it go pose",
        "Anna": "anna frozen, young woman, strawberry blonde hair in twin braids, blue eyes, freckles, green and black coronation dress or travel outfit, cheerful optimistic expression, adventurous princess",
        "Rapunzel": "rapunzel tangled, young woman, extremely long golden blonde hair 70 feet, large green eyes, purple dress barefoot, princess locked in tower, cheerful creative expression, frying pan weapon",
        "Moana": "moana disney, young woman, long curly dark brown hair, brown eyes, polynesian features brown skin, red patterned outfit, demigod necklace, brave determined ocean explorer",
        "Jasmine": "princess jasmine aladdin, young woman, long black hair with headband, large brown eyes, olive arabesque skin, teal crop top and pants, gold earrings, beautiful independent arabian princess",
        "Ariel": "ariel little mermaid, young woman, long flowing red hair, large blue eyes, green mermaid tail, purple seashell bra, curious adventurous expression, beautiful mermaid princess",
        "Belle": "belle beauty and the beast, young woman, long brown hair often in low ponytail with blue ribbon, hazel brown eyes, blue village dress or yellow ball gown, bookworm, french beauty",
        "Mulan": "mulan disney, young woman, long straight black hair (or short when disguised), brown eyes, asian chinese features, traditional chinese dress or warrior armor, brave honorable expression",
        "Pocahontas": "pocahontas disney, young woman, very long flowing black hair, brown eyes, native american features, tan skin, buckskin dress, necklace from mother, one with nature, proud beautiful",
        "Tiana": "tiana princess and frog, young woman, black hair in updo, brown eyes, dark skin, green dress, jazz age new orleans, hardworking chef aspirations, beautiful determined",
        "Merida": "merida brave, young woman, wild curly voluminous red hair, blue eyes, scottish princess, green medieval dress, archery bow, brave fierce independent, freckles",
        "Megara": "megara meg hercules, young woman, long dark auburn hair in high ponytail, purple eyes, slender figure, purple greek dress, sarcastic cynical expression, beautiful, sold soul to hades",
        "Esmeralda": "esmeralda hunchback notre dame, young woman, long wavy black hair, green eyes, romani dancer, white top purple skirt, tambourine, beautiful kind rebellious,olive skin",
        "Vanessa": "vanessa villain form of ursula, human disguise, extremely beautiful, long dark brown hair, blue eyes (hypnotic), nautilus shell necklace, white dress, seductive",
        
        # ============================================
        # PIXAR
        # ============================================
        "Elastigirl": "elastigirl helen parr incredibles, adult woman, short brown hair, brown eyes, red and black super suit, athletic thicc figure especially hips, stretchy powers, mom superhero",
        "Violet Parr": "violet parr incredibles, teenage girl, long black hair often covering face, lavender eyes, shy, red and black super suit, invisibility and force fields, awkward teen",
        
        # ============================================
        # AVATAR: THE LAST AIRBENDER / KORRA
        # ============================================
        "Azula": "azula avatar, young woman, black hair in topknot with bangs, golden sharp eyes, fire nation armor red and gold, beautiful cruel sadistic expression, blue fire bender, princess, prodigy",
        "Katara": "katara avatar, young woman, long brown wavy hair with hair loopies, blue eyes, water tribe blue outfit, tan skin, waterbender, kind motherly but fierce, necklace from mother",
        "Toph Beifong": "toph beifong avatar, young girl, black hair in large bun, milky blind green eyes, earth kingdom outfit green and yellow, earthbender master, brash tough expression, metalbending creator",
        "Mai": "mai avatar, young woman, long straight black hair, pale skin, bored emotionless expression, fire nation dark clothes, throws knives and stilettos, azula's friend, dry personality",
        "Ty Lee": "ty lee avatar, young woman, long brown hair in braid, grey eyes, pink circus acrobat outfit, cheerful bubbly expression, chi blocker, extremely flexible gymnast, azula's friend",
        "Korra": "korra avatar, young woman, short brown hair often in ponytail with wolftail, blue eyes, water tribe blue outfit, athletic extremely muscular for woman, dark skin, cocky confident expression, avatar, bisexual",
        "Asami Sato": "asami sato legend of korra, young woman, long wavy black hair, green eyes, red lipstick, pale skin, elegant wealthy heiress, engineer, red outfit often, beautiful refined, bisexual",
        "Lin Beifong": "lin beifong legend of korra, adult woman, grey hair bob cut, green eyes, scars on cheek, metalbender armor, tough police chief expression, earthbender, toph's daughter",
        "Suyin Beifong": "suyin beifong legend of korra, adult woman, grey hair in bob, green eyes, matriarch of zaofu, elegant metal clan outfit, metalbender, sophisticated",
        
        # ============================================
        # TEEN TITANS / DC ANIMATED
        # ============================================
        "Raven": "raven teen titans, young woman, short purple hair, pale greyish skin, violet eyes, gem on forehead chakra, dark blue hooded cloak, leotard, gothic dark magic, monotone expression, daughter of trigon",
        "Starfire": "starfire teen titans, young woman, extremely long flowing red hair, solid green glowing eyes, orange skin, purple outfit revealing, alien, cheerful naive, shoots green energy, very tall busty",
        "Terra": "terra teen titans, young woman, long blonde hair, blue eyes, black and yellow outfit, earth powers, troubled past, slim athletic",
        "Blackfire": "blackfire teen titans, young woman, long black curly hair, glowing purple eyes, purple outfit more revealing than starfire, evil sister, seductive cruel expression",
        "Harley Quinn": "harley quinn dc animated, young woman, blonde hair in twin pigtails dipped red and blue, pale skin, blue and red eyes makeup, revealing red and blue jester outfit, crazy cheerful expression, baseball bat, puddin obsessed",
        "Poison Ivy": "poison ivy dc, young woman, long red hair, green skin, green eyes, literally wearing only leaves, plants growing, seductive evil expression, eco terrorist, plant powers, beautiful",
        "Catwoman": "catwoman dc, young woman, short or long black hair, green eyes, black latex catsuit skintight, cat ears headpiece, whip, thief, seductive mysterious expression, athletic figure",
        "Batgirl": "batgirl barbara gordon dc, young woman, long red hair, blue eyes, black and yellow bat suit, cape, detective, acrobatic, beautiful heroic",
        
        # ============================================
        # ADVENTURE TIME / CARTOON NETWORK
        # ============================================
        "Marceline": "marceline abadeer adventure time, young woman, long black hair flowing, greyish blue skin, vampire fangs, bite marks on neck, red boots and tank top, bass guitar axe, vampire queen, rock aesthetic, pointed ears",
        "Princess Bubblegum": "princess bubblegum adventure time, young woman, very long pink hair, pink skin made of gum, golden tiara, pink dress, scientist ruler, proper speech but secretly dark, tall slender",
        "Flame Princess": "flame princess adventure time, young woman, made of fire orange and yellow, flame hair, cute angry fire girl, elemental princess",
        
        # ============================================
        # CYBERPUNK EDGERUNNERS
        # ============================================
        "Lucy (Edgerunners)": "lucy cyberpunk edgerunners, young woman, short white bob haircut with bangs, blue eyes, cybernetic enhancements, white cropped top and pants, netrunner, futuristic, mysterious beautiful, dreams of the moon",
        "Rebecca (Edgerunners)": "rebecca cyberpunk edgerunners, young woman petite, pink hair in twin tails, cybernetic arms and enhancements, pink eyes, small but aggressive, oversized weapons, chaotic energy, cute but deadly",
        
        # ============================================
        # MISCELLANEOUS POPULAR
        # ============================================
        "Zero Two": "zero two darling in the franxx, young woman, long pink hair with white restraint headband, cyan eyes with red rings, small red horns, red pilot suit, seductive playful expression, dinosaur girl, beautiful",
        "Hatsune Miku": "hatsune miku vocaloid, young woman, extremely long teal twintails past feet, teal eyes, black and teal outfit with detached sleeves, digital idol android, headphones, cute pop star, number 01 on arm",
        "Tohru (Dragon Maid)": "tohru kobayashi dragon maid, young woman, long blonde hair, red gradient tips, red eyes with slit pupils, green horns and tail, maid outfit, busty figure, lovesick obsessed expression with kobayashi, dragon",
        "Kanna Kamui": "kanna kamui dragon maid, young girl appearance, white lavender hair, blue eyes, dragon horns and tail, gothic lolita outfit, deadpan expression, dragon child, cute, consumes electricity",
        "Violet Evergarden": "violet evergarden, young woman, blonde hair with ribbon, blue eyes, mechanical prosthetic arms silver, white dress with detailing, doll-like emotionless beautiful, auto memory doll, former soldier, emerald brooch",
        "Toga Himiko": "toga himiko my hero academia, young woman, blonde messy hair in twin buns, yellow cat-like eyes, crazed yandere smile, fangs, school uniform, blood collection equipment, stalker creepy cute",
        "Mai Sakurajima": "mai sakurajima bunny girl senpai, young woman, long straight black hair, blue-violet eyes, bunny girl outfit black, tall slender beautiful, cool aloof expression, actress, adolescence syndrome",
        "Kaguya Shinomiya": "kaguya shinomiya love is war, young woman, long black hair with red ribbon bow, red eyes, rich ojou-sama, red eyes, detective expression, high school uniform, beautiful wealthy ice queen secretly romantic",
        "Chika Fujiwara": "chika fujiwara love is war, young woman, light pink hair with black bow, blue eyes, cheerful chaotic expression, school uniform, unpredictable, cute troublemaker",
        "Yor Forger": "yor forger spy x family, young woman, long black hair, red eyes, beautiful elegant, red dress normally with earrings, secretly assassin thorn princess, black assassin outfit for missions, kind but deadly",
        "Power (CSM)": "power chainsaw man, young woman, long wild blonde hair, red horns, sharp teeth, red eyes, crazy expression, white shirt blood stained, blood fiend devil, chaotic, beautiful feral energy",
        "2B (Nier)": "2b nier automata, young woman, short white hair with blindfold visor, pale skin, black gothic leotard dress, thigh high boots, android, katana, stoic beautiful, mole under lips",
        "A2 (Nier)": "a2 nier automata, young woman, long wild white hair, tattered black clothing, damaged body showing endoskeleton, fierce warrior android, aggressive expression",
        
        # ============================================
        # POKEMON
        # ============================================
        "Misty": "misty pokemon, young woman, short orange hair in side ponytail, blue-green eyes, fair skin, yellow crop top, red suspenders, blue denim shorts, water trainer, tomboy, athletic slim figure, feisty expression",
        "May": "may pokemon, young woman, brown hair with green bandana, blue eyes, fair skin, red and blue outfit, petite curvy figure, coordinator, cheerful personality",
        "Dawn": "dawn pokemon, young woman, dark blue hair with gold clips, blue eyes, fair skin, black and pink dress, white scarf, petite figure, coordinator, cheerful",
        "Serena": "serena pokemon xy, young woman, honey blonde hair, blue eyes, fair skin, pink outfit with hat and ribbon, performer, slender figure, loves fashion, crush on ash",
        "Cynthia": "cynthia pokemon champion, adult woman, very long wavy blonde hair, grey eyes, black outfit with long coat, sinnoh champion, tall elegant figure, beautiful powerful, black dress underneath",
        "Jessie": "jessie team rocket pokemon, adult woman, incredibly long magenta red hair in dramatic swoosh style, blue eyes, white and red team rocket uniform with midriff, curvy figure, dramatic villain",
        "Nurse Joy": "nurse joy pokemon, young woman, pink hair in loops, blue eyes, nurse outfit white and pink, kind smile, healer, pretty identical nurses",
        "Officer Jenny": "officer jenny pokemon, young woman, blue-green hair under police cap, eyes matching hair, police uniform, authoritative, pretty identical officers",
        "Marnie": "marnie pokemon sword shield, young woman, black hair with undercut styled over one eye, pale skin, punk style, dark clothes with pink and black, pale blue eyes, reserved expression, cute punk girl",
        "Nessa": "nessa pokemon sword shield, young woman, long black hair with blue streaks, dark skin, blue eyes, water gym leader, swim outfit blue, tall athletic model figure, beautiful confident",
        "Bea": "bea pokemon sword shield, young woman, grey short hair, dark grey eyes, fighting gym leader, orange shorts and sports bra showing abs, athletic muscular, serious expression, bandaged fists",
        "Sonia": "sonia pokemon sword shield, adult woman, long orange ginger hair, green eyes, lab coat over short dress, tall curvy figure, pokemon professor assistant, intelligent beautiful",
        "Hilda": "hilda pokemon black white, young woman, long brown hair in high ponytail with cap, blue eyes, white tank top, very short shorts, curvy figure, confident bold expression",
        "Rosa": "rosa pokemon black white 2, young woman, long brown hair in twin buns, blue eyes, pink and white outfit with visor, cheerful expression, cute",
        "Gloria": "gloria pokemon sword shield, young woman, short brown hair, grey eyes, scottish tam beret, grey dress and cardigan, determined expression, galar protagonist",
        "Clair": "clair pokemon dragon master, young woman, long light blue hair in ponytail, blue eyes, revealing blue body suit cape, dragon trainer, proud confident, tall slender",
        "Elesa": "elesa pokemon, young woman, blonde hair in unique headphone style, blue eyes, model, nimbasa gym leader electric type, yellow and black outfit, tall slender supermodel",
        "Skyla": "skyla pokemon, young woman, red hair in high ponytail, blue eyes, flying gym leader, blue outfit, pilot, cheerful energetic, athletic figure",
        "Korrina": "korrina pokemon, young woman, blonde hair in ponytail with helmet, grey eyes, fighting gym leader, roller skating outfit, athletic energetic, mega evolution",
        "Lillie": "lillie pokemon sun moon, young woman, long pale blonde hair, green eyes, white dress with hat, elegant refined, alola region, gentle kind expression, slender delicate figure",
        "Lusamine": "lusamine pokemon, adult woman, long blonde hair, green eyes, white bodysuit, very slender tall figure, aether foundation president, beautiful cold elegant, lillie's mother",
        
        # ============================================
        # MY LIFE AS A TEENAGE ROBOT
        # ============================================
        "Jenny/XJ-9": "jenny wakeman xj-9 my life as a teenage robot, teenage robot girl, metallic silver-blue body, white pigtails, blue eyes with visible circuits, round head, robotic joints, red and white cheerleader-style outfit painted on, heroic expression, created by mom nora, teen superhero robot",
        "Misty (Teenage Robot)": "misty from my life as a teenage robot, human teenage girl, short brown hair, yellow outfit, melodys friend, jealous of jenny initially",
        
        # ============================================
        # FAIRLY ODDPARENTS
        # ============================================
        "Trixie Tang": "trixie tang fairly oddparents, teenage girl, long black hair in headband, purple eyes, purple and white cheerleader outfit or purple dress, popular girl, beautiful, snooty rich expression, dimmsdale",
        "Veronica": "veronica fairly oddparents, teenage girl, blonde hair, friend of trixie, pink outfit, dimmsdale",
        "Tootie": "tootie fairly oddparents, young girl, black hair in pigtails, braces, glasses, purple dress, obsessed with timmy, vicky's sister",
        "Vicky": "vicky fairly oddparents, teenage girl, orange red ponytail, green eyes, green crop top, black pants, evil babysitter, mean expression, iconic villain",
        
        # ============================================
        # JIMMY NEUTRON
        # ============================================
        "Cindy Vortex": "cindy vortex jimmy neutron, young girl, blonde hair in ponytail, green eyes, pink shirt, genius rival to jimmy, competitive bossy expression, smart",
        "Libby Folfax": "libby folfax jimmy neutron, young girl, dark skin, black hair in braids, purple outfit, cindy's best friend, music lover, fashionable",
        "Beautiful Gorgeous": "beautiful gorgeous jimmy neutron, adult woman, blonde hair, spy villain, femme fatale, beautiful seductress, black spy outfit",
        
        # ============================================
        # DANNY PHANTOM
        # ============================================
        "Sam Manson": "sam manson danny phantom, teenage girl, short black hair in ponytail, purple eyes, goth aesthetic, purple and black outfit, crop top with exposed midriff, combat boots, ultra-recyclo-vegetarian, danny's friend and love interest, beautiful goth",
        "Paulina": "paulina sanchez danny phantom, teenage girl, long black hair, teal eyes, latina features, pink outfit, popular cheerleader, extremely beautiful, shallow but gorgeous",
        "Valerie Gray": "valerie gray danny phantom, teenage girl, dark skin, black hair in short style, ghost hunter, red hunter suit, athletic, brown eyes",
        "Ember McLain": "ember mclain danny phantom, ghost rockstar, flaming blue hair like fire, green skin, purple and black rocker outfit with guitar, rebellious expression, remember my name",
        "Desiree": "desiree danny phantom, ghost genie woman, long flowing black hair, green skin, purple and gold genie outfit revealing, wishes themed villain, seductive expression",
        "Spectra": "spectra danny phantom, ghost woman, short black hair, green skin, suit dress, therapist disguise, feeds on misery, beautiful sinister",
        
        # ============================================
        # ED EDD N EDDY
        # ============================================
        "Nazz": "nazz ed edd n eddy, teenage girl, short blonde hair, blue eyes, cool girl of cul-de-sac, purple tank top, jeans, popular blonde, laid back cool expression",
        "Marie Kanker": "marie kanker ed edd n eddy, teenage girl, blue hair covering one eye, trailer park girl, tank top, aggressive, obsessed with edd, kanker sister",
        "Lee Kanker": "lee kanker ed edd n eddy, teenage girl, curly red hair covering eyes, polka dot shirt, leader of kanker sisters, aggressive",
        "May Kanker": "may kanker ed edd n eddy, teenage girl, blonde bucktooth, kanker sister, obsessed with ed, flannel shirt",
        
        # ============================================
        # POWERPUFF GIRLS
        # ============================================
        "Blossom": "blossom powerpuff girls, young superhero girl, long orange-red hair with big red bow, pink eyes, pink dress with black stripe, leader, smart and confident, flying, cartoon style, super powers",
        "Bubbles": "bubbles powerpuff girls, young superhero girl, blonde hair in pigtails, baby blue eyes, light blue dress with black stripe, sweet cute innocent, flying, cartoon style",
        "Buttercup": "buttercup powerpuff girls, young superhero girl, short black flipped hair, green eyes, green dress with black stripe, tomboy tough fighter, flying, cartoon style",
        "Sedusa": "sedusa powerpuff girls, adult villain woman, long wild black hair that comes alive, green eyes, red dress, femme fatale, seductive evil",
        "Miss Bellum": "miss bellum powerpuff girls, adult woman, long curly red hair, face never fully shown, very curvaceous figure in red dress and heels, mayors assistant, sexy secretary trope",
        
        # ============================================
        # DEXTER'S LABORATORY
        # ============================================
        "DeeDee": "deedee dexters laboratory, teenage girl, tall slender, long blonde hair in ponytails, blue eyes, pink ballet tutu and leotard, ballerina, annoying sister, happy expression, long legs",
        
        # ============================================
        # KIM POSSIBLE
        # ============================================
        "Kim Possible": "kim possible, teenage girl, long red-orange hair, green eyes, fair skin, black crop top and cargo pants, athletic cheerleader spy figure, confident heroic expression, teen hero, call me beep me",
        "Shego": "shego kim possible, adult woman, long black hair with green tint, green skin from comet, black and green catsuit, villain, green plasma powers, sarcastic evil smirk, athletic curvy figure",
        "Bonnie Rockwaller": "bonnie rockwaller kim possible, teenage girl, brown hair in ponytail, teal eyes, cheerleader uniform, rival to kim, mean girl, beautiful but snobby",
        
        # ============================================
        # TOTALLY SPIES
        # ============================================
        "Sam (Totally Spies)": "sam totally spies, teenage girl, long red hair, green eyes, green spy catsuit skintight, intelligent leader of trio, athletic figure, beverly hills spy",
        "Clover": "clover totally spies, teenage girl, long blonde hair, blue eyes, red spy catsuit skintight, fashion obsessed, flirty, athletic curvy figure, beverly hills spy",
        "Alex (Totally Spies)": "alex totally spies, teenage girl, short black hair, brown eyes, yellow spy catsuit skintight, athletic sporty, asian features, beverly hills spy",
        
        # ============================================
        # WINX CLUB
        # ============================================
        "Bloom": "bloom winx club, young fairy woman, long orange-red hair, cyan blue eyes, sparkly blue fairy outfit with wings, fire powers, princess of domino, beautiful slender",
        "Stella": "stella winx club, young fairy woman, long blonde hair, hazel eyes, orange sparkly fairy outfit with wings, sun and moon powers, fashionable princess, beautiful",
        "Flora": "flora winx club, young fairy woman, long brown hair, green eyes, pink and green fairy outfit with wings, nature powers, gentle sweet, tan skin",
        "Musa": "musa winx club, young fairy woman, dark blue hair in pigtails, blue eyes, red fairy outfit with wings, music powers, asian features, tomboyish",
        "Tecna": "tecna winx club, young fairy woman, short magenta hair, teal eyes, purple tech fairy outfit with wings, technology powers, logical smart",
        "Layla/Aisha": "aisha layla winx club, young fairy woman, long curly brown hair, blue eyes, dark skin, green fairy outfit with wings, morphix water powers, athletic tomboy princess",
        
        # ============================================
        # THE INCREDIBLES
        # ============================================
        "Elastigirl/Helen": "elastigirl helen parr incredibles, adult woman, short brown hair, brown eyes, red and black super suit, very curvy figure especially wide hips and thighs, stretchy powers, mom superhero, athletic",
        "Violet Parr": "violet parr incredibles, teenage girl, long black hair covering face sometimes, violet eyes, shy, red and black super suit, slender, invisibility powers, awkward teen superhero",
        "Mirage (Incredibles)": "mirage incredibles, adult woman, short platinum blonde hair, grey eyes, white tight dress, slender figure, mysterious assistant, seductive",
        
        # ============================================
        # W.I.T.C.H.
        # ============================================
        "Will Vandom": "will vandom witch, teenage girl, short red hair, brown eyes, guardian leader, pink wings fairy form, petite, energy powers",
        "Irma Lair": "irma lair witch, teenage girl, brown hair in bob, blue eyes, water guardian, humor personality, curvy figure",
        "Taranee Cook": "taranee cook witch, teenage girl, dark skin, brown hair in braids, brown eyes behind glasses, fire guardian, shy initially",
        "Cornelia Hale": "cornelia hale witch, teenage girl, long blonde hair, blue eyes, earth guardian, fashion conscious, snobby but loyal, tall slender beautiful",
        "Hay Lin": "hay lin witch, teenage girl, long black hair in pigtails, brown eyes, asian features, air guardian, artistic, cheerful",
        
        # ============================================
        # SAMURAI JACK
        # ============================================
        "Ashi": "ashi samurai jack, young woman, long black hair (later short), dark eyes, asian features, athletic warrior body, daughters of aku black bodysuit or leaves, becomes good, beautiful fierce",
        
        # ============================================
        # COURAGE THE COWARDLY DOG
        # ============================================
        "Muriel Bagge": "muriel bagge courage cowardly dog, elderly woman, grey hair in bun, glasses, scottish, kind grandmother, apron dress, eustace's wife",
        
        # ============================================
        # CLONE HIGH
        # ============================================
        "Cleopatra (Clone High)": "cleopatra clone high, teenage girl clone, long black hair with gold accessories, egyptian features stylized, revealing outfits, popular mean girl, beautiful, party animal",
        "Joan of Arc (Clone High)": "joan of arc clone high, teenage girl clone, short black bob hair, goth aesthetic, purple outfit, cynical intelligent, crush on abe, beautiful",
        
        # ============================================
        # FOSTERS HOME
        # ============================================
        "Frankie Foster": "frankie foster fosters home for imaginary friends, young adult woman, long red hair in ponytail, green eyes, casual outfit with jacket, caretaker for imaginary friends, tired but caring, pretty, freckles",
        
        # ============================================
        # ATOMIC BETTY
        # ============================================
        "Atomic Betty": "atomic betty, young girl, red hair in pigtails, galactic guardian hero, white and red space suit, dual life as normal preteen and superhero",
        
        # ============================================
        # CODE LYOKO
        # ============================================
        "Yumi Ishiyama": "yumi ishiyama code lyoko, teenage girl, short black hair, dark eyes, japanese, black outfit, lyoko warrior geisha form, martial arts, serious cool",
        "Aelita Schaeffer": "aelita schaeffer code lyoko, teenage girl, short pink hair, green eyes, elf-like lyoko form, ai program became human, gentle intelligent, pink fairy outfit on lyoko",
        
        # ============================================
        # LILO & STITCH
        # ============================================
        "Nani Pelekai": "nani pelekai lilo and stitch, young adult woman, long black hair, brown eyes, hawaiian features, tan skin, athletic surfer body, lilo's big sister, red top, caring but stressed",
        
        # ============================================
        # AMERICAN DRAGON JAKE LONG
        # ============================================
        "Rose (American Dragon)": "rose american dragon jake long, teenage girl, long blonde hair in ponytail, blue eyes, huntsgirl outfit or regular clothes, love interest to jake, dragon slayer turned ally, beautiful, athletic",
        "Trixie Carter": "trixie carter american dragon, teenage girl, dark skin, purple hair, jake's friend, sass attitude, stylish",
        "Sun Park": "sun park american dragon, adult woman, korean dragon mentor, wise elderly but beautiful in younger scenes",
        
        # ============================================
        # 6TEEN
        # ============================================
        "Nikki Wong": "nikki wong 6teen, teenage girl, short purple hair, punk rock style, sarcastic, works at khaki barn, asian features, edgy",
        "Caitlin Cooke": "caitlin cooke 6teen, teenage girl, long blonde hair, valley girl, pink outfit, shopaholic, bubbly",
        "Jen Masterson": "jen masterson 6teen, teenage girl, brown hair in ponytail, athletic, works at penalty box, responsible, practical",
        
        # ============================================
        # BRATZ (Animated)
        # ============================================
        "Cloe (Bratz)": "cloe bratz, teenage girl, long blonde hair, blue eyes, fashion doll style, glamorous outfit, angel nickname, beautiful glam",
        "Yasmin (Bratz)": "yasmin bratz, teenage girl, long brown hair, hazel eyes, latina features, fashion doll style, pretty princess nickname",
        "Jade (Bratz)": "jade bratz, teenage girl, long black hair, brown eyes, asian features, fashion doll style, kool kat nickname, edgy fashion",
        "Sasha (Bratz)": "sasha bratz, teenage girl, dark skin, brown eyes, bunny boo nickname, fashion doll style, urban style, confident",
        
        # ============================================
        # STATIC SHOCK
        # ============================================
        "Shenice Vale": "shenice vale gear static shock, teenage girl, dark skin, short hair, becomes hero, tech genius",
        
        # ============================================
        # X-MEN EVOLUTION
        # ============================================  
        "Rogue (Evolution)": "rogue x-men evolution, teenage girl, brown hair with white streak in front, green eyes, gothic style, southern belle, cannot touch, beautiful mysterious",
        "Kitty Pryde (Evolution)": "kitty pryde x-men evolution, teenage girl, brown hair in ponytail, blue eyes, valley girl speech, phases through objects, cute bubbly",
        "Jean Grey (Evolution)": "jean grey x-men evolution, teenage girl, long red hair, green eyes, popular preppy, telepathic, beautiful, cheerleader-type",
        
        # ============================================
        # SCOOBY DOO MODERN
        # ============================================
        "Daphne Blake": "daphne blake scooby doo, young woman, long red-orange hair with purple headband, violet-blue eyes, purple dress, danger-prone, beautiful fashionable, mystery inc",
        "Velma Dinkley": "velma dinkley scooby doo, young woman, short brown bob hair, brown eyes behind thick glasses, orange turtleneck, red pleated skirt, genius detective, jinkies, cute nerdy",
        
        # ============================================
        # GENSHIN IMPACT
        # ============================================
        "Raiden Shogun": "raiden shogun ei genshin impact, woman, long purple hair with braid, purple eyes, elegant archon, electro vision, kimono-like outfit, calm powerful expression, inazuma ruler",
        "Keqing": "keqing genshin impact, young woman, purple twin tails, purple eyes, liyue yuheng, electro vision, elegant chinese outfit, determined expression",
        "Ganyu": "ganyu genshin impact, young woman, long blue hair with horns, golden eyes, adeptus half-qilin, cryo vision, floral outfit, gentle expression",
        "Hu Tao": "hu tao genshin impact, young woman, long brown hair with red tips, red flower eyes, wangsheng funeral director, pyro vision, playful mischievous expression",
        "Yae Miko": "yae miko genshin impact, woman, long pink hair with fox ears, wise pink eyes, guuji of grand narukami shrine, electro vision, seductive cunning",
        "Shenhe": "shenhe genshin impact, young woman, long white hair, icy blue eyes, adeptus disciple, cryo vision, ethereal cold beauty",
        "Yelan": "yelan genshin impact, woman, short dark blue hair, teal eyes, liyue intelligence, hydro vision, seductive spy aesthetic, dice earrings",
        "Eula": "eula genshin impact, young woman, long pale blue hair, golden eyes, lawrence clan, cryo claymore, elegant noble outfit, tsundere",
        "Mona": "mona genshin impact, young woman, long blue hair with twin tails, purple eyes, astrologer, hydro vision, revealing bodysuit, confident",
        "Lisa": "lisa genshin impact, woman, short curly purple hair, green eyes, librarian witch, electro vision, revealing witch outfit, ara ara personality",
        "Jean": "jean genshin impact, woman, long blonde hair in ponytail, blue eyes, acting grand master, anemo vision, knight outfit, responsible beauty",
        "Kuki Shinobu": "kuki shinobu genshin impact, young woman, green hair with mask, green eyes, arataki gang deputy, electro vision, ninja outfit, capable",
        
        # ============================================
        # HONKAI STAR RAIL
        # ============================================
        "Kafka": "kafka honkai star rail, woman, long purple hair, heterochromia eyes red and gold, stellaron hunter, mysterious alluring, elegant suit",
        "Silver Wolf": "silver wolf honkai star rail, young woman, grey-white hair with purple tips, yellow eyes, hacker gamer girl, hoodie, playful cocky",
        "Himeko": "himeko honkai star rail, woman, long red hair, amber eyes, astral express navigator, mature elegant, red dress",
        "Seele": "seele honkai star rail, young woman, purple bob hair, purple eyes, butterfly theme, cute yet deadly, determined",
        "Fu Xuan": "fu xuan honkai star rail, young woman, long brown hair with ornate headdress, red eyes, divination master, petite powerful, xianzhou luofu",
        "Jingliu": "jingliu honkai star rail, woman, long white hair with blindfold, sealed eyes, former sword champion, ice powers, tragic beauty",
        
        # ============================================
        # BLUE ARCHIVE
        # ============================================
        "Asuna (Blue Archive)": "asuna ichinose blue archive, young woman, long blonde hair with red ribbon, red eyes, c&c club, seductive student, revealing outfit",
        "Karin": "karin kakudate blue archive, young woman, long pink hair, blue eyes, justice task force, student soldier, serious beauty",
        "Hoshino": "hoshino takanashi blue archive, young woman, short grey-blue hair, sleepy blue eyes, abydos student, lazy but skilled, small and cute",
        "Aru": "aru rikuhachima blue archive, young woman, long blonde hair with horns headband, red eyes, problem solver 68 leader, self-proclaimed villain, chuunibyou",
        
        # ============================================
        # AZUR LANE
        # ============================================
        "Atago (Azur Lane)": "atago azur lane, woman, long black hair with dog ears, golden eyes, takao-class cruiser, ara ara onee-san, revealing kimono",
        "Taihou": "taihou azur lane, woman, long black hair, red eyes, aircraft carrier, yandere obsessive, revealing outfit, very large bust",
        "Formidable": "formidable azur lane, woman, long silver-white hair with black bow, blue eyes, illustrious-class, elegant gothic, twintails",
        "Shinano": "shinano azur lane, woman, long white hair with fox ears and tails, sleepy purple eyes, aircraft carrier, shrine maiden outfit, largest ship",
        
        # ============================================
        # PERSONA SERIES
        # ============================================
        "Ann Takamaki": "ann takamaki persona 5, young woman, long blonde wavy hair with pigtails, blue eyes, panther thief, red latex catsuit, model student",
        "Makoto Niijima": "makoto niijima persona 5, young woman, short brown hair with braid, red eyes, queen thief, student council president, serious biker aesthetic",
        "Futaba Sakura": "futaba sakura persona 5, young woman, long orange hair, brown eyes behind glasses, navigator hacker, gamer girl, petite otaku",
        "Haru Okumura": "haru okumura persona 5, young woman, short fluffy brown hair, brown eyes, noir thief, gentle rich girl, pink aesthetic",
        "Rise Kujikawa": "rise kujikawa persona 4, young woman, reddish-brown hair in twintails, brown eyes, idol risette, cheerful flirty, orange outfit",
        "Mitsuru Kirijo": "mitsuru kirijo persona 3, woman, long red hair, red eyes, student council president, ice persona, elegant mature",
        
        # ============================================
        # FINAL FANTASY
        # ============================================
        "Aerith Gainsborough": "aerith gainsborough final fantasy 7, young woman, long brown hair with pink bow, green eyes, flower girl, pink dress, gentle healer",
        "Cloud (Female)": "female cloud strife genderswap final fantasy 7, young woman, spiky blonde hair, blue mako eyes, soldier buster sword, serious beautiful",
        "Tifa Lockhart": "tifa lockhart final fantasy 7, young woman, long black hair, red-brown eyes, martial artist bartender, white tank top, large bust athletic",
        "Yuna": "yuna final fantasy 10, young woman, short brown hair, heterochromia blue and green eyes, summoner, traditional sendian dress, gentle",
        "Lightning": "lightning claire farron final fantasy 13, woman, pink hair, blue eyes, l'cie soldier, stoic serious, guardian corps uniform",
        "Rikku": "rikku final fantasy 10, young woman, blonde hair with braids and headband, green swirl eyes, al bhed thief, revealing yellow bikini outfit, cheerful",
        
        # ============================================
        # CLASSIC ANIME WAIFUS
        # ============================================
        "Asuka Langley": "asuka langley soryu evangelion, young woman, long orange-red hair, blue eyes, eva pilot plugsuit, tsundere fiery, german japanese",
        "Misato Katsuragi": "misato katsuragi evangelion, woman, long purple hair, brown eyes, nerv captain, mature sexy, red jacket, beer lover",
        "CC (Code Geass)": "cc code geass, woman, long green hair, golden-amber eyes, immortal witch, pizza lover, mysterious seductive",
        "Kallen Stadtfeld": "kallen stadtfeld code geass, young woman, short red hair, blue eyes, guren pilot, fiery rebel, revealing bunny suit or pilot suit",
        "Yoruichi Shihouin": "yoruichi shihouin bleach, woman, long purple hair, golden cat eyes, former captain, dark-skinned, athletic sexy, flash goddess",
        "Rangiku Matsumoto": "rangiku matsumoto bleach, woman, long wavy orange hair, blue eyes, lieutenant, very curvaceous busty, lazy glamorous",
        "Nelliel": "nelliel tu odelschwanck nel bleach, woman, long teal-green hair, hazel eyes, former espada, athletic curvy, hollow mask remnant",
        "Erza Scarlet": "erza scarlet fairy tail, woman, long scarlet red hair, brown eyes, requip mage, armor or bunny suit, strong beautiful",
        "Mirajane Strauss": "mirajane strauss fairy tail, woman, long white hair, blue eyes, she-devil takeover, model beautiful, revealing outfits, sweet but deadly",
        "Lucy Heartfilia": "lucy heartfilia fairy tail, young woman, long blonde hair usually in side ponytail, brown eyes, celestial wizard, curvy busty, blue outfit",
        
        # ============================================
        # MORE DISNEY / PIXAR
        # ============================================
        "Megara": "megara hercules disney, young woman, long dark purple hair in ponytail, violet eyes, greek woman, purple dress, sarcastic seductive",
        "Esmeralda": "esmeralda hunchback of notre dame disney, young woman, long black wavy hair, green eyes, romani dancer, tan skin, curvy beautiful, red dress",
        "Pocahontas": "pocahontas disney, young woman, long black hair flowing, brown eyes, native american princess, tan skin, athletic, one with nature",
        "Moana": "moana disney, young woman, long dark curly hair, brown eyes, polynesian voyager, tan skin, athletic, red outfit with island patterns",
        "Rapunzel": "rapunzel tangled disney, young woman, extremely long blonde magical hair, large green eyes, princess tower, pink dress, barefoot, innocent",
        "Elsa": "elsa frozen disney, young woman, platinum blonde hair in braid, blue eyes, ice queen, pale skin, blue ice dress, powerful elegant",
        "Anna": "anna frozen disney, young woman, strawberry blonde hair with white streak, blue eyes, princess of arendelle, freckles, warm personality, green dress",
        "Merida": "merida brave disney pixar, young woman, wild curly red hair, blue eyes, scottish princess, freckles, green dress, archer rebellious",
        "Raya": "raya and the last dragon disney, young woman, long black hair, brown eyes, southeast asian warrior, athletic, skilled fighter, strong",
        "Mirabel Madrigal": "mirabel madrigal encanto disney, young woman, curly black hair with glasses, brown eyes, colombian, curvy, green dress, no powers but special",
        "Isabela Madrigal": "isabela madrigal encanto disney, young woman, long black hair with flowers, brown eyes, colombian beauty, perfect graceful, flower powers, purple dress",
        
        # ============================================
        # MORE MODERN ANIME
        # ============================================
        "Power (Chainsaw Man)": "power chainsaw man, young woman, long blonde messy hair with red horns, yellow eyes, blood fiend, chaotic feral, fang tooth, flat chested",
        "Makima": "makima chainsaw man, woman, long red-brown hair worn in braids, yellow ringed eyes, control devil, professional suit, manipulative seductive, mysterious",
        "Reze": "reze chainsaw man, young woman, short dark purple hair, purple eyes, bomb devil hybrid, cute cafe worker disguise, explosive personality",
        "Himeno": "himeno chainsaw man, woman, short dark hair with eyepatch, one brown eye, public safety, cigarette smoker, seductive older woman, ghost devil contract",
        "Yor Forger": "yor forger spy x family, woman, long black hair, red eyes, assassin thorn princess, red dress or combat outfit, elegant deadly, kind mother",
        "Marin Kitagawa": "marin kitagawa my dress up darling, young woman, long blonde hair with pink tips, pink eyes, gyaru makeup, cosplayer, curvy, energetic friendly",
        "Mai Sakurajima": "mai sakurajima bunny girl senpai, young woman, long black hair, blue-purple eyes, actress bunny suit, elegant beautiful, tsundere",
        "Rio Futaba": "rio futaba bunny girl senpai, young woman, short dark hair, brown eyes glasses, science girl, quiet intelligent, modest figure",
    }
    
    QUALITY_PRESETS = {
        "Ultra Detailed": "masterpiece, best quality, ultra detailed, extremely detailed face, perfect anatomy, 8k uhd, intricate details, sharp focus, professional lighting, volumetric lighting, ray tracing, subsurface scattering, accurate character design, perfect likeness, recognizable character, iconic appearance, same character, exact match",
        "High Quality Anime": "masterpiece, best quality, highly detailed, perfect anatomy, sharp focus, beautiful anime art, professional, vibrant colors, accurate character, recognizable, same design, canonical appearance",
        "Anime Style": "masterpiece, best quality, anime style, detailed anime face, beautiful anime art, vibrant saturated colors, clean crisp lines, cel shaded, anime key visual, accurate character design, official art style",
        "Semi-Realistic": "masterpiece, best quality, semi-realistic, detailed, beautiful, realistic anime, 3d render quality, accurate features, recognizable character, same person",
        "Cartoon Style": "cartoon style, animated, clean lines, vibrant colors, cel shaded, best quality, detailed, accurate character design, recognizable, on-model",
        "Maximum Accuracy": "extremely detailed, perfect character likeness, accurate character design, recognizable iconic character, same character, exact match, canonical appearance, official art style, perfect anatomy, masterpiece, best quality, 8k uhd, same hair color, same eye color, same outfit colors",
        "PERFECT MATCH": "EXACT CHARACTER, IDENTICAL DESIGN, PERFECT CHARACTER MATCH, same exact character design, same hair style and color, same eye shape and color, same outfit design, same color scheme, on-model, official art style, canonical appearance, indistinguishable from reference, perfect reproduction, masterpiece, best quality, 8k uhd, accurate proportions",
    }
    
    CLOTHING_OPTIONS = {
        "Canon/Default": "",
        "Nude": ", completely nude, naked, bare skin, nipples visible, full body nudity, uncensored, anatomically correct anime, exposed body",
        "Topless": ", topless, bare breasts exposed, nipples visible, no top, bare chest, half nude",
        "Lingerie": ", wearing sexy lingerie, lace bra and panties, garter belt, stockings, seductive pose, intimate apparel",
        "Bikini": ", wearing bikini, swimsuit, beach scene, wet skin, summer, swimwear",
        "Micro Bikini": ", wearing micro bikini, string bikini, barely covered, extreme revealing swimwear",
        "See-Through": ", wearing see-through clothing, transparent fabric, nipples visible through clothes, sheer outfit",
        "Bunny Suit": ", wearing playboy bunny suit, bunny ears, fishnet stockings, bow tie collar, bunny girl costume",
        "Maid Bikini": ", wearing bikini maid outfit, frilly apron only, revealing maid costume, skimpy maid",
        "Maid Outfit": ", wearing maid outfit, maid dress, frilly apron, maid headdress, serving",
        "School Uniform": ", wearing japanese school uniform, sailor fuku, pleated skirt, school girl",
        "Gym Clothes": ", wearing tight gym clothes, sports bra, buruma shorts, athletic wear, sporty",
        "Dress Formal": ", wearing elegant formal dress, evening gown, sophisticated, ballroom",
        "Latex/Leather": ", wearing tight latex suit, leather outfit, shiny material, dominatrix style, skintight",
        "Traditional/Kimono": ", wearing traditional kimono, japanese clothing, obi sash, elegant traditional",
        "Chinese Dress": ", wearing chinese dress, cheongsam, qipao, side slit, mandarin collar",
        "Bodysuit": ", wearing tight bodysuit, form-fitting, plugsuit, skintight suit",
        "Armor": ", wearing armor, fantasy armor, battle outfit, warrior",
        "Custom": "",
    }
    
    # Comprehensive negative prompt for anime/cartoon character accuracy
    NEGATIVE_PROMPT = "deformed, distorted, disfigured, bad anatomy, wrong anatomy, extra limbs, missing limbs, floating limbs, mutated hands, extra fingers, missing fingers, fused fingers, too many fingers, long neck, mutation, poorly drawn face, poorly drawn hands, bad proportions, gross proportions, malformed limbs, cross-eyed, blurry, low quality, jpeg artifacts, signature, watermark, WRONG CHARACTER, DIFFERENT CHARACTER, OFF-MODEL, inaccurate design, WRONG HAIR COLOR, WRONG EYE COLOR, wrong outfit, unrecognizable, wrong color scheme, different art style, merged characters, mixed design, wrong proportions, different series style, not the same character"
    
    @classmethod
    def INPUT_TYPES(cls):
        characters = sorted(cls.CHARACTERS.keys())
        return {
            "required": {
                "character": (characters, {"default": characters[0]}),
                "quality": (list(cls.QUALITY_PRESETS.keys()), {"default": "Ultra Detailed"}),
                "clothing": (list(cls.CLOTHING_OPTIONS.keys()), {"default": "Canon/Default"}),
            },
            "optional": {
                "additional_details": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt", "character_name")
    FUNCTION = "generate"
    CATEGORY = "Mason/Characters"
    
    def generate(self, character, quality, clothing, additional_details=""):
        # Build prompt
        prompt_parts = []
        
        # Add quality prefix with accuracy emphasis
        prompt_parts.append(self.QUALITY_PRESETS[quality])
        
        # Add character name explicitly for recognition
        prompt_parts.append(f"{character}")
        
        # Add detailed character description
        prompt_parts.append(self.CHARACTERS[character])
        
        # Add clothing modification
        if clothing != "Canon/Default" and clothing != "Custom":
            prompt_parts.append(self.CLOTHING_OPTIONS[clothing])
        
        # Add custom details
        if additional_details.strip():
            prompt_parts.append(additional_details.strip())
        
        final_prompt = ", ".join(filter(None, prompt_parts))
        return (final_prompt, self.NEGATIVE_PROMPT, character)


# Keep backwards compatibility with old node name
AnimeCharacterSelector = AnimeCharacterSelectorV2


NODE_CLASS_MAPPINGS = {
    "MasonAnimeCharacterSelectorV2": AnimeCharacterSelectorV2,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonAnimeCharacterSelectorV2": "🎌 Character Selector V2 (260+ Anime/Cartoon)",
}

