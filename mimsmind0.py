# usage: python mimsmind0.py [length]
# In this version, the program generates a random number with number of digits equal to length. 
# If the command line argument length is not provided, the default value is 1. Then, the program 
# prompts the user to type in a guess, informing the user of the number of digits expected. The 
# program will then read the user input, and provide basic feedback to the user. If the guess is 
# correct, the program will print a congratulatory message with the number of guesses made and 
# terminate the game. Otherwise, the program will print a message asking the user to guess a higher 
# or lower number, and prompt the user to type in the next guess.

###################################################################################################


# Import
from sys import exit
from sys import argv
import random

# Code
def random_with_N_digits(a):
    """this function takes an argument of a integer and returns a random integer
    with length of a. Function will be called in mimsmind1 with a as passed from
    the command line"""
    range_start = 10**(a-1)
    range_end = (10**a)-1
    return random.randint(range_start, range_end)

def mimsmind0():
    if not len(argv) > 1:
        command_line = 1 # if nothing is passed from the command line, len(argv)
    # will be less than 1, therefore the default value will be 1.
    else:
        command_line = argv[1]
    digits = int(command_line)
    n = 1
    r = random_with_N_digits(digits) # calling the function defined above and
    # passing the value as entered from the command line as the argument. If
    # nothing was entered from the command line, the default of 3 will be passed.
    print "Let's play the mimsmind0 game."
    print "Guess a " + str(command_line) + "-digit number: "
    while True:
        next = raw_input("> ")
        try:
            next == int(next)
            if int(next) == r:
                print "Congratulations. You guessed the correct number in " + str(n) + " tries."
                return
            if int(next) < r:
                print "Try again. Guess a higher number:"
            if int(next) > r:
                print "Try again. Guess a lower number:"
        except: 
            print "Try again. Enter a real number:"
        n = n + 1




# Main
def main():
    # Start the game
    mimsmind0()

if __name__ == '__main__':
    main()

