#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 45
# Triangular, pentagonal, and hexagonal
# Author: Eugene Kolo - 2015
# Contact: www.eugenekolo.com
#
# http://projecteuler.net/problem=45
################################################################################

import heapq

def triangle_generator():
    n = 1
    while True:
        t = n * (n + 1) // 2
        yield t
        n += 1


def pentagonal_generator():
    n = 1
    while True:
        p = n * ((3 * n) - 1) // 2
        yield p
        n += 1


def hexagonal_generator():
    n = 1
    while True:
        h = n * ((2 * n) - 1)
        yield h
        n += 1

def solve():
    tg = triangle_generator()
    pg = pentagonal_generator()
    hg = hexagonal_generator()

    count = 0
    last_n = 0
    for n in heapq.merge(tg, pg, hg):
        if n == last_n:
            count += 1
        else:
            count = 1

        if count == 3 and n > 40755:
            return n

        last_n = n

if __name__ == '__main__':
    print(solve())
