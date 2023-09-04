'''
Problem 8. Mini-Max Sum. Given five positive integers, find the minimum and maximum values that can be calculated 
by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of 
two space-separated long integers.
https://www.hackerrank.com/challenges/mini-max-sum/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum=0
    arr.sort()
    for items in arr:
        sum+=items
    print(sum-arr[len(arr)-1],sum-arr[0])    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
