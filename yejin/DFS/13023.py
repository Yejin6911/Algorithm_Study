import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start, cnt):
    if cnt == 5:
        # 시간초과
        # global check
        # check = True
        print(1)
        sys.exit()
    for i in relation[start]:
        if not checked[i]:
            checked[i] = 1
            dfs(i, cnt+1)
            checked[i] = 0


n, m = map(int, input().split())
relation = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

# check = False
checked = [0 for _ in range(n)]
for i in range(n):
    checked[i] = 1
    dfs(i, 1)
    checked[i] = 0

# if check:
#     print(1)
# else:
#     print(0)
print(0)
