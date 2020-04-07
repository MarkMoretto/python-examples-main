
"""
Purpose: Create a algorithm/process to identify white and black piano keyboard keys.
Date created: 2020-04-06

Contributor(s):
    Mark M.
"""



first_two_group = 5
first_three_group = 10
group_step = 12


def incrementer(obj, n_values=3, step=2):
    n = 0
    output = obj
    while n < n_values:
        yield output
        output += step
        n += 1



def create_key_color_dict(verbose=False, key_dict = None):
    keys = [i for i in range(1, 89)]
    if key_dict is None:
        ddict = {}

    two_start = first_two_group
    three_start = first_three_group

    ddict[1] = "W"
    ddict[2] = "B"
    to_skip = [1, 2]

    for k in keys:
        if not k in to_skip:
            if k == three_start:
                three_group = list(incrementer(three_start, 3))
                for i in three_group:
                    ddict[i] = "B"
                    to_skip.append(i)
                three_start += group_step
    
            elif k == two_start:
                two_group = list(incrementer(two_start, 2))
                for i in two_group:
                    ddict[i] = "B"
                    to_skip.append(i)
    
                two_start += group_step
    
            else:
                ddict[k] = "W"

        if verbose:
            msg = f"Key: {k}:\n\tTwo start: {two_start}\n\t"
            msg += f"Three start: {three_start}\n\tTo_skip: {to_skip}"
            print(msg)
    return dict(sorted(ddict.items(), key=lambda x: x[0]))

if __name__ == "__main__":
    key_color_dict = create_key_color_dict()
    print(key_color_dict.items())




