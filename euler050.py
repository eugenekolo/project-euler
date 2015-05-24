#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 50
# Consecutive prime sum
# Author: Eugene Kolo 2014
# Contact: www.eugenekolo.com

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
################################################################################

def solve():
    import math
    from eulerlib import isPrime

    pList = [2]
    pSums = [2]
    LIMIT = 1000000

    # Get some primes and sum them consecutively
    i = 1 # Keep track of the index of pSums
    num = 3 # Keep track of the prime number
    add = 0 
    while (add + num < LIMIT):
        if isPrime(num):
            pList.append(num)
            add = pSums[i-1] + num
            pSums.append(add)
            i += 1
        num += 2

    # Find the max consecutive sum starting from each prime
    maxAdds = 0; maxNum = 0
    endLen = len(pSums)
    pSums.reverse() # Flip the list
    for prime in pList:
        for add in pSums[:endLen]:
            # Summing from the current prime consecutively,
            # this add is the max prime you can get
            if isPrime(add):
                maxNum = add
                maxAdds = len(pList[pList.index(prime):])-pSums.index(add)
                endLen = pSums.index(add) # New prime starts must be able to beat the current maxAdds
                break
            pSums[pSums.index(add)] -= prime # Subtract prime from each sum to get the sums starting from the next prime
        # Break if maxAdds is at it's highest possible
        if maxAdds > len(pList[pList.index(prime):]):
            break

    return maxAdds

if __name__ == '__main__':
    print(solve())
