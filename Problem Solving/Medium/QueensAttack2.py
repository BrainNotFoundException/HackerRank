#!/bin/python3

import os

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    
    numsq=0
    
    s1=False
    s2=False
    s3=False
    s4=False
    rup=False
    rdown=False
    cright=False
    cleft=False
    d=0
    shortestrup=n
    shortestrdown=n
    shortestcleft=n
    shortestcright=n
    shortests1=n
    shortests2=n
    shortests3=n
    shortests4=n
    
    for i in obstacles:
        r = i[0]
        c = i[1]
        
        if r == r_q:
            d=c-c_q
            
            if d>0:
                if shortestcright>d:
                    shortestcright=d
                cright=True
            
            else:
                if shortestcleft>abs(d):
                    shortestcleft=abs(d)
                cleft=True
        
        elif c == c_q:
            d=r-r_q
            
            if d>0:
                if shortestrup>d:
                    shortestrup=d
                rup=True
            
            else:
                if shortestrdown>abs(d):
                    shortestrdown=abs(d)
                rdown=True
        
        elif abs(r-r_q)==abs(c-c_q):
            rd = r-r_q
            cd = c-c_q
            
            if rd>0 and cd<0:
                if shortests1>rd:
                    shortests1=rd
                s1=True
            
            elif rd>0 and cd>0:
                if shortests2>rd:
                    shortests2=rd
                s2=True
            
            elif rd<0 and cd>0:
                if shortests3>cd:
                    shortests3=cd
                s3=True
            
            elif rd<0 and cd<0:
                if shortests4>abs(cd):
                    shortests4=abs(cd)
                s4=True
            
    
    if not rdown:
        numsq+=r_q-1
    else:
        numsq+=shortestrdown-1
    
    if not rup:
        numsq+=n-r_q
    else:
        numsq+=shortestrup-1
    
    if not cleft:
        numsq+=c_q-1
    else:
        numsq+=shortestcleft-1
    
    if not cright:
        numsq+=n-c_q
    else:
        numsq+=shortestcright-1
    
    if not s1:
        
        if n-r_q<c_q-1:
            numsq+=n-r_q
        
        else:
            numsq+=c_q-1
    else:
        numsq+=shortests1-1
    
    if not s2:
        
        if n-r_q< n-c_q:
            numsq+=n-r_q
        
        else:
            numsq+=n-c_q
    else:
        numsq+=shortests2-1
    
    if not s3:
        
        if r_q-1<n-c_q:
            numsq+=r_q-1
        
        else:
            numsq+=n-c_q
    else:
        numsq+=shortests3-1
    if not s4:
        
        if r_q-1<c_q-1:
            numsq+=r_q-1
        
        else:
            numsq+=c_q-1
    else:
        numsq+=shortests4-1
    
    return numsq
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
