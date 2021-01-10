
"""
Stackoverflow question 549755: Printing chunked loops of formatted data.

Source: https://stackoverflow.com/questions/54975518/python-printing-before-after-different-lines/55013864#55013864

Contributor: Mark Moretto
Date: 2019-03-05
Email: otteromkram@gmail.com
"""


### your main body element with {} to pass a number
element = '[td][center]Label[img]Image{}.jpg[/img][/center][/td]'

### The number of "blocks" you want to print.
max_item_blocks = 3

### Define a start value of 1
start = 1

### Our simple loop with join() function
while max_item_blocks > 0:

    ### End value is start + 5
    end = start + 5


    ### The join function with the integer value of a loop passing to our element stirng.
    ### The range goes an extra 1 beyond what you think, unless you set a start value.
    ### So, range(10) is 0,1,2,3,4,5,6,7,8,9.
    print('[tr]\n' + '\n'.join([element.format(i) for i in range(start, end)]) + '\n[\\tr]')

    ### Start takes ending value
    start = end

    ### Ending value is now start + 5
    end = start + 5

    ### Reduce our block counts by 1
    max_item_blocks -= 1

