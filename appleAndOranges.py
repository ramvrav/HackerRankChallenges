'''
Problem 12. Apple and Orange. Complete the countApplesAndOranges function which should print the number of apples 
and oranges that land on Sam's house, each on a separate line.
https://www.hackerrank.com/challenges/apple-and-orange/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    cntrApple, cntrOrange=0,0
    
    for apple in apples:
        location=a+apple
        if location >= s and location <= t:
            cntrApple+=1
    for orange in oranges:
        location=b+orange
        if location>=s and location<=t:
            cntrOrange+=1
    print(cntrApple)
    print(cntrOrange)
  

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
