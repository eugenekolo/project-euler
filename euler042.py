#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 42
# Coded triangle numbers
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# http://projecteuler.net/problem=42
################################################################################
def solve():
    # This problem is really bruteforceable, as 16K text is nothing, a word is probably only up to len ~25 too
    # this means you only need to calculate up to t_n > 26*~25
    # No point in over optimizing this, but we'll do some small optimizations and try to keep this general
    # without making too many assumptions

    wordsFile = open('./assets/words.txt','r')
    words = wordsFile.read()
    wordsFile.close()
    words = words.split(',') # Separate the words into a list
    words = [word.strip('"') for word in words] # Strip the leading and trailing "

    # Precompute the t_n list up to the longest word in the file
    triNums = []; n = 1
    while (int(.5*n*(n+1)) < 26*len(max(words, key=len))): # Longest word might just be all Z's for max value
        triNums.append(int(.5*n*(n+1)))
        n += 1

    # Compute the value of each word and check if it's a triNum
    count = 0
    for word in words:
       value = 0 
       for i in range(0,len(word)):
           value += ord(word[i])-64 # UTF8 offset by 64 for English words
       if (value in triNums):
           count += 1

    return count

if __name__ == '__main__':
    print(solve())


