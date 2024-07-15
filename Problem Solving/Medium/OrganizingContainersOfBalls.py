#!/bin/python3

import os

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    
    balls=[0]*len(container)
    contsizes=[0]*len(container)
    
    
    for i in range(len(container)):
        currentcontainer=container[i]
        for j in range(len(currentcontainer)):
            balls[j]+=currentcontainer[j]
        for j in currentcontainer:
            contsizes[i]+=j
    balls.sort()
    contsizes.sort()
    
    if balls==contsizes:
        return 'Possible'
    else:
        return 'Impossible'
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
