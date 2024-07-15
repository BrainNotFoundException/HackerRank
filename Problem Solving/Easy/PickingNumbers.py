#!/bin/python3

import os
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    
    high=0
    for i in a:
        ca=[]
        for j in a:
            if 0<=j-i<=1:
                ca.append(j)
        print(ca)
        if len(ca)>high:
            print(ca)
            high=len(ca)
        
    return high

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
