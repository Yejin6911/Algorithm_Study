import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    row = list(map(int, input().split()))
    data.append(row)

for i in range(1, n):
    for j in range(i+1):
        # 두번째 줄
        if i == 1:
            data[i][j] = data[i-1][0]+data[i][j]
        # 맨 앞 원소
        elif j == 0:
            data[i][j] = data[i-1][j]+data[i][j]
        # 맨 뒷 원소
        elif j == i:
            data[i][j] = data[i-1][j-1]+data[i][j]
        # 나머지
        else:
            data[i][j] = max(data[i-1][j-1]+data[i][j],
                             data[i-1][j]+data[i][j])

print(max(data[-1]))
