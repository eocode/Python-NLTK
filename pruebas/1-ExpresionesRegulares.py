import nltk
import re

nltk.download('cess_esp')

corpus = nltk.corpus.cess_esp.sents()
flatten = [w for l in corpus for w in l]

# Filtrar palabras que cumplan un expresión regular
arr = [w for w in flatten if re.search('es', w)]
print(arr[:5])

# Palabras que terminen con es
arr = [w for w in flatten if re.search('es$', w)]
print(arr[:5])

# Palabras que empiece con es
arr = [w for w in flatten if re.search('^es', w)]
print(arr[:5])

# Palabras que tenga un rango
arr = [w for w in flatten if re.search('^[ghi]', w)]
print(arr[:5])

# Clausuras,
# * repetir 0 o más veces
# + repetir 1 o más veces
arr = [w for w in flatten if re.search('^[no]*', w)]
print(arr[:5])
arr = [w for w in flatten if re.search('^[no]+', w)]
print(arr[:5])
