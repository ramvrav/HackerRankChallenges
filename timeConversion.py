'''
Problem 10. Time Conversion. Given a time in 12-hour AM/PM format, convert it to military (24-hour) time. 
Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour 
clock, and 12:00:00 on a 24-hour clock.
https://www.hackerrank.com/challenges/time-conversion/problem
'''
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    time_splt=s.split(':')
    time_seconds=time_splt.pop()
    time_splt.append(time_seconds[:2])
    time_splt.append(time_seconds[2:])
    if time_splt[len(time_splt)-1]=='PM' and time_splt[0] != '12':
        time_hour = int(time_splt[0]) + 12
        return('{}:{}:{}'.format(time_hour,time_splt[1],time_splt[2]))
    elif time_splt[len(time_splt)-1]=='AM' and time_splt[0] == '12':
        time_hour = '00'
        return('{}:{}:{}'.format(time_hour,time_splt[1],time_splt[2]))
    else:
        return('{}:{}:{}'.format(time_splt[0],time_splt[1],time_splt[2]))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
