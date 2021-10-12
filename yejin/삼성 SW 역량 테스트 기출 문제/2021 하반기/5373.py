import sys
input = sys.stdin.readline


def spin1(side, dir):
    new = [[0]*3 for _ in range(3)]
    now = cube[side]
    if dir == '+':
        for i in range(3):
            new[i][2] = now[0][i]
            new[i][1] = now[1][i]
            new[i][0] = now[2][i]
    else:
        for i in range(3):
            new[i][0] = now[0][2-i]
            new[i][1] = now[1][2-i]
            new[i][2] = now[2][2-i]
    return new


# 0:위 ,1:아래, 2: 앞 3: 뒤, 4:왼, 5:오
def spin2(side, dir):
    if side == 'U':
        if dir == '-':
            cube[2][0], cube[5][0], cube[3][0], cube[4][0] = cube[4][0], cube[2][0], cube[5][0], cube[3][0]
        else:
            cube[2][0], cube[5][0], cube[3][0], cube[4][0] = cube[5][0], cube[3][0], cube[4][0], cube[2][0]
        cube[0] = spin1(0, dir)
    elif side == 'D':
        if dir == '-':
            cube[2][2], cube[5][2], cube[3][2], cube[4][2] = cube[5][2], cube[3][2], cube[4][2], cube[2][2]
        else:
            cube[2][2], cube[5][2], cube[3][2], cube[4][2] = cube[4][2], cube[2][2], cube[5][2], cube[3][2]
        cube[1] = spin1(1, dir)
    elif side == 'F':
        if dir == '-':
            temp1 = [cube[1][0][0], cube[1][0][1], cube[1][0][2]]
            temp2 = [cube[0][2][0], cube[0][2][1], cube[0][2][2]]
            temp3 = [cube[5][0][0], cube[5][1][0], cube[5][2][0]]
            temp4 = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
            cube[1][0][0], cube[1][0][1], cube[1][0][2] = temp4[0], temp4[1], temp4[2]
            cube[0][2][0], cube[0][2][1], cube[0][2][2] = temp3[0], temp1[1], temp3[2]
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = temp1[2], temp1[1], temp1[0]
            cube[4][0][2], cube[4][1][2], cube[4][2][2] = temp2[2], temp2[1], temp2[0]
        else:
            temp1 = [cube[1][0][0], cube[1][0][1], cube[1][0][2]]
            temp2 = [cube[0][2][0], cube[0][2][1], cube[0][2][2]]
            temp3 = [cube[5][0][0], cube[5][1][0], cube[5][2][0]]
            temp4 = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
            cube[1][0][0], cube[1][0][1], cube[1][0][2] = temp3[2], temp1[1], temp3[0]
            cube[0][2][0], cube[0][2][1], cube[0][2][2] = temp4[2], temp4[1], temp4[0]
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = temp2[0], temp2[1], temp2[2]
            cube[4][0][2], cube[4][1][2], cube[4][2][2] = temp1[0], temp1[1], temp1[2]
        cube[2] = spin1(2, dir)
    elif side == 'B':
        if dir == '-':
            temp1 = [cube[1][2][0], cube[1][2][1], cube[1][2][2]]
            temp2 = [cube[0][0][0], cube[0][0][1], cube[0][0][2]]
            temp3 = [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
            temp4 = [cube[4][0][0], cube[4][1][0], cube[4][2][0]]
            cube[1][2][0], cube[1][2][1], cube[1][2][2] = temp3[2], temp3[1], temp3[0]
            cube[0][0][0], cube[0][0][1], cube[0][0][2] = temp4[2], temp4[1], temp4[0]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = temp2[0], temp2[1], temp2[2]
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = temp1[0], temp1[1], temp1[2]
        else:
            temp1 = [cube[1][2][0], cube[1][2][1], cube[1][2][2]]
            temp2 = [cube[0][0][0], cube[0][0][1], cube[0][0][2]]
            temp3 = [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
            temp4 = [cube[4][0][0], cube[4][1][0], cube[4][2][0]]
            cube[1][2][0], cube[1][2][1], cube[1][2][2] = temp4[0], temp4[1], temp4[2]
            cube[0][0][0], cube[0][0][1], cube[0][0][2] = temp3[0], temp3[1], temp3[2]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = temp1[2], temp1[1], temp1[0]
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = temp2[2], temp2[1], temp2[0]
        cube[3] = spin1(3, dir)
    elif side == 'L':
        if dir == '-':
            temp1 = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
            temp2 = [cube[2][0][0], cube[2][1][0], cube[2][2][0]]
            temp3 = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
            temp4 = [cube[3][0][2], cube[3][1][2], cube[3][2][2]]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = temp2[0], temp2[1], temp2[2]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = temp3[0], temp3[1], temp3[2]
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = temp4[2], temp4[1], temp4[0]
            cube[3][0][2], cube[3][1][2], cube[3][2][2] = temp1[2], temp1[1], temp1[0]
        else:
            temp1 = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
            temp2 = [cube[2][0][0], cube[2][1][0], cube[2][2][0]]
            temp3 = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
            temp4 = [cube[3][0][2], cube[3][1][2], cube[3][2][2]]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = temp4[2], temp4[1], temp4[0]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = temp1[0], temp1[1], temp1[2]
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = temp2[0], temp2[1], temp2[2]
            cube[3][0][2], cube[3][1][2], cube[3][2][2] = temp3[2], temp3[1], temp3[0]
        cube[4] = spin1(4, dir)
    else:
        if dir == '-':
            temp1 = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            temp2 = [cube[2][0][2], cube[2][1][2], cube[2][2][2]]
            temp3 = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            temp4 = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = temp4[2], temp4[1], temp4[0]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp1[0], temp1[1], temp1[2]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = temp2[0], temp2[1], temp2[2]
            cube[3][0][0], cube[3][1][0], cube[3][2][0] = temp3[2], temp3[1], temp3[0]

        else:
            temp1 = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            temp2 = [cube[2][0][2], cube[2][1][2], cube[2][2][2]]
            temp3 = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            temp4 = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = temp2[0], temp2[1], temp2[2]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp3[0], temp3[1], temp3[2]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = temp4[2], temp4[1], temp4[0]
            cube[3][0][0], cube[3][1][0], cube[3][2][0] = temp1[2], temp1[1], temp1[0]
        cube[5] = spin1(5, dir)


t = int(input())
for _ in range(t):
    cube = [
        [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
        [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
        [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
        [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
        [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    ]
    n = int(input())
    data = input().split()
    for d in data:
        spin2(d[0], d[1])
    for x in range(3):
        print(*cube[0][x])
