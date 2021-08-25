import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

length = [0 for _ in range(n)]
length[0] = 1

for i in range(1, n):
    for j in range(i):
        # j번쨰 수보다 크고 j번쨰 까지의 부분수열의 길이가 저장 된 부분수열의 길이 보다 긴 경우
        if A[i] > A[j] and length[i] < length[j]:
            length[i] = length[j]
    length[i] += 1

print(max(length))
