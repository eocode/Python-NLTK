# Wordnet es una base de datos con catácter léxico
# Se compone de conjuntos de sinonimos (synsets) cada uno expresando un concepto diferente
# Diferentes synsets se relacionan por su relación conceptual semántica
# Synset - Carro, Auto, Automóvil, Coche - Vehículo motorizado de cuatro rueda impulsado por un motor de combustion interna
# La wordnet tiene diferentes jerarquías
# La idea del Wordnet es tener una estructura tipo grafo.
# Un synset se relaciona con otro synset dependiendo de la generalidad del concepto.
# Conceptos claves:
# Hiperonimo: Es un synset mas generalizado que puede abarcar varias palabras. El ejemplo de la clase es que Artefacto es un hiperónimo de vehículo motorizado.
# Hiponimo: Es un synset que no es general sino más específico.

import nltk

nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn

# synset: grupo de sinómimos de una palabra.
ss = wn.synsets('carro', lang='spa')
print(ss)
for syn in ss:
    print(syn.name, ' : ', syn.definition())
    for name in syn.lemma_names():
        print(' * ', name)

import networkx as nx
import matplotlib.pyplot as plt


def clousure_graph(synset, fn):
    seen = set()
    graph = nx.DiGraph()
    labels = {}

    def recurse(s):
        if not s in seen:
            seen.add(s)
            labels[s.name] = s.name().split('.')[0]
            graph.add_node(s.name)
            for s1 in fn(s):
                graph.add_node(s1.name)
                graph.add_edge(s.name, s1.name)
                recurse(s1)

    recurse(synset)
    return graph, labels


def draw_text_graph(G, labels):
    fig = plt.figure(figsize=(18, 12))
    pos = nx.planar_layout(G, scale=18)
    nx.draw_networkx_nodes(G, pos, node_color="red", linewidths=0, node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=20, labels=labels)
    nx.draw_networkx_edges(G, pos)
    plt.xticks([])
    plt.yticks([])
    fig.savefig('1.-Fundamentos/graph.png', bbox_inches="tight")


print('Hiponimo: ', ss[0].hyponyms())
print('Hiperonimo: ', ss[0].hypernyms())

G, labels = clousure_graph(ss[0], fn=lambda s: s.hyponyms())
draw_text_graph(G, labels)

G, labels = clousure_graph(ss[0], fn=lambda s: s.hypernyms())
draw_text_graph(G, labels)
