#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Commonly used functions for Euler Project (www.projecteuler.com)
# Author: Eugene Kolo 2014
# Contact: www.eugenekolo.com
################################################################################

import math, sys, os
from collections import defaultdict

# Simple prime check for number n
def isPrime(n):
    if n == 2 or n == 3: return True # 2 or 3
    if n < 2 or n%2 == 0: return False # 1, negative or even
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0: 
            return False
    return True

# Sieve of Eratosthenes, finds prime #s up to n in O(nloglogn)
def PrimeSieve(n):
    # Assume [0,n) are all primes
    primes = [True for i in range(0,n)]
    for i in range(2,int(math.ceil(math.sqrt(n)))):
        if primes[i] is True:
            a = 0
            while (i**2 + a*i < n): # Remove every multiple of i
                primes[i**2 + a*i] = False
                a += 1

    return [i for i in range(2,n) if primes[i] is True]

# Return the nth fibonacci number
def fib(n):
    counter = 2 # Start at fib(2) as F_1 = 1, F_2 = 1
    last, cur = 1,1
    while(counter < n):
        tmpcur = cur
        cur = cur + last
        last = tmpcur
        counter += 1
    return cur

# Output the next power of 10 of log10(n) (2->10, 82->100, 255->1000)
# [TODO] Optimize in some bit twiddling and basic integer math instead?
def next10(n):
    return 10**int(math.ceil(math.log(n,10)))

# Sum of the proper divisiors of n
def sumDivisors(n):
    total = 1 # n always has at least the pal '1' as a divisor
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            # Add the divisor pair, except only 1 of a perfect square
            if (i != n/i):
                total += (i + n/i) 
            else:
                total += i
    return total

# Check if input string is a palindrome
def isPalindrome(string):
    for i in range(0,len(string)//2):
        if (string[i] != string[len(string)-1-i]):
            return False
    return True

# Concatenated product of n and mylist
# n = 192, mylist = [1 2 3], output = '192'+'384'+'576' = 192384576
def concatProd(n, mylist):
    prods = [n * i for i in mylist]
    return int("".join([str(prod) for prod in prods]))

# Returns True if n is a pandigital number
def isPanDig(n):
    n = str(n)
    if (len(n) <= 9 and len(n) > 0): # Number must be 1 to 9 digits long
        for i in range(1,len(n)+1): # Range of all the digits
            if n.find(str(i)) == -1: # Digit not found
                return False
    else: 
        return False
    return True

# Returns a dictionary of factors->amount
# n = 644 -> {(2,2),(7,1),(23,1)}
def factor(n):
    d = defaultdict(int)
    # Make n odd and get rid of the prime 2's
    while n%2 == 0:
        n = n/2
        d[2] += 1
    # Factor n down by trial divison
    # This works because once an odd divisor is found, it must be prime 
    # otherwise a previous one would have already occured
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0: 
            n = n/i
            d[i] +=1 
    # n is prime
    if (n > 2):
        d[n] += 1

    return d

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

#[TODO] Make this a singleton
class stdoutToggle:
    actualstdout = sys.stdout
    def on(self):
        sys.stdout = self.actualstdout
    def off(self):
        sys.stdout = open(os.devnull,'w')



