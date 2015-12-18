#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 47
# Distinct primes factors
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
################################################################################
import math
import eulerlib

# Find the amount of prime factors for each number and keep track of the consecutive numbers with 4 factors
primes = 0; consec = 0
i = 0
while (True):
    i += 1
    primes = len(eulerlib.factor(i).keys())
    if primes == 4: consec += 1
    else: consec = 0
    if (consec == 4): break

print(i-3) # i is the position of the 4th number, we want the 1st
    
