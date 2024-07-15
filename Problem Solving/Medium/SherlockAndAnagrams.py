#!/bin/python3
import os

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    
    count = 0
    
    for i in range(1, len(s)):
        
        for j in range(0, len(s)):
            
            scomp = sorted(s[j:j+i])
            
            for k in range(j+1, len(s)):
                
                scurrent = sorted(s[k:k+i])
                if scomp==scurrent:
                    count+=1
                
                
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
