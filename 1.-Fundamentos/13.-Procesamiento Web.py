import nltk

nltk.download('punkt')
nltk.download('stopwords')
from nltk import word_tokenize
from urllib import request

url = 'https://www.gutenberg.org/files/2554/2554-0.txt'
response = request.urlopen(url)
raw = response.read().decode('utf8')
print(len(raw))
tokens = word_tokenize(raw)
print(tokens[:20])
# bettering tokens with nltk
pattern = r'''(?x)                  # Flag para iniciar el modo verbose
              (?:[A-Z]\.)+          # Hace match con abreviaciones como U.S.A.
              | \w+(?:-\w+)*        # Hace match con palabras que pueden tener un guión interno
              | \$?\d+(?:\.\d+)?%?  # Hace match con dinero o porcentajes como $15.5 o 100%
              | \.\.\.              # Hace match con puntos suspensivos
              | [][;"'?():-_`]      # Hace match con signos de puntuación
'''
tokens2 = nltk.regexp_tokenize(raw, pattern)
print(tokens2[:50])
text = nltk.Text(tokens2)
print(text.collocations())
