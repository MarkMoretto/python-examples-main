
"""
Purpose: can't reset variables in while loop. Need to determine whether user input matches calculated solution.
Date created: 2019-04-07
Contributor(s): Mark Moretto


Ref: https://stackoverflow.com/questions/55562119/looping-main-function-while-resetting-variables/55562260#55562260
"""

# Mix it up a little by hiding the user's suggested solution with getpass()
from getpass import getpass

### Set iterator variable to avoid hard-coding the script
max_iterations = 5


def evaluate_expression(first_input, second_input, operator):
    """
        Function to handle arithmetic
    """
    my_solution = 0
    if operator == '+':
        my_solution = first_input + second_input
    elif operator == '-':
        my_solution = first_input - second_input
    elif operator == '/':
        # Can't divide by zero, so we have to handle that.
        if second_input != 0:
            my_solution = first_input / second_input
        else:
            my_solution = 0
    elif operator == '*':
        my_solution = first_input * second_input
    return my_solution
        
def main():

    ### Counters
    correct_guesses = 0
    incorrect_guesses = 0
    try_counter = 1

    while try_counter <= max_iterations:      
        num1 = int(input("Enter First Input: "))
        num2 = int(input("Enter Second Input: "))
        op = str(input("Enter Operator: "))
        UserSolution = int(getpass("Enter Solution: ")) # Hide the input

        ### We van evaluate the expression and return the result to a variable using eval()
        # temp_solution = eval(f'{num1} {op} {num2}')

        ## Traditional evaluation method
        #if op == '+':
        #    my_solution = num1 + num2
        #elif op == '-':
        #    my_solution = num1 - num2
        #elif op == '/':
        #    my_solution = num1 / num2
        #elif op == '*':
        #    my_solution = num1 * num2

        # Call our expression and evaluate the results
        if evaluate_expression(num1, num2, op) == UserSolution:
            print('You\'re correct!')
            correct_guesses += 1
        else:
            print('Incorrect answer!')
            incorrect_guesses += 1

        try_counter += 1
    print(f'Number of correct guesses: {correct_guesses]\nNumber of incorrect guesses: {incorrect_guesses}')
