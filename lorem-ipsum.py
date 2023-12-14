import random

def generate_syllable_word():
    syllables = [
        'na', 'po', 'čát', 'ku', 'řil', 'bůh', 'ne', 'be', 'a', 'ze', 'mi', 'mě', 'by', 'la', 'pus', 'tá', 'ná', 'nad', 'pro', 'nou', 'tů', 'ní', 'tma', 'A', 'le', 
        'vo', 'da', 'vz', 'šel', 'se', 'Bo', 'ží', 'I', 'Buď', 'lo', 'Vi', 'děl', 'že', 'je', 'do', 'bré', 'od', 'dě', 'lil', 'naz', 'val', 'tmu', 'no', 'cí', 'Byl',
        've', 'čer', 'jit', 'ro', 'den', 'prv', 'ba', 'u', 'vod', 'pod', 'bem', 'sto', 'kaž', 'mo', 'ři', 'to', 'Bu', 'ta', 'ké', 'Za', 'nej', 'ným', 'mov', 'ím', 'ho',
        'dru', 'hu', 'plo', 'dy', 'Ze', 'leň', 'vy', 'hy', 'li', 'n', 'roz', 'mno', 'žu', 'jí', 'me', 'ny', 'tak', 'í', 'tře', 'tí', 'te', 'ské', 'bě', 'va', 'ci', 'dou',
        'zna', 'ča', 'sů', 'dnů', 'let', 'Ta', 'ať', 'sví', 'ti', 'mí', 'sta', 'U', 'či', 'nil', 'de', 'dvě', 'ká', 'vět', 'ší', 'vlá', 'dlo', 'dne', 'nší', 'v', 'i', 'umí',
        'tý', 'He', 'ži', 'čiš', 'ha', 'vě', 'lét', 'av', 'lé', 'tej', 'bou', 'Bůh', 'net', 'ry', 'ma', 'ni', 'té', 'vše', 'ja', 'k', 'ých', 'hbi', 'ji', 'miž', 'za', 'hem',
        'ly', 'kon', 'če', 'sa', 'svý', 'zás', 'tu', 'py', 'sed', 'mé', 'd', 'čil', 'své', 'dí', 'kte', 'ré', 'ko', 'nal', 'pře', 'nat', 'veš', 'ke', 'hna', 'l', 'pos', 'til',
        'mý', 'něm', 'tel', 'pis', 'jak', 'ře', 'kdy', 'žád', 'né', 'pol', 'křo', 'vis', 'ani', 'cha', 'vla', 'žo', 'člo', 'ka', 'rý', 'ob', 'lá', 'jen', 'zá', 'pla', 'stu', 'pá', 
        'ce', 'lý', 'zem', 'ský', 'tvo', 'pra', 'ch', 'vd', 'mu', 'pí', 'věk', 'vým', 'rem', 'har', 'du', 'e', 'nu', 'vil', 'tam', 'dal', 'ví', 'žá', 's', 
'dob', 'jíd', 'lu', 'hra', 'pak', 'poz', 'z', 'chá', 'zí', 'tud', 'dál', 'čty', 'hla', 'vní', 'ky', 'jmé', 'šon', 'ten', 'níž', 'zla', 'von', 'men', 'kar', 'ol', 
'hé', 'gí', 'kúš', 'chi', 'kel', 'asý', 'rie', 'eu', 'žil', 'při', 'dé', 'jez', 'ně', 'pad', 'neš', 'aby', 'byl', 'sám', 'ním', 'moc', 'vi', 'dý', 'vý', 'r', 'měl', 'jme', 
        'vat', 'jej', 'zví', 'řa', 'ale', 'šla', 'vná', 'mra', 'až', 'us', 'nul', 'dno', 'ber', 'vr', 'el', 'sem', 'ut', 'bra', 'zvo', 'lal', 'kos', 'tě', 'zý', 'vá', 'opu', 'stí',
        'muž', 'ot', 'mat', 'lne', 'jed', 'lem', 'oba', 'dva', 'sty'
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
