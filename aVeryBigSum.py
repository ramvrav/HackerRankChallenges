'''
Problem 4. A Very Big Sum. Calculate and print the sum of the elements in an array, keeping in mind that some of 
those integers may be quite large.
https://www.hackerrank.com/challenges/a-very-big-sum/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    results=0
    for values in ar:
        results+=values
    return(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
