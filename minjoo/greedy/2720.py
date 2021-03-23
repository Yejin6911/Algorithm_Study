import sys

t = int(sys.stdin.readline()) # 테스트 케이스
m = [25, 10, 5, 1]
for _ in range(t):
    c = int(sys.stdin.readline()) # 거스름돈
    result = []
    for i in range(4):
        q = c // m[i]
        result.append(q)
        if(q > 0):
            c = c % m[i]
    for i in range(4):
        print(result[i], end=' ')
    print("")

