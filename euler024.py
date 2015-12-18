#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 24
# Lexicographic permutations
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible 
# permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically 
# or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
################################################################################

def solve():
    import itertools

    # Extremely easy in python to just get all permutations of a string in lexicographic order.
    perms = list(itertools.permutations("0123456789",10)) # Chap 9.7: Permutations are emitted in lexicographic sort order.
    return int("".join(perms[999999]))

if __name__ == '__main__':
    print(solve())
