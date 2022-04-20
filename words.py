from urllib import request
import html2text
import nltk, re


def freq_words(url, n, encoding='utf8'):
    req = request.urlopen(url)
    html = req.read().decode(encoding)
    text = html2text.html2text(html)
    tokens = re.findall('\w+', text)
    tokens = [t.lower() for t in tokens]
    fd = nltk.FreqDist(tokens)
    return [t for (t, _) in fd.most_common(n)]
