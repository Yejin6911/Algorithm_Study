import sys

input = sys.stdin.readline
inf = 5
result = inf

def check(): # i번 세로선의 결과가 i번인지
    for i in range(1, n+1):
        temp = i
        for j in range(1, h+1):
            if(s[j][temp] == 1):
                temp += 1
            elif(s[j][temp-1] == 1):
                temp -= 1
        if(temp != i):
            return False
    return True

def dfs(num, cnt):
    global result
    if(result != 5): # result가 갱신됐으면 return
        return
    if(num == cnt):
        if(check()):
            result = cnt
        return
    for j in range(1, n):
        for i in range(1, h+1):
            # 좌, 우, 본인 자리에 연결선 없으면
            if(s[i][j-1] == 0 and s[i][j+1] == 0 and s[i][j] == 0):
                s[i][j] = 1 # 연결선 추가
                dfs(num, cnt+1)
                s[i][j] = 0 # 연결선 삭제
                while(i < h):
                    if(s[i][j-1] and s[i][j+1]):
                        break
                    i += 1

n, m, h = map(int, input().split())
s = [[0] * (n+1) for i in range(h+1)]
for i in range(m):
    a, b = map(int, input().split())
    s[a][b] = 1 # 가로선
    
for i in range(4): # 3까지
    dfs(i, 0)
    if(result != inf): # result가 갱신됐으면
        print(result)
        break # 최솟값 찾는거니까 그냥 break
if(result == inf): # result 갱신 안됐으면 -1
    print(-1)
