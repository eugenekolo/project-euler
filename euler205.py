#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 205
# Dice Game
# Author: Eugene Kolo 2014
# Contact: www.eugenekolo.com

# Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
# Peter and Colin roll their dice and compare totals: the highest total wins. The result 
# is a draw if the totals are equal.
# What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded 
# to seven decimal places in the form 0.abcdefg
################################################################################
def solve():
    from itertools import product

    # Get all permutations of: 6 sided die rolled 6 times
    # and a 4 sided die rolled 9 times
    cList = list(product('123456',repeat=6)) # 6**6 combos
    pList = list(product('1234',repeat=9)) # 4**9 combos
    total = len(cList) * len(pList) # Total amount of combos

    # bin[i] = number of combos that add up to i, max sum(i) = [6*6,4*9] respectively
    cBins = [0 for x in range(0,6*6+1)]
    pBins = [0 for x in range(0,4*9+1)]

    # Create 2 histograms of colin's and pete's probabilities
    for i in range(0,len(cList)):
        # Convert list of strings into list of nums, then sum up and increment the bin count
        cBins[sum(map(int, cList[i]))] += 1
    for i in range(0,len(pList)):
        # Convert list of strings into list of nums, then sum up and increment the bin count
        pBins[sum(map(int, pList[i]))] += 1
        
    # Add up the number of games that pete wins in
    pWins = 0
    for p in range(0,len(pBins)):
        for colin in cBins[:p]: # Any dice roll less than the sum of pBins[p] is a pWin
            pWins += pBins[p]*colin
                    
    return round(float(pWins)/float(total),7)
    
if __name__ == '__main__':
    print(solve())
