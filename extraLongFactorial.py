'''
Problem 29. Extra long factorials. Complete the extraLongFactorials function in the editor below. It should print the 
result and return.
https://www.hackerrank.com/challenges/extra-long-factorials/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    result = math.factorial(n)
    print(result)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
