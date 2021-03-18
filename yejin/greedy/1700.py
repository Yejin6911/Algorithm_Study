import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
stocks = list(map(int, sys.stdin.readline().rstrip().split()))

plug = []
cnt = 0
max_index = 0
change = 0

for i in range(K):
    now = stocks[i]
    if now in plug:
        continue
    elif len(plug) < N:
        plug.append(stocks[i])
        continue
    else:
        for p in plug:
            # 이후에 다시 사용되지 않는 용품이 있는 경우
            if p not in stocks[i:]:
                change = p
                break
            # 이후에 사용되는 경우 - 가장 나중에 사용되는 용품을 선택
            elif stocks[i:].index(p) > max_index:
                max_index = stocks[i:].index(p)
                change = p
        plug[plug.index(change)] = now
        max_index = 0
        change = 0
        cnt += 1

print(cnt)
