'''
Problem30. Cut the sticks. You are given a number of sticks of varying lengths. You will iteratively cut the sticks into 
smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length 
of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that 
shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.
https://www.hackerrank.com/challenges/cut-the-sticks/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    result = []
    
    while arr:
        # Append the number of remaining sticks to the result list
        result.append(len(arr))

        # Find the length of the shortest stick
        min_length = min(arr)

        # Cut each stick and discard the pieces of the shortest length
        arr = [stick - min_length for stick in arr if stick > min_length]

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
