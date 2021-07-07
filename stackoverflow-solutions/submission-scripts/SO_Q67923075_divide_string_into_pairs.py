
"""
Purpose: Stackoverflow answer
Date created: 2021-06-10

Split and map numeric strings.
URL: https://stackoverflow.com/questions/67923075/divide-a-string-into-pairs/67923200#67923200

Contributor(s):
    Mark M.
"""


ip = 'MDSYS.SDO_GEOMETRY(2003, NULL, NULL, MDSYS.SDO_ELEM_INFO_ARRAY(1, 1003, 1), MDSYS.SDO_ORDINATE_ARRAY(22027, 22943, 22026, 22939, 22025, 22936, 22025, 22932, 22027, 22929, 22030, 22926)'

split_string_1 = "MDSYS.SDO_ORDINATE_ARRAY("
split_string_2 = ")"


if __name__ == "__main__":

    data = list(map(int, ip.split(split_string_1)[1].split(split_string_2)[0].split(", ")))
    
    
    result = list(zip(data[:-1], data[1:]))
    
    print(result)