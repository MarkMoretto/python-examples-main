
"""
Purpose: SO answer
Date created: 2021-10-28

https://stackoverflow.com/questions/69761150/python-why-am-i-getting-typeerrors-on-these-two-problems-recursion/69761356#69761356

Contributor(s):
    Mark M.
"""

lst1 = [1, 2.2, 4, "string"]
for item in lst1:
    # print(item, "is a ", type(item))
    if type(item) == str:
        print("this is a string: ", item)
    elif type(item) == int or float:
        print("ok for ", item)
        if item % 2 * 10 == 0:
            print("ok 2 for ", item)


def recEvenNumbers(lst, evens = None):
    'return a count of all the even numbers(ints and floats) in the list'
    if evens is None:
        evens = [0]

    if lst:
        item, *lst = lst
        # Check for string first, pass if detected.
        if type(item) == str:
            pass
        elif type(item) == int or float:
            if item % 2 * 10 == 0:
                evens[0] += 1
        return recEvenNumbers(lst, evens)
    return evens[0]

recEvenNumbers(lst1)



def recMerge(a, b):
    'Merge two strings together recursivly'
    # Check types
    if type(a) == type(b) == str:
        # Run until b is empty.
        if len(b) > 0:
            # Deconstructing into single and rest of items with asterisk.
            aa, *a_rest = a
            bb, *b_rest = b
            # New `a` value that prepends the rest of a in
            # front of the concatenation of the current a and b characters.
            # Since a_rest is a list, we should "collect" the items back into
            # a proper string format.
            a = "".join(a_rest) + aa + bb
            # Return the new a with another concatenated list for the
            # remaining b items.
            return recMerge(a, "".join(b_rest))
    # Return a.  Ensure that it is a string.
    return "".join(a)

A = "abc"
B = "def"
recMerge(A, B)

# def recMerge(a,b):
#     'Merge two strings together recursivly'
#     if len(a)==0:
#         return
#     elif len(b)==0:
#         return
#     else:
#         if type(a) == str:
#             if type(b) == str:
#                 return a[0] + b[0] + recMerge(a[1:], b[1:])


# def recEvenNumbers(lst):
#     'return a count of all the even numbers(ints and floats) in the list'
#     evens = 0
    
#     if lst == []:
#         return
#     else:
#         if type(lst[0])== int or float:
#             if ((lst[0]%2*10))==0:
#                 evens = evens+1
#             return recEvenNumbers(lst[1:], evens + 1)
