import sys

cnt = 1
while True:
    L, P, V = map(int, sys.stdin.readline().rstrip().split())
    if L == 0 and P == 0 and V == 0:
        break
    Max = L*(V//P)
    # 나머지가 L보다 작으면 해당 일수만큼 더하고
    if V % P < L:
        Max += V % P
    # 나머지가 L보다 크거나 같으면 L만 결과값에 더해준다.
    else:
        Max += L
    print("Case "+str(cnt)+": "+str(Max))
    cnt += 1
