
"""
Purpose: Add plus-signs to string; But, really, the user wanted to parse URL values
Date created: 2019-04-20
Contributor(s): Mark Moretto

URL: https://stackoverflow.com/questions/48816981/replacing-spaces-in-lists/55778937#55778937
"""

import urllib

## Create an empty dictionary to hold values (for questions and answers).
data = dict()

## Sample input
input = 'This is my question'

### Data key can be 'Question'
data['Question='] = input

### We'll pass that dictionary hrough the urlencode method
url_values = urllib.parse.urlencode(data)

### And print results
print(url_values)


#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#Alternatively, you can setup the dictionary a little better if you only have a couple of key-value pairs

## Input
input = 'This is my question'

# Our dictionary; We can set the input value as the value to the Question key
data = {
    'Question=': input
    }

print(urllib.parse.urlencode(data))