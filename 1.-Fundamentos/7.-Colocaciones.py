import nltk

nltk.download("book.txt")
from nltk.book import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

fig = plt.figure(figsize=(10, 4))
threshold = 2
md_bigrams = list(bigrams(text1))
filtered_bigrams = [bigram for bigram in md_bigrams if len(bigram[0]) > threshold and len(bigram[1]) > threshold]
filtered_bigrams_dist = FreqDist(filtered_bigrams)

filtered_words = [word for word in text1 if len(word) > threshold]
filtered_word_dist = FreqDist(filtered_words)

df = pd.DataFrame()
df['bi_grams'] = list(set(filtered_bigrams))
df['word_0'] = df.bi_grams.apply(lambda x: x[0])
df['word_1'] = df.bi_grams.apply(lambda x: x[1])
df['bi_gram_freq'] = df['bi_grams'].apply(lambda x: filtered_bigrams_dist[x])
df['word_0_freq'] = df['word_0'].apply(lambda x: filtered_word_dist[x])
df['word_1_freq'] = df['word_1'].apply(lambda x: filtered_word_dist[x])

# PMI Pointwise Mutual Information (PMI)
# Es una métrica basada en teria de la información para encontrar collocations
# PMI = log((P(w1,w2))/(P(w1)*P(w2)))
# Se obtienen valores negativos
# Colocaciones son muy cercanas a 0

df['PMI'] = df[['bi_gram_freq', 'word_0_freq', 'word_1_freq']].apply(
    lambda x: np.log2(x.values[0] / (x.values[1] * x.values[2])), axis=1)
df.sort_values(by='PMI', ascending=False)
df['log(bi_gram_freq)'] = df['bi_gram_freq'].apply(lambda x: np.log2(x))

fig = px.scatter(x=df.PMI.values, y=df['log(bi_gram_freq)'].values, color=df['PMI'] + df['log(bi_gram_freq)'],
                 hover_name=df['bi_grams'].values, width=600, height=600, labels={'x': 'PMI', 'y': 'Log(Bigam Freq)'})
fig.show()
# fig.savefig('1.-Fundamentos/colocations1.png', bbox_inches="tight")

print(df)
