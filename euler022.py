#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 22
# Names scores
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing 
# over five-thousand first names, begin by sorting it into alphabetical order. Then working 
# out the alphabetical value for each name, multiply this value by its alphabetical position 
# in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
################################################################################

# name score = alphabetical sort position * alphabetical value
# COLIN = 938 * 53
def solve():
    names = open('./assets/names.txt', 'r')
    # Strip all '"' from the file, split the names separated by ',' into a list
    namesList = ((names.read()).replace('"', '')).split(',')
    names.close() 
    namesList = sorted(namesList) 
    total = 0
    for name in namesList:
        value = 0
        for i in range(0,len(name)):
            value += ord(name[i])-64 # ASCII names offset by 64
        total += (namesList.index(name)+1) * value

    return total

if __name__ == '__main__':
    print(solve())
