# Un N-grama es una secuencia de n palabras
# De ahi se puedden obtener bi-gramas (separación de dos) o tri-gramas (separación en tuplas de tres)
# Estoy aprendiendo cosas increíbles

# Colocaciones
# Palabras que suenan mejor que otras en cierta frase
# Le dieron ganas de dormir
# Le introdujeron ganas de dormir

import nltk

nltk.download("book.txt")
from nltk.book import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

fig = plt.figure(figsize=(10, 4))
md_bigrams = list(bigrams(text1))
fdist = FreqDist(md_bigrams)
fdist.most_common(10)
# fdist.plot(10)
# fig.savefig('practicas/freqDist3.png', bbox_inches="tight")
threshold = 2
filtered_bigrams = [bigram for bigram in md_bigrams if len(bigram[0]) > threshold and len(bigram[1]) > threshold]
filtered_dist = FreqDist(filtered_bigrams)
filtered_dist.plot(20)
fig.savefig('practicas/freqDist3.png', bbox_inches="tight")

from nltk.util import ngrams

md_trigrams = list(ngrams(text1, 3))
fdist = FreqDist(md_trigrams)
print(fdist.most_common(10))
fdist.plot(10)
fig.savefig('practicas/freqDist3.png', bbox_inches="tight")