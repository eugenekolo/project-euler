/*******************************************************************************
// Euler 17
// Number letter counts
// Author: Eugene Kolo - 2014
// Contact: www.eugenekolo.com

// If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
// If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
*******************************************************************************/

#include <iostream>
#include <cmath>

int main() { 
    int sum = 0;
    int tempSum = 0;
    // Number of letters found in each i-1'th for each digits place: e.g. ones[5](five) = 4
    int hundreds[] = {0, 10, 10, 12, 11, 11, 10, 12, 12, 11}; // Additional +7 added for the word "hundred"
    int tens[] = {0, 0, 6, 6, 5, 5, 5, 7, 6, 6}; // 00, and 10, are set to 0 to avoid double counting with teens[]
    int teens[] = {3, 6, 6, 8, 8, 7, 7, 9, 8, 8}; // This is for the special cases of 10(ten),11(eleven)...19(nineteen)
    int ones[] = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4};
  
    for (int i = 1; i <= 1000; i++) {
        // Get the digit of each digits place
        int hundredsPlace = floor((i%1000)/100);
        int tensPlace = floor((i%100)/10);
        int onesPlace = floor(i%10);
        tempSum = 0;
        if (tensPlace >= 2 || tensPlace == 0) { // x2-9x or x0x
            tempSum = hundreds[hundredsPlace] + tens[tensPlace] + ones[onesPlace];
        }
        else { // x1x
            tempSum = hundreds[hundredsPlace] + teens[onesPlace];
        }
        
        if (hundredsPlace > 0 && (onesPlace > 0 || tensPlace > 0)) {
            tempSum += 3; // add 3 for "and"
        }
        sum += tempSum;
    }
    std::cout << sum + 11 << std::endl; // 11 for "one thousand"
    
    return 0;
}
