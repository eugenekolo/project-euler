#!/usr/bin/perl
################################################################################
# Euler 7
# 10001st prime
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
################################################################################

use strict;
use POSIX;
use Eulerlib; 

my $number = 0;
my $nthPrime = 10001;
my $numOfPrimes = 0;
while ($numOfPrimes != $nthPrime) {
    $number++;
    if (Eulerlib::isPrime($number)) {
        $numOfPrimes++;
    }
}
print "${nthPrime}th Prime = $number\n";



