import re

# Raw text
import nltk

print(r'es es \n una prueba')

texto = """ Cuando sea el rey del mundo (imaginaba él en su cabeza) no tendré que  preocuparme por estas bobadas. 
            Era solo un niño de 7 años, pero pensaba que podría ser cualquier cosa que su imaginación le permitiera 
            visualizar en su cabeza ..."""

print(re.split(r' ', texto))

# Tokenizar con Expresiones Regulares

print(re.split(r'[ \t\n]+', texto))

print(re.split(r'[ \W\t\n]+', texto))

# Usando NLTK
texto = 'En los E.U. esa postal vale $15.50 ...'
print(re.split(r'[ \W\t\n]+', texto))

pattern = r'''(?x)                  # Flag para iniciar el modo verbose
              (?:[A-Z]\.)+            # Hace match con abreviaciones como U.S.A.
              | \w+(?:-\w+)*         # Hace match con palabras que pueden tener un guión interno
              | \$?\d+(?:\.\d+)?%?  # Hace match con dinero o porcentajes como $15.5 o 100%
              | \.\.\.              # Hace match con puntos suspensivos
              | [][.,;"'?():-_`]    # Hace match con signos de puntuación
              '''
result = nltk.regexp_tokenize(texto, pattern)
print(result)