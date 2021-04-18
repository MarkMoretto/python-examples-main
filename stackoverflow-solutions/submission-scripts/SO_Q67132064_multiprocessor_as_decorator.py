
"""
Purpose: Stackoverflow
Date created: 2021-04-17

Title: Python Multiprocessing Pool as Decorator
URL: https://stackoverflow.com/questions/67132064/python-multiprocessing-pool-as-decorator

https://docs.python.org/3/reference/datamodel.html#metaclasses
https://docs.python.org/3/reference/datamodel.html
https://docs.python.org/3.7/library/copyreg.html?highlight=copyreg#module-copyreg
https://bytes.com/topic/python/answers/552476-why-cant-you-pickle-instancemethods#edit2155350
https://stackoverflow.com/questions/6780907/python-wrap-class-method

Contributor(s):
    Mark M.
"""


import time
from multiprocessing import Pool
from functools import partial

try:
    import copyreg
except ModuleNotFoundError as e:
    import copy_reg as copyreg

from types import MethodType, ModuleType


def parallel(num_processes):
    def parallel_decorator(func, num_processes=num_processes):
        def parallel_wrapper(iterable, **kwargs):
            func = partial(func, **kwargs)
            p = Pool(processes=num_processes)
            output = p.map(func, iterable)
            p.close()
            return output

        return parallel_wrapper
    return parallel_decorator

@parallel(6)
def test_func(x):
    time.sleep(1)
    return x


class MetaPool(type):
    @staticmethod
    def wrap(func):

        def outer(self):
            _proc = func(self)
            func = partial(func, **kwargs)
            p = Pool(processes=num_processes)
            output = p.map(func, iterable)
            p.close()
            return output

        return outer
    # def __new__(cls,

class Parallel:
    def __int__(self, num_processes):
        self.num_processes = num_processes

    def __call__(self, func):
        def parallel_decorator(func, num_processes=num_processes):
            def parallel_wrapper(iterable, **kwargs):
                func = partial(func, **kwargs)
                p = Pool(processes=num_processes)
                output = p.map(func, iterable)
                p.close()
                return output
    
            return parallel_wrapper
        return parallel_decorator

class Star:
    def __init__(self, n):
        self.n = n

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            print(self.n*'*')
            result = fn(*args, **kwargs)
            print(result)
            print(self.n*'*')
            return result
        return wrapper

@Star(5)
def addit(a, b):
    return a + b

addit(10, 20)