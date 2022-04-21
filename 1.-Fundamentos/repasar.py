# Dado un conjunto de bigramas, md_bigrams = list(bigrams(text1)) de un text1 con su respectiva distribución de frecuencias fdist = FreqDist(md_bigrams), si queremos obtener una lista filtrada de bigramas tales que la primera palabra del bigrama tenga longitud mayor o igual a 5 caracteres y la segunda palabra tenga una frecuencia de aparición en el texto mayor a 50 veces, entonces debo escribir:
md_bigrams = []
fdist = [(4,4)]
a = [bigram for bigram in md_bigrams if len(bigram[0])>=5 and fdist(bigram[1]) > 50]

# Una de las siguientes frases es falsa sobre el lexicon WordNet:

##Un synset puede tener más de dos palabras.

# Las colocaciones:

##Se pueden calcular simplemente obteniendo los n-gramas más frecuentes en un texto o corpus.