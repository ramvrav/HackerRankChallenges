'''
Problem 22. There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are 
thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the 
number of the current cloud plus or . The player must avoid the thunderheads. Determine the minimum number of jumps 
it will take to jump from the starting postion to the last cloud. It is always possible to win the game. For each game, 
you will get an array of clouds numbered if they are safe or if they must be avoided.
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    i = 0
    jumpCount = -1
    while i < len(c):
        jumpCount += 1
        if (i < len(c)-2) and (c[i+2] == 0):
            i+=1
        i += 1
    return jumpCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
