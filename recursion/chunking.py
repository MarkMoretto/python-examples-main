

from typing import Iterator, Iterable

def chunkerator(obj: Iterable, stepsize: int = 10) -> Iterator:
    """
    Recursively "step" through iterable object in efficient manner.

    Parameters
    ----------
    obj : Iterable
        Object to iterate over, such as a list of numbers or strings.
    stepsize : int
        Size of each "chunk" to return.  Default: 10.
        
    Returns
    -------
    None

    Yields
    ------
    Iterator
        A generator object that will step through an iterable for a given step size
        until complete.
        
    >>> tester = list(map(str, range(15)))
    >>> list(chunkerator(tester, 5))
    [['0', '1', '2', '3', '4'],
    ['5', '6', '7', '8', '9'],
    ['10', '11', '12', '13', '14']]		
    """

    if obj:
        chunk, obj = obj[0:stepsize], obj[stepsize:]

    try:
        yield chunk
        yield from chunkerator(obj, stepsize=stepsize)
    except (RuntimeError, StopIteration, UnboundLocalError):
        pass

	
if __name__ == "__main__":

    import doctest
    doctest.testmod()
