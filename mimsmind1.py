# usage: python mimsmind1.py [length]

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

def mimsmind1():
    if not len(argv) > 1: 
        command_line = 3 # if nothing is passed from the command line, len(argv)
    # will be less than 1, therefore the default value will be 3.
    else:
        command_line = argv[1] 
    digits = int(command_line)
    max_rounds = (2**int(command_line) + int(command_line))
    print max_rounds
    n = 1
    r = random_with_N_digits(digits) # calling the function defined above and
    # passing the value as entered from the command line as the argument. If
    # nothing was entered from the command line, the default of 3 will be passed.
    print "Let's play the mimsmind0 game."
    print "You have " + str(max_rounds) + " chances to guess a " + str(command_line) + "-digit number: "
    while n <= max_rounds:
        next = raw_input("> ")
        try:
            next == int(next)
            if int(next) == r:
                print "Congratulations. You guessed the correct number in " + str(n) + " tries."
                return
        except: 
            print "Try again. Enter a real number:"
        n += 1
        for i in range(digits):
            bulls = 0
            cows = 0
            if next[i] == str(r)[i]:
                bulls += 1
            elif next[i] in str(r): 
                cows += 1
            print '  %i Bull(s), %i Cow(s)' % (bulls, cows)
    print "Sorry, you have run out of chances"




# Main
def main():
    # Start the game
    mimsmind1()

if __name__ == '__main__':
    main()
