import random

def generate_syllable_word():
    
    syllables = ["a","o","u", "z", "k", "ž","do", "za", "ma", "na",  "pro", "se",

    ]
    
    # random počet slabik slova od 1 do 4
    syllable_count = random.randint(1, 4)

    # Vytvoření slova s náhodným počtem slabik
    word = ""
    for _ in range(syllable_count):
        # nahodne vybrat slabiku
        word += random.choice(syllables)
    return word

def add_new_words(lorem_ipsum_words, count=10):
    for _ in range(count):
        custom_word = generate_syllable_word()
        lorem_ipsum_words.append(custom_word)

def generate_lorem_ipsum(sentence_count= int(input("zadejte počet vět který chcete vygenerovat: ")), words_per_sentence= random.randint(5,12)):
    lorem_ipsum_words = []

    #pridani novych slov s random poctem slabik
    add_new_words(lorem_ipsum_words, count=10)

    lorem_ipsum = []
    for _ in range(sentence_count):
        sentence = " ".join(random.sample(lorem_ipsum_words, words_per_sentence))
        lorem_ipsum.append(sentence.capitalize() + ".")
    return " ".join(lorem_ipsum)


lorem_ipsum_txt = generate_lorem_ipsum()
print(lorem_ipsum_txt)