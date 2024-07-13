#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER. 
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    s=0
    b=False
    cv=0
    
    for i in path:
        if i == 'U':
            s+=1
        elif i == 'D':
            s-=1
            
        if s<0:
            if not b:
                b=True
                cv+=1
        if s>=0:
            if b:
                b=False
                
    return cv

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
