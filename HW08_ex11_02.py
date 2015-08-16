#!/usr/bin/env python
# Exercise 2  
# Dictionaries have a method called get that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value; 
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
##############################################################################

# Imports

# Body

def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    print d

def histogram_new(s):
    d = {}
    for c in s:
        d[c] = d.get(c,0) + 1
    return d
    

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    with open('pledge.txt', 'r') as fin:
        lines = fin.read()
        s = ''.join(c for c in lines if c not in ('.',';',':',','))  
        pledge_list = s.split()
        return pledge_list

##############################################################################
def main():  # DO NOT CHANGE BELOW
    print histogram_new(get_pledge_list())

if __name__ == '__main__':
    main()
