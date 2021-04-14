def diffuse():
    for i in range(r):
        for j in range(c):
            if rooms[i][j] > 0:\
                cnt = 0 # 방향마다 확산 수 세기
                for k in range(4): #방향
                    x, y = i+dx[k], j+dy[k]
                    if not(0<=x<r and 0<=y<c): continue # 범위밖
                    if (x,y) == (air[0],0): continue #공청
                    if (x,y) == (air[1],0): continue #공청
                    cnt += 1 #드디어 확산 가능
                    rooms2[x][y] = rooms2[x][y] + rooms[i][j] // 5 #확산 옆에 추가
                rooms2[i][j] = rooms[i][j] + rooms2[i][j] - (rooms[i][j] // 5) * cnt #확산한 만큼 나한테서 차감 #괄호 주의


def clean():
    #공기청정기로 먼저 없어지는 애를 먼저
    # 위 반시계
    for i in range(air[0]-2,-1,-1):#옮기는 애 기준 # 식에서 우항 기존
        rooms2[i+1][0] = rooms2[i][0]
    for i in range(1,c):
        rooms2[0][i-1] = rooms2[0][i]
    for i in range(1, air[0]+1): #air[0]까지
        rooms2[i-1][-1] = rooms2[i][-1]
    for i in range(c-2, 0, -1):
        rooms2[air[0]][i+1] = rooms2[air[0]][i]
    rooms2[air[0]][1] = 0 #clean 바람
    # 아래 시계
    for i in range(air[1]+2, r):
        rooms2[i-1][0] = rooms2[i][0]
    for i in range(1, c):
        rooms2[-1][i-1] = rooms2[-1][i]
    for i in range(r-2, air[1]-1, -1):
        rooms2[i+1][-1] = rooms2[i][-1]
    for i in range(c-2, 0, -1):
        rooms2[air[1]][i+1] = rooms2[air[1]][i]
    rooms2[air[1]][1] = 0 #clean 바람


r, c, t = map(int, input().split())
rooms = [ list(map(int, input().split())) for _ in range(r)]

# 공청 위치
air = []
for i in range(r):
    if rooms[i][0] == -1:
        air.append(i)
        
#서 동 북 남
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

#한번 이동시 마다의 temp
rooms2 = [[0]*c for _ in range(r)]

#한번 실행 - room2
diffuse()
clean()

# t-1번 시행
for i in range(t-1):
    rooms = rooms2.copy()
    rooms2 = [[0]*c for _ in range(r)]
    diffuse()
    clean()
        
# 결과
res = 0
for i in range(r):
    for j in range(c):
            res = res + rooms2[i][j]
            #print([rooms2[i][j]], end = '')
    #print('')
print(res)
