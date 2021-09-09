from fractions import Fraction

print_dict = lambda d: print("\n".join([f"{k}: {v}" for k, v in d.items()]))

def dice_sample(number_of_sides: int = 6) ->:
    """Prints basic sample space and value frequency for the roll
    of two unbiased dice with N sides.
    
    Parameters
    ----------
    number_of_sides : int
        Number of faces for each die.  Face values start at 1 and
        go up to the given number of sides.  Default: 6.
    
    Returns
    -------
    None
    """
    
    die_values = range(1, number_of_sides + 1)

    sample_space = {}
    for v1 in die_values:
        for v2 in die_values:
            total = v1 + v2
            if not total in sample_space:
                sample_space[total] = [(v1, v2)]
            else:
                sample_space[total] += [(v1, v2)]

    ss_size = sum(len(v) for v in sample_space.values())
    sample_space_freq = {k:Fraction(len(v), ss_size) for k, v in sample_space.items()}
    
    # Output
    print("Sample space of dice rolls:\n")
    print_dict(sample_space)
    print("\nValue frequency of dice rolls:\n")
    print_dict(sample_space_freq)

    
if __name__ == "__main__":
    print("Please enter number of sides for both dice\n(or, leave blank for 6)")
    n_faces = input(">>> ")
    
    if n_faces:
        n_faces = int(n_faces)
        dice_sample(n_faces)
    else:
        n_faces = 6

    dice_sample()
