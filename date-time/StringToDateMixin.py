

import re
import datetime as dt


def cls_prop(name, data_type):
    """Helper function to define class properties."""

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


class DateReformatter:

    date_string = cls_prop('date_string', str)

    DATE_RE_PATTERN = r"(\d{1,2}\/\d{1,2}\/\d{2,4}|\d{2,4}-\d{1,2}-\d{1,2})"

    YEAR_RE_PATTERN = r"\d?\d?(\d{2})"

    def __init__(self, date_string):
        self.date_string = date_string
        self.yr_prefix = re.sub(self.YEAR_RE_PATTERN, \
                                r"\1", f"{dt.datetime.today().year}")
        self.result = None

    def __repr__(self):
        return "<DateFormatMixin class>"

    def run(self):
        """Run reformatter, assuming that date_string is properly set."""

        #-- Compile regular expression patterns
        self.p = re.compile(self.DATE_RE_PATTERN)
        self.p_yr = re.compile(self.YEAR_RE_PATTERN)

        #-- Determine if string is in a general date format.
        res = self.p.match(self.date_string)

        #-- Split date_string into tokens; Considers '-' or '/' separators.
        self.date_parts = re.split(r"-|\/", self.date_string)

        if res:
            #-- If date_string is ISO8601 format.
            if '-' in self.date_string:
                new_yr = self.p_yr.sub(r"\1", self.date_parts[0])

                self.date_string = (
                        f"{self.yr_prefix}{new_yr}-" # Format -> 20##-##-##
                        + "-".join([f"{int(i):0>2}" for i in self.date_parts[1:]])
                        )

                self.result = dt.datetime.strptime(self.date_string, "%Y-%m-%d")

            else:
                new_yr = self.p_yr.sub(r"\1", self.date_parts[2])

                self.date_string = (
                        "/".join([f"{int(i):0>2}" for i in self.date_parts[:2]])
                        + f"/{self.yr_prefix}{new_yr}" # Format -> ##/##/20##
                        )

                self.result = dt.datetime.strptime(self.date_string, "%m/%d/%Y")
        else:
            print("Could not match date string.")

        output = self.result
        return output

def mixin_tests():
    """DateFormatMixin class test function."""
    base_case = dt.datetime(2019, 1, 1, 0, 0)

    test_dict = {
        0: "2019-01-01",
        1: "2019-1-1",
        2: "19-1-1",
        3: "1/1/19",
        4: "01/01/19",
        5: "01/01/2019",
    }

    for k, v in test_dict.items():
        dfm = DateReformatter(v)
        res = dfm.run()
        assert (res == base_case), f"Test error for key: {k}"
        
if __name__ == "__main__":
	#-- Run mixin tests
	mixin_tests()
