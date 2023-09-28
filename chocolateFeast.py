'''
Problem 31. Little Bobby loves chocolate. He frequently goes to his favorite 5 & 10 store, Penny Auntie, to buy them. 
They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate. 
He has 15 to spend, bars cost 3, and he can turn in 2 wrappers to receive another bar. Initially, he buys 5 bars and has 
5 wrappers after eating them. He turns in 4 of them, leaving him with 1, for 2 more bars. After eating those two, he has 3 
wrappers, turns in 2 leaving him with 1 wrapper and his new bar. Once he eats that one, he has wrappers and turns them in 
for another bar. After eating that one, he only has 1 wrapper, and his feast ends. Overall, he has eaten 5+2+1+1=9 bars.
https://www.hackerrank.com/challenges/chocolate-feast/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    # Calculate the initial number of chocolates Bobby can buy
    chocolates_bought = n // c
    wrappers = chocolates_bought
    
    total_chocolates = chocolates_bought
    
    # Continue as long as Bobby has enough wrappers to exchange for more chocolates
    while wrappers >= m:
        # Calculate the number of chocolates he can get from wrappers
        chocolates_from_wrappers = wrappers // m
        
        # Update the total number of chocolates
        total_chocolates += chocolates_from_wrappers
        
        # Calculate the remaining wrappers after exchanging
        remaining_wrappers = wrappers % m
        
        # Calculate the new total number of wrappers
        wrappers = chocolates_from_wrappers + remaining_wrappers
    
    return total_chocolates

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])
        result = chocolateFeast(n, c, m)
        fptr.write(str(result) + '\n')
    fptr.close()
