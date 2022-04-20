import nltk.collocations
from nltk import BigramCollocationFinder
from nltk.book import text1
from nltk.collections import *

bigram_measure = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(text1)
finder.apply_freq_filter(20)
finder.nbest(bigram_measure.pmi, 10)

nltk.download('cess_esp')
corpus = nltk.corpus.cess_esp.sents()
flatten_corpus = [w for l in corpus for w in l]
finder = BigramCollocationFinder.from_documents(corpus)
finder.apply_freq_filter(10)
print(finder.nbest(bigram_measure.pmi, 10))
print(flatten_corpus[:50])
