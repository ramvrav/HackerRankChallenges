'''
Problem 28. Find digit. An integer d is a divisor of an integer n if the remainder of n/d=0. Given an integer, 
for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring 
within the integer.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    # Convert the integer to a string to iterate through its digits
    num_str = str(n)
    
    # Initialize a variable to count divisors
    divisor_count = 0
    
    # Iterate through the digits
    for digit_char in num_str:
        digit = int(digit_char)
        
        # Check if the digit is a divisor of n and not equal to zero
        if digit != 0 and n % digit == 0:
            divisor_count += 1
    
    return divisor_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
