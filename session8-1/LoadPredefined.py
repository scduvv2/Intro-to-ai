# Import the Gensim library's downloader package which provides
# access to predefined embeddings and other corpora.
import gensim.downloader


# Get a list of all the predefined things in the set.  This will
# be a dict that breaks into two pieces, corpora which we can use
# for text info, and models that we can access.
gensim.downloader.info()

# This lists the available models.
gensim.downloader.info()['models'].keys()


# We will use a smaller model that is trained on wikipedia.  You can
# find the info here.
gensim.downloader.info()['models']['glove-wiki-gigaword-50']

# Now download the model itself.
#  (NOTE: This may take a little while)
GloveModel = gensim.downloader.load('glove-twitter-50')

# And now we can do some simple synonym or similarity lookup
# based upon the text.
print(GloveModel.most_similar("cat"))


# And given a sequence of words print out the most similar for each.
# This can be readily extended to any word list. 
Words = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for W in Words:
    print(GloveModel.most_similar(W)[0][0])
