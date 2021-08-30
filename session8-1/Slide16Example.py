import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import TweetTokenizer 


nationalParks = ''
cdc = ''

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
response = requests.get("https://cheat.sh/pip3", headers=headers)
soup = BeautifulSoup(response.text, features='lxml')
print(soup.get_text())
PageText = soup.get_text()

Req2 = requests.get(nationalParks)
print(Req2.text[0:100])
Req3 = requests.get(cdc)
print(Req3.text[0:100])


sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
Punctuation = sentence_detector.tokenize(PageText.strip())

Twitter - TweetTokenizer()
print(Twitter.tokenize(PageText))
print(Punctuation)