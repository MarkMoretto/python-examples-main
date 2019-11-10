"""
Topic: The Monty Hall Problem Solved with Sets
Author: Mark Moretto
Date Started: 12/23/2017

Examples:
  In[1]: MontyHallSim(1000)
  Number of wins: 685
  Number of losses: 315
  Winning percentage: 68.50%

  In[2]: MontyHallSim(1000, switch=False)
  Number of wins: 333
  Number of losses: 667
  Winning percentage: 33.30%
"""


def MontyHallSim(iterations=100, number_of_doors=3, switch=True):
    import random, copy

    if isinstance(iterations, int) == False:
        print("Please enter integer value for number of iterations!")

    ### Set variables for counting results
    wins = 0
    losses = 0

    ### Getting range of possible door selections
    ### I added one to a bunch of these to simulate real-life options
    ### (No one is going to have a door '0' on a game show)
    doorCount = int(number_of_doors)
    allDoors = [i for i in range(1, doorCount + 1)]



    ### Here's where we run each simulation and add results to our win/loss counters
    for i in range(1, iterations + 1):

        # Copying list of door selections; Randomizing those
        closedDoors = copy.copy(allDoors)
        nonWinningDoors = copy.copy(allDoors)
        random.shuffle(closedDoors)
        random.shuffle(nonWinningDoors)

        ### Contestant selects door; Winning door selected
        selectedDoor = random.choice(allDoors)
        winningDoor = random.choice(allDoors)

        ### Closed (unselectable) doors and non-winning door lists filtered
        closedDoors.remove(selectedDoor)
        nonWinningDoors.remove(winningDoor)

        ### Closed doors and non-winners converted to sets
        closedSet = set(tuple(closedDoors))
        nonWinSet = set(tuple(nonWinningDoors))

        ### Opening doors that are neither winners nor the contestant's selection
        ### For more on sets: https://docs.python.org/2/library/sets.html
        doorsToOpen = list(closedSet.intersection(nonWinSet))

        ### Make a list of remaining doors with the contestant's choice and winner
        remainingDoors = copy.copy(closedDoors)
        random.shuffle(doorsToOpen)
        remainingDoors.remove(doorsToOpen[0])

        ### If switch == True, contestant switches door selection.
        ### Otherwise, contestant sticks with selection
        if switch:
            tempDoor = copy.copy(remainingDoors)
            selectedDoor = tempDoor.pop()
        else:
            selectedDoor = selectedDoor

        ### Tally-up points for correct and incorrect selections
        if selectedDoor == winningDoor:
            wins += 1
        elif selectedDoor != winningDoor:
            losses += 1

    winPercent = (wins/(wins+losses))*100
    print('Number of wins: {}\nNumber of losses: {}'.format(wins, losses))
    print('Winning percentage: {:.2f}%'.format(winPercent))
