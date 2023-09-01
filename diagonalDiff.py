'''
Problem 5. Diagonal Difference. Given a square matrix, calculate the absolute difference between the sums of 
its diagonals.
https://www.hackerrank.com/challenges/diagonal-difference/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(a):
    matrixDimension=len(a)
    primaryDiagonalSum = sum(a[i][i] for i in range(matrixDimension))
    secondaryDiagonalSum = sum(a[i][matrixDimension-i-1] for i in range(matrixDimension))
    return abs(primaryDiagonalSum - secondaryDiagonalSum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()
