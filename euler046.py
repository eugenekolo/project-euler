#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 46
# Goldbach's other conjecture
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# It was proposed by Christian Goldbach that every odd composite number can be written 
# as the sum of a prime and twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
################################################################################

import eulerlib
import math

# Can prove the conjecture by assuming it to be true for each number until it's proven false
# n = p + 2*s means that sqrt(s) = sqrt((n-p)/2) must be an integer
primes = [2,3,5,7]; n = 9
conjecture = True
while (conjecture):
    n += 2
    if (not eulerlib.isPrime(n)):
        conjecture = False # Assume the conjecture is false
        # Find the prime p and square s that satisfies the conjecture
        for p in primes: 
            if (math.sqrt((n - p)/2) % 1 == 0):
                conjecture = True
                break
    else:
        primes.append(n)

print(n)
