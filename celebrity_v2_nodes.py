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
        
        # ============================================
        # ADULT CONTENT CREATORS / PERFORMERS
        # ============================================
        "Mia Khalifa": "mia khalifa, woman, long dark brown hair with glasses often, brown eyes, lebanese american features, curvy busty figure large bust, age early 30s, controversial former adult performer now sports commentator influencer, middle eastern beauty",
        "Lana Rhoades": "lana rhoades amara maple, woman, long brown hair (or blonde), blue-green eyes, fair skin, very curvy enhanced figure large bust, full lips, age late 20s, former adult actress now influencer, beautiful all american enhanced",
        "Riley Reid": "riley reid, woman, brown hair varies, brown eyes, petite very small figure, fair skin, age early 30s, famous adult performer, girl next door look, playful expression, small frame",
        "Abella Danger": "abella danger, woman, brown hair, hazel brown eyes, jewish ukrainian heritage, curvy athletic figure, age late 20s, adult performer, expressive, fit dancer body",
        "Angela White": "angela white, woman, long dark brown hair, brown hazel eyes, australian, very curvaceous busty natural figure, fair skin, age late 30s, adult performer producer, intelligent beautiful",
        "Mia Malkova": "mia malkova, woman, long blonde hair, blue eyes, fair skin, fit athletic figure, age early 30s, adult performer, dancer flexibility, all american blonde beauty",
        "Adriana Chechik": "adriana chechik, woman, long dark brown hair, brown eyes, mixed heritage, athletic petite figure, age early 30s, former adult performer now twitch streamer gamer, energetic",
        "Nicole Aniston": "nicole aniston, woman, long blonde hair, brown eyes, fair skin, athletic toned figure enhanced bust, age early 40s, adult performer, california girl aesthetic",
        "Madison Ivy": "madison ivy, woman, red hair (varies), hazel eyes, petite very fit figure enhanced bust, age late 30s, adult performer, athletic small frame, distinctive look",
        "Asa Akira": "asa akira, woman, long black hair, brown eyes, japanese american features, petite slender figure, age late 30s, adult performer author, asian beauty, articulate",
        "Lisa Ann": "lisa ann, woman, long dark brown hair, brown eyes, italian heritage, curvaceous mature figure, age early 50s, legendary milf performer, mature beauty",
        "Brandi Love": "brandi love, woman, blonde hair, blue eyes, fair skin, fit toned mature figure, age early 50s, adult performer, mature elegant, fitness focused",
        "Kendra Lust": "kendra lust, woman, long dark brown hair, brown eyes, fit athletic muscular figure, age mid 40s, adult performer, gym physique, milf category",
        "Eva Lovia": "eva lovia, woman, long dark brown hair, brown eyes, mixed japanese spanish heritage, petite curvy figure, age early 30s, former adult performer, exotic beautiful",
        "Dani Daniels": "dani daniels, woman, long brown hair, brown eyes, fair skin, fit athletic figure, age mid 30s, adult performer artist, tomboy aesthetic, natural beauty",
        "Sasha Grey": "sasha grey, woman, dark brown hair short or long, grey-blue eyes, fair skin, slender figure, age mid 30s, former adult performer now actress dj, alternative edgy, intelligent",
        "Jenna Jameson": "jenna jameson, woman, platinum blonde hair, blue eyes, fair skin, curvaceous enhanced figure, age depicted 1990s-2000s prime, legendary adult performer, iconic",
        "Tera Patrick": "tera patrick, woman, long dark brown hair, brown eyes, mixed thai heritage, tall curvaceous figure, age depicted 2000s prime, legendary adult performer, exotic bombshell",
        "Jesse Jane": "jesse jane, woman, blonde hair, blue eyes, fair skin, curvaceous enhanced figure, age depicted 2000s prime, adult performer, barbie-like, all american blonde",
        "Kayden Kross": "kayden kross, woman, long blonde hair, blue eyes, slender athletic figure, fair skin, age mid 30s, adult performer director, elegant beauty, intelligent",
        "Stoya": "stoya, woman, dark brown hair pale skin gothic aesthetic, blue eyes, slender petite figure, age mid 30s, adult performer writer, alternative intellectual, striking pale beauty",
        "Janice Griffith": "janice griffith, woman, dark brown hair, brown eyes, petite small figure, fair skin, age late 20s, adult performer, alternative look, tattoos",
        "Elsa Jean": "elsa jean, woman, long blonde hair, blue eyes, very petite small figure, fair skin, age late 20s, adult performer, innocent look, tiny blonde",
        "Piper Perri": "piper perri, woman, blonde hair, blue eyes, extremely petite very small figure, fair skin, age late 20s, adult performer, tiny frame",
        "Gabbie Carter": "gabbie carter, woman, long brown hair, brown eyes, curvy busty natural figure very large bust, age early 20s, adult performer, natural curves, girl next door",
        "Autumn Falls": "autumn falls, woman, long dark brown hair, brown eyes, latina features, very curvy busty natural figure, age early 20s, adult performer, young curvy latina",
        "Emily Willis": "emily willis, woman, long dark brown hair, brown eyes, argentine heritage, petite fit figure, age early 20s, adult performer, energetic exotic",
        "Lena Paul": "lena paul, woman, long red-brown hair, blue eyes, curvy natural figure large natural bust, fair skin, age late 20s, adult performer, natural redhead curves",
        "Natasha Nice": "natasha nice, woman, long brown hair, brown eyes, french heritage, curvy busty natural figure, age mid 30s, adult performer, natural voluptuous french beauty",
        "Valentina Nappi": "valentina nappi, woman, long dark brown hair, brown eyes, italian features, curvy figure, olive skin, age early 30s, adult performer, italian beauty, athletic",
        "Eva Elfie": "eva elfie, woman, long blonde hair, blue eyes, russian features, petite slender figure, fair skin, age early 20s, adult performer influencer, russian blonde, cute innocent look",
        "Lexi Luna": "lexi luna, woman, short dark hair, brown eyes, petite curvy busty figure, age mid 30s, adult performer, milf aesthetic, approachable",
        "Reagan Foxx": "reagan foxx, woman, long dark brown hair, brown eyes, fit toned mature figure, age mid 40s, adult performer, milf fitness, sophisticated",
        "Skylar Vox": "skylar vox, woman, brown hair, brown eyes, very busty curvy young figure, age early 20s, adult performer, young natural curves",
        "LaSirena69": "lasirena69, woman, long dark hair, brown eyes, venezuelan latina features, extremely curvy busty figure, tan skin, age early 30s, adult performer, exotic latina curves",
        "Kendra Sunderland": "kendra sunderland, woman, long blonde hair, blue eyes, tall busty figure, fair skin, age late 20s, adult performer, library girl fame, blonde bombshell",
        "Haley Reed": "haley reed, woman, blonde hair, blue eyes, petite slender figure, fair skin, age late 20s, adult performer, girl next door blonde",
        
        # ============================================
        # ONLYFANS / SOCIAL MEDIA ADULT CREATORS
        # ============================================
        "Amouranth": "amouranth kaitlyn siragusa, woman, long red hair, green eyes, fair skin, fit curvy figure, age early 30s, twitch streamer onlyfans creator, cosplay, gamer girl, beautiful redhead",
        "Mia Malkova": "mia malkova, woman, long blonde hair, blue eyes, athletic fit figure dancer body, age early 30s, adult performer onlyfans, flexibility, all american blonde",
        "Alinity": "alinity natalia mogollon, woman, long dark brown hair, brown eyes, colombian heritage, slender figure, age early 30s, twitch streamer, latina beauty",
        "Indiefoxx": "indiefoxx, woman, long dark brown hair, brown eyes, hispanic features, curvy figure, age late 20s, streamer onlyfans, asmr content",
        "Bhad Bhabie": "bhad bhabie danielle bregoli, woman, brown hair often blonde, brown eyes, fair skin, petite figure, age early 20s, rapper onlyfans, controversial, cash me outside fame",
        "Iggy Azalea": "iggy azalea, woman, long blonde hair, blue eyes, australian, curvy enhanced figure, age early 30s, rapper onlyfans, tall statuesque, australian accent",
        "Blac Chyna": "blac chyna, woman, varies hair colors often blonde or colorful, brown eyes, black american features, very curvaceous enhanced figure, age mid 30s, model onlyfans, exaggerated curves",
        "Tana Mongeau": "tana mongeau, woman, long blonde hair, blue eyes, fair skin, curvy figure, age mid 20s, youtuber onlyfans, influencer, bold personality",
        "Trisha Paytas": "trisha paytas, woman, long blonde hair, brown eyes, curvy plus size figure, age mid 30s, youtuber onlyfans, controversial, dramatic",
        
        # ============================================
        # RISING STARS / NEWER ACTRESSES
        # ============================================
        "Madelyn Cline": "madelyn cline, woman, long blonde hair, blue eyes, fair skin, slender fit figure, age late 20s, outer banks actress, beach vibes, southern beauty",
        "Chase Sui Wonders": "chase sui wonders, woman, long dark hair, brown eyes, mixed asian heritage, slender figure, age late 20s, actress singer, unique beauty",
        "Rachel Zegler": "rachel zegler, woman, long dark brown hair, brown eyes, colombian heritage, slender figure, age early 20s, west side story snow white, rising star, powerful voice",
        "Sadie Sink": "sadie sink, woman, long red hair, blue eyes, fair skin freckles, slender figure, age early 20s, stranger things max, striking redhead, expressive",
        "Millie Bobby Brown": "millie bobby brown, woman, brown hair varies, brown eyes, british, petite figure, age early 20s, stranger things eleven, young star grown up",
        "Hunter Schafer": "hunter schafer, woman, long blonde hair, blue eyes, very tall slender model figure, fair skin, age mid 20s, euphoria jules, model actress, androgynous beauty",
        "Maude Apatow": "maude apatow, woman, dark curly hair, brown eyes, fair skin, slender figure, age late 20s, euphoria lexi, nepotism baby turned talent, natural beauty",
        "Alexa Demie": "alexa demie, woman, dark hair often styled dramatically, brown eyes, latina features, slender figure, age early 30s, euphoria maddy, dramatic makeup iconic, stunning",
        "Barbie Ferreira": "barbie ferreira, woman, brown hair, brown eyes, brazilian heritage, plus size curvy figure, age late 20s, euphoria kat, body positive, beautiful curves",
        "Storm Reid": "storm reid, woman, brown hair varies, brown eyes, black american features, slender figure, age early 20s, euphoria rue's sister, rising star",
        "Maitreyi Ramakrishnan": "maitreyi ramakrishnan, woman, long dark brown hair, brown eyes, tamil canadian heritage, slender figure, age early 20s, never have i ever, south asian representation",
        "Lana Condor": "lana condor, woman, long dark hair, brown eyes, vietnamese heritage, petite figure, age late 20s, to all the boys, asian american beauty",
        "Isabela Merced": "isabela merced, woman, long dark brown hair, brown eyes, peruvian heritage, petite curvy figure, age early 20s, dora transformers, rising latina star",
        "Xochitl Gomez": "xochitl gomez, woman, long dark brown hair, brown eyes, mexican heritage, teen figure, age late teens, doctor strange america chavez, young rising star",
        "Dominique Thorne": "dominique thorne, woman, black hair varies, brown eyes, trinidadian heritage, slender figure, age late 20s, black panther ironheart, rising star",
        "Letitia Wright": "letitia wright, woman, black hair varies, brown eyes, guyanese british, slender figure, age early 30s, black panther shuri, rising star",
        "Ella Purnell": "ella purnell, woman, dark brown hair, large green eyes, british, slender petite figure, age late 20s, yellowjackets fallout, distinctive large eyes",
        "Diana Silvers": "diana silvers, woman, brown hair, blue eyes, fair skin, tall slender model figure, age late 20s, booksmart, model actress, natural beauty",
        "Thomasin McKenzie": "thomasin mckenzie, woman, blonde hair, blue eyes, new zealand features, slender figure, age mid 20s, jojo rabbit, innocent beauty",
        "Jessie Buckley": "jessie buckley, woman, red curly hair, blue eyes, irish features, slender figure, age mid 30s, fargo, fiery redhead actress",
        "Daisy Edgar-Jones": "daisy edgar jones, woman, brown hair, green eyes, british, slender figure, age late 20s, normal people, english rose beauty",
        "Phoebe Dynevor": "phoebe dynevor, woman, auburn hair, blue eyes, british, slender figure, age late 20s, bridgerton daphne, regency beauty",
        "Simone Ashley": "simone ashley, woman, long dark brown hair, brown eyes, british tamil heritage, slender figure, age late 20s, bridgerton kate, south asian british beauty",
        "Charithra Chandran": "charithra chandran, woman, long dark hair, brown eyes, british indian heritage, slender figure, age late 20s, bridgerton edwina, south asian beauty",
        
        # ============================================
        # MORE INFLUENCERS / TIKTOK / YOUTUBE
        # ============================================
        "Charli D'Amelio": "charli damelio, woman, long dark brown hair, brown eyes, italian heritage, petite dancer figure, age early 20s, tiktok star, dancer, girl next door",
        "Dixie D'Amelio": "dixie damelio, woman, dark brown hair, brown eyes, fair skin, slender figure, age early 20s, tiktok star singer, charli's sister",
        "Loren Gray": "loren gray, woman, blonde or varies hair, blue eyes, fair skin, slender figure, age early 20s, tiktok star singer, doll-like features",
        "Avani Gregg": "avani gregg, woman, dark hair often styled dramatically, brown eyes, mixed heritage, petite figure, age early 20s, tiktok star, makeup skills",
        "Madi Monroe": "madi monroe, woman, blonde hair, blue eyes, fair skin, slender figure, age early 20s, tiktok star, blonde beauty",
        "Nessa Barrett": "nessa barrett, woman, dark hair varies, brown eyes, fair skin, slender figure, age early 20s, tiktok star singer, alternative aesthetic",
        "Sommer Ray": "sommer ray, woman, long brown hair, brown eyes, fit extremely toned figure famous glutes, age late 20s, fitness influencer, gym body, squat queen",
        "Jen Selter": "jen selter, woman, long dark brown hair, brown eyes, fit toned figure famous glutes, age late 20s, fitness influencer, booty gains pioneer",
        "AnlleLa Sagra": "anllela sagra, woman, long brown hair, hazel eyes, colombian features, extremely fit muscular feminine figure, age late 20s, fitness model bodybuilder, athletic curves",
        "Michelle Lewin": "michelle lewin, woman, long blonde hair, brown eyes, venezuelan heritage, extremely fit muscular feminine figure, age mid 30s, fitness influencer, muscular beauty",
        "Brittany Renner": "brittany renner, woman, long dark hair, brown eyes, black american features, fit curvy athletic figure, age early 30s, fitness influencer, controversial, fit curves",
        "Lele Pons": "lele pons, woman, long blonde or brown hair, brown eyes, venezuelan heritage, slender figure, age late 20s, vine youtube star, latina influencer",
        "Hannah Stocking": "hannah stocking, woman, long dark brown hair, blue eyes, tall slender figure, fair skin, age early 30s, youtube comedian, tall beauty",
        "Liza Koshy": "liza koshy, woman, dark brown hair, brown eyes, mixed indian heritage, petite figure, age late 20s, youtube comedian actress, energetic cute",
        "Emma Chamberlain": "emma chamberlain, woman, brown hair varies, green eyes, fair skin, slender figure, age early 20s, youtube influencer, relatable aesthetic, coffee obsessed",
        "Alix Earle": "alix earle, woman, long blonde hair, blue eyes, fair skin, slender figure, age early 20s, tiktok influencer, grwm queen, all american",
        
        # ============================================
        # MORE MODELS / INSTAGRAM MODELS  
        # ============================================
        "Suki Waterhouse": "suki waterhouse, woman, long blonde hair, blue eyes, british, slender figure, fair skin, age early 30s, model actress singer, english rose",
        "Doutzen Kroes": "doutzen kroes, woman, long blonde hair, blue eyes, dutch features, tall slender figure, age late 30s, victorias secret angel, dutch supermodel",
        "Candice Swanepoel": "candice swanepoel, woman, long blonde hair, blue eyes, south african, tall slender figure, age mid 30s, victorias secret angel, blonde goddess",
        "Jasmine Tookes": "jasmine tookes, woman, long brown hair, brown eyes, black american features, tall athletic figure, age early 30s, victorias secret angel, athletic beauty",
        "Taylor Hill": "taylor hill, woman, long brown hair, green eyes, fair skin, tall slender figure, age late 20s, victorias secret angel, girl next door model",
        "Cami Morrone": "camila morrone, woman, long brown hair, brown eyes, argentine heritage, slender figure, age late 20s, model actress, natural beauty",
        "Yris Palmer": "yris palmer, woman, long dark hair, brown eyes, latina features, curvy fit figure, age early 30s, influencer entrepreneur, beauty mogul",
        "Amber Rose": "amber rose, woman, shaved platinum blonde head signature, brown eyes, mixed heritage, curvy figure, age early 40s, model influencer, bold look",
        "Jordyn Woods": "jordyn woods, woman, varies hair, brown eyes, black american features, curvy plus size figure, age late 20s, influencer model, body positive curves",
        "Tammy Hembrow": "tammy hembrow, woman, long blonde hair, blue eyes, australian, extremely fit curvy figure famous glutes, age late 20s, fitness influencer, gym body goals",
        "Natalie Roser": "natalie roser, woman, long blonde hair, blue eyes, australian, slender model figure, fair skin, age early 30s, fitness model, aussie blonde",
        "Nikita Dragun": "nikita dragun, woman, varies dramatic hair, brown eyes, trans woman vietnamese heritage, slender figure, age late 20s, influencer, dramatic glam",
        
        # ============================================
        # ADDITIONAL MUSICIANS
        # ============================================
        "Ice Spice": "ice spice, woman, distinctive orange curly hair, brown eyes, black american dominican heritage, curvy figure, age early 20s, rapper, unique hair signature, rising star",
        "Saweetie": "saweetie, woman, long blonde hair or varies, brown eyes, filipino chinese black heritage, slender curvy figure, age early 30s, rapper, icy girl, glamorous",
        "Normani": "normani, woman, long dark hair varies, brown eyes, black american features, fit dancer figure, age late 20s, former fifth harmony solo, powerful dancer",
        "Kehlani": "kehlani, woman, varies hair often colorful, brown eyes, mixed filipino black heritage, fit figure, tattoos, age late 20s, r&b singer, alternative beautiful",
        "Summer Walker": "summer walker, woman, long black hair, brown eyes, black american features, slender figure, age late 20s, r&b singer, soft-spoken beauty",
        "Jhene Aiko": "jhene aiko, woman, long dark hair, brown eyes, mixed japanese heritage, petite slender figure, tattoos, age mid 30s, r&b singer, ethereal beauty",
        "Tinashe": "tinashe, woman, long dark curly hair, brown eyes, mixed danish zimbabwean heritage, fit dancer figure, age early 30s, singer dancer, athletic beautiful",
        "Tyla": "tyla, woman, long dark hair, brown eyes, south african coloured heritage, slender figure, age early 20s, water singer, rising star, south african beauty",
        "Sabrina Carpenter": "sabrina carpenter, woman, blonde hair, brown eyes, petite figure, fair skin, age mid 20s, singer actress, disney alum grown up, espresso singer",
        "Tate McRae": "tate mcrae, woman, long brown hair, brown eyes, canadian, slender dancer figure, age early 20s, singer dancer, teen star grown up",
        
        # ============================================
        # GAMERS / STREAMERS
        # ============================================
        "Loserfruit": "loserfruit kathleen belsten, woman, long brown hair sometimes pink, brown eyes, australian, slender figure, age late 20s, twitch streamer fortnite, bubbly personality",
        "Fuslie": "fuslie leslie fu, woman, long dark hair, brown eyes, chinese american heritage, petite figure, age early 30s, twitch streamer, asian beauty gamer",
        "QuarterJade": "quarterjade jodi lee, woman, long dark hair, brown eyes, asian american heritage, petite figure, age late 20s, twitch streamer, gamer girl",
        "Kyedae": "kyedae, woman, long dark hair, brown eyes, japanese canadian heritage, slender figure, age early 20s, valorant streamer, gamer girlfriend aesthetic",
        "AriaSaki": "ariasaki, woman, long dark hair, brown eyes, asian heritage, petite figure, age late 20s, twitch streamer, anime aesthetic",
        "39daph": "39daph, woman, dark hair, brown eyes, korean canadian heritage, petite figure, age mid 20s, artist streamer, artistic edgy",
        "Sydeon": "sydeon, woman, dark hair, brown eyes, black american features, slender figure, age late 20s, twitch streamer offlinetv, gamer personality",
        "Lily Pichu": "lily pichu, woman, long dark hair, brown eyes, asian heritage, very petite figure, age early 30s, twitch streamer artist, cute voice anime aesthetic",
        
        # ============================================
        # K-POP IDOLS
        # ============================================
        "Jennie (BLACKPINK)": "jennie kim blackpink, woman, dark brown or blonde hair varies, cat-like eyes brown, korean features, petite slender figure, age late 20s, kpop idol, fierce sexy, fashion icon",
        "Lisa (BLACKPINK)": "lalisa manobal lisa blackpink, woman, long blonde or various hair, brown eyes, thai features, tall slender dancer figure, age late 20s, kpop idol, powerful dancer, model beauty",
        "Rosé (BLACKPINK)": "park chaeyoung rose blackpink, woman, long blonde or pink hair, brown eyes, korean australian, slender figure, age late 20s, kpop idol, angelic voice, elegant",
        "Jisoo (BLACKPINK)": "kim jisoo blackpink, woman, long dark brown hair, brown eyes, classic korean beauty, slender figure, age late 20s, kpop idol actress, visual, traditional beauty",
        "IU": "lee jieun iu, woman, long brown or black hair, brown eyes, korean features, petite slender figure, age early 30s, korean singer actress, innocent look, national sweetheart",
        "Irene (Red Velvet)": "bae joohyun irene red velvet, woman, long dark hair varies, brown eyes, perfect korean features, slender figure, age early 30s, kpop idol, legendary visual",
        "Tzuyu (TWICE)": "chou tzuyu twice, woman, long dark hair, brown eyes, taiwanese features, tall slender figure, age mid 20s, kpop idol, elegant tall beauty",
        "Wonyoung": "jang wonyoung, woman, long dark hair often styled, brown eyes, korean features, very tall slender figure, age late teens, kpop idol ive, doll-like, elegant",
        "Karina (aespa)": "yoo jimin karina aespa, woman, dark or colored hair, brown eyes, korean features, tall slender figure, age early 20s, kpop idol, ai concept, fierce beautiful",
        "Winter (aespa)": "kim minjeong winter aespa, woman, varies hair color, brown eyes, korean features, slender figure, age early 20s, kpop idol, innocent cute",
        
        # ============================================
        # MORE ACTRESSES - CLASSIC & CURRENT
        # ============================================
        "Monica Bellucci": "monica bellucci, woman, long dark brown hair, brown eyes, italian features, curvaceous voluptuous figure, age 40s-50s depicted, italian actress, timeless beauty, sensual",
        "Salma Hayek": "salma hayek, woman, long dark brown hair, brown eyes, mexican heritage, very curvaceous busty figure, age 50s, actress, latina bombshell, hourglass",
        "Sofia Vergara": "sofia vergara, woman, long brown hair, brown eyes, colombian features, very curvaceous busty figure, age 50s, modern family actress, colombian bombshell",
        "Jennifer Love Hewitt": "jennifer love hewitt, woman, long dark brown hair, brown eyes, fair skin, curvy busty figure, age 40s, actress, girl next door curves",
        "Megan Good": "megan good, woman, long dark hair, brown eyes, black american features, curvy figure, age early 40s, actress, beautiful black woman",
        "Rashida Jones": "rashida jones, woman, long dark hair, brown eyes, mixed black white heritage, slender figure, age late 40s, actress, natural beauty",
        "Hannah Waddingham": "hannah waddingham, woman, long blonde hair, blue eyes, british tall figure, statuesque, age late 40s, ted lasso actress, powerful presence",
        "Juno Temple": "juno temple, woman, long blonde hair, blue eyes, british petite figure, fair skin, age mid 30s, ted lasso actress, pixie-like",
        "Florence Pugh": "florence pugh, woman, short or medium blonde hair, green eyes, british, curvy petite figure, age late 20s, oppenheimer actress, bold beautiful",
        "Ana de Armas": "ana de armas, woman, long brown hair, green hazel eyes, cuban heritage, slender figure, age mid 30s, bond girl actress, exotic beauty",
        "Eiza Gonzalez": "eiza gonzalez, woman, long dark hair, brown eyes, mexican heritage, slender fit figure, age early 30s, actress, latina beauty",
        "Aubrey Plaza": "aubrey plaza, woman, long dark hair, brown eyes, puerto rican heritage, slender figure, age late 30s, parks and rec actress, deadpan beauty",
        "Elizabeth Olsen": "elizabeth olsen, woman, long strawberry blonde hair, blue-green eyes, fair skin, slender figure, age mid 30s, scarlet witch actress, natural beauty",
        "Hailee Steinfeld": "hailee steinfeld, woman, long dark brown hair, hazel eyes, fair skin, slender figure, age late 20s, actress singer, girl next door",
        "Samara Weaving": "samara weaving, woman, blonde hair, brown eyes, australian, slender figure, age early 30s, actress, striking features",
        "Margaret Qualley": "margaret qualley, woman, long dark hair, blue eyes, tall slender figure, fair skin, age late 20s, actress model, elegant dancer",
        "Daisy Ridley": "daisy ridley, woman, brown hair, hazel eyes, british, slender fit figure, fair skin, age early 30s, star wars rey, natural beauty",
        "Emilia Clarke": "emilia clarke, woman, dark brown hair, blue-green eyes, british petite, slender figure, age late 30s, game of thrones daenerys, expressive",
        "Nathalie Emmanuel": "nathalie emmanuel, woman, long curly dark hair, brown eyes, british black heritage, slender figure, age mid 30s, game of thrones missandei, natural curls",
        
        # ============================================
        # MORE ADULT PERFORMERS - NEWER
        # ============================================
        "Violet Myers": "violet myers, woman, long dark hair, brown eyes, mixed german filipino heritage, very busty curvy natural figure, age mid 20s, adult performer, exotic curves",
        "Savannah Bond": "savannah bond, woman, long blonde hair, blue eyes, australian, tall athletic busty figure, age late 20s, adult performer, aussie blonde bombshell",
        "Blake Blossom": "blake blossom, woman, long brown hair, blue eyes, fair skin, very busty natural figure tall, age early 20s, adult performer, natural beauty curves",
        "Coco Lovelock": "coco lovelock, woman, red hair, blue eyes, very petite small figure, fair skin, age early 20s, adult performer, tiny redhead",
        "Kenzie Reeves": "kenzie reeves, woman, blonde hair, blue eyes, very petite small figure, fair skin, age mid 20s, adult performer, tiny blonde",
        "Vanna Bardot": "vanna bardot, woman, brown hair, brown eyes, petite figure, fair skin, age early 20s, adult performer, girl next door",
        "Vina Sky": "vina sky, woman, long dark hair, brown eyes, vietnamese heritage, very petite small figure, age mid 20s, adult performer, tiny asian",
        "Aria Lee": "aria lee, woman, dark hair, brown eyes, korean heritage, petite figure, age mid 20s, adult performer, cute asian",
        "Avery Cristy": "avery cristy, woman, blonde hair, blue eyes, petite busty figure, age early 20s, adult performer, busty blonde teen",
        "Lily Lou": "lily lou, woman, brown hair, brown eyes, thick curvy figure, age early 20s, adult performer, thick curves",
        "Kazumi": "kazumi, woman, long dark hair, brown eyes, japanese heritage, petite curvy figure, tattoos, age late 20s, adult performer influencer, tattooed asian",
        "Baby Alien": "baby alien, woman, blonde hair, blue eyes, very petite small figure under 5 feet, age 20s, adult performer, famously tiny, pocket-sized",
        "Sophie Rain": "sophie rain, woman, dark hair, brown eyes, petite figure, age early 20s, rising content creator, viral spiderman",
        
        # ============================================
        # SPORTS FIGURES
        # ============================================
        "Paige Spiranac": "paige spiranac, woman, long blonde hair, blue eyes, athletic curvy figure, fair skin, age late 20s, golfer influencer, sporty bombshell",
        "Alex Morgan": "alex morgan, woman, long brown hair, brown eyes, athletic slender toned figure, fair skin, age mid 30s, soccer player, athlete beauty",
        "Simone Biles": "simone biles, woman, dark hair often with color, brown eyes, black american features, extremely petite muscular gymnast figure, age late 20s, olympian, powerful tiny athlete",
        "Olivia Dunne": "livvy dunne olivia dunne, woman, long blonde hair, blue eyes, slender athletic gymnast figure, fair skin, age early 20s, lsu gymnast influencer, tiktok famous",
        "McKayla Maroney": "mckayla maroney, woman, long brown hair, brown eyes, athletic curvy figure, age mid 20s, former olympian gymnast, not impressed meme, grown up beauty",
        
        # ============================================
        # CLASSIC BEAUTIES / VINTAGE
        # ============================================
        "Marilyn Monroe": "marilyn monroe, woman, platinum blonde hair iconic, blue eyes, fair skin, hourglass curvy figure, 1950s aesthetic, classic hollywood icon, red lips, beauty mark",
        "Brigitte Bardot": "brigitte bardot, woman, long blonde hair, blue eyes, french features, slender curvy figure, 1960s aesthetic, french actress, sex symbol, pouty lips",
        "Raquel Welch": "raquel welch, woman, long brown hair, brown eyes, tan skin, curvaceous hourglass figure, 1960s-70s aesthetic, one million years bc bikini icon",
        "Sophia Loren": "sophia loren, woman, long brown hair, brown eyes, italian features, voluptuous curvy figure, classic hollywood, italian goddess",
        "Jayne Mansfield": "jayne mansfield, woman, platinum blonde hair, blue eyes, extremely curvaceous busty figure, 1950s aesthetic, classic bombshell, hourglass extreme",
        "Betty Page": "bettie page, woman, black hair signature bangs, blue eyes, fair skin, pinup curvy figure, 1950s pinup queen, iconic poses, vintage aesthetic",
        
        # ============================================
        # ROYALTY / SOCIALITES
        # ============================================
        "Kate Middleton": "kate middleton catherine princess of wales, woman, long brown hair, green eyes, british elegant, slender figure, age early 40s, royal, sophisticated class",
        "Meghan Markle": "meghan markle duchess of sussex, woman, long dark brown hair, brown eyes, mixed race heritage, slender figure, age early 40s, royal actress, american princess",
        "Paris Hilton": "paris hilton, woman, long blonde hair, blue eyes, fair skin, slender figure, age early 40s, socialite heiress, 2000s icon, thats hot",
        "Nicole Richie": "nicole richie, woman, long brown hair, brown eyes, slender petite figure, age early 40s, socialite, simple life era",
        
        # ============================================
        # INTERNATIONAL STARS
        # ============================================
        "Deepika Padukone": "deepika padukone, woman, long dark hair, brown eyes, indian features, tall slender elegant figure, age late 30s, bollywood actress, indian beauty",
        "Priyanka Chopra": "priyanka chopra, woman, long dark hair, brown eyes, indian features, slender figure, age early 40s, bollywood actress miss world, indian international star",
        "Alia Bhatt": "alia bhatt, woman, long dark hair varies, brown eyes, indian petite features, slender petite figure, age late 20s, bollywood actress, cute indian star",
        "Fan Bingbing": "fan bingbing, woman, long black hair, dark eyes, chinese features, slender elegant figure, age early 40s, chinese actress, porcelain beauty",
        "Dilraba Dilmurat": "dilraba dilmurat, woman, long dark hair, brown eyes, uyghur chinese features, slender figure, age early 30s, chinese actress, exotic eurasian beauty",
        "Gal Gadot": "gal gadot, woman, long dark brown hair, brown eyes, israeli tall slender figure, age late 30s, wonder woman actress, tall exotic beauty",
    }
    
    QUALITY_PRESETS = {
        "Ultra Photorealistic": "photorealistic, hyperrealistic, 8k uhd, dslr quality, raw photo, realistic skin texture with pores, realistic detailed eyes with reflections, sharp focus, professional photography, studio lighting, subsurface scattering, volumetric lighting, cinematic, award winning photo, highly detailed face, perfect likeness, accurate facial features, identical to reference, same exact person",
        "High Quality Photo": "photorealistic, high resolution, extremely detailed face, realistic, professional photo, natural lighting, 4k uhd, sharp focus, accurate likeness, detailed eyes, skin texture, recognizable person, same face",
        "Artistic Portrait": "artistic portrait, painterly style, professional lighting, beautiful, elegant, studio portrait, detailed face, expressive, masterpiece, best quality, accurate likeness",
        "Glamour Shot": "glamour photography, professional studio lighting, magazine cover quality, perfect makeup, styled hair, studio background, fashion photography, detailed face, polished, recognizable celebrity",
        "Casual/Candid": "candid photography, natural lighting, realistic, casual, authentic moment, unposed, street photography, detailed face, 4k, same person",
        "Maximum Likeness": "extremely detailed face, perfect likeness, accurate facial features, photorealistic portrait, celebrity lookalike, recognizable, identical features, same person, exact match, hyperdetailed face, studio portrait, 8k uhd, sharp focus, face match, identical face structure, same bone structure, same eye shape, same nose, same lips",
        "PERFECT CLONE": "EXACT LIKENESS, IDENTICAL PERSON, PERFECT FACE MATCH, same exact facial features, same bone structure, same eye shape and color, same nose shape, same lip shape, same face proportions, photorealistic clone, indistinguishable from reference, carbon copy, perfect reproduction, 8k uhd, hyperdetailed face, studio lighting, masterpiece, best quality",
    }
    
    CLOTHING_OPTIONS = {
        "Default/Dressed": "",
        "Nude": ", completely nude, naked, bare skin, full frontal nudity, nipples visible, anatomically correct nude, artistic nude photography, uncensored, no clothes, exposed body",
        "Topless": ", topless, bare breasts exposed, no shirt, bare chest, nipples visible, half nude",
        "Lingerie": ", wearing sexy lingerie, lace bra and panties, garter belt, stockings, seductive pose, intimate apparel, sheer lace",
        "Bikini": ", wearing small bikini, two piece swimsuit, beach setting, toned body visible, wet skin, swimwear model",
        "Micro Bikini": ", wearing micro bikini, extremely small swimsuit, string bikini, barely covered, revealing swimwear",
        "Sheer/See-Through": ", wearing sheer see-through clothing, transparent fabric, nipples visible through clothes, revealing outfit",
        "Evening Gown": ", wearing elegant evening gown, formal dress, red carpet style, designer dress, glamorous",
        "Casual": ", casual outfit, jeans and top, relaxed style, everyday clothes",
        "Athletic Wear": ", wearing athletic clothes, sports bra and shorts, yoga pants, workout gear, toned body visible, gym outfit",
        "Swimsuit One-Piece": ", wearing one piece swimsuit, beach, model pose, swimwear",
        "Red Carpet": ", red carpet outfit, designer dress, glamorous, jewelry, styled hair, formal event",
        "Business Attire": ", professional business attire, blazer and skirt, sophisticated, office wear",
        "Bodysuit": ", wearing tight bodysuit, form-fitting, catsuit, skintight",
        "Custom": "",
    }
    
    # Comprehensive negative prompt for quality AND likeness accuracy
    NEGATIVE_PROMPT = "deformed, distorted, disfigured, bad anatomy, wrong anatomy, extra limbs, missing limbs, floating limbs, mutated hands, extra fingers, missing fingers, fused fingers, too many fingers, long neck, mutation, poorly drawn face, poorly drawn hands, bad proportions, gross proportions, malformed limbs, cross-eyed, blurry, low quality, jpeg artifacts, signature, watermark, bad face, ugly face, WRONG FACE, DIFFERENT PERSON, DIFFERENT FACE, NOT THE SAME PERSON, unrecognizable, wrong identity, bad likeness, inaccurate features, wrong eye color, wrong hair color, wrong skin tone, wrong nose shape, wrong lip shape, merged faces, mixed features, hybrid face, composite face, wrong bone structure, different ethnicity than reference, age mismatch, wrong facial structure"
    
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
    
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt", "celebrity_name")
    FUNCTION = "generate"
    CATEGORY = "Mason/Characters"
    
    def generate(self, celebrity, quality, clothing, additional_details=""):
        prompt_parts = []
        
        # Add quality prefix with likeness emphasis
        prompt_parts.append(self.QUALITY_PRESETS[quality])
        
        # Add the celebrity name explicitly for LoRA/embedding matching
        celeb_name = celebrity.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
        prompt_parts.append(f"{celebrity}")
        
        # Add celebrity details
        prompt_parts.append(self.CELEBRITIES[celebrity])
        
        # Add clothing
        if clothing != "Default/Dressed" and clothing != "Custom":
            prompt_parts.append(self.CLOTHING_OPTIONS[clothing])
        
        # Add custom details
        if additional_details.strip():
            prompt_parts.append(additional_details.strip())
        
        final_prompt = ", ".join(filter(None, prompt_parts))
        return (final_prompt, self.NEGATIVE_PROMPT, celebrity)


# Backwards compatibility
CelebritySelector = CelebritySelectorV2


NODE_CLASS_MAPPINGS = {
    "MasonCelebritySelectorV2": CelebritySelectorV2,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonCelebritySelectorV2": "⭐ Celebrity Selector V2 (250+ People)",
}

