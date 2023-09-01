'''
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the 
number of times she breaks her season record for most points and least points in a game. Points scored in the first 
game establish her record for the season, and she begins counting from there. 
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    cntrHighScore,cntrLowScore = 0,0
    HighScore,LowScore = scores[0],scores[0]
    for score in scores:
        if score > HighScore:
            HighScore=score
            cntrHighScore+=1
        elif score < LowScore:
            LowScore=score
            cntrLowScore+=1
    return(cntrHighScore,cntrLowScore)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
