'''
Problem 19. Day of the Programmer. Marie invented a Time Machine and wants to test it by time-traveling to visit Russia 
on the Day of the Programmer (the 256th day of the year) during a year in the inclusive range from 1700 to 2700.
From 1700 to 2700, Russia's official calendar was the Julian calendar;since 1919 they used the Gregorian calendar 
system. The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 
31st was February 14th. This means that in 1918, February 14th was the 32nd day of the year in Russia. In both calendar 
systems, February is the only month with a variable amount of days; it has 29 days during a leap year, and 28 days 
during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years 
are either of the following: Divisible by 400 or Divisible by 4 and not divisible by 100.Given a year y, find the date 
of the 256th day of that year according to the official Russian calendar during that year. Then print it in the format 
dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is y.
https://www.hackerrank.com/challenges/day-of-the-programmer/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(year):
    if year == 1918:
        return('26.09.{}'.format(year))
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return('12.09.{}'.format(year))
    else:
        return('13.09.{}'.format(year))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input())
    result = solve(year)
    fptr.write(result + '\n')
    fptr.close()
