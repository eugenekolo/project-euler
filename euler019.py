#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# Euler 19
# Counting Sundays
# Author: Eugene Kolo - 2014
# Contact: www.eugenekolo.com

# You are given the following information, but you may prefer to do some research for yourself.
# http://projecteuler.net/problem=19
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
################################################################################

# Check if input year is a leap year
def isLeapYear(year):
    if (year % 4 == 0 and ((year % 400 == 0) or (year % 100 != 0)) ): return True
    return False

def solve():
    firstOfTheMonth = [1] # 1 Jan 1900 was a Monday
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Magic lists!
    # Generate day of the 1st of the month for year 1900
    for month in range(1,12):
        firstOfTheMonth.append( (firstOfTheMonth[month-1] + daysInMonth[month-1])%7 )

    year = 1901
    sundays = 0
    while (year < 2001):  
        # Check if previous year was a leap year or if current year is a leap year and shift 1 extra accordingly
        if isLeapYear(year-1):
            for month in range(0,2):
                firstOfTheMonth[month] = (1+firstOfTheMonth[month]) % 7
        elif isLeapYear(year):
            for month in range(2,12):
                firstOfTheMonth[month] = (1+firstOfTheMonth[month]) % 7
        # Check by 1 for every month
        for month in range(0,12):
            firstOfTheMonth[month] = (1 + firstOfTheMonth[month]) % 7
        # Count the number of sundays on the 1st of the month
        for month in range(0,12):
            if (firstOfTheMonth[month] == 0):
                sundays += 1
        year += 1

    return sundays


if __name__ == '__main__':
    print(solve())

