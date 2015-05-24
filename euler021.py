#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 21
# Amicable numbers
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b 
# are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
################################################################################

def solve():
    from eulerlib import sumDivisors
    total = 0
    for n in range(1,10000):
        # Definition of an amicable number
        if (n == sumDivisors(sumDivisors(n)) and sumDivisors(n) != n):
            total += n
            
    return total

if __name__ == '__main__':
    solve()
