import nltk  # Package for NLP

texto = """ Cuando sea el rey del mundo (imaginaba él en su cabeza) no tendré que  preocuparme por estas bobadas. 
            Era solo un niño de 7 años, pero pensaba que podría ser cualquier cosa que su imaginación le permitiera 
            visualizar en su cabeza ..."""

sentences = nltk.sent_tokenize(texto)  # Sentence tokenizer
print(sentences)

words = nltk.word_tokenize(texto)
print(words)
