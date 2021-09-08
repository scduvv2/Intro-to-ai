from nltk.corpus import stopwords
import gensim
import requests
from bs4 import BeautifulSoup

import nltk
from nltk.tokenize import TweetTokenizer
# nltk.download('punkt')
# nltk.download('stopwords')


nationalParks = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'
cdc_myths = 'https://www.cdc.gov/coronavirus/2019-ncov/vaccines/facts.html'


nationalParksReq = requests.get(nationalParks)


cdc_mythsReq = requests.get(cdc_myths)

# print(nationalParksReq.text[0:100])
# print(cdc_mythsReq.text[0:100])


SoupText_nationalParksReq = BeautifulSoup(
    nationalParksReq.text, features="lxml")
PageText_nationalParksReq = SoupText_nationalParksReq.get_text()
# print(PageText_nationalParksReq[1000:2000])

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
response = requests.get("https://cheat.sh/pip3", headers=headers)
soup = BeautifulSoup(response.text, features='lxml')
# print(soup.get_text())


sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
Punctuation = sentence_detector.tokenize(PageText_nationalParksReq.strip())
# print(Punctuation)

Sentences = nltk.tokenize.sent_tokenize(PageText_nationalParksReq.strip())
# print(Sentences)

Words = nltk.tokenize.word_tokenize(PageText_nationalParksReq.strip())
# print(Words)

Twitter = TweetTokenizer()
# print(Twitter.tokenize(PageText_nationalParksReq))

stopWords = set(stopwords.words('english'))
# for word in stopwords.words('english'):
#    print(word)

otherGarbage = ['.', ',', ')', '(', '[', ']',
                '/', '``', '\'\'', '^', '*', ';', '-', ':', '°F', '°C',
                'AfrikaansالعربيةAzərbaycancaБългарскиČeštinaDanskDeutschEestiEspañolEsperantoفارسیFøroysktFrançais한국어HrvatskiÍslenskaItalianoעבריתქართულიLietuviųമലയാളംNederlands日本語Norsk', 'bokmålPolskiRuna', 'SimiРусскийSimple', 'EnglishSlovenčinaСрпски']
cleanWords = []
for word in Words:
    if word.lower() not in stopWords and word not in otherGarbage:
        cleanWords.append(word.lower())
# print(len(Words))
print(len(cleanWords))
print(cleanWords)

dataset = []
for d in cleanWords:
    dataset.append([d])

# print(dataset)

Model = gensim.models.Word2Vec(dataset, min_count=2)
print(Model.wv.key_to_index)
top5 = list(Model.wv.key_to_index.keys())[0:100]
print(top5)
for W in top5:
    print('my word:' + W + ' most similar:' + Model.wv.most_similar(W)[0][0])

vector = Model.wv['mountains']
# print(vector)

#sim = Model.wv.most_similar('peaks', topn=10)
# print(sim)


#Req = requests.get('https://nationalapprenticeship.org/')

# print(Req.text[0:100])

#SoupText = BeautifulSoup(Req.text, features="lxml")

#PageText = SoupText.get_text()
# print(PageText[2200:2500])
