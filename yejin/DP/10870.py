import sys
input = sys.stdin.readline

n = int(input())
result = [0, 1]
for i in range(2, n+1):
    result.append(result[i-1]+result[i-2])

print(result[n])
