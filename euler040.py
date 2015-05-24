#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 40
# Champernowne's constant
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
################################################################################
def solve():
    # Simple concatenation of a string with all positive integers until the length of the string is > 1M
    numstr = "0"
    n = 0
    while (len(numstr) < 1000001):
        n += 1
        numstr += str(n)

    return int(numstr[1]) * int(numstr[10]) * int(numstr[100]) * int(numstr[1000]) * int(numstr[10000]) * int(numstr[100000])*int(numstr[1000000])

if __name__ == '__main__':
    print(solve())
