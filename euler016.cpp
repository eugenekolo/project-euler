/*******************************************************************************
* Euler 16
* Power digit sum
* Author: Eugene Kolo - 2014
* Contact: www.eugenekolo.com
*
* 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
* What is the sum of the digits of the number 21000?
*******************************************************************************/

#include <iostream>
#include "InfInt.h"

// Makes use of the InfInt.h library found at http://code.google.com/p/infint/source/browse/trunk/InfInt.h?r=8
int main() {

  InfInt num = 1;

  // Calculate 2^1000
  for (int i = 1; i <= 1000; i++) {
    num = num*2;
  }
  
  // Add the digits
  int sum = 0;
  for (int i = 0; i <= num.numberOfDigits()-1; i++) {
    sum = sum + num.digitAt(i);
  }
  std::cout << sum << std::endl;
  return 0;
}
