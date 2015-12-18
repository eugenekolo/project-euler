#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 36
# Double-base palindromes
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
################################################################################

def solve():
    from eulerlib import isPalindrome
    total = 0
    for num in range(1,1000000):
        # Strip the 0b from the binary string
        if (isPalindrome(str(num)) and isPalindrome(bin(num).replace("0b",""))):
            total += num
    return total

if __name__ == '__main__':
    print(solve())
