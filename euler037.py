#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 37
# Truncatable primes
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# The number 3797 has an interesting property. Being prime itself, it is possible 
# to continuously remove digits from left to right, and remain prime at each stage: 
# 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
################################################################################

# Can view this problem as an "appendable primes" problem instead
# The MSD (Most Significant Digit) and LSD (Least Significant Digit) of a number must both be prime
# for the number to be able to truncate left and right and produce primes
# The numbers in between must be able to form primes going left and going right from the MSD and LSD

import eulerlib

def isTruncPrime(num):
    num = str(num)
    if len(num) < 2: # 2,3,5,7 are not considered to be truncatable primes
        return False
    for i in range(0,len(num)): # Truncate left to right
        if (not eulerlib.isPrime(int(num[i:]))):
            return False
    for i in range(1,len(num)): # Truncate right to left
        if (not eulerlib.isPrime(int(num[:i]))):
            return False
    return True

def solve():
    total = 0
    for num in range(1000000):
        if isTruncPrime(num):
            total += num

    return total

if __name__ == '__main__':
    print(solve())
