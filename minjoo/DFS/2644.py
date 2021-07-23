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
ans = 0

def dfs(a, b):
    global visited, ans
    visited[a] = 1
    for i in range(len(dic[a])):
        if(dic[a][i] == b):
            ans += 1
            return ans
        if(dic[a][i] in dic.keys() and visited[dic[a][i]] == 0):
            ans += 1
            dfs(dic[a][i], b)
    return -1

print(dfs(a, b))

# 푸는중