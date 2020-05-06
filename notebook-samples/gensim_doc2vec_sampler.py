
"""
Purpose: Gensim doc2vec
Date created: 2020-05-05

Contributor(s):
    Mark M.
"""


from os import chdir
import os.path
chdir(r"C:\Users\Work1\Desktop\Info\GitHub\python-examples-main\notebook-samples")

import logging
import gensim
import smart_open
from collections import Counter

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



test_data_dir = os.path.join(gensim.__path__[0], 'test', 'test_data')
lee_train_file = os.path.join(test_data_dir, 'lee_background.cor')
lee_test_file = os.path.join(test_data_dir, 'lee.cor')


def read_and_process(filename, tokens_only=False):
    with smart_open.open(filename, encoding="8859") as f:
        for i, line in enumerate(f):
            tokens = gensim.utils.simple_preprocess(line)
            if tokens_only:
                yield tokens
            else:
                yield gensim.models.doc2vec.TaggedDocument(tokens, [i])

train_corp = [i for i in read_and_process(lee_train_file, False)]
test_corp = list(read_and_process(lee_train_file, True))


# print(train_corp[:2])

# Train model
model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=40)
model.build_vocab(train_corp)


# Infer a vector
vector = model.infer_vector(['only', 'you', 'can', 'prevent', 'forest', 'fires'])
print(vector)

# Validate and assess using testing data set
ranks = []
second_ranks = []
for doc_id in range(len(train_corp)):
    inferred_vector = model.infer_vector(train_corp[doc_id].words)
    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    rank = [docid for docid, sim in sims].index(doc_id)
    ranks.append(rank)

    second_ranks.append(sims[1])


counts = Counter(ranks)



print('Document ({}): «{}»\n'.format(doc_id, ' '.join(train_corp[doc_id].words)))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('SECOND-MOST', 1), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(train_corp[sims[index][0]].words)))

