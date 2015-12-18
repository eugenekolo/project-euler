#!/usr/bin/perl
################################################################################
# Euler 5
# Smallest multiple
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
################################################################################

use strict;
use POSIX;

my $stepsize = 2*3*5*7*13*17*19; # The number has to be divisible by the prime multiples from 1..20
for (my $num = $stepsize; $num <= 1000000000; $num += $stepsize) {
    foreach my $divisor (1..20) { # TODO: Can remove the primes
        # Check if every dividend is an integer
        if (  ($num/$divisor) != ceil($num/$divisor) ) { # Ceil of an integer should return the integer
            last;
        }
        # If the number passes every divisor check, then you found the #
        if ($divisor == 20) {
            print "$num\n";
            exit;
        }
    }
}

