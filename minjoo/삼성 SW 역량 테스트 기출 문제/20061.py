# blue 좀더 고치기.. 예제 4번부터
import sys
input = sys.stdin.readline

n = int(input()) # 블록을 놓은 횟수
red = [[0]*4 for _ in range(4)]
blue = [[0]*4 for _ in range(6)]
green = [[0]*4 for _ in range(6)]
result = 0

def green_board(t, x, y):
    global green
    if(t == 1):
        for i in range(5, -1, -1):
            if(green[i][y] == 0):
                green[i][y] = 1
                break
    elif(t == 2):
        for i in range(5, -1, -1):
            if(green[i][y] == 0 and green[i][y+1] == 0):
                green[i][y], green[i][y+1] = 1, 1
                break
    elif(t == 3):
        for i in range(5, 0, -1):
            if(green[i][y] == 0 and green[i-1][y] == 0):
                green[i][y], green[i-1][y] = 1, 1
                break

def blue_board(t, x, y):
    global blue
    if(t == 1):
        for i in range(5, -1, -1):
            if(blue[i][x] == 0):
                blue[i][x] = 1
                break
    elif(t == 2):
        for i in range(5, 0, -1):
            if(blue[i][x] == 0 and blue[i-1][x] == 0):
                blue[i][x], blue[i-1][x] = 1, 1
                break
    elif(t == 3):
        for i in range(5, -1, -1):
            if(blue[i][x] == 0 and blue[i][x+1] == 0):
                blue[i][x], blue[i][x+1] = 1, 1
                break

def check1(color): # 가득찬 행/열 처리
    global result
    for i in range(6):
        if(not(0 in color[i])): # 0이 없으면
            result += 1 # 1점 획득
            temp = color[:i]
            color = color[i+1:]
            color = temp + color
            color.insert(0, [0, 0, 0, 0])
    return color

def check2(color): # 연한 칸에 있는 블록 처리
    for i in range(2):
        if(1 in color[i]):
            color.insert(0, [0, 0, 0, 0])
            color.pop()
    return color
            

for _ in range(n):
    t, x, y = map(int, input().split())
    blue_board(t, x, y)
    green_board(t, x, y)
    blue = check1(blue)
    green = check1(green)
    blue = check2(blue)
    green = check2(green)

print(result)
num = 0
for i in range(len(green)):
    num += sum(green[i])
for i in range(len(blue)):
    num += sum(blue[i])
print(num)
print(green)
print(blue)
   
        
