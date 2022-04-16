from nltk.corpus import swadesh

print(swadesh.fileids())
print(swadesh.words('en'))
en2es = swadesh.entries(['en', 'es'])

translate = dict(en2es)
print(translate['sauce'])
