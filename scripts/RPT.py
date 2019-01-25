import re

vowels = 'аоэуияёеюы'
accented_vowels = 'а́о́э́у́и́я́ёе́ю́ы́'
vow_ak = 'ао'
consonants = ''

def softness(word):
    word = re.sub(r'\bю','йу',word)
    word = re.sub(r'\bя','йа',word)
    word = re.sub(r'\bе','йэ',word)
    word = re.sub(r'\bё','йо́',word)

    word = re.sub(r'(?<=[' + vowels + accented_vowels + 'ьъ])ю','йу',word)
    word = re.sub(r'(?<=[' + vowels + accented_vowels + 'ьъ])е','йэ',word)
    word = re.sub(r'(?<=[' + vowels + accented_vowels + 'ьъ])я','йа',word)
    word = re.sub(r'(?<=[' + vowels + accented_vowels + 'ьъ])ё','йо́',word)
    word = re.sub(r'(?<=[ьъ])и','йи',word)

    word = re.sub(r'(?<=[^йчщ])ь','\'',word)
    word = re.sub(r'(?<=[йчщ])ь','',word)
    word = re.sub(r'ъ','',word)
    word = re.sub(r'(?<=[^йчщ])ю','\'у',word)
    word = re.sub(r'(?<=[^йчщ])я','\'а',word)
    word = re.sub(r'(?<=[^йчщ])е','\'э',word)
    word = re.sub(r'(?<=[^йчщ])ё','\'о́',word)
    word = re.sub(r'(?<=[йчщ])ё','о́',word)
    word = re.sub(r'(?<=[йчщ])ю','у',word)
    word = re.sub(r'(?<=[йчщ])я','а',word)
    word = re.sub(r'(?<=[йчщ])е','э',word)
    word = re.sub(r'(?<=[^йчщжшц'+vowels+accented_vowels+'])и','\'и', word)

    return word

def akanje()
    akanje1 = r'[' + vow_ak + '](?!́)(?=(?=.*[' + vowels + '].*(о́|а́))|\b)'
    akanje2 = r'[оа](?!́)(?=[^оа]*(о́|а́))'

    return akanje2
