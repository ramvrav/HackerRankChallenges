'''
Problem 18. Migratory Birds. You have been asked to help study the population of birds migrating across the continent. 
Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is 
spotted, its id number will be added to your array of sightings. You would like to b256th) e able to find out which 
type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or 
more types of birds are equally common, choose the type with the smallest ID number.
https://www.hackerrank.com/challenges/migratory-birds/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(ar):
    cntrN, myValue=0,0
    for n in range(1,6):
        if ar.count(n) > cntrN:
            myValue=n
            cntrN=ar.count(n)
    return(myValue)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = migratoryBirds(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
