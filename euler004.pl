#!/usr/bin/perl
################################################################################
# Euler 4
# Largest palindrome product
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#################################################################################

use strict;

my $max = 0;

# Check if the product of every number from 100..999 * 100..999 is a palindrome and compare to the last max
foreach my $firstNum (100..999) {
    foreach my $secondNum (100..999) {
        my $product = $firstNum * $secondNum; 
        if ($product eq (reverse $product)) { # A palindrome is defined as $foo == reverse($foo)
            if ($max < $product) {
                $max = $product;
            }
        }
    }
}

print "Max palindrome = $max\n";

