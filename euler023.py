#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 23
# Non-abundant sums
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# http://projecteuler.net/problem=23
################################################################################
def solve():
    from eulerlib import sumDivisors

    LIMIT = 28123
    abundants = []
    # Create a list of all abundant numbers below LIMIT
    for n in range(1,LIMIT+1):
        if (sumDivisors(n) > n):
            abundants.append(n)

    # Get the total of all numbers from 1 to LIMIT
    total = sum(range(1,LIMIT+1))

    # Subtract all abundant sums to get the non-abundant sums (Set theory)
    subs = {} # Make use of a hash for O(1) lookup
    for i in range(0,len(abundants)):
        for j in range(i,len(abundants)):
            mysum = abundants[i] + abundants[j]
            if (mysum > LIMIT):
                break # Every addition past this will be >LIMIT
            if (mysum not in subs): # Not previously subtracted
                total -= mysum
                subs[mysum] = 1
            if (abundants[i] > LIMIT/2): 
                break # Every addition past this will be >LIMIT
    return total

if __name__ == '__main__':
    print(solve())
