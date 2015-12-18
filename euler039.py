#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 39
# Integer right triangles
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
################################################################################
def solve():
    import math

    LIMIT = 1000
    perims = [0 for i in range(0,LIMIT+1)] # List of number of solutions per perimeter
    for a in range(1,int(LIMIT/3)):
        for b in range(a,math.floor((LIMIT-a)/2)):
            c = math.sqrt(a**2 + b**2)
            p = int(a + b + c) # Perimeter 
            if (c % 1 == 0 and p <= LIMIT): # Integer solution 
                perims[p] += 1 # Solution hit

    return perims.index(max(perims)) # Print the index with the highest hits

if __name__ == '__main__':
    print(solve())
