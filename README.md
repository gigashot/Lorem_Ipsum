Generátor Lorem Ipsum
Tento Python skript generuje text podobný Lorem Ipsum pomocí vlastního algoritmu pro generování slov na základě slabik. Vygenerovaný text lze buď vytisknout do konzole nebo uložit do textového souboru.

Použití
Spusťte skript pomocí následujícího příkazu:

python lorem_ipsum_generator.py
Požadovaný počet vět zadejte, když budete vyzváni.

Volitelně se rozhodněte, zda chcete vytvořit textový soubor s vygenerovaným textem.

Struktura kódu
generate_syllable_word()
Funkce pro generování náhodného slova s náhodným počtem slabik.

add_new_words(lorem_ipsum_words, count=10)
Funkce pro přidání určeného počtu vlastních slov do seznamu slov Lorem Ipsum.

generate_lorem_ipsum(sentence_count, words_per_sentence)
Hlavní funkce pro generování textu Lorem Ipsum.
Vyzve uživatele k zadání počtu vět k vygenerování (výchozí hodnota je uživatelský vstup) a nastaví náhodný počet slov na větu.
Používá předchozí funkce k vytvoření seznamu slov, náhodně vybírá slova pro každou větu a kapitalizuje první písmeno každé věty.

Tiskne vygenerovaný text Lorem Ipsum do konzole.

Ptá se uživatele, zda chce vytvořit textový soubor.

V případě kladné odpovědi žádá o název souboru, vytváří textový soubor s poskytnutým názvem a zapisuje vygenerovaný text do souboru.
Tiskne zprávu oznamující, zda byl soubor vytvořen.
