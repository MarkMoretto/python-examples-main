#!/bin/python
# -*- coding: utf-8 -*-

__all__ = [
    "df_downcast"
    ]

from __future__ import annotations

# from pandas import DataFrame, to_numeric
import pandas as pd

# --- / Types to convert / ---
type_map={
    "integer": ["int", "int32", "int64"],
    "float": ["float", "float32", "float64"],
    }


def df_downcast(d: pd.DataFrame) -> None:
    """Downcast numeric data types in pandas DataFrame.

    Parameters
    ----------
    d : DataFrame
        pandas DataFrame with at least one numeric data type.

    Returns
    -------
    None

    Examples
    --------
    >>> df = DataFrame({"col1": [1,2,3], "col2": [1.1, 2.2, 3.3]})
    >>> df["col1"].dtype
    dtype('int64')
    >>> df["col2"].dtype
    dtype('float64')    
    >>> df_downcast(df)
    >>> df["col1"].dtype
    dtype('int8')
    >>> df["col2"].dtype
    dtype('float32')
    """
    for _type, _typelist in type_map.items():
        for c in d.select_dtypes(include=_typelist).columns:
            d.loc[:, c] = pd.to_numeric(d.loc[:, c], downcast=_type)



# ---/ Pandas Extension / ---
@pd.api.extensions.register_dataframe_accessor("slim")
class Downcaster:
    """pandas extension to "slimify" a dataframe via downcasting types.

    Parameters
    ----------
    pandas_obj : pd.DataFrame | None
        The object should be instantiated between importing pandas and creation of your
        first DataFrame.  It will be apart of the dataframe and called directly.
        Any subsequent calls, unless the dataframe is updated with new data,
        will have no effect.

    Returns
    -------
    None

    Examples
    --------
    >>> df = DataFrame({"col1": [1,2,3], "col2": [1.1, 2.2, 3.3]})
    >>> df["col1"].dtype
    dtype('int64')
    >>> df["col2"].dtype
    dtype('float64')
    >>> df.slim()
    >>> df["col1"].dtype
    dtype('int8')
    >>> df["col2"].dtype
    dtype('float32')
    """
    
    TYPE_MAP = {
        "integer": ["int", "int32", "int64"],
        "float": ["float", "float32", "float64"],
        }
    
    def __init__(self, pandas_obj) -> None:
        self._obj = pandas_obj

    def __call__(self) -> None:
        for _type, _typelist in self.TYPE_MAP.items():
            for c in self._obj.select_dtypes(include=_typelist).columns:
                self._obj.loc[:, c] = pd.to_numeric(self._obj.loc[:, c], downcast=_type)


            
if __name__ == "__main__":
    import doctest
    doctest.testmod()
