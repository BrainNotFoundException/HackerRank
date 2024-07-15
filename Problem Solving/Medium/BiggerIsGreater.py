#!/bin/python3

import os

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    
    s='no answer'
    found = False
    
    for i in range(len(w)-2, -1, -1):
        
        for j in range(len(w)-1, i, -1):
            
            if w[i]<w[j]:
                
                found = True
                w=list(w)
                w[i], w[j] = w[j], w[i]
                s= ''.join(w[:i+1])+''.join(sorted(w[i+1:]))
                break
        
        if found:
            break
    
    
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
