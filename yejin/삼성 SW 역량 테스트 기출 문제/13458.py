import sys

N = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

cnt = N
for i in range(N):
    if data[i] - B >= 0:
        cnt += (data[i]-B)//C
        if (data[i]-B) % C != 0:
            cnt += 1

print(cnt)
