
"""
Purpose: Tokenize a corpus in Python
Date created: 2019-10-18

SO Ref: https://stackoverflow.com/questions/58452692/tokenize-a-corpus-of-10-documents-in-python

Contributor(s):
    Mark M.
"""



import os
import re

base_path = r'C:\Users\Work1\Desktop\Info\PythonFiles\kaggle-movie-reviews\movie_reviews\movie_reviews'



base_Path = r'C:\location\to\folder\with\document\files

# Instantiate an empty dictonary
ddict = {}

# were going to walk our directory
for root, subdirs, filename in os.walk(base_path):
    # For each sub directory ('neg' and 'pos,' in this case)
    for d in subdirs:
        # Create a NEW dictionary with the subdirectory name as key
        ddict[d] = {}

        # Create a path to the subdirectory
        subroot = os.path.join(root, d)

        # Get a list of files for the directory
        # Save time by creating a new path for each file
        file_list = [os.path.join(subroot, i) for i in os.listdir(subroot) if i.endswith('txt')]

        # For each file in the filelist, open and read the file into the
        # subdictionary
        for f in file_list:
            # Basename = root name of path to file, or the filename
            fkey = os.path.basename(f)

            # Read file and set as subdictionary value
            with open(f, 'r') as f:
                ddict[d][fkey] = f.read()
            f.close()



len(ddict.keys()) # 2
len(ddict['neg'].keys()) # 1000
len(ddict['pos'].keys()) # 1000

# sample filename
dictkey = 'pos'
filekey = 'cv000_29590.txt'
tst1 = ddict[dictkey][filekey]

### Simple counter dictionary function
def val_counter(iterable, output_dict=None):
    if output_dict is None:
        output_dict = dict()
    for i in iterable:
        if i in output_dict.keys():
            output_dict[i] += 1
        else:
            output_dict[i] = 1
    return output_dict


def wordcounts(corpus, dirname='pos', keep_small_words=False, count_dict=None):
    if count_dict is None:
        count_dict = dict()

    get_words_pat = r'(?:\s*|\n*|\t*)?([\w]+)(?:\s*|\n*|\t*)?'
    p = re.compile(get_words_pat)

    def clean_corpus(x):
        clear_ws_pat = r'\s+' # Replace all whitespace with single-space
        remove_punc_pat = r'[^\w+]' # Find nonalphanumeric characters

        # Remove punctuation
        tmp1 = re.sub(remove_punc_pat, ' ', x)
        
        # Respace whitespace and return
        return re.sub(clear_ws_pat, ' ', tmp1)


    keylist = list(corpus[dirname])


    for k in keylist:
        cleand = clean_corpus(corpus[dirname][k])

        # Tokenize based on size
        if keep_small_words:
            tokens = p.findall(cleand)
        else:
            # limit to results > 1 char in length
            tokens = [i for i in p.findall(cleand) if len(i) > 1]


        for i in tokens:
            if i in count_dict.keys():
                count_dict[i] += 1
            else:
                count_dict[i] = 1

    # Return dictionary once comlpete
    return count_dict


### Simple counter dictionary function
def val_counter(iterable, output_dict=None):
    if output_dict is None:
        output_dict = dict()
    for i in iterable:
        if i in output_dict.keys():
            output_dict[i] += 1
        else:
            output_dict[i] = 1
    return output_dict


### Dictionary sorted function
dict_sort = lambda d, descending=True: dict(sorted(d.items(), key=lambda x: x[1], reverse=descending))

# Run our function for positive corpus values
pos_result_dict = wordcounts(ddict, 'pos')

## Sort results (necessary for a lot of stuff,
## like frequency distributions, interquartile ranges, etc.)
pos_result_dict = dict_sort(pos_result_dict)


# Create dictionary of how frequent each count value is
freq_dist = val_counter(pos_result_dict.values())
freq_dist = dict_sort(freq_dist)



# Stats functions
k_count = lambda x: len(x.keys())
sum_vals = lambda x: sum([v for k, v in x.items()])
calc_avg = lambda x: sum_vals(x) / k_count(x)

# Get mean (arithmetic average) of word counts
mean_dict = calc_avg(pos_result_dict)

# Top-half of results.  We count shrink this even further, if necessary
top_dict = {k:v for k, v in pos_result_dict.items() if v >= mean_dict}


tot_count= sum([v for v in top_dict.values()])
for k, v in top_dict.items():
    pct_ = round(v / tot_count, 4)
    print('Word: ', k, ', count: ', v, ', %-age: ', pct_)



from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
        'This is the first document.',
        'This document is the second document.',
        'And this is the third one.',
        'Is this the first document?',
        ]
vectorizer = TfidfVectorizer()


X = vectorizer.fit_transform(corpus)
tst1 = ' '.join(corpus)

dtest = val_counter(p.findall(tst1))
tot_count= sum([v for v in dtest.values()])
for k, v in dtest.items():
    pct_ = round(v / tot_count, 4)
    print('Word: ', k, ', count: ', v, ', %-age: ', pct_)
