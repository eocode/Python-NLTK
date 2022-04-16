import nltk

nltk.download('book')
from nltk.book import *

print(text1.tokens[:10], len(text1))


# Riqueza léxica de un texto
# R = total palabras unicas / total de palabras
# = longitud del vocabulario / longitud del texto

# Obtenemos las palabras únicas

def riqueza_lexica(texto):
    vocabulario = sorted(set(texto))
    return len(vocabulario) / len(texto)


def porcentaje_palabra(palabra, texto):
    return 100 * texto.count(palabra) / len(texto)


print('Riqueza lexica ', riqueza_lexica(text1))
print('Porcentaje ', porcentaje_palabra('monster', text1))
print('Repeticiones ', text1.count('monster'))
