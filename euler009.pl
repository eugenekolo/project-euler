#!/usr/bin/perl
################################################################################
# Euler 9
# Special Pythagorean triplet
# Author: Eugene Kolo 2014
# Contact: www.eugenekolo.com

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
################################################################################

# a can only go up to 332 if a < b < c
# b can only go from a+1 to 499 if a < b < c
foreach my $a (1..332) {
    foreach my $b ($a+1.. 499) {
        my $c = 1000 - $a - $b;
        if ( ($a + $b + $c) != 1000) { # Numbers have to add up to 1000
            next;
        }
        if ( ($a**2 + $b**2) == $c**2) { # Numbers have to follow a^2+b^2=c^2
            print "$a + $b + $c = 1000\n";
            print "$a^2 + $b^2 = $c^2\n";
            print "$a*$b*$c = " . $a*$b*$c . "\n";
        }
    }
}
