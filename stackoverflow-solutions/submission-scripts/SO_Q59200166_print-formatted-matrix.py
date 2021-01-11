
"""
Purpose: Stackoverflow question 59200166
Topic: Print row and column labels for strings grid in Python
Date created: 2019-12-05

Ref URI: https://stackoverflow.com/questions/59200166/print-row-and-column-labels-for-strings-grid-in-python/59201063#59201063

Contributor(s):
    Mark M.
"""


def readLevel(n):
    '''takes an integer as argument representing the level number
    and reads the appropriate game board file. Returns it as a 
    2D list of strings.'''

    try:
        file = open(f'./levels/ascii_level{n}.txt','r')
        game_board = []
    
        for line in file:
            ascii_string = list(line.rstrip())
            game_board.append(ascii_string)
    
        file.close()
    
        return game_board
    
    except FileNotFoundError:
        print(f"Failed to read level {n}. Game ending.")


### Recreate this
def displayBoard(gameBoard):
'''takes a gameboard 2D list as argument and displays it to the 
console with row and column labels included'''


    for row in gameBoard:
        board_grid = ''
        for ele in row:
            board_grid += str(ele)
        print(board_grid)



############ Sample grid #################

output = [['#', '#', '#', '@', '@', '#', '#', '#', '%'],
 ['#', '#', '@', '@', '&', '&', '&', '#', '%'],
 ['@', '#', '#', '#', '#', '#', '&', '#', '%'],
 ['@', '@', '@', '@', '#', '#', '#', '%', '%'],
 ['#', '@', '%', '%', '%', '%', '%', '%', '%']]




################## Start of solution ##############################

lpad = ' ' * 3
col_len = len(output[0])
num_list = ''.join([str(i) for i in range(col_len)])
divider = '-' * col_len
msg = f'{lpad}{num_list}\n{lpad}{divider}'

for i in range(len(output)):
    values = ''.join([i for i in output[i]])
    msg += f'\n0{i}|{values}'


print(msg)


### Final function
def displayBoard(gameBoard):
    '''takes a gameboard 2D list as argument and displays it to the 
    console with row and column labels included'''


    # Pad board by three spaces
    lpad = ' ' * 3

    # Column length
    col_len = len(output[0])

    # List of numbers from 0 through col_len - 1
    num_list = ''.join([str(i) for i in range(col_len)])

    # Ddivider
    divider = '-' * col_len

    # First part of stirng output
    msg = f'{lpad}{num_list}\n{lpad}{divider}'

    # Iterate rows
    for i in range(len(output)):
        # Join elements of row with no space in between
        values = ''.join([i for i in output[i]])
        # Append values to mesage with a 0, row number, and vertical line
        msg += f'\n0{i}|{values}'

    # Print results
    print(msg)





