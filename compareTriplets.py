'''
Problem 3. Compare the Triplets. The function compareTriplets must return an array of two integers, the first being 
Alice's score and the second being Bob's.
https://www.hackerrank.com/challenges/compare-the-triplets/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    cntra=0
    cntrb=0
    for values in range(3):
        if a[values]>b[values]:
            cntra+=1
        elif a[values]<b[values]:
            cntrb+=1
    return('{}{}'.format(cntra,cntrb))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
