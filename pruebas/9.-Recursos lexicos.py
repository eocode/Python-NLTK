import nltk

nltk.download('book')
from nltk.book import *
from nltk.corpus import stopwords

# Información de las palabras sobre su contexto de uso
# Adjetivos
# Sustantivos
# Artículos
# Pronombres
# Verbos
# Adverbios
# Interjecciones
# Preposiciones
# Conjunciones

# Palabras unicas del corpus
vocab = sorted(set(text1))

# Distribución de frecuencia de aparición
word_freq = FreqDist(text1)

# Stopwords
# Son Palabras muy usadas en el lenguaje que usualmente son filtradas en un pipeline
# print(stopwords.words('spanish'))


def stopwords_percentage(text):
    stopwd = stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwd]

    return len(content) / len(text)


print(stopwords_percentage(text1))
