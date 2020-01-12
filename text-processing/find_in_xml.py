

import os
import re
import typing as T

Q = T.TypeVar('Q', str, int, float)
N = T.TypeVar('N', int, float)
s_vec = T.List[str]
iter_str = T.Iterable[str]


def enum(it: T.Iterable[Q], start: int = 0) -> T.Dict[int, Q]:
    n = start
    for element in it:
        yield n, element
        n += 1

def tokenizer(it: iter_str, split_by_chars: str = '\n') -> s_vec:
    return [i.strip() for i in it.split(split_by_chars)]

def no_blanks(it: iter_str, split_by_chars: str = '\n') -> s_vec:
    return [i for i in tokenizer(it) if len(i) > 0]

def enum_dict(it: T.Iterable[Q]) -> T.Dict[int, Q]:
    return {k:v for k, v in enum(it)}


xml_pth = r'<filepath>>.xml'
with open(xml_pth, 'r') as xmlf:
    xml_raw = xmlf.read()

data = re.sub(r"(><)(?!\/)", ">\n<", xml_raw)
ddict = enum_dict(data.split('\n'))

search_term = '<keyword>'
for k in ddict.keys():
    ln = str(ddict[k])
    if search_term in ln.lower():
        kwrd_pos = ln.lower().index(search_term)
        print(f"{k} - {kwrd_pos}: {ln[kwrd_pos:kwrd_pos + len(search_term)]}")
