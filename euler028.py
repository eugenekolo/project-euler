#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 28
# Number spiral diagonals
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
################################################################################
def solve():
    # The sum of the diagonals is the sum of the corners of every layer
    gapSize = 1 # Gap between corners
    corners = 0 # Every layer after the 1st one has 4 corners
    total = 1 # 1st layer's diagonal sum is 1
    gapSinceCorner = 0 # Number of elements since the last corner
    # Sum the corners of every layer by iterating through every element in every layer
    for i in range(1,1001**2+1): # an n by n square has n**2 elements
        if gapSinceCorner == gapSize+1: # A corner is found every gap
            gapSinceCorner = 0
            corners += 1
            total += i
        if corners == 4: # Every layer (4 corners) sees an increase of 2 more elements between corners (gap)
            corners = 0
            gapSize += 2
        gapSinceCorner += 1

    return total

if __name__ == '__main__':
    print(solve())


