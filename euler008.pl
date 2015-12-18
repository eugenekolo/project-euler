#!/usr/bin/perl
################################################################################
# Euler 8
# Largest product in a series
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# Find the greatest product of five consecutive digits in the 1000-digit number.
################################################################################

my $bigNum = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";

my $fivedigs;
my $length = length($bigNum);
my $max = 0;
my $maxdigs;

# Create a bigNum string and substr into it to get individual digits, multiply and track the maximum found so far
foreach my $bigNumIndex (0..$length-1) {
    my $fiveDigits = substr($bigNum, $bigNumIndex, 5);
    my $product = substr($fiveDigits, 0, 1) * substr($fiveDigits, 1, 1) * substr($fiveDigits, 2, 1) * substr($fiveDigits, 3, 1) * substr($fiveDigits, 4, 1);
    if ($product > $max) {
        $maxdigs = $fiveDigits;
        $max = $product;
    }
}
print "$max\n";
