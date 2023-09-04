'''
Problem 6. Plus Minus. Given an array of integers, calculate the fractions of its elements that are positive, 
negative, and are zeros. Print the decimal value of each fraction on a new line.
https://www.hackerrank.com/challenges/plus-minus/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    arrDimension=len(arr)
    count_negatives = len(list(filter(lambda x: x < 0, arr)))
    count_positives = len(list(filter(lambda x: x >0, arr)))
    count_zeros = len(list(filter(lambda x: x == 0, arr)))
    
    print(round(count_positives/arrDimension,6))
    print(round(count_negatives/arrDimension,6))
    print(round(count_zeros/arrDimension,6))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
