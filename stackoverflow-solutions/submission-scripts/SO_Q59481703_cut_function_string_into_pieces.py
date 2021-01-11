
"""
Purpose: Stakoverflow response:
Date created: 2019-12-25

Title: Own programming language: cut function into pieces
Ref: https://stackoverflow.com/questions/59481703/own-programming-language-cut-function-into-pieces?noredirect=1#comment105139985_59481703

Contributor(s):
    Mark M.
"""

import re

functions = {
   'out': [
      {'reversed': '"Hello"' } , {'in':''} # (those two dictionaries are in an array)
   ] 
}

functions['out'][0]['reversed']
functions['out'][1]['in']



input_str = 'out(reversed("Hello"),in("User"))'

func_pat = r"(\w+?)\((.*)\)" # Split the function name and arguments
res = re.match(func_pat, input_str).groups(0)
func_name = res[0] # out
func_args = res[1].split(',')

args_pat = r"(\w+?)\(\"?(\w+)\"?\)" # Split argument functions and arguments
args1 = re.match(args_pat, func_args[0]).groups(0)
args2 = re.match(args_pat, func_args[1]).groups(0)


# Set output_string to empty string value
output_string = ''

# Run through your functions dictionary/json
for k in functions.keys():
    # If the function key matches our regex result
    if k == func_name:
        # Iterate through all sub-dictionaries
        for idx in range(len(functions[k])):
            # For the key value pairs in the current dictionary items
            for key, val in functions[k][idx].items():
                # If the key matches our first argumen, first value
                # which is the name of the function
                if key == args1[0]:
                    # Reverse the passed value in our argument and append it to the string
                    output_string += str(args1[1])[::-1]
                # Otherwise, if the key matches the first value of our second argument
                elif key == args2[0]:
                    # Append the user input string
                    output_string += str(args2[1])



