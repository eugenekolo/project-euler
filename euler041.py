#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 41
# Pandigital prime
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# We shall say that an n-digit number is pandigital if it makes use of all the digits 
# 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
################################################################################
def solve():
    import eulerlib
    import itertools

    # Create a base pandigital and examine all permutations to see if any of them are prime and large
    # Can optimize by searching backwards instead (from basePan = 987654321)
    basePan = ""
    panDigMax = 0
    for n in range(1,10):
        basePan += str(n) # Concat the n digit string to the base to create a pandigital
        perms = list(itertools.permutations(basePan)) # All permutations of a pandigital are pandigital
        for perm in perms:
            panDig = int("".join(perm)) # Form an int from the iterable
            if (eulerlib.isPrime(panDig) and panDig > panDigMax):
                panDigMax = panDig

    return panDigMax

if __name__ == '__main__':
    print(solve())
