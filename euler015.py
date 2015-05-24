#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 15
# Lattice paths
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# http://projecteuler.net/problem=15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the 
# right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
################################################################################

# Each path to a right-down corner must go down a and right b in a a x b grid
# This is 20+20 for a 20 x 20 grid. 
# Each move has the option of right or down unless prohibited
# This is equivalent to 20+20 choose 20

# Can do this by importing math.factorial, but where's the fun in that?
# 40C20 = (40!)/(20!*20!) = prod(i,40,21)/prod(i,20,1) = prod(i+n/i, 1, 20) 
def solve():
    numer = 1; denom = 1 # Simpler floating point arthimetic 
    for i in range(1,21):
        numer *= i+20;
        denom *= i;
    return(numer/denom)

if __name__ == '__main__':
    print(solve())
