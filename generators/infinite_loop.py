
"""
Purpose: Infinite generator for numbers within a range.
Date created: 2020-01-12

Contributor(s):
    Mark M.
"""


def _i_range(start, stop = None, increment = None):
    """Simple integer range generator."""
    i = int(start)

    if stop is None:
        i_stop = int(start)
        i = int(0)
    else:
        i_stop = int(stop)

    if increment is None or increment is 0:
        i_incr = int(1)
    else:
        i_incr = int(increment)


    while i < i_stop:
        yield i
        i += i_incr

def xrange(start, stop = None, increment = None):
    """Implementation of range generator. Output is a list of integers"""
    return [i for i in _i_range(start, stop, increment)]



def range_generator(min_, max_, incr_ = None):
    """
    Generator to loop through a range of values indefinitely.
    """
    i_min = int(min_)
    i_max = int(max_)

    if incr_ is None or incr_ is 0:
        i_incr = int(1)
    else:
        i_incr = int(incr_)

    while True:
        n = i_min
        while n <= i_max:
            yield n
            n += i_incr


def range_generator_func(minimum, maximum, n_values, increment = None):
    """Returns a collection of numerical values based on the min/max constraints."""
    rng = range_generator(minimum, maximum, increment)
    return [rng.__next__() for i in xrange(n_values)]



if __name__ == '__main__':
    print('Infinite generator test.\nThis generator will loop in a specified range until stopped.')

    #-- Sample data; N is number of iterations to perform
    start = 1
    end = 5
    N = 20
    print(f"Variables used:\nStart: {start}\nEnd: {end}\nNumber of results: {N}")

    # Results from the generator function
    output = "\n\nResults from using a function that implements the generator:\n"
    results_1 = range_generator_func(start, end, N)
    output += ', '.join([f"{i}" for i in results_1])

    # Results from the generator itself.
    output += "\n\nResults from the generator itself:\n"
    rng = range_generator(start, end)
    results_2 = [rng.__next__() for i in xrange(N)]
    output += ', '.join([f"{i}" for i in results_2])

    print(output)




