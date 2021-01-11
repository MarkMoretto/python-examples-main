
"""
Purpose: Remove header section from text file
Date created: 2019-04-17
Contributor(s): Mark Moretto

Ref: https://stackoverflow.com/questions/55737348/python-code-to-delete-headers-from-txt-files
"""

import tempfile
from io import StringIO
data = StringIO()

file_path = r'C:\Users\...\...'

# Set the numder of lines you'd like to exclude
header_end = 82

### Read your data into a StringIO container
with open(file_path, 'r') as f:
    data.write(f.read())

### Split linkes by \n (newline)
tokens = data.getvalue().split('\n')

### Rejoin with a newline, but start at the header index value plus one.
output_str = '\n'.join(tokens[header_end + 1:])

### Create a tempfile with '.txt' suffix; print(path) to find out file location (should be in temp folder)
fd, path = tempfile.mkstemp(suffix='.txt')
try:
    with os.fdopen(fd, 'w') as tmp:
        tmp.write(output_str)
except IOError:
    print('Error writing temp file.')


### To rcleanup and remove the file
if os.path.isfile(path):
    try:
        os.remove(path)
    finally:
        os.unlink(path)


