
"""
Purpose: stackoverflow solution.
Date created: 2021-03-04

Title: How to generate a lists of lists or nested from user input while outputting amount of times a word is stated?
URL: https://stackoverflow.com/questions/66483811/how-to-generate-a-lists-of-lists-or-nested-from-user-input-while-outputting-amou/66484266#66484266
Contributor(s):
    Mark M.
"""



sample = "Nice day #running #10k #power #running"

# Output: [running,10k, power, running] and [[running,2],[10k,1],[power,1]]


def incr(el, ddict):
    if not el in ddict:
        ddict[el] = 1
    else:
        ddict[el] += 1



def process_input(string, key_char = "#"):

    # Creating a clean list of keywords by a given target character.
    base_list = [i.replace(f"{key_char}", "") for i in string.split(" ") if i[0] == f"{key_char}"]

    # We can use the list.count() function on a set of keywords
    # to return the instance of each word within a given string.
    word_count_list = [[w, base_list.count(w)] for w in set(base_list)]

    return base_list, word_count_list

process_input(sample)