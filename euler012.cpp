/*******************************************************************************
// Euler 12
// Highly divisible triangular number
// Author: Eugene Kolo - 2014
// Contact: www.eugenekolo.com

// http://projecteuler.net/problem=12
*******************************************************************************/

#include <iostream>
#include <cmath> 

int main () { 
    int nth = 1;
    int triNum = 0;
    int numOfDivisors = 0;
    while (numOfDivisors <= 500) {
        numOfDivisors = 0;
        // nth triNum = (n-1)th triNum + n, meaning: 7th triNum = 6th triNum + 7
        triNum = triNum + nth; 
        for (int i = 2; i <= floor(sqrt(triNum)); i++) {
            if (triNum % i == 0) {
                numOfDivisors = numOfDivisors + 2;
            }
        }
        numOfDivisors = numOfDivisors + 2; // Account for (1,triNum) divisor pair
        nth++;
    }
    std::cout << triNum << std::endl;
    return 0;
}
    
