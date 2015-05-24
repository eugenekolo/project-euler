#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 35
# Circular primes
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# The number, 197, is called a circular prime because all rotations of the digits: 
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
################################################################################
def solve():
    import itertools
    from eulerlib import isPrime

    # This could be a bit faster, but most of the time is spent in checking if num is a prime or not

    circular = 1 # 2 is prime
    for num in range(3,1000000,2):
        if (isPrime(num)):
            circular += 1 # Assume the prime is circular
            # Make sure every rotation is a prime too
            num = str(num)
            numL = [num[x] for x in range(0,len(num))] # Number represented as a list of digits
            for i in range(0,len(numL)):
                numL.append(numL.pop(0)) # List Rotation
                rot = int("".join(numL)) # Back into a num you go
                if (not isPrime(rot)):
                    circular -= 1 # Nope, we were wrong, this prime isn't circular :(
                    break
    return circular

if __name__ == '__main__':
    print(solve())
