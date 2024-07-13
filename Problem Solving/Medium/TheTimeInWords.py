#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    s=''
    numbas = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
        'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six',
        'twenty seven', 'twenty eight', 'twenty nine', 'thirty']

    if m ==0:
        s = numbas[h-1]+ ' o\' clock'
    elif m<=30:
        if m==15:
            s='quarter past '+numbas[h-1]
        elif m==30:
            s = 'half past '+numbas[h-1]
        else:
            if m==1:
                s=numbas[m-1]+' minute past '+ numbas[h-1]
            else:
                s=numbas[m-1]+' minutes past '+ numbas[h-1]
    elif m>30:
        if m==45:
            s='quarter to '+numbas[h]
        else:
            s=numbas[59-m]+ ' minutes to '+numbas[h]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
