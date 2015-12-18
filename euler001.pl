#!/usr/bin/perl
################################################################################
# Euler 1
# Multiples of 3 and 5
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 
# 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
################################################################################

use strict;

my $sum = 0;
foreach my $num (3...999) {
    if ($num % 3 == 0 || $num % 5 == 0) {
        $sum += $num;
    }
}
print "$sum\n";
