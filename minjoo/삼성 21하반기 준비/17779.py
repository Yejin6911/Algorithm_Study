import sys
input = sys.stdin.readline

n = int(input())
board = []
board.insert(0, [0 for _ in range(n+1)])

for _ in range(n):
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    board.append(arr)

def solution(x, y, d1, d2):
    population = [0 for _ in range(5)]
    visited = [[0] * (n+1) for _ in range(n+1)]

    for i in range(d1+1):
        visited[x+i][y-i] = 5
        visited[x+d2+i][y+d2-i] = 5

    for i in range(d2+1):
        visited[x+i][y+i] = 5
        visited[x+d1+i][y-d1+i] = 5

    for i in range(n+1):
        if(visited[i].count(5) > 1):
            flag = 0
            for j in range(n+1):
                if(flag == 0 and visited[i][j] == 5):
                    flag = 1
                elif(flag == 1 and visited[i][j] != 5):
                    visited[i][j] = 5
                elif(flag == 1 and visited[i][j] == 5):
                    break

    for r in range(1, x+d1+1):
        for c in range(1, y+1):
            if(visited[r][c] != 5):
                visited[r][c] = 1

    for r in range(1, x+d2+1):
        for c in range(y+1, n+1):
            if(visited[r][c] != 5):
                visited[r][c] = 2

    for r in range(x+d1, n+1):
        for c in range(1, y-d1+d2+1):
            if(visited[r][c] != 5):
                visited[r][c] = 3

    for r in range(x+d2+1, n+1):
        for c in range(y-d1+d2, n+1):
            if(visited[r][c] != 5):
                visited[r][c] = 4
    for i in range(1, n+1):
        for j in range(1, n+1):
            population[visited[i][j] - 1] += board[i][j]

    return max(population) - min(population)

ans = sys.maxsize
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if(1 < x+d1+d2 <= n and 1 <= y-d1 < y and y < y+d2 <= n):
                    temp = solution(x, y, d1, d2)
                    ans = min(ans, temp)

print(ans)