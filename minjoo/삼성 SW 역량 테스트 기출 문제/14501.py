import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
day = []
money = []
for _ in range(n):
    d, m = map(int, input().split())
    day.append(d)
    money.append(m)

if(day[0] > n):
    temp = [[0]]
else:
    temp = [[0], [1]]
temp_complete = []
idx = 0

def decision(temp):
    global n
    while(temp):
        t = temp.pop()
        if(len(t) == n):
            temp_complete.append(t)
            continue

        if(t[-1] == 1): # 이전에 넣은게 1이면
            for _ in range(day[len(t)-1]-1):
                if(len(t) == n):
                    break
                t.append(0) # 0 넣어주기
    
        if(len(t) == n): # 길이체크
            temp.append(t)
            continue

        a = n - len(t)
        if(day[len(t)] > a):
            t.append(0)
            temp.append(t)
        else:
            tx, ty = deepcopy(t), deepcopy(t)
            tx.append(1)
            temp.append(tx)
            ty.append(0)
            temp.append(ty)
        
decision(temp)

result = 0
for i in range(len(temp_complete)):
    benefit = 0
    for j in range(n):
        benefit += temp_complete[i][j] * money[j]
    if(result < benefit):
        result = benefit

print(result)


        
    


