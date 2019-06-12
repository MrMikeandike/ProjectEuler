"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import numpy as np
import time
from datetime import timedelta
#param
n = 600851475143
n = 13195
def check_prime(k):
    print('checking if prime', k)
    beginning = time.time()
    #for i in
    for i in gen_all(np.floor_divide(k, 2)):
        if k % i == 0:
            future = time.time()
            print(f"did not find prime {k} in {(future - beginning) / 60} minutes")
            return False
    future = time.time()
    print(f"found prime {k} in {(future - beginning)/60} minutes")
    return True


def gen_all(max_i):
    i = 2
    while i <= max_i:
        yield i
        i += 1


def gen_odd(max_i):
    # note: we are excluding 1 here.
    if max_i % 2 == 0:
        i = max_i - 1
    else:
        i = max_i
    while i >= 3:
        yield i
        i -= 2

def gen_prime_2(to_factor=n):
    primes = []
    check = gen_all(np.floor_divide(to_factor,2))
    for num in check:
        for against in gen_all(np.floor_divide(num,2)):

            check_done()

def check_done()




def get_max_prime_factor(n=n):
    # rule out all numbers above n/2 since theres no number small enough to multiply them by to get n
    max_possible = np.floor_divide(n, 2)
    print('check_prime')
    # primes have to be odd so we cant discard all even numbers
    gen_odd_factors = (x for x in gen_odd(max_possible) if n % x == 0)
    print('gen_odd_factors created')
    return [x for x in gen_odd_factors if check_prime(x) is True]


primes = get_max_prime_factor()