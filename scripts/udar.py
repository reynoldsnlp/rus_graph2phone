import udar

analyzer = udar.Udar('analyzer')
token = analyzer.lookup('слова')
for reading in token.readings:
    if 'Gen' in reading:
        print(token, 'is Genitive!')
