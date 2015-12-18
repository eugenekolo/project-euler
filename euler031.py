#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 31
# Coin sums
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
################################################################################
def solve():
    coins = (200,100,50,20,10,5,2,1)
    total = 0
    for baseCoin in coins:
        total = baseCoin
        i = 0
        while (total != 200 and i < 8):
            total += coins[i]
            i += 1

if __name__ == '__main__':
    print(solve())



