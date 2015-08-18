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

def bulls_cows(next, r, digits):
    bulls = 0
    cows = 0
    random1 = r
    digits = digits
    # random1 = 456 # test random variable
    # next = '555' # test user chosen string
    next = next
    temp = str(random1) # need to create a temporary variable so that it doesn't check
            # same integer again and say 1 bull, 1 cow for the same integer if 
            # that integer repeats
    for i in range(digits):
        if next[i] == str(random1)[i]:
            bulls += 1
            temp = next.replace(next[i], 'a') # set temporary variable here if integer was already found to be a bull
        else:
            pass
    for i in range(digits):
        # if next[i] in str(r) and next[i] != str(r)[i]: 
        if next[i] in temp and next[i] != temp[i]:# compare to new temp string
        #instead of original user inputted string
            cows += 1
        else:
            pass
    print '  %i Bull(s), %i Cow(s)' % (bulls, cows)

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
        bulls_cows(next, r, digits)
    print "Sorry, you have run out of chances"


# Main
def main():
    # Start the game
    mimsmind1()
    # print bulls_cows()

if __name__ == '__main__':
    main()
