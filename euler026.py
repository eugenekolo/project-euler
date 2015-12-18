#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 26
# Reciprocal cycles
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# A unit fraction contains 1 in the numerator. The decimal representation of the 
# unit fractions with denominators 2 to 10 are given:
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen 
# that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
################################################################################
def solve():
    import eulerlib

    # The maximum period of cycle is O(10**ceil(log10(n))) (next10)
    # This makes this problem bruteforceable by just keeping a running history of the remainders from long division
    # The iterative function will cycle when it hits a previous long division remainder
    # Evident by working out 1/7 by long divsion
    rems = {}
    maxl = 0; maxd = 0
    for d in range(1,1000):
        rems.clear() # Reset the remainders hash for this d
        index = 0
        rem = eulerlib.next10(d) % d # Long division remainder
        while (rem not in rems):
            rems[rem] = index
            rem = (rem * eulerlib.next10(1000)) % d # Get the next iterated remainder
            index += 1
        l = index - rems[rem] # Period length of the cycle
        if (l > maxl):
            maxd = d
            maxl = l

    return maxd

if __name__ == '__main__':
    print(solve())

