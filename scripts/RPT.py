import re

vowels = 'аоэуияёеюы'
vow_ak = 'ао'
consonants = ''

def softness(word):
    word = re.sub(r'(?<=(\s|[' + vowels + 'ьъ]))ю','йу',word)
    word = re.sub(r'(?<=(\s|[' + vowels + 'ьъ]))е','йэ',word)
    word = re.sub(r'(?<=(\s|[' + vowels + 'ьъ]))я','йа',word)
    word = re.sub(r'(?<=(\s|[' + vowels + 'ьъ]))ё','йо',word)
    word = re.sub(r'(?<=[ьъ])и','йи',word)

    word = re.sub(r'ь','\'',word)
    word = re.sub(r'ъ','',word)
    word = re.sub(r'ю','\'у',word)
    word = re.sub(r'я','\'а',word)
    word = re.sub(r'е','\'э',word)
    word = re.sub(r'ё','\'о',word)

    '''(?<![жчщшцй\s])и'''
    return word


def akanje()
    akanje1 = r'[' + vow_ak + '](?!́)(?=(?=.*[' + vowels + '].*(о́|а́))|\b)'
    akanje2 = r'[оа](?!́)(?=[^оа]*(о́|а́))'

    return akanje2
