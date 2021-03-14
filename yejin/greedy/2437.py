# 이해가 어려웠던 문제! 꼭 방법이랑 원리 기억하기!

import sys

N = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()


result = 0
for i in range(N):
    # 현재 새로 사용하려는 추의 무게가 지금까지 사용한 추의 무게의 힙+1한 값보다 작은 경우 사용 가능
    if result+1 < data[i]:
        break
    result += data[i]

print(result+1)
