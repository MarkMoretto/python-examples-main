
"""
Purpose: MXNet Word Embedding
Date created: 2020-05-04

https://gluon-nlp.mxnet.io/examples/word_embedding/word_embedding_training.html

Contributor(s):
    Mark M.
"""

import os
os.chdir(r"C:\Users\Work1\Desktop\Info\GitHub\python-examples-main\notebook-samples")
CSV_PATH = rf"{os.getcwd()}\csv-files\kiva-data.csv"

import re
import gensim
import numpy as np
import pandas as pd
import scipy.stats as ss

pd.set_option("mode.chained_assignment", None)
pd.set_option("display.max_columns", 50)
pd.set_option('display.max_rows', 999)
pd.set_option('precision', 4)

np.random.seed(786)

df = pd.read_csv(CSV_PATH)
dfs = df.sample(n=1000)

df.info()

### Create corpus
text_corpus = dfs["en"].values.tolist()

# Treat each element like a document
# Split and convert to lowercase, then
# get word frequency counts for each element
# Drop any counts below 1.
stopwords = re.split(r"\s+?", "for a of the and to in")

texts = [[word for word in doc.lower().split() if word not in stopwords] for doc in text_corpus]



frequency = dict()
for ix, doc in enumerate(texts):
    frequency[ix] = dict()
    for token in doc:
        if not token in frequency[ix]:
            frequency[ix][token] = 1
        else:
            frequency[ix][token] += 1


corpus = [[word for word, freq in frequency[ix].items() if freq > 1] \
           for ix in frequency.keys()]

corpdict = gensim.corpora.Dictionary(corpus)

# save dictionary for later
corpdict.save(r"data\kivy-sample-dict.txt")

# bag-of-words (BoW) corpus
bow_corpus = [corpdict.doc2bow(i) for i in corpus]
gensim.corpora.MmCorpus.serialize(r"data\kivy-sample-bow-corpus.mm", bow_corpus)
# Now we have some encoded words:
#print(bow_corpus[:3])


# Create a tf-idf model
tfidf = gensim.models.TfidfModel(bow_corpus)


# Transform entire corpus
tfidf_corpus = tfidf[bow_corpus]





# Similarity queries
lsi = gensim.models.LdaModel(bow_corpus, id2word=corpdict, num_topics=2)

index = gensim.similarities.MatrixSimilarity(lsi[bow_corpus])
index.save(r"data\kiva-sample-lsi.index")

# index = similarities.MatrixSimilarity.load(r"data\kiva-sample-lsi.index")


# Montemurro and Zanette’s entropy based keyword extraction algorithm
mckwrds = gensim.summarization.mz_keywords

big_text = " ".join(text_corpus)
text_keywords = mckwrds(big_text, scores=True, threshold=0.001)

text_keywords2 = mckwrds(big_text, scores=True,weighted=False, threshold=1.0)

text_keywords3 = mckwrds(big_text, scores=True,weighted=False, threshold="auto")



















