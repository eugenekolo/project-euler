################################################################################
# Commonly used functions for Euler Project (www.projecteuler.com)
# Author: Eugene Kolo 2014
# Contact: www.eugenekolo.com
################################################################################

package Eulerlib;
use strict;
use POSIX;

# Simple trial division bruteforce prime checker
sub isPrime {
    my $num = shift;
    if ($num == 2 || $num ==3) {return 1;} # 2 or 3
    if ($num < 2 || $num % 2 == 0) {return 0;} # 1, negative, or even
    for (my $i = 3; $i < sqrt($num)+1; $i += 2) {
        if ($num % $i == 0) {
            return 0;
        }
    }
    return 1;
}

# Return the nth fibonacci number
# [TODO] Could use some optimization
# Starts at F_1 = 1, F_1 = 2
sub fib {
    my $n = shift;
    my $counter = 2; # Start at fib(2) as F_1 = 1, F_2 = 1
    my @sum = (1,1);
    my $nth = 0;
    while ($counter < $n) {
        $nth = $sum[1] + $sum[0];
        @sum[0] = @sum[1];
        @sum[1] = $nth;
        $counter += 1;
    }
    return $sum[1];
}
1;
