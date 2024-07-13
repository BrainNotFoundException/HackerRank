#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    
    finalranks = []
    newranked=[ranked[0]]
    
    for i in range(1, len(ranked)):
        
        if not ranked[i]==ranked[i-1]:
            newranked.append(ranked[i])
    
    c = len(newranked)-1
    for i in player:
        found=False
        for j in range(c, -1, -1):
            if newranked[j]>i:
                found=True
                print('>', i)
                finalranks.append(j+2)
                c=j
                break
            elif newranked[j]==i:
                found=True
                print('==', i)
                finalranks.append(j+1)
                c=j
                break
        if not found:
            finalranks.append(1)
        found=False
    
    return finalranks

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
