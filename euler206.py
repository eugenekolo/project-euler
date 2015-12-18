#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 206
# Concealed Square
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each "_" is a single digit.
################################################################################
def solve():
    from math import sqrt
    # Get the maximum and minimum number that can be squared to be of the form
    # Round the max and min to the nearest 10 as only a multiple of 10 can be squared and end in 0 
    minNum = int(round(int(sqrt(1020304050607080900)),-1))
    maxNum = int(round(int(sqrt(1929394959697989990)),-1))

    # Search the range for a number whose square has the form
    for num in xrange(maxNum, minNum, -10):
        square = str(num**2)
        if square[2] == '2' and square[4] == '3' and square[6] == '4' and square[8] == '5' and square[10] == '6' and square[12] == '7' and square[14] == '8' and square[16] == '9':
            return num

if __name__ == '__main__':
    print(solve())
