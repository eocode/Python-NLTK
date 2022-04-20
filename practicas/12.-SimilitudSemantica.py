from nltk.corpus import wordnet as wn


def show_syns(word):
    ss = wn.synsets(word, lang='spa')
    for syn in ss:
        print(syn.name(), ' : ', syn.definition())
        for name in syn.lemma_names():
            print(' * ', name)
    return ss


ss = show_syns('perro')
perro = ss[0]
ss2 = show_syns('gato')
gato = ss2[0]
ss3 = show_syns('animal')
animal = ss3[0]

print(animal.path_similarity(perro))
print(animal.path_similarity(gato))
print(perro.path_similarity(perro))
