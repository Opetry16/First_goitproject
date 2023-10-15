CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATE = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
             "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")


TRANS = {}

for character, transliteration in zip(CYRILLIC_SYMBOLS, TRANSLATE):
    TRANS[ord(character)] = transliteration
    TRANS[ord(character.upper())] = transliteration.upper()

def translate(text):

    translated_text = text.translate(TRANS)
    
    return translated_text
