'''
Problem 7. Staircase. Write a program that prints a staircase of size n.
https://www.hackerrank.com/challenges/staircase/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    rows = n - 2
    for stairs in range(1,n):
        print(' ' * rows, '#' * stairs)
        rows -= 1
    print('#' * n)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
