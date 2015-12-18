#!/usr/bin/perl
################################################################################
# Euler 6
# Sum square difference
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
################################################################################

use strict;

my $sumOfNums = 0;
my $sumOfSquares = 0;
foreach my $num (1..100) {
    $sumOfNums = $sumOfNums + $num;
    $sumOfSquares += $num**2;
}
my $squareOfSOM = $sumOfNums**2;
my $difference = $squareOfSOM - $sumOfSquares;
print "$difference\n";
    
