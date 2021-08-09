import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
relation = {}
for _ in range(m):
    a, b = map(int, input().split())
    if(b in relation.keys()):
        relation[b].append(a)
    else:
        relation[b] = [a]

# print(relation)

def dfs(x, cnt):
    global ans
    if(x in relation.keys()):
        cnt += 1
        for i in range(len(relation[x])):
            dfs(relation[x][i], cnt)

    ans = max(ans, cnt)
    


answer = []
maxans = 0
for i in range(1, n+1):
    ans = 0
    dfs(i, 0)
    if(maxans < ans):
        maxans = ans
        answer = [i]
    elif(maxans == ans):
        answer.append(i)

for i in answer:
    print(i, end=' ')
# # print(answer)
# maxans = max(answer)
# for i in range(len(answer)):
#     if(answer[i] == maxans):
#         print(i+1, end=' ')