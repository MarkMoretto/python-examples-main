
"""
Purpose: 
Date created: 2020-10-06

https://stackoverflow.com/questions/64236489/how-to-convert-column-values-into-a-martix-using-python

Contributor(s):
    Mark M.
"""


items  = ['A', 'B','C','D','E']


# Make combinations
pairs = [f"{colA[i]}{colA[j]}" for i in range(len(items)) for j in range(len(items))]

# Find max character count per combo
max_sz = max(map(len, pairs))

# Set initial row to items list
output = [[" "] + items]

# Append additional rows based on starting character
for c in items:
    tmp = [c] + [p for p in pairs if str(p).startswith(c)]
    output.append(tmp)

# Format with specified padding from max_sz
final = ""
for ln in output:
    final += " ".join([f"{i:>{max_sz}}" for i in ln]) + "\n"

print(final)
