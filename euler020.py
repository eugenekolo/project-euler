#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 20
# Factorial digit sum
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
################################################################################
def solve():
    import math
    fact = str(math.factorial(100)) # Create a string equal to 100!
    fact = bytearray(fact,'utf-8') # Change the string to a bytearray, default encoding is ASCII
    sum = 0
    for i in range(0,len(fact)):
        sum += fact[i]-48 # Numbers offset by 48 in ASCII
    return sum

if __name__ == '__main__':
    print(solve())
