import sys
input = sys.stdin.readline


def dfs(now):
    # 연산자 모두 사용
    if sum(operator) == 0:
        if now not in selected:
            total = A[0]
            for i in range(len(now)):
                if now[i] == 0:
                    total += A[i+1]
                elif now[i] == 1:
                    total -= A[i+1]
                elif now[i] == 2:
                    total *= A[i+1]
                else:
                    if total < 0:
                        temp = (-total)//A[i+1]
                        total = -temp
                    else:
                        total //= A[i+1]
        global M, m
        if total > M:
            M = total
        if total < m:
            m = total
        return
    else:
        for op in range(4):
            if operator[op] != 0:
                operator[op] -= 1
                dfs(now+[op])
                operator[op] += 1


INF = sys.maxsize
n = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))  # [+,-,x,/]
selected = []
M = -INF
m = INF

for op in range(4):
    if operator[op] != 0:
        now = [op]
        operator[op] -= 1
        dfs(now)
        operator[op] += 1

print(M)
print(m)
