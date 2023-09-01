'''
Problem 2. Simple Array Sum. Given an array of integers, find the sum of its elements.
https://www.hackerrank.com/challenges/simple-array-sum/problem
'''
#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    results=0
    for xvalues in ar:
        results+=xvalues
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    
    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
