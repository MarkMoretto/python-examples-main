
"""
Purpose: subgrid sums revisited
Date created: 2020-10-26

Improve this monstrosity:
    https://github.com/MarkMoretto/python-examples-main/blob/master/matrices/submartix_sums.py

Contributor(s):
    Mark M.


Example:

  9  8  7
  6  5  4
  3  2  1
  
For subgrids of 2x2, we have the sum of values:
  9 8 6 5 = 28
  8 7 5 4 = 24
  6 5 3 2 = 16
  5 4 2 1 = 12
  Total --> 80
    
"""


def cls_property(name, data_type):
    """Helper function to define class properties.
    
    Example:
        >>>class A:
                a_name = cls_property("abc", str)
                def __init__(self, name):
                    self.a_name = name
                
        >>>a = A("bill")
        >>>a.a_name
        'bill'
        >>>a.__abc
        'bill'
    """

    masked_name = "__" + name

    @property
    def prop(self):
        return getattr(self, masked_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, data_type):
            raise TypeError(f"Expected data type for {name} is {data_type}.")
        setattr(self, masked_name, value)

    return prop



class SubgridSum:

    matrix = cls_property("matrix", list)
    matrixR = cls_property("matrixR", list)
    matrixT = cls_property("matrixT", list)
    matrixTR = cls_property("matrixTR", list)

    def __init__(self, matrix):
        self.matrix = matrix
        self.__set_transforms()

    def __repr__(self):


    def __set_transforms(self):
        self.matrixT = list(map(list, zip(*self.matrix)))
        self.matrixR = self.matrix[::-1]
        self.matrixTR = self.matrixT[::-1]

    @staticmethod
    def __print_format(iterable):
        return "\n".join((map(lambda e: "".join(map(str, e)), iterable)))





a = [[j for j in range(i, i + 3)] for i in range(1, 10, 3)]
ss = SubgridSum(a)


def print_matrix(matrix):
    print("\n".join((map(lambda e: "".join(map(str, e)), matrix))))