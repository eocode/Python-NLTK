import requests
from bs4 import BeautifulSoup
import re
from nltk.tokenize import regexp_tokenize
import html2text

url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'
r = requests.get(url)
html = r.text
to_text = html2text.html2text(html)
print(to_text)

tokens = re.findall('\w+', to_text)
print(tokens[:50])
