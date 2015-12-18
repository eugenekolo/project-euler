#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 27
# Quadratic primes
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# http://projecteuler.net/problem=27
################################################################################
def solve():
    import eulerlib

    # Maximization of consecutive primes from the quadratic: n^2 + an + b
    # Where |a| < 1000 and |b| < 1000 and n starts at 0
    maxab = 0
    maxprimes = 0
    bPrimes = eulerlib.PrimeSieve(1000)
    for a in range(-999,1000,2): # a must be odd to satisify n = 1 case (1+a+b=prime)
        for b in bPrimes: # b must be pos prime to satisfiy n = 0 case (0+0+b=prime)
            n = 0
            while eulerlib.isPrime(n**2 + a*n + b):
                n += 1
            if (n > maxprimes):
                maxprimes = n
                maxab = a*b

    return maxab

if __name__ == '__main__':
    print(solve())
