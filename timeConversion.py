'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
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
