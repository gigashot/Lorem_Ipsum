import random

def generate_syllable_word():
    syllables = [
        'na', 'po', 'čát', 'ku', 'stvo', 'řil', 'bůh', 'ne', 'be', 'a', 'ze', 'mi', 'mě', 'by', 'la', 'pus', 'tá', 'prázd', 'ná', 'nad', 'pro', 'past', 'nou', 'tů', 'ní', 
'tma', 'A', 'le', 'vo', 'da', 'vz', 'šel', 'se', 'duch', 'Bo', 'ží', 'I', 'řekl', 'Buď', 'svět', 'lo', 'Vi', 'děl', 'že', 'je', 'do', 'bré', 'od', 'dě', 'lil', 
'Svět', 'naz', 'val', 'dnem', 'tmu', 'no', 'cí', 'Byl', 've', 'čer', 'jit', 'ro', 'den', 'prv', 'klen', 'ba', 'u', 'prostřed', 'vod', 'pod', 'bem', 'sto', 'kaž', 
'souš', 'Souš', 'mo', 'ři', 'to', 'Bu', 'ta', 'ké', 'Za', 'nej', 'ným', 'stro', 'mov', 'ím', 'ho', 'dru', 'hu', 'plo', 'dy', 'Ze', 'leň', 'vy', 'hy', 'li', 'n', 
'roz', 'mno', 'žu', 'jí', 'me', 'ny', 'tak', 'í', 'tře', 'tí', 'te', 'ské', 'bě', 'va', 'ci', 'dou', 'zna', 'mení', 'ča', 'sů', 'dnů', 'let', 'Ta', 'ať', 'jsou', 
'sví', 'ti', 'mí', 'sta', 'U', 'či', 'nil', 'de', 'dvě', 'ká', 'vět', 'ší', 'vlá', 'dlo', 'dne', 'nší', 'v', 'i', 'hvěz', 'umí', 'stil', 'čtvr', 'tý', 'He', 'mžete',
 'ži', 'čiš', 'ha', 'vě', 'lét', 'av', 'lé', 'tej', 'skou', 'bou', 'Bůh', 'net', 'ry', 'ma', 'ni', 'té', 'vše', 'ja', 'k', 'ých', 'hbi', 'tých', 'čichů', 'ji', 
'miž', 'za', 'hem', 'ly', 'kon', 'če', 'sa', 'svý', 'zás', 'tu', 'py', 'sed', 'mé', 'd', 'čil', 'své', 'dí', 'kte', 'ré', 'ko', 'nal', 'pře', 'stal', 'nat', 'veš',
 'ke', 'hna', 'l', 'pos', 'til', 'mý', 'neboť', 'něm', 'tel', 'pis', 'jak', 'ře', 'kdy', 'hospodin', 'ještě', 'žád', 'né', 'pol', 'křo', 'vis', 'ani', 'cha', 'vla',
 'žo', 'deštěm', 'člo', 'ka', 'rý', 'ob', 'lá', 'jen', 'zá', 'pla', 'stu', 'pá', 'ce', 'lý', 'zem', 'ský', 'vrch', 'tvo', 'pra', 'ch', 'vd', 'echl', 'mu', 'chří', 'pí',
 'dech', 'věk', 'vým', 'rem', 'sadil', 'har', 'du', 'e', 'nu', 'východě', 'vil', 'tam', 'dal', 'růst', 'ví', 'žá', 'hled', 's', 'dob', 'jíd', 'lu', 'střed', 'hra', 'pak',
 'poz', 'z', 'chá', 'zí', 'tud', 'dál', 'čty', 'hla', 'vní', 'ky', 'jmé', 'šon', 'ten', 'níž', 'zlato', 'zla', 'skvě', 'von', 'prys', 'men', 'kar', 'ol', 'hé', 'gí', 'chón', 
'kúš', 'chi', 'kel', 'východně', 'asý', 'rie', 'eu', 'frat', 'hrady', 'stře', 'žil', 'při', 'kázal', 'dé', 'smíš', 'jíst', 'však', 'jez', 'kdybys', 'ně', 'jedl', 'pad', 'neš', 
'smrti', 'aby', 'byl', 'sám', 'ním', 'moc', 'vnou', 'když', 'zvěř', 'ptač', 'vedl', 'vi', 'nazve', 'dý', 'vý', 'r', 'měl', 'jme', 'vat', 'jej', 'zví', 'řa', 'ale', 'šla', 'vná', 'uvedl',
'mra', 'až', 'us', 'nul', 'vzal', 'dno', 'jeho', 'ber', 'vr', 'el', 'sem', 'ut', 'bra', 'ženu', 'zvo', 'lal', 'kost', 'mých', 'kos', 'tě', 'ženou', 'zý', 'vá', 'vždyť', 'vzat', 'jest',
 'opu', 'stí', 'muž', 'ot', 'mat', 'lne', 'ženě', 'jed', 'lem', 'oba', 'dva', 'žena', 'sty'
   ]
    syllable_count = random.randint(1, 4)
    word = ""
    for _ in range(syllable_count):
        word += random.choice(syllables)
    return word

def add_new_words(lorem_ipsum_words, count=10):
    for _ in range(count):
        custom_word = generate_syllable_word()
        lorem_ipsum_words.append(custom_word)

def generate_lorem_ipsum(sentence_count=int(input("Zadejte počet vět který chcete vytvořit ")), words_per_sentence=random.randint(5, 12)):
    lorem_ipsum = []
    for _ in range(sentence_count):
        lorem_ipsum_words = []
        add_new_words(lorem_ipsum_words, count=10)
        sentence = " ".join(random.sample(lorem_ipsum_words, words_per_sentence))
        lorem_ipsum.append(sentence.capitalize() + ".")
        
    return " ".join(lorem_ipsum)

lorem_ipsum_txt = generate_lorem_ipsum()
print(lorem_ipsum_txt)

user_choice = input("Chcete vytvořit textový dokument ? ano/ne: ").lower()
if user_choice == "ano":
    file_name = input("Zadejte název souboru ") + ".txt"
    with open(file_name, 'w') as file:
        file.write(lorem_ipsum_txt)
    print(f"soubor - {file_name} byl vytvořen")
    
elif user_choice == "ne":
    print("Textový soubor nevytvořen")
else:
    print("neznámý vstup, zadejte ano/ne")
