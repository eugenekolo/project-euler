#!/usr/bin/perl

# http://projecteuler.net/problem=152

use strict;

my $prevN = 1/2;

my $test = &sumAtoB(2,80);
print "$test\n";

sub sumAtoB() {
    my $A = shift;
    my $B = shift;
    my $sum = 0;
    foreach my $i ($A..$B) {
        $sum = $sum + (1/$i**2);
    }
    return $sum;
}
