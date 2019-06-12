# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# -- Find the sum of all the multiples of 3 or 5 below 1000 --
import numpy as np
import math
import sys

#np.set_printoptions(suppress=True, precision=0, threshold=sys.maxsize)
def get_multiples(n=1000, lcd_list=[3,5]):
    # multiply 3 and 5 by 1,2,3,4....n/3 or n/5
    multiples_each_lcd = np.array([])
    for lcd in lcd_list:
        highest_cd = np.floor(n/lcd)

        multiples_lcd = np.dot(np.arange(start=1, stop=(highest_cd+1), step=1), lcd)
        multiples_each_lcd = np.append(multiples_each_lcd, multiples_lcd)
    unique = np.unique(multiples_each_lcd)
    if unique[-1] == n:
        unique = np.delete(unique, -1)

    return unique

def get_multiples_simple(n=1000, lcd_list=[3,5]):


    lcd_array = np.array(lcd_list)
    #notice range is 1,n since its up to but not including N !
    return [x for x in range(1,n) if True in (np.mod(x,lcd_array) == 0)]

print(np.add.reduce(get_multiples()))
print(np.add.reduce(get_multiples_simple()))