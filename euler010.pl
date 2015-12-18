#!/usr/bin/perl
################################################################################
# Euler 10
# Summation of primes
# Author: Eugene Kolo 2014
# Contact: www.eugenekolo.com

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
################################################################################

use strict;
use POSIX;
use Eulerlib;

my $sum = 0;
my $limit = 2000000;
foreach my $num (1..$limit) {
    if (Eulerlib::isPrime($num)) {
        $sum = $sum + $num;
    }
}
print "$sum\n";
