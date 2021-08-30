import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import TweetTokenizer 
from nltk.corpus import stopwords
import gensim


nationalParks = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'
cdc = ''

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
response = requests.get("https://cheat.sh/pip3", headers=headers)
soup = BeautifulSoup(response.text, features='lxml')
print(soup.get_text())
PageText = soup.get_text()

Req2 = requests.get(nationalParks)
#print(Req2.text[0:100])
soup = BeautifulSoup(Req2.text, features='lxml')
parks = soup.get_text()
#Req3 = requests.get(cdc)
#print(Req3.text[0:100])


nltk.download('punkt')
nltk.download('stopwords')
sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
Punctuation = sentence_detector.tokenize(parks.strip())

Twitter = TweetTokenizer()
#print(Twitter.tokenize(parks))
#print(Punctuation)
useLess = [] 
useLess.append('.')
useLess.append(',')
useLess.append("'")
useLess.append('"')
useLess.append('^')
useLess.append('`')
useLess.append('/')
useLess.append(':')
useLess.append('(')
useLess.append(')')
useLess.append('[')
useLess.append(']')
for word in stopwords.words('english'):
  useLess.append(word)
  print(word)


Words = nltk.tokenize.word_tokenize(parks)
dataset = []
for d in Words:
  if d not in useLess:
    dataset.append([d])

#print(dataset)  
Model = gensim.models.Word2Vec(dataset, min_count=2)
print('############################################################')
print(Model.wv.key_to_index)

vector= Model.wv['mountains']
print(vector)