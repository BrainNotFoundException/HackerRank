#!/bin/python3

import os

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    length = len(A)
    width = len(A[0])
    sarea = 0
    
    for i in range(length):
        for j in range(width):
            up=i-1
            left=j-1
            
            if up>=0:
                sarea+= abs(A[i][j]-A[up][j])
            else:
                sarea+=A[i][j]
            if left>=0:
                sarea+= abs(A[i][j]-A[i][left])
            else:
                sarea+=A[i][j]
            
            if i==length-1:
                sarea+=A[i][j]
            if j==width-1:
                sarea+=A[i][j]
            
            if A[i][j]>0:
                sarea+=2
                
            
    return sarea

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
        
    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
