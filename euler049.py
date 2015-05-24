#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 49
# Prime permutations
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
# but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
################################################################################
def solve():
    import itertools
    from eulerlib import isPrime

    # Bruteforce approach:
    # 1. Choose a 1st term, check if it's prime, else test next term
    # 2. Get the permutations of the 1st term
    # 3. Choose an arithmetic add
    # 4. Check if 2nd and 3rd terms are prime, else test next add
    # 5. Check if their permutations, print solution
    for i in range(1001,3333,2):
        if not isPrime(i): continue
        # Get the permutations of the 1st number in the arirthmetic sequence
        perms = itertools.permutations(str(i), 4)
        perms = list(perms)
        for k in range(len(perms)):
            perms[k] = ''.join(perms[k])
        for j in range(2,3333,2):
            if not isPrime(i+j) or not isPrime(i+2*j): continue
            if ((str(i+j) in perms) and (str(i+2*j) in perms)):
                print(str(i) + " " + str(i+j) + " " + str(i+2*j) + " Are permutations")

if __name__ == '__main__':
    print(solve())

