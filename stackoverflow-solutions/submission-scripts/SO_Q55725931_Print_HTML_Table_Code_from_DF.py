

"""
Purpose: Print out an HTML table structure using Pandas
Date: 2019-04-17
Contributor(s): Mark Moretto

Ref: https://stackoverflow.com/questions/55725931/csv-file-to-editable-table-in-html-using-python
"""
import pandas as pd

ddict = {
    'Id': ['1', '2', '3', '4', '5', '6'],
    'Value': ['2','5', '7', '10', '15', '4'],
    'Name': ['Paul','Sam', 'Jill', 'Karl', 'Sally', 'Irma']
}

df = pd.DataFrame(ddict)

### Print the table tag
print('<table>')

### Print the headers to a <th> tag; Close each <th> for every line
print('\t<tr>\n\t\t<th>' + '\t\t<th>'.join([f'{i}</th>\n' for i in df.columns.values.tolist()]) + '\t</tr>')

### Iterate over dataframe values; Enclose each value in a <td> tag
for i, v in enumerate(df.values):
    print('\t<tr>\n\t\t<td>' + '\t\t<td>'.join([f'{x}</td>\n' for x in v]) + '\t</tr>')

### Print table tag closure.
print('</table>')

