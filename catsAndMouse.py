'''
Problem 25. Two cats and a mouse are at various positions on a line. You will be given their starting positions. 
Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at 
equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.
You are given q queries in the form of x, y, and z representing the respective positions for cats A and B, and for 
mouse C. Complete the function to return the appropriate answer to each query, which will be printed on a new line. 
If cat catches the mouse first, print Cat A. If cat catches the mouse first, print Cat B. If both cats reach the mouse 
at the same time, print Mouse C as the two cats fight and mouse escapes.
https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    catA = abs(x-z)
    catB = abs(y-z)
    if (catA < catB):
        return "Cat A"
    elif (catB < catA):
        return "Cat B"
    else:
        return "Mouse C"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        fptr.write(result + '\n')
    fptr.close()
