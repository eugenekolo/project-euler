#!/usr/bin/perl
################################################################################
# Euler 3
# Largest prime factor
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
################################################################################

use strict;
use POSIX;
use Eulerlib;

my $multiple = 2;
my $num = 600851475143;
my $maxPrime = 0;

while ($multiple <= sqrt($num)) {
    if ( $num/$multiple == ceil($num/$multiple)) { # $num is evenly divisible by $multiple
        if ( Eulerlib::isPrime($multiple) ) {
            if ($multiple > $maxPrime) {
                $maxPrime = $multiple;
            }
        }
    }
    $multiple++;
}

print "Largest prime factor = $maxPrime\n";
