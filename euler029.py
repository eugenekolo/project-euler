#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 29
# Distinct powers
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# http://projecteuler.net/problem=29
################################################################################

def solve():
    # Really simple problem about just keeping a history of previously discovered terms
    d = {}
    for a in range(2,101):
        for b in range(2,101):
            d[a**b] = True

    return(len(d.keys()))
        
if __name__ == '__main__':
    print(solve())
