
"""
Purpose: Stackoverflow response
Date created: 2020-08-14

https://stackoverflow.com/questions/63421089/get-difference-between-responses-constantly-updating/63421225#63421225

Contributor(s):
    Mark M.
"""

import json

flattener = lambda lst: [i for e in lst for i in (flattener(e) if isinstance(e, dict) else [e])]

flattener = lambda lst: [i for e in lst for i in (flattener(e) if isinstance(e, dict) else [e])]

def flatten(iterable):
    """Recursive flattening of sublists."""

    if len(iterable) > 1:
        res = flatten(iterable[0])
    else:
        res = iterable[0]

    return res


# Base data
current = json.dumps({'values': [{'value': 'value1',},{'value': 'value2',}]})
current = json.loads(current)

while True:
    # Read data
    new_read = json.dumps({'values': [{'value': 'value1_changed',},{'value': 'value2',}]})
    new_read = json.loads(new_read)

        # Check if data exists
        if new_read:
            # Run through each key

            for key in new_read.keys():
                # set interim variable for the new list
                v_new = new_read[key]

                # Check if key exits in the current data
                if current[key]:
                    # Create temp variable for current data
                    v_current = current[key]

                    # For each element in the new data list
                    for dd in v_new:
                        # For each element in the current data list
                        for cc in v_current:

                            # List comprehension to compare values
                            res = [v for k, v in dd.items() if cc[k] != v]

                        # If we get a result, print all results
                        if len(res) > 0:
                            print("\n".join(res))

                # If the current data doesn't have the key, print hte key
                else:
                    print(key)


            for d in new_read["values"].items():
                for k, v in new_read["values"][i].items():
                    if current["values"][i][k] != v:
                            print(k, v)
            # for i in range(len(new_read["values"])):
            #     for k, v in new_read["values"][i].items():
            #         if current["values"][i][k] != v:
            #                 print(k, v)
    # Set current to new_read
    current = new_read

    # Break on False clause
    break

