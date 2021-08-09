import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(now):
    if now in state:
        return
    state.append(now)
    if now[0] == 0:
        result.append(now[2])
    if now[0]:
        # a->b
        water = min(now[0], b-now[1])
        dfs([now[0]-water, now[1]+water, now[2]])
        # a->c
        water = min(now[0], c-now[2])
        dfs([now[0]-water, now[1], now[2]+water])
    if now[1]:
        # b->a
        water = min(now[1], a-now[0])
        dfs([now[0]+water, now[1]-water, now[2]])
        # b->c
        water = min(now[1], c-now[2])
        dfs([now[0], now[1]-water, now[2]+water])
    if now[2]:
        # c->a
        water = min(now[2], a-now[0])
        dfs([now[0]+water, now[1], now[2]-water])
        # c->b
        water = min(now[2], b-now[1])
        dfs([now[0], now[1]+water, now[2]-water])


a, b, c = map(int, input().split())
result = []  # 결과
state = []  # 물의양 상태 저장하는 배열
dfs([0, 0, c])

for i in sorted(result):
    print(i, end=' ')
