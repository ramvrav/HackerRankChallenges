'''
Problem 9. Birthday Cake Candles. You are in-charge of the cake for your niece's birthday and have decided the cake 
will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out 
the tallest ones. Your task is to find out how many candles she can successfully blow out.
https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    tall_candle_type=max(ar)
    tall_candles=ar.count(tall_candle_type)
    return(tall_candles)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
