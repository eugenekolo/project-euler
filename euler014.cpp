/*******************************************************************************
// Euler 14
// Longest Collatz sequence
// Author: Eugene Kolo - 2014
// Contact: www.eugenekolo.com

// http://projecteuler.net/problem=14
*******************************************************************************/

#include <iostream>

/// Simple bruteforce Solution. 
// Better approach is to keep a log and cache. Meaning, once you get to a # you have already seen, then you already know the size of that chainSize from that starting number and do not need to compute any further
// Meaning: Collatz(10) = 10->5->16->8->4->2->1, Size=7
// Collatz(13) = 13->40->20->10... = 13->40->20->Collatz(10), Size = 3+Collatz(10) 
int main () {
    int startNum = 1000000;
    int chainSize = 0;
    int maxChainSize = 0;
    int maxNum = 0;
    long long num;
    for(long long i = startNum; i > 0; i--) {
        num = i;
        chainSize = 0;
        while(num != 1) {
            if (num % 2 == 0) { // Even
                num = num/2;
            }
            else { // Odd
                num = 3*num + 1;
            }
            chainSize++;
        }
        if (chainSize > maxChainSize) {
            maxChainSize = chainSize;
            maxNum = i;
        }
    }
    std::cout << "maxNum = " << maxNum << " produces a max chain size of " << maxChainSize <<  std::endl;
    return 0;
}
