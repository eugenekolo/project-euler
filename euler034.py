#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 34
# Digit factorials
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
################################################################################
def solve():
    import math
    # Computes the sum of factorials of num's digits
    # e.g. 145 = 1! + 4! + 5! = 145
    # Can speed this up by cacheing the factorials of 1-9 instead of recomputing each time
    # Although, most time is spent in the division I believe, perhaps remove division by using a table
    def sumOfFactDigits(num):
        total = 0
        while (num > 0):
            total = total + math.factorial(num % 10)
            num //= 10
        return (total)

    # Similar to problem 30, an 8 digit number has a maximum sum of 8*9! which is 
    # only 7 digits and can never equal the 8 digit number
    return(sum([num for num in range(3,7*math.factorial(9)) if (num==sumOfFactDigits(num))]))

if __name__ == '__main__':
    print(solve())
