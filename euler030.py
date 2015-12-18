#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 30
# Digit fifth powers
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#     1634 = 14 + 64 + 34 + 44
#     8208 = 84 + 24 + 04 + 84
#     9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
################################################################################
def solve():
    # Computes the sum of nth powers of num's digits
    # e.g. 1634,4 = 1**4 + 6**4 + 3**4 + 4**4 = 1634
    def sumOfPowerDigits(num, n):
        total = 0
        while (num > 0):
            total = total + (num % 10)**n
            num //= 10
        return (total)

    # 9^5 = 59049, so the maximum a 5 digit number (99999) can be is 5*9^5 = 295245
    # A 6 digit number can be 6*9^5 = 354294 which is a 6 digit number, whereas
    # a 7 digit number can be 7*9^5 = 413343 which is also a 6 digit number, which means 
    # that a maximum 7 digit number can never add be be the sum of the power digits
    # so our limit is therefore 6*9^5
    return sum([num for num in range(2,6*9**5) if (num==sumOfPowerDigits(num,5))])

if __name__ == '__main__':
    print(solve())
