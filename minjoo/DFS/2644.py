import sys

n = int(input()) # 전체 사람의 수
a, b = map(int, input().split())
m = int(input()) # 관계의 개수

dic = {}
for _ in range(m):
    x, y = map(int, input().split())
    if(x in dic.keys()):
        dic[x].append(y)
    else:
        dic[x] = [y]
    if(y in dic.keys()):
        dic[y].append(x)
    else:
        dic[y] = [x]
print(dic)
visited = [0 for _ in range(n+1)]
flag = 0
answer = sys.maxsize
def dfs(a, b, ans):
    global visited, flag, answer
    visited[a] = 1
    if(a == b):
        if(answer > ans):
            answer = ans
            return
    for i in range(len(dic[a])):
        if(dic[a][i] == b):
            ans += 1
            flag = 1
            if(answer > ans):
                answer = ans
                return
        if(dic[a][i] in dic.keys() and visited[dic[a][i]] == 0):
            ans += 1
            dfs(dic[a][i], b, ans)


dfs(a, b, 0)
print(visited)
if(flag == 1):
    print(answer)
else:
    print("-1")

# 푸는중중중