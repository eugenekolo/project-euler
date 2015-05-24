#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 32
# Pandigital products
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity 
# can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
################################################################################
def solve():
    import itertools

    # Simple bruteforce by placing a multiplicand and multiplier 
    # Some optimizations for impossible products, kind of slow at ~8s
    # [TODO] Speed up

    perms = list(itertools.permutations("123456789")) # All 1 through 9 pandigitals
    total = 0
    products = {} # Keep track of what products were already added
    for perm in perms:
        for i in range(1,8): # Place the multiplicand
            multiplicand = int("".join(perm[:i]))
            if (multiplicand > int("".join(perm[i+1:]))): # Impossible product
                break
            for j in range(i+1,9): # Place the multiplier
                multiplier = int("".join(perm[i:j]))
                product = int("".join(perm[j:])) # Place the product
                ourProd = multiplicand * multiplier
                if (ourProd > product): # Impossible product
                    break
                if (ourProd == product and product not in products):
                    total += product
                    products[product] = True

    return total        

if __name__ == '__main__':
    print(solve())
 
