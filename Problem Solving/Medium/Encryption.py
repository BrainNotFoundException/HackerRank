#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    s=s.replace(' ', '')
    x=len(s)
    ncols=math.ceil(math.sqrt(x))
    out=''
    for i in range(0, ncols):
        out+=s[i::ncols]+' '
    
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
