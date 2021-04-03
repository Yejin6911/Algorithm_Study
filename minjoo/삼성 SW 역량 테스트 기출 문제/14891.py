import sys

input = sys.stdin.readline

gear = [list(map(int, list(input().strip()))) for _ in range(4)]
gear.insert(0, 0)
k = int(input()) # 회전 횟수
r = [list(map(int, input().split())) for _ in range(k)]

def rotation(num, direction): # num번째 톱니바퀴 회전
    global gear
    if(direction == -1): # 반시계 방향
        temp = gear[num].pop(0)
        gear[num].append(temp)
    else: # 시계 방향
        temp = gear[num].pop()
        gear[num].insert(0, temp)

for i in range(k):
    num, direction = r[i]
    left = direction
    right = direction
    action = [0,0,0,0,0] # 회전 방향 저장
    action[num] = direction
    for j in range(num, 1, -1): # num기준 왼쪽 톱니바퀴
        if(gear[j][6] != gear[j-1][2]): # 다른 극이면
            left = left*(-1) # 반대 방향
            action[j-1] = left
        else:
            break
    for j in range(num, 4): # num기준 오른쪽 톱니바퀴
        if(gear[j][2] != gear[j+1][6]): # 다른 극이면
            right = right*(-1) # 반대방향
            action[j+1] = right
        else:
            break
    for a in range(1, 5):
        if(action[a] == 0):
            continue
        rotation(a, action[a]) # 회전

result = 0 # 최종 점수
if(gear[1][0] == 1):
    result += 1
if(gear[2][0] == 1):
    result += 2
if(gear[3][0] == 1):
    result += 4
if(gear[4][0] == 1):
    result += 8

print(result)
