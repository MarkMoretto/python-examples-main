"""
Summary: IPython magic function for Windows users to print a sample
        of data from a file to the Jupyter Notebook output

Date created: 2021-07-04

Contributor(s):
    mark moretto
"""
import re
from IPython.core.magic import register_line_magic

@register_line_magic
def header(line: str) -> None:
    """IPython magic method to read first N lines of a file if
    using Windows platform.
    
    Parameters
    ----------
    filepath : str
        Relative or absolute filepath to a data file.
    n_lines : int
        Number of lines to print.  Default: 10.
    
    Example Usage
    -------------
    %header data\my-data.csv 5
    
    Returns
    -------
    None    
    """
    lines = re.split(r"\s+", line)
    filepath = lines[0]

    # Set number of lines variable default and update
    # if valid data present.
    n_lines: int = 10
    if len(lines) == 2:
        n_lines = int(lines[1])

    output: list = []
    with open(filepath) as f:
        # first N lines
        for _ in range(n_lines):
            output.append(f.readline())
    print("".join(output))
