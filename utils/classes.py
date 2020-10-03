"""
Summary: Functions and misc for helping to define class objects.
Date created: 2020-10-03
Contributor(s):
    Mark Moretto
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
