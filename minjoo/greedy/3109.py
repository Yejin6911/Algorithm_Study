import sys

r, c = map(int, sys.stdin.readline().split())
road = []
direc = [[-1, 1], [0, 1], [1, 1]] # 오른쪽위, 오른쪽, 오른쪽아래
for _ in range(r):
    road.append(list(sys.stdin.readline().replace("\n","")))

def search(x, y):
    road[x][y] = 'x' # 시작점에 파이프 설치
    if(y == c-1): # 빵집에 도달했으면 True
        return True

    for i in range(3):
        xx = x + direc[i][0]
        yy = y + direc[i][1]
        if(0<= xx < r and 0<= yy < c): # 범위 체크
            if(road[xx][yy] == '.'): # 길이 있으면
                if(search(xx, yy)): 
                    return True
    return False 
    #             break
    # if(xx == -1 and yy == -1):
    #     return [-1, -1]
    # else:
    #     # print("xx, yy", xx, yy)
    #     return [xx, yy]

answer = 0
for i in range(r):
    if(search(i, 0)):
        answer += 1
    #     # print("catch")
    #     x, y = i, 0
    #     while(y < c-1 and x < r-1):
    #         x, y = search(x, y)
    #         if(x == -1 and y == -1):
    #             break
    # if(y == (c-1)):
    #     # print("x,y", x, y)
    #     answer += 1
print(answer)


