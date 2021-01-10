
"""
Purpose: Stackoverflow answers
Date created: 2020-12-01
URL: https://stackoverflow.com/questions/65102025/python-list-of-tuples-sum-of-tuples-having-same-first-value-in-this-case/65102353#65102353

Contributor(s):
    Mark M.
"""



li=[('name1', 5, 10), ('name2', 3, 2), ('name1', 6, 3)]

# Get length of structure
li_len = len(li)

# Create empty collection
outdict = {}

# Iterate over all elements
for i in range(li_len):
    tmpname = li[i][0] # Temp name variable
    tmpvalues = li[i][1:] # Temp values variable

    # If not temp name in dictionary keys
    if not tmpname in outdict:
        # Create entry with values as first values
        outdict[tmpname] = list(tmpvalues)
    else:
        # Otherwise, iterate values and update entry by position
        for j in range(len(tmpvalues)):
            outdict[tmpname][j] += tmpvalues[j]

# Reformat for output
result = [tuple([k] + v) for k, v in outdict.items()]

# Print result
print(result)





counted = []
for i in range(li_len):
    i_tmp = list(li[i])
    for j in range(i, li_len):
        if li[j][0] in counted:
            break

        elif i_tmp[0] == li[j][0]:
            counted.append(i_tmp[0])
            for k in range():


