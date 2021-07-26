

words = ["hello", "world", "this", "is", "fantastic!",]

def recur_dict(items: list, index_start: int = 1, d: dict = None, i: int = 0) -> dict:
    """Return dictionary of iteratively-added items from a list.
    
    Parameters
    ----------
    iterable : list
        List of items from which we will forge our iterable collection.
    index_start : int
        Base value to start an index in the iterable collection. Default: 1.
    d : dict
        Iterable key-value collection for housing our incrementally-large string objects. Default: None.
    i : int
        Incremental indexer for proper placement of our items within the iterable collection. Default: 0.

    Returns
    -------
    dict
        Iterable key-value collection of increasing string size.
    """

    # Determine if iterable still exists
    #   If not, return dictionary object.
    if iterable:

        # Split next item off of indexable collection.
        word, items = items[0], items[1:]

        # Create a dictionary if it does not exist
        if d is None:
            d = {}

        # If we're just starting, we don't have any prior results to
        # engorge our data with, so just set the first key to the 
        # first value.

        # The first key will be our base index (0) plus the starting
        # index that is passed as an argument.
        if i == 0:
            d[i + index_start] = word

        # Otherwise, add the next word to an immutable string and set it to the
        # current calculated index.
        else:
            d[i + index_start] = " ".join([d[i], word])

        # Return our function with updated values.
        return recur_dict(items, index_start, d, i + 1)

    # Return our dictionary once complete.
    return d

if __name__ == "__main__":
	result = recur_dict(words)
	if result:
		print("\n".join([f"{k}: {v}" for k, v in result.items()]))

# --- Expected output --- #
#     1: hello
#     2: hello world
#     3: hello world this
#     4: hello world this is
#     5: hello world this is fantastic!
