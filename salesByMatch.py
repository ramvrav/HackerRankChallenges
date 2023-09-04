"""
Problem 20. Sales by match. There is a large pile of socks that must be paired by color. Given an array of integers 
representing the color of each sock, determine how many pairs of socks with matching colors there are.
https://www.hackerrank.com/challenges/sock-merchant/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    unique_array_and_count = dict()
    for sock in ar:
        if sock in unique_array_and_count:
            unique_array_and_count[sock] += 1
        else:
            unique_array_and_count[sock] = 1
    
    # Initialize the pair count
    pairs = 0
    
    # Iterate over the unique list
    for sock_count in unique_array_and_count.values():
        # If the count is divisible by 2 then it's a pair,
        # divide it and grab the amount of pairs
        if sock_count % 2 == 0:
            pairs += sock_count // 2
        else:
            # If the count is not divisible by 2 then it has a loose pair,
            # find the remainder after dividing by two and remove it from the sum,
            # then divide it by 2 and grab the actual amount of pairs.
            pairs += (sock_count - sock_count % 2) // 2
    
    return pairs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
