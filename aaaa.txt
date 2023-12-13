import random

def generate_syllable_word():
    syllables = [
        "Na", "po", "čát", "ku", "stvo", "řil", "Bůh", "ne", "be", "a", "ze", "mi", "Ze", "mě", "by", "la", "pus",
        "tá", "prázd", "ná", "nad", "pro", "past", "nou", "tů", "ní", "tma", "A", "le", "vo", "da", "vz", "ná", "šel",
        "se", "duch", "Bo", "ží", "I", "řekl", "Buď", "svět", "lo", "Vi", "děl", "že", "je", "do", "bré", "od", "dě",
        "lil", "Svět", "lo", "naz", "val", "dnem", "tmu", "no", "cí", "Byl", "ve", "čer", "jit", "ro", "den", "prv",
        "ní", "klen", "ba", "u", "prostřed", "vod", "pod", "bem", "sto", "kaž", "souš", "Souš", "mo", "ři", "to", "Bu",
        "ta", "ké", "řekl", "Za", "ze", "le", "nej", "ným", "stro", "mov", "ím", "ho", "dru", "hu", "plo", "dy", "Ze",
        "leň", "vy", "da", "ze", "hy", "by", "li", "n", "roz", "mno", "žu", "jí", "se", "me", "ny", "se", "tak", "Ze",
        "leň", "vy", "da", "hy", "by", "li", "n", "roz", "mno", "žu", "jí", "se", "me", "ny", "tak", "Za", "ze", "le",
        "nej", "se", "ze", "le", "ní", "a", "se", "me", "ny", "ze", "leň", "vy", "da", "hy", "by", "li", "n", "roz",
        "mno", "žu", "jí", "se", "me", "ny", "a", "hy", "stro", "mov", "í", "ne", "se", "plo", "dy", "se", "se", "me",
        "ny", "Vi", "děl", "že", "to", "bré", "Byl", "ve", "čer", "jit", "ro", "den", "tře", "tí", "Bu", "te", "svět",
        "la", "ne", "be", "ské", "klen", "bě", "va", "la", "den", "od", "no", "ci", "Bu", "dou", "na", "zna", "mení",
        "ča", "sů", "dnů", "let", "Ta", "svět", "la", "ať", "jsou", "na", "ne", "be", "ské", "klen", "bě", "a", "sví",
        "ti", "la", "nad", "ze", "mí", "sta", "lo", "se", "tak", "U", "či", "nil", "te", "de", "dvě", "ká", "vět", "ší",
        "a", "vlá", "dlo", "ve", "dne", "me", "nší", "v", "no", "ci", "u", "či", "nil", "i", "hvěz", "dy", "umí", "stil",
        "a", "v", "no", "ci", "od", "dě", "lo", "va", "la", "svět", "lo", "tak", "Byl", "ve", "čer", "jit", "ro", "den",
        "čtvr", "tý", "Bu", "He", "mžete", "vo", "dy", "ži", "vo", "čiš", "nou", "ha", "vě", "tí", "lét", "av", "ci",
        "lé", "tej", "te", "nad", "ze", "mí", "pod", "ne", "be", "skou", "klen", "bou", "I", "stvo", "řil", "Bůh", "ve",
        "li", "ké", "net", "vo", "ry", "roz", "ma", "ni", "té", "dru", "hy", "vše", "li", "ja", "k", "ých", "hbi", "tých",
        "ži", "vo", "čichů", "ji", "miž", "se", "za", "hem", "ži", "ly", "vo", "dy", "stvo", "řil", "i",
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
