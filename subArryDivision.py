'''
Problem 16. Subarray Division. Lily has a chocolate bar that she wants to share it with Ron for his birthday. 
Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the 
length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. 
You must determine how many ways she can divide the chocolate.
https://www.hackerrank.com/challenges/the-birthday-bar/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s, d, m):
    count = 0
    for index in range(len(s)-m+1):
        count += int(sum(s[index:index+m]) == d)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = list(map(int, input().rstrip().split()))
    dm = input().split()
    d = int(dm[0])
    m = int(dm[1])
    result = solve(s, d, m)
    fptr.write(str(result) + '\n')
    fptr.close()
