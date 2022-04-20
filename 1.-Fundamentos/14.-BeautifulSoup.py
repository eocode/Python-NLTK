import requests
from bs4 import BeautifulSoup
import re
from nltk.tokenize import regexp_tokenize

url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
print(soup)
text = soup.get_text()
print(text)
tokens = re.findall('\w+', text)
print(tokens)
