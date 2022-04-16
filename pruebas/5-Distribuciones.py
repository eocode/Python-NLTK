import nltk
import matplotlib.pyplot as plt

nltk.download('book')
from nltk.book import *
import matplotlib.pyplot as plt
import numpy as np

# # Calcular las freiemcoas de las palabras
fig = plt.figure(figsize=(10, 4))
# plt.gcf().subplots_adjust(bottom=0.15)  # to avoid x-ticks cut-off
fdist = FreqDist(text1)
# print(fdist.most_common(20))
#
# type(fdist.plot(20))
# fig.savefig('pruebas/freqDist.png', bbox_inches="tight")

# Distribycuibes sobre contenido con filtro
long_words = [palabra for palabra in text1 if len(palabra) > 5]
vocabulario_filtrado = sorted(set(long_words))[:10]
print(vocabulario_filtrado)
palabras_interesantes = [(palabra, fdist[palabra]) for palabra in set(text1) if
                         len(palabra) > 5 and fdist[palabra] > 10]
print(palabras_interesantes)
# Convertir a numpy
dtypes = [('word', 'S10'), ('frequency', int)]
palabras_interesantes = np.array(palabras_interesantes, dtype=dtypes)
print(palabras_interesantes)
palabras_interesantes = np.sort(palabras_interesantes, order='frequency')
print(palabras_interesantes)

top_words = 20
# plt.figure(figsize=(10, 5))
x = np.arange(len(palabras_interesantes[-top_words:]))
y = [freq[1] for freq in palabras_interesantes[-top_words:]]
plt.plot(x, y)
plt.xticks(x, [str(freq[0]) for freq in palabras_interesantes[-top_words:]], rotation='vertical')
plt.grid(True)
fig.savefig('pruebas/freqDist2.png', bbox_inches="tight")
