
"""
Purpose: Stackoverflow post
Date created: 2020-08-04

URL: https://stackoverflow.com/questions/63257534/code-infinitely-runs-loop-and-i-dont-see-why/63257658#63257534

Contributor(s):
    Mark M.
"""


"""
# Original code
while gameOver == False:
    print('\nWhere would you like to move?\nYou can chose top-, mid-, or bot- with L, M, or R at the end')
    move_spot = '_' # I feel like this should reset move_spot every time the loop runs, meaning the user has to give an input
    while move_spot not in theBoard.keys():
        move_spot = input()
    theBoard[move_spot] = userChar
    comp_spot = '_'
    while move_spot not in theBoard.keys():
        comp_spot = random.choice(list(theBoard))
    theBoard[comp_spot] = compChar

    printBoard(theBoard)
"""


import random



moves = [
    "top-L",
    "top-M",
    "top-R",
    "mid-L",
    "mid-M",
    "mid-R",
    "bot-L",
    "bot-M",
    "bot-R",
    ]

theBoard = {k:v for k, v in enumerate(moves)}


actions = dict(
        user=[],
        computer=[],
        )

# tot_actions = list(actions.values())


move_spot = None
gameOver = False
player_move = True
comp_move = not player_move

while not gameOver:

    print('\nWhere would you like to move?\nPlease enter a number from the following list:')
    print("\n".join([f"{k}: {v}" for k, v in theBoard.items()]))
    while player_move:
        try:
            move_spot = int(input('> '))
    
            actions["user"].append(move_spot)

            theBoard = {k:v for k, v in theBoard.items() if not k in actions["user"]}
            if len(theBoard) > 0:
                player_move = False
                comp_move = not player_move
            else:
                gameOver = True
        except ValueError:
            print("Pleae enter an integer value.")
            pass

    while comp_move:
        comp_spot = random.choice(list(theBoard.keys()))
        actions["computer"].append(comp_spot)
        theBoard = {k:v for k, v in theBoard.items() if not k in actions["computer"]}
        if len(theBoard) > 0:
            comp_move = False
            player_move = not comp_move
        else:
            gameOver = True

    gameOver = True

print(theBoard)