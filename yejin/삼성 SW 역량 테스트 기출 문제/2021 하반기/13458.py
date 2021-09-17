import sys
import math
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

total = n
# 총감독관 감시 인원 제외
for i in range(n):
    if A[i] <= B:
        A[i] = 0
    else:
        A[i] -= B
    # 부감독관 인원 계산
    total += math.ceil(A[i]/C)
print(total)
