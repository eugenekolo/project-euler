#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 38
# Pandigital multiples
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# http://projecteuler.net/problem=38
################################################################################

def solve():
    # Simple bruteforce concatenated product pandigital number
    # Can optimize this a bit by limiting the ranges down, but this is fast enough at <1s
    import eulerlib
    maxProd = 0
    for n in range(1,10000):
        for i in range(1,10):
            concatProd = eulerlib.concatProd(n, range(1,i+1))
            if (len(str(concatProd)) == 9 and eulerlib.isPanDig(concatProd) and concatProd > maxProd):
                maxProd = concatProd

    return maxProd

if __name__ == '__main__':
    print(solve())
