#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 48
# Self powers
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
################################################################################
def solve():
    # Simplest code, no optimization, pure bruteforce and use of infinite nums in python
    sum = 0;
    for i in range(1,1000):
        sum += i**i;
    return sum % (10**10);

if __name__ == '__main__':
    print(solve())
