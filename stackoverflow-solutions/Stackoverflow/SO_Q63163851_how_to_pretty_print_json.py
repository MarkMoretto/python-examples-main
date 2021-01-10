
"""
Purpose: Stackoverflow question - pretty print json
Date created: 2020-07-29

URL: https://stackoverflow.com/questions/63163851/how-to-pretty-print-json-string-whose-value-is-also-a-json-string-in-python/63164049#63164049


Contributor(s):
    Mark M.
"""

import json

json_string = '{"content": [{"key": "value"}], "otherContent": [{"key2": "value"}]}'

loaded_json = json.loads(string)
json.dumps(string, sort_keys=True, indent=4)

json.JSONEncoder(indent=8).