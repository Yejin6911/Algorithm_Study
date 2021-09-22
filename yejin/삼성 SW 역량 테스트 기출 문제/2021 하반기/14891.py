import sys
import copy
input = sys.stdin.readline


# 회전
def spin(gear, dir):
    new_gear = []
    # 시계방향
    if dir == 1:
        for i in range(-1, 7):
            new_gear.append(gear[i])
    # 반시계방향
    else:
        for i in range(1, 9):
            new_gear.append(gear[i % 8])
    return new_gear


def calculate(gears):
    total = 0
    for i in range(4):
        total += 2**i*int(gears[i][0])
    return total


# 톱니바퀴
gears = [list(map(int, list(input().rstrip()))) for _ in range(4)]
k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    num -= 1
    new_gears = copy.deepcopy(gears)
    new_gears[num] = spin(gears[num], dir)

    # 왼쪽부분 고려:
    l_idx = num-1
    l_dir = -dir
    l_check = gears[num][6]
    while l_idx >= 0:
        # 서로 다른 극일 때
        if gears[l_idx][2] != l_check:
            new_gears[l_idx] = spin(gears[l_idx], l_dir)
            l_check = gears[l_idx][6]
            l_dir = -l_dir
            l_idx -= 1
        # 같은 극일 때
        else:
            for i in range(0, l_idx+1):
                new_gears[i] = gears[i]
            break
    # 오른쪽 부분 고려
    r_idx = num+1
    r_dir = -dir
    r_check = gears[num][2]
    while r_idx <= 3:
        # 서로 다른 극일 때
        if gears[r_idx][6] != r_check:
            new_gears[r_idx] = spin(gears[r_idx], r_dir)
            r_check = gears[r_idx][2]
            r_dir = -r_dir
            r_idx += 1
        # 같은 극일 때
        else:
            for i in range(r_idx, 4):
                new_gears[i] = gears[i]
            break
    gears = new_gears

print(calculate(gears))
