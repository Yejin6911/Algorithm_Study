n = int(input())
k = int(input())
pos = [[] for _ in range(k)]
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for i in range(k):
    pos[i].append(x[i])
    pos[i].append(y[i])
    
answer = 0
col = [0] * (n+1)

def promising(i, col):
    for k in range(1, i):
        if(col[i] == col[k] or (abs(col[i]-col[k]) == abs(i-k))):
            return False
        if([k, col[k]] in pos):
            return False
        if([i, col[i]] in pos):
            return False
    return True

def check(i, col):
    global answer
    n = len(col) - 1
    if(promising(i, col)):
        if(i == n):
            answer += 1
        else:
            for j in range(1, n+1):
                col[i+1] = j
                check(i+1, col)

check(0, col)
print()
print(answer)
    

