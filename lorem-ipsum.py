import random

def generate_syllable_word():
    syllables = ["a", "o", "u", "z", "k", "ž", "do", "za", "ma", "na", "pro", "se"]
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
    lorem_ipsum_words = []
    add_new_words(lorem_ipsum_words, count=10)

    lorem_ipsum = []
    for _ in range(sentence_count):
        sentence = " ".join(random.sample(lorem_ipsum_words, words_per_sentence))
        lorem_ipsum.append(sentence.capitalize() + ".")
    return " ".join(lorem_ipsum)

lorem_ipsum_txt = generate_lorem_ipsum()
print(lorem_ipsum_txt)

user_choice = input("Chcete vytvořit textový dokument ?  ano/ne: ").lower()
if user_choice == "ano":
    file_name = input("Zadejte název souboru ") + ".txt"
    with open(file_name, 'w') as file:
        file.write(lorem_ipsum_txt)
    print(f"soubor - {file_name} byl vytvořen")
    
elif user_choice == "ne":
    print("Textový soubor nevytvořen")
else:
    print("neznámý vstup, zadejte ano/ne")