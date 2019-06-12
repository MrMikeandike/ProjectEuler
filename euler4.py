""" ----- CHALLENGE -----
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

""" ----- SPIT BALLING -----
create generator that gets every palindrome in decending order 
(so if max number is 998001, start at 98989 and iterate down in columns beginning with middle row.
98989, 98889, 98789... 
then outer column
97979, then iterate middle again.

really, we only need half if it -- and then mirror it. check if even number of terms or odd.
the beginning will be unoptimized since if its 998001, you will take 998 as half and iter down and get 998899 and then discard later  
"""
import numpy as np
def get_max_possible_value(digits):
    max_number = int(('9'*digits))**2
    max_str = str(max_number)
    left_half_index = int(np.ceil(len(max_str)/2))
    left_half_start = int(max_str[:left_half_index])
    offset = len(max_str) % 2

    _halfs = range(left_half_start, 0, -1)

    ## test
    to_string = (lambda t: list(str(t)))
    to_flipped = lambda t: np.flip(t)

    halfs = (list(str(x)) for x in _halfs)
    #flipped = (list(np.flip(x)) for x in halfs)


    combined = (int(''.join(x + list(np.flip(x))[offset:])) for x in halfs)
    while(True):
        if combined.__next__() <= max_number:
            break

    options = int(('9'*digits))
    for num in combined:
        for factor in range(options, 0, -1):
            if num % factor == 0:
                return [factor, num/factor, num]
            elif (num/factor) > factor:
                break

    #return combined
get_max_possible_value(3)








