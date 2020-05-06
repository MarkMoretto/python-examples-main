
"""
Purpose: NLP - Phrase detection
Date created: 2020-05-05

https://radimrehurek.com/gensim/models/phrases.html#module-gensim.models.phrases

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