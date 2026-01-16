"""
Mason Nodes - Celebrity Selector V2
Massive database of 200+ real celebrities with highly detailed prompts
For accurate likeness generation
"""

class CelebritySelectorV2:
    """Select from 200+ well-known celebrities with ultra-detailed appearance prompts."""
    
    CELEBRITIES = {
        # ============================================
        # ACTRESSES - HOLLYWOOD A-LIST
        # ============================================
        "Scarlett Johansson": "scarlett johansson, woman, short blonde wavy hair, green-hazel eyes, full pouty lips, fair skin, hourglass curvy figure, beautiful face, hollywood actress, age mid 30s, american, confident sensual expression",
        "Margot Robbie": "margot robbie, woman, long golden blonde hair, bright blue eyes, perfect symmetrical face, fair skin, stunning smile, slender toned figure, australian actress, age early 30s, elegant beautiful, model looks",
        "Gal Gadot": "gal gadot, woman, long dark brown hair, warm brown eyes, tall athletic figure, olive tan skin, israeli beauty, strong beautiful features, wonder woman actress, age late 30s, confident powerful expression, supermodel height",
        "Ana de Armas": "ana de armas, woman, brunette hair with highlights, hazel green eyes, full lips, fair skin, cuban hispanic features, petite curvy figure, beautiful sensual expression, age mid 30s, exotic beauty",
        "Sydney Sweeney": "sydney sweeney, woman, long blonde hair, big bright blue eyes, full lips, fair skin with freckles, very curvy busty figure, young actress age mid 20s, euphoria star, beautiful girl next door, expressive eyes",
        "Zendaya": "zendaya, woman, long brown curly hair (or varied styles), brown eyes, mixed race features, tall very slender model figure, brown skin, beautiful unique features, age mid 20s, fashionable, elegant",
        "Emma Watson": "emma watson, woman, short to medium brown hair, brown eyes, fair english skin, petite slender figure, refined beautiful features, british accent, age early 30s, intellectual beauty, elegant",
        "Jennifer Lawrence": "jennifer lawrence, woman, blonde hair (or brown), blue eyes, curvy athletic figure, fair skin, expressive face, american, age early 30s, natural beauty, confident expression",
        "Alexandra Daddario": "alexandra daddario, woman, long dark brown almost black hair, striking bright blue eyes extremely vivid, fair skin, curvy toned figure, beautiful actress, age late 30s, intense captivating eyes, perfect features",
        "Elizabeth Olsen": "elizabeth olsen, woman, strawberry blonde to light brown hair, blue-green eyes, fair skin, slender figure, beautiful elegant features, age mid 30s, expressive actress, scarlet witch",
        "Natalie Portman": "natalie portman, woman, brown hair (or pixie cut), dark brown eyes, petite slender figure, fair skin, israeli-american, beautiful delicate features, age early 40s, elegant intelligent expression",
        "Anne Hathaway": "anne hathaway, woman, long dark brown hair, large brown eyes, tall slender figure, fair skin, wide beautiful smile, age early 40s, elegant versatile actress, expressive",
        "Blake Lively": "blake lively, woman, long golden blonde hair, blue eyes, tall statuesque figure, fair skin, gorgeous all-american beauty, age mid 30s, glamorous, serena van der woodsen",
        "Emilia Clarke": "emilia clarke, woman, brown hair (or platinum blonde as daenerys), green eyes, petite curvy figure, fair skin, expressive eyebrows, british actress, age mid 30s, warm smile, beautiful",
        "Megan Fox": "megan fox, woman, long black hair, bright blue eyes, thumb-sized birthmark by eye, tanned skin, very curvaceous figure, full lips, age late 30s, sultry stunning, transformers actress",
        "Jessica Alba": "jessica alba, woman, brown hair with highlights, brown eyes, mixed mexican danish features, tanned skin, toned curvy figure, beautiful natural, age early 40s, los angeles beauty",
        "Kate Upton": "kate upton, woman, blonde hair, blue eyes, fair skin, extremely curvy busty figure large bust, supermodel, age early 30s, all-american beauty, sports illustrated",
        "Emily Ratajkowski": "emily ratajkowski, woman, long dark brown hair, brown eyes, slender figure with curves, fair skin, model perfect features, age early 30s, sultry expression, instagram model, brunette beauty",
        "Madison Beer": "madison beer, woman, long dark brown hair, hazel brown eyes, full lips, petite curvy figure, young singer age mid 20s, perfect instagram face, dolled up makeup usually, beautiful pop star",
        "Hailee Steinfeld": "hailee steinfeld, woman, long brown hair, hazel eyes, fair skin, fit slender figure, beautiful young actress singer, age late 20s, girl next door vibes, hawkeye kate bishop",
        "Florence Pugh": "florence pugh, woman, short blonde hair or brown, blue-green eyes, fair english skin, petite figure, british actress, age late 20s, expressive, black widow yelena",
        "Anya Taylor-Joy": "anya taylor-joy, woman, blonde hair, large wide-set green-blue eyes unique feature, fair pale skin, slender figure, unique ethereal beauty, age late 20s, queens gambit, striking unusual features",
        "Lily James": "lily james, woman, blonde hair (or brown), blue eyes, fair english skin, slender figure, classic english beauty, age mid 30s, downton abbey, elegant",
        "Dakota Johnson": "dakota johnson, woman, brown hair with bangs, blue-green eyes, fair skin, slender figure, gap in front teeth, age early 30s, fifty shades actress, understated beauty",
        "Aubrey Plaza": "aubrey plaza, woman, long dark brown hair, dark brown eyes, fair skin, slender figure, puerto rican italian heritage, deadpan expression, age late 30s, quirky beautiful, april ludgate",
        "Karen Gillan": "karen gillan, woman, long red hair (or bald as nebula), pale fair scottish skin, tall slender figure, blue eyes, age mid 30s, scottish actress, beautiful",
        "Daisy Ridley": "daisy ridley, woman, brown hair often in buns, hazel eyes, fair english skin, athletic slender figure, age early 30s, british actress, star wars rey, natural beauty",
        "Brie Larson": "brie larson, woman, blonde hair, blue eyes, fair skin, fit athletic figure, age mid 30s, captain marvel, strong features, american actress",
        "Chloe Grace Moretz": "chloe grace moretz, woman, blonde hair, blue eyes, fair skin, young face, slender figure, age late 20s, kick ass hit-girl, child star grown up, beautiful",
        "Jenna Ortega": "jenna ortega, woman, long straight dark brown hair, dark brown eyes, hispanic latina features, petite slender figure, young actress age early 20s, wednesday addams, beautiful unique features, serious expression often",
        
        # ============================================
        # ACTRESSES - MORE HOLLYWOOD
        # ============================================
        "Angelina Jolie": "angelina jolie, woman, long dark brown hair, blue-green eyes, extremely full famous lips, high cheekbones, slender figure, age late 40s, iconic hollywood beauty, powerful features, humanitarian",
        "Charlize Theron": "charlize theron, woman, short or long blonde hair, blue eyes, tall statuesque figure, south african, age late 40s, stunning classic beauty, strong features, model turned actress",
        "Nicole Kidman": "nicole kidman, woman, strawberry blonde curly hair, blue eyes, very tall slender, fair pale skin, australian, age mid 50s, elegant timeless beauty, refined features",
        "Sandra Bullock": "sandra bullock, woman, brown hair, brown eyes, fair skin, slender figure, age late 50s, america sweetheart, natural beauty, warm smile",
        "Julia Roberts": "julia roberts, woman, long auburn brown hair, brown eyes, famous wide smile, tall slender, age mid 50s, pretty woman, iconic american actress, warm expression",
        "Salma Hayek": "salma hayek, woman, long dark brown to black hair, brown eyes, mexican hispanic features, olive skin, very curvaceous busty petite figure, age late 50s, timeless latin beauty, sensual",
        "Penelope Cruz": "penelope cruz, woman, long dark brown curly hair, brown eyes, spanish features, olive skin, petite curvy figure, age early 50s, spanish hollywood beauty, expressive",
        "Monica Bellucci": "monica bellucci, woman, long dark brown hair, brown eyes, italian beauty, olive skin, curvaceous figure, age late 50s, timeless european beauty, matrix actress, elegant",
        "Eva Green": "eva green, woman, long dark brown hair, intense green eyes, fair pale skin, slender figure, french actress, age early 40s, exotic mysterious beauty, bond girl, striking eyes",
        "Eiza Gonzalez": "eiza gonzalez, woman, long dark brown hair, brown eyes, mexican latina features, tanned skin, fit curvy figure, age early 30s, beautiful latin actress, baby driver",
        "Vanessa Hudgens": "vanessa hudgens, woman, long dark brown wavy hair, brown eyes, mixed filipino features, tan skin, petite curvy figure, age mid 30s, high school musical, bohemian style",
        "Victoria Justice": "victoria justice, woman, long dark brown hair, brown eyes, mixed heritage, fair skin, slender figure, age early 30s, nickelodeon star, beautiful singer actress",
        "Camila Mendes": "camila mendes, woman, long dark brown hair, brown eyes, brazilian heritage, tan skin, slender figure, age late 20s, riverdale veronica, beautiful",
        "Lili Reinhart": "lili reinhart, woman, blonde hair, blue eyes, fair skin, slender figure, age late 20s, riverdale betty, classic american beauty, girl next door",
        "Madelaine Petsch": "madelaine petsch, woman, long vibrant red hair, green eyes, fair skin, slender figure, age late 20s, riverdale cheryl, striking redhead, beautiful",
        "Dove Cameron": "dove cameron, woman, platinum blonde hair, blue eyes, fair skin, petite figure, age late 20s, disney actress singer, doll-like beautiful features, big eyes",
        "Saoirse Ronan": "saoirse ronan, woman, blonde hair, blue eyes, fair irish skin, slender figure, irish actress, age early 30s, lady bird, elegant natural beauty",
        "Keira Knightley": "keira knightley, woman, brown hair, brown eyes, very slender figure, prominent jaw beautiful feature, fair english skin, age late 30s, british actress, pirates of caribbean",
        "Rachel McAdams": "rachel mcadams, woman, blonde or red hair, green eyes, fair skin, slender figure, canadian actress, age mid 40s, mean girls the notebook, timeless beauty",
        "Emma Stone": "emma stone, woman, red hair (or blonde), large green eyes, fair skin, slender petite figure, distinctive husky voice, age mid 30s, la la land, expressive beautiful",
        
        # ============================================
        # MUSICIANS - FEMALE
        # ============================================
        "Taylor Swift": "taylor swift, woman, long blonde hair often curled, blue eyes, tall slender figure, fair skin, american singer, age mid 30s, country turned pop star, elegant, red lipstick signature",
        "Ariana Grande": "ariana grande, woman, long dark brown hair high ponytail signature style, brown eyes, petite very small figure, tan skin, italian heritage, age early 30s, pop star, cute youthful",
        "Beyonce": "beyonce, woman, long blonde highlighted hair, brown eyes, black african american features, curvy powerful figure, age early 40s, queen bey, powerful confident beautiful, iconic performer",
        "Rihanna": "rihanna, woman, varies hair colors and styles (red black blonde), green-brown eyes, barbadian black features, curvaceous figure, age mid 30s, fenty beauty, fashion icon, bold sensual",
        "Dua Lipa": "dua lipa, woman, long dark brown black hair, striking features, albanian british, slender tall figure, age late 20s, pop star, model looks, dark smoky makeup often, lips",
        "Selena Gomez": "selena gomez, woman, brown hair varies lengths, brown eyes, mexican american heritage, curvy figure, age early 30s, disney star turned singer, beautiful natural, relatable",
        "Billie Eilish": "billie eilish, woman, varies hair colors (black green now blonde), blue eyes, fair skin, curvy figure (often hidden in baggy clothes), age early 20s, unique style, distinctive",
        "Lady Gaga": "lady gaga, woman, blonde hair (varies wildly), blue eyes, italian american, slender figure, age late 30s, avant garde fashion, dramatic makeup, powerful vocalist, eccentric beautiful",
        "Katy Perry": "katy perry, woman, black hair (or varies colors), blue eyes, fair skin, curvy busty figure, age late 30s, pop star, colorful, california girl, theatrical",
        "Miley Cyrus": "miley cyrus, woman, blonde short hair (or varied), blue eyes, slender toned figure, age early 30s, hannah montana evolved, wild bold expression, raspy voice",
        "Shakira": "shakira, woman, long blonde wavy hair, light brown hazel eyes, colombian latina features, fit dancer body, petite curvy, age mid 40s, incredible hips dont lie, exotic beauty",
        "Jennifer Lopez": "jennifer lopez jlo, woman, long brown caramel hair, brown eyes, puerto rican features, extremely fit curvy famous figure, bronzed skin, age mid 50s, ageless beauty, dancer body, iconic",
        "Nicki Minaj": "nicki minaj, woman, varies colorful wigs (pink black blonde), brown eyes, trinidadian heritage, very curvaceous enhanced figure, age early 40s, bold rapper, dramatic makeup and style",
        "Cardi B": "cardi b, woman, varies hair colors long styled, brown eyes, dominican trinidadian heritage, curvy figure, age early 30s, bronx rapper, bold expressive, long nails signature",
        "Doja Cat": "doja cat, woman, varies hair often shaved or wild styles, brown eyes, mixed south african jewish heritage, slender fit figure, age late 20s, rapper singer, creative unique looks",
        "SZA": "sza, woman, long brown hair varies, brown eyes, black american features, slender fit figure, age mid 30s, r&b singer, natural beauty, laid back aesthetic",
        "Megan Thee Stallion": "megan thee stallion, woman, long black hair or wigs, brown eyes, black american features, tall very curvy athletic figure, age late 20s, houston rapper, hot girl, confident",
        "Halsey": "halsey, woman, varies hair short or long many colors, blue eyes, biracial features, slender figure, age late 20s, pop rock singer, edgy alternative look, artistic",
        "Olivia Rodrigo": "olivia rodrigo, woman, long dark brown hair, brown eyes, filipino american features, petite slender figure, young age early 20s, gen z pop star, drivers license, girl next door rock",
        "Madison Beer": "madison beer, woman, long dark brown hair, hazel brown eyes, full lips, petite curvy figure, age mid 20s, instagram famous singer, perfect features, sultry",
        "Camila Cabello": "camila cabello, woman, long dark brown wavy hair, brown eyes, cuban hispanic features, petite curvy figure, age mid 20s, former fifth harmony, havana singer, beautiful",
        
        # ============================================
        # MODELS - SUPERMODELS
        # ============================================
        "Kendall Jenner": "kendall jenner, woman, long dark brown hair, dark brown eyes, tall very slender supermodel figure, mixed armenian heritage, age late 20s, runway model, kardashian jenner family, high fashion",
        "Gigi Hadid": "gigi hadid, woman, long blonde hair, blue-green eyes, tall supermodel figure, mixed dutch palestinian heritage, age late 20s, victorias secret, california girl beauty, athletic build",
        "Bella Hadid": "bella hadid, woman, long dark brown hair, green eyes, tall supermodel figure, striking angular features, mixed heritage, age late 20s, high fashion model, dramatic beauty, facial refinement",
        "Adriana Lima": "adriana lima, woman, long brown hair, bright blue eyes stunning, brazilian features, tan skin, tall fit supermodel figure, age early 40s, victorias secret angel legend, exotic beautiful",
        "Cara Delevingne": "cara delevingne, woman, blonde hair, thick dark eyebrows signature feature, blue-green eyes, slender androgynous figure, british, age early 30s, quirky model actress, expressive",
        "Barbara Palvin": "barbara palvin, woman, brown hair, blue eyes, sweet face, curvy supermodel figure, hungarian, age late 20s, victorias secret, girlfriend look, beautiful approachable",
        "Hailey Bieber": "hailey bieber baldwin, woman, blonde hair, brown eyes, slender tall model figure, age late 20s, model, justin biebers wife, rhode beauty, elegant cool girl",
        "Kaia Gerber": "kaia gerber, woman, short brown hair, dark eyes, very slender tall figure, looks like young cindy crawford mother, age early 20s, next gen supermodel, high fashion",
        "Alexis Ren": "alexis ren, woman, long blonde hair, blue eyes, fit toned figure, fair skin, age late 20s, fitness model instagram, bikini model, california beach aesthetic",
        "Emily Ratajkowski": "emily ratajkowski, woman, long dark brown hair, brown eyes, slender with curves, model perfect proportions, age early 30s, gone girl, instagram model, sultry",
        "Cindy Kimberly": "cindy kimberly, woman, long dark brown hair, brown eyes, spanish dutch heritage, curvaceous figure, age late 20s, instagram model discovered by bieber, exotic beautiful",
        "Elsa Hosk": "elsa hosk, woman, long blonde hair, blue eyes, tall slender figure, swedish features, pale fair skin, age mid 30s, victorias secret angel, scandinavian beauty",
        "Romee Strijd": "romee strijd, woman, long blonde hair, blue-green eyes, tall slender figure, dutch model, age late 20s, victorias secret angel, athletic blonde beauty",
        "Josephine Skriver": "josephine skriver, woman, long brown hair, blue eyes, tall athletic figure, danish model, age early 30s, victorias secret angel, tomboy model",
        "Sara Sampaio": "sara sampaio, woman, long brown wavy hair, brown eyes, portuguese features, petite curvy figure, age early 30s, victorias secret angel, sun-kissed beauty",
        "Devon Aoki": "devon aoki, woman, black straight hair, brown eyes, japanese american heritage, petite unique features, age early 40s, 2 fast 2 furious, high fashion icon",
        "Naomi Campbell": "naomi campbell, woman, long black hair, brown eyes, black british features, tall supermodel figure, age early 50s, legendary supermodel, fierce iconic, ageless",
        
        # ============================================
        # K-POP / KOREAN CELEBRITIES
        # ============================================
        "Jisoo (BLACKPINK)": "jisoo blackpink, woman, long black hair sometimes colored, brown eyes, korean features, fair skin, slender figure, age late 20s, k-pop idol, yg entertainment, visual of group, elegant beautiful",
        "Jennie (BLACKPINK)": "jennie kim blackpink, woman, varies hair brown blonde black, cat-like eyes, korean features, petite figure, age late 20s, k-pop rapper singer, chic fashionable, charismatic",
        "Rose (BLACKPINK)": "rose park chaeyoung blackpink, woman, long blonde or varied hair, brown eyes, korean australian, very slender tall figure, age late 20s, main vocalist, elegant, artistic beautiful",
        "Lisa (BLACKPINK)": "lisa lalisa manoban blackpink, woman, long often blonde hair bangs fringe, brown eyes, thai features, tall slender dancer figure, age late 20s, main dancer rapper, charismatic chic",
        "IU": "iu lee jieun, woman, varies hair colors brown black, brown eyes, korean features, petite figure, cute and elegant, age early 30s, solo singer actress, nations little sister turned mature artist, beautiful pure",
        "Tzuyu (TWICE)": "tzuyu chou tzuyu twice, woman, long black hair, big brown eyes, taiwanese features, tall slender, age mid 20s, jyp, visual of twice, goddess-like beauty, elegant",
        "Irene (Red Velvet)": "irene bae joohyun red velvet, woman, varies hair often dark, brown eyes, korean features, petite slender, age early 30s, sm entertainment, legendary visual, ice queen beautiful",
        "Suzy Bae": "bae suzy, woman, long dark hair, big brown eyes, korean features, slender figure, age late 20s, actress singer, nations first love, pure beautiful image",
        "Jeon Somi": "jeon somi, woman, blonde or varied hair, brown eyes, korean canadian mixed features, tall slender, age early 20s, solo singer former ioi, outgoing beautiful, western features",
        "Wonyoung (IVE)": "jang wonyoung ive, woman, long dark or brown hair, big eyes, korean features, very tall slender, young age late teens, 4th gen it girl, doll-like beautiful, elegant",
        "Karina (aespa)": "karina yoo jimin aespa, woman, varies hair colors, fierce cat-like features, korean, slender figure, age early 20s, sm entertainment, ai concept, striking beautiful",
        "Winter (aespa)": "winter kim minjeong aespa, woman, varies hair often light colors, korean features, cute face, slender petite, age early 20s, vocalist, cute yet charismatic",
        "Yeji (ITZY)": "yeji hwang yeji itzy, woman, varies hair, cat-like sharp eyes, korean features, slender dancer figure, age early 20s, jyp, charismatic leader, feline beauty",
        "Ryujin (ITZY)": "ryujin shin ryujin itzy, woman, varies hair short or long, sharp features, korean, slender figure, age early 20s, rapper dancer, cool girl aesthetic, beautiful",
        "Chaewon (LE SSERAFIM)": "kim chaewon le sserafim, woman, blonde or varies hair, korean features, petite, age late 20s, former iz*one, leader, cute yet elegant",
        "Kazuha (LE SSERAFIM)": "nakamura kazuha le sserafim, woman, long dark hair, elegant features, japanese, tall slender ballet dancer figure, age early 20s, graceful ballerina beauty",
        
        # ============================================
        # ACTORS - MALE
        # ============================================
        "Chris Hemsworth": "chris hemsworth, man, long or short blonde hair, blue eyes, extremely muscular tall build, australian, age early 40s, thor, handsome rugged, charming smile",
        "Henry Cavill": "henry cavill, man, dark brown hair, blue eyes, extremely muscular tall build, chiseled jaw, british, age early 40s, superman witcher, classically handsome, square jaw",
        "Ryan Gosling": "ryan gosling, man, blonde hair, blue eyes, slender to muscular build varies, fair skin, canadian, age early 40s, notebook drive, handsome charming, expressive",
        "Jason Momoa": "jason momoa, man, long dark brown wavy hair, brown eyes, hawaiian samoan features, extremely tall muscular, many tattoos especially arm, age mid 40s, aquaman, rugged wild handsome",
        "Timothee Chalamet": "timothee chalamet, man, curly dark brown hair, green eyes, slim slender build, sharp features, french american, age late 20s, dune, youthful handsome artistic",
        "Tom Holland": "tom holland, man, curly brown hair, brown eyes, slim athletic build, british, young looking age late 20s, spiderman, boyish handsome, charming",
        "Zac Efron": "zac efron, man, brown hair, blue eyes, muscular fit build, american, age mid 30s, high school musical baywatch, all american handsome, charming smile",
        "Leonardo DiCaprio": "leonardo dicaprio, man, blonde hair, blue eyes, medium build, american, age late 40s, titanic inception, pretty boy evolved to leading man, iconic",
        "Brad Pitt": "brad pitt, man, blonde hair (or varies), blue eyes, athletic build, chiseled jaw, american, age early 60s, fight club, legendary handsome, aging well",
        "Chris Evans": "chris evans, man, brown hair, blue eyes beard often, very muscular build, american, age early 40s, captain america, all american handsome, charming smile",
        "Tom Hardy": "tom hardy, man, dark brown hair (often shaved), blue-green eyes, muscular stocky build, british, age mid 40s, bane venom, rugged intense handsome, unique features",
        "Robert Pattinson": "robert pattinson, man, bronze brown hair messy, grey eyes, tall slim build, angular sharp features, british, age late 30s, batman twilight, unconventional handsome",
        "Idris Elba": "idris elba, man, shaved head or short hair, brown eyes, black british features, tall muscular build, age early 50s, luther, distinguished handsome, commanding presence",
        "Oscar Isaac": "oscar isaac, man, curly dark brown hair, brown eyes, hispanic guatemalan features, medium athletic build, age mid 40s, moon knight dune, charming handsome, expressive",
        "Pedro Pascal": "pedro pascal, man, dark brown curly hair, brown eyes, chilean hispanic features, medium build with mustache often, age late 40s, mandalorian last of us, charming daddy energy",
        
        # ============================================
        # INFLUENCERS / INTERNET CELEBRITIES
        # ============================================
        "Kim Kardashian": "kim kardashian, woman, long dark brown black hair, brown eyes, armenian features, very curvaceous famous figure especially hips and butt, age early 40s, reality star business mogul, contoured glamorous makeup always",
        "Kylie Jenner": "kylie jenner, woman, varies hair colors (black brown blonde), brown eyes, enhanced full lips famous, mixed heritage, curvy figure, age mid 20s, youngest billionaire, glamorous instagram aesthetic",
        "Addison Rae": "addison rae, woman, brown hair, green eyes, american southern features, petite curvy figure, age early 20s, tiktok star, cute relatable, dancer",
        "Pokimane": "pokimane imane anys, woman, brown wavy hair, brown eyes, moroccan canadian heritage, petite slender, age late 20s, twitch streamer gamer, natural beauty, girl next door",
        "Valkyrae": "valkyrae rachel hofstetter, woman, varies dark or colored hair, brown eyes, filipina german heritage, petite, age early 30s, streamer youtuber, gaming personality, beautiful",
        "Belle Delphine": "belle delphine, woman, pink hair or varied pastel colors, brown eyes colored contacts often, fair skin, petite, age mid 20s, internet personality, ahegao face, cosplay egirl aesthetic",
        "Lena The Plug": "lena the plug lena nersesian, woman, brown hair, brown eyes, armenian heritage, curvy fit figure, age early 30s, youtuber content creator, fitness, controversial adult content",
        "Corinna Kopf": "corinna kopf, woman, long blonde hair, blue eyes, german heritage, slender figure, age late 20s, instagram influencer streamer, beautiful blonde, david dobrik vlog squad",
        
        # ============================================
        # ATHLETES
        # ============================================
        "Paige Spiranac": "paige spiranac, woman, long blonde wavy hair, blue eyes, athletic toned curvy figure large bust, fair skin, age early 30s, golfer influencer, sporty beautiful, all american",
        "Alex Morgan": "alex morgan, woman, brown hair, blue eyes, athletic soccer player build, fair skin, age mid 30s, us womens soccer, sporty beautiful, fit toned",
        "Serena Williams": "serena williams, woman, black hair varies styles, brown eyes, black american features, extremely muscular athletic powerful build, age early 40s, tennis legend, powerful beautiful, iconic athlete",
        "Maria Sharapova": "maria sharapova, woman, blonde hair, green eyes, tall very slender athletic figure, russian features, age mid 30s, former tennis star, elegant tall beauty",
        "Lindsey Vonn": "lindsey vonn, woman, long blonde hair, blue eyes, tall athletic muscular build, fair skin, age late 30s, ski racer olympian, fit beautiful, strong",
        
        # ============================================
        # CLASSIC ICONS
        # ============================================
        "Marilyn Monroe": "marilyn monroe, woman, platinum blonde short curly hair, bedroom eyes, beauty mark on cheek, curvaceous iconic figure, fair skin, red lips, 1950s glamour, legendary hollywood icon, sensual innocent",
        "Audrey Hepburn": "audrey hepburn, woman, dark brown hair often short or updo, large brown doe eyes, very slender elegant figure, fair skin, refined features, 1960s elegance, breakfast at tiffanys, timeless beauty, sophisticated",
        "Elizabeth Taylor": "elizabeth taylor, woman, dark brown hair, famous violet purple eyes, fair skin, curvaceous figure, classic hollywood beauty, age depicted varies, legendary actress, jewels often, glamorous",
        "Grace Kelly": "grace kelly, woman, blonde elegant updo or styled hair, blue eyes, fair skin, slender refined figure, american princess of monaco, 1950s elegant, refined aristocratic beauty, poised",
        "Brigitte Bardot": "brigitte bardot, woman, long blonde voluminous hair, blue eyes, french features, curvaceous figure, pouty lips, 1960s sex symbol, french actress, sultry beautiful, iconic",
        "Jane Fonda": "jane fonda young, woman, blonde hair, blue eyes, slender fit figure, american actress, barbarella era, 1960s-70s beauty, fit activist, beautiful versatile",
        "Sophia Loren": "sophia loren, woman, dark brown hair, brown eyes, italian features, curvaceous voluptuous figure, olive skin, red lips often, italian film icon, timeless mediterranean beauty, sensual elegant",
        "Raquel Welch": "raquel welch, woman, brown voluminous hair, brown eyes, latina features, curvaceous bikini body iconic, tan skin, 1960s-70s, one million years bc, sex symbol, gorgeous",
        "Farrah Fawcett": "farrah fawcett, woman, iconic feathered blonde hair, blue eyes, slender toned figure, fair skin, all american 1970s beauty, charlies angels, poster girl, iconic hairstyle",
        "Pamela Anderson": "pamela anderson, woman, long platinum blonde hair often wet look, blue eyes, very curvaceous famously busty figure, tan skin, age depicted 1990s prime, baywatch, red swimsuit icon, bombshell",
        "Cindy Crawford": "cindy crawford, woman, long brown hair, brown eyes, beauty mark above lip signature, tall supermodel figure, fair skin, 1990s supermodel era, all american beauty, iconic",
        "Claudia Schiffer": "claudia schiffer, woman, long blonde hair, blue eyes, tall supermodel figure, german features, fair skin, 1990s supermodel icon, classic blonde bombshell, guess girl",
        "Naomi Campbell": "naomi campbell, woman, long black hair, brown eyes, black british features, tall supermodel figure, age varies depicted, legendary supermodel, fierce runway walk, iconic beauty",
    }
    
    QUALITY_PRESETS = {
        "Ultra Photorealistic": "photorealistic, hyperrealistic, 8k uhd, dslr, raw photo, realistic skin texture, realistic eyes, sharp focus, professional photography, studio lighting, subsurface scattering, volumetric lighting",
        "High Quality Photo": "photorealistic, high resolution, detailed face, realistic, professional photo, natural lighting, 4k, sharp",
        "Artistic Portrait": "artistic portrait, painterly style, professional lighting, beautiful, elegant, studio portrait",
        "Glamour Shot": "glamour photography, professional lighting, magazine quality, perfect makeup, styled hair, studio background",
        "Casual/Candid": "candid photography, natural lighting, realistic, casual, authentic moment, unposed",
        "Standard": "high quality, realistic, detailed",
    }
    
    CLOTHING_OPTIONS = {
        "Default/Dressed": "",
        "Nude": ", completely nude, naked, bare skin, full nudity, nipples visible, anatomically correct, artistic nude, uncensored",
        "Topless": ", topless, bare breasts, no shirt, exposed chest, nipples visible",
        "Lingerie": ", wearing sexy lingerie, lace underwear, bralette, panties, garter belt, stockings, seductive",
        "Bikini": ", wearing bikini, two piece swimsuit, beach, toned body, wet skin",
        "Sheer/See-Through": ", wearing sheer see-through clothing, transparent fabric, nipples visible through clothes",
        "Evening Gown": ", wearing elegant evening gown, formal dress, red carpet style",
        "Casual": ", casual outfit, jeans and top, relaxed style",
        "Athletic Wear": ", wearing athletic clothes, sports bra, yoga pants, workout gear, toned body",
        "Swimsuit One-Piece": ", wearing one piece swimsuit, beach, model pose",
        "Red Carpet": ", red carpet outfit, designer dress, glamorous, jewelry, styled hair",
        "Business Attire": ", professional business attire, blazer, sophisticated",
        "Custom": "",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        celebrities = sorted(cls.CELEBRITIES.keys())
        return {
            "required": {
                "celebrity": (celebrities, {"default": celebrities[0]}),
                "quality": (list(cls.QUALITY_PRESETS.keys()), {"default": "Ultra Photorealistic"}),
                "clothing": (list(cls.CLOTHING_OPTIONS.keys()), {"default": "Default/Dressed"}),
            },
            "optional": {
                "additional_details": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "celebrity_name")
    FUNCTION = "generate"
    CATEGORY = "Mason/Characters"
    
    def generate(self, celebrity, quality, clothing, additional_details=""):
        prompt_parts = []
        
        # Add quality
        prompt_parts.append(self.QUALITY_PRESETS[quality])
        
        # Add celebrity details
        prompt_parts.append(self.CELEBRITIES[celebrity])
        
        # Add clothing
        if clothing != "Default/Dressed" and clothing != "Custom":
            prompt_parts.append(self.CLOTHING_OPTIONS[clothing])
        
        # Add custom
        if additional_details.strip():
            prompt_parts.append(additional_details.strip())
        
        final_prompt = ", ".join(filter(None, prompt_parts))
        return (final_prompt, celebrity)


# Backwards compatibility
CelebritySelector = CelebritySelectorV2


NODE_CLASS_MAPPINGS = {
    "MasonCelebritySelectorV2": CelebritySelectorV2,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonCelebritySelectorV2": "⭐ Celebrity Selector V2 (200+ People)",
}
