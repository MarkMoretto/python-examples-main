"""
Summary: Pandas extension for converting 15-character Salesforce IDs to 18-character Salesforce IDs
Date: 2020-10-12
Contibutor(s):
    Mark Moretto

"""

from functools import lru_cache
from pandas import DataFrame
from pandas.api.extensions import DataFrame, register_series_accessor

@register_series_accessor("sf")
class PandasSalesforceIdConverter:
    """
    Salesforce ID converter extension for Pandas.  This should be applied to a series (column) and not the entire dataframe.
    
    """
    
    # Class variables
    __ASCII_UPPERCASE = "".join([chr(i) for i in range(65, 91)])
    
    # All alphabetic uppercase letters and numbers 0 - 5.
    CHARS = __ASCII_UPPERCASE + "012345"
    
    
    def __init__(self, pandas_object):
        self.__obj = pandas_object

    
    @staticmethod
    def __get_bin_list(string):
        """Checks for uppercase letters within ID. Tags 1 if found, 0 otherwise."""
        return [1 if str(c).isupper() else 0 for c in string]
 
    
    @lru_cache(maxsize=1000)
    def __convert_id(self, value):
        """Convert 15-character Salesforce ID 18-character version."""

        # If value is not alphanumeric.
        if not value.isalnum():
            return ""
        
        # If character count of value not equal to 15, return value.
        elif len(value) != 15:
            return value
        
        # if alphanumeric and 15 characters long.
        else:
            calculated_chars: str = str()
            
            chunks: list = [value[i:i+5] for i in range(0, 15, 5)]
                        
            for chunk in chunks:
                bin_list = self.__get_bin_list(chunk)
                idx = self.decoder(bin_list)
                calculated_chars += self.CHARS[idx]
            
            return f"{value}{calculated_chars}"
            
        
    @staticmethod
    def decoder(binary_list):
        """Return decimal value from collection of binary values."""
        list_len = len(binary_list)
        return sum([2**i if binary_list[i] == 1 else 0 for i in range(list_len)])
    

    @property
    def convert(self):
        return self.__obj.apply(self.__convert_id)
        
        
# Tests

id_test_dict = dict(
    sfid_in = ["a0r90000008cJza", "aCQR000000018HT", "aCQR000000018HYOAY"],
    sfid_expected = ["a0r90000008cJzaAAE", "aCQR000000018HTOAY", "aCQR000000018HYOAY"],
    )

df1 = DataFrame(id_test_dict)

df1.loc[:, "sfid_actual"] = df1["sfid_in"].sf.convert
