
"""
Purpose: Stackoverflow Q65159938
Date created: 2020-12-05

https://stackoverflow.com/questions/65159938/dictionary-of-named-tuples-in-python-and-speed-ram-performance

Contributor(s):
    Mark M.
"""


import ctypes as C


def wrap_function(lib, funcname, restype, argtypes):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

N = C.c_uint32(1000000)


class Tri(C.Structure):
    pass

class Tris(C.Structure):
    pass


Tri._fields_ = [
            ("id", C.c_uint16),
            ("name", C.c_wchar_p),
            ("isvalid", C.c_uint8),
            ]

Tris._fields_ = [
            ("idx", C.c_uint16 * N),
            ("tri_array", Tri * N),
            ]





tri = Tri(0, "thello", True)
tri1 = Tri(1, "fhello", False)
# br_tri = C.byref(Tri(0, "hello", 1))


import os
import psutil
import time
import collections
import typing
from sys import getsizeof

t0 = time.time()
d = {i: Tri(i+1, r"hello", 1) for i in range(1000000)}
t1 = time.time()
print('%.3f s  %.1f MB' % (time.time()-t0, psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2))
del d


import os, psutil, time, collections, typing
Tri = collections.namedtuple('Tri', 'id,name,isvalid')
Tri2 = typing.NamedTuple("Tri2", [('id', int), ('name', str), ('isvalid', bool)])