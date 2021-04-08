import sys

input = sys.stdin.readline


# 해당 면 바꾸기
def spin_1(space, direction):
    temp = [[0]*3 for _ in range(3)]
    now = cube[space]
    if direction == '+':
        for i in range(3):
            temp[i][2] = now[0][i]
            temp[i][1] = now[1][i]
            temp[i][0] = now[2][i]
    else:
        for i in range(3):
            temp[i][0] = now[0][2-i]
            temp[i][1] = now[1][2-i]
            temp[i][2] = now[2][2-i]
    return temp


# 0: w, 1:y, 2: r, 3:o, 4: g, 5: b
# 해당 면 이외의 부분 바꾸기
def spin_2(space, direction):
    if space == 'U':
        if direction == '-':
            r = cube[2][0]
            b = cube[5][0]
            o = cube[3][0]
            g = cube[4][0]
            cube[2][0], cube[5][0], cube[3][0], cube[4][0] = g, r, b, o
        else:
            r = cube[2][0]
            b = cube[5][0]
            o = cube[3][0]
            g = cube[4][0]
            cube[2][0], cube[5][0], cube[3][0], cube[4][0] = b, o, g, r
        cube[0] = spin_1(0, direction)
    elif space == 'D':
        if direction == '-':
            r = cube[2][2]
            b = cube[5][2]
            o = cube[3][2]
            g = cube[4][2]
            cube[2][2], cube[5][2], cube[3][2], cube[4][2] = b, o, g, r
        else:
            r = cube[2][2]
            b = cube[5][2]
            o = cube[3][2]
            g = cube[4][2]
            cube[2][2], cube[5][2], cube[3][2], cube[4][2] = g, r, b, o
        cube[1] = spin_1(1, direction)
    elif space == 'F':
        if direction == '-':
            y1, y2, y3 = cube[1][0][0], cube[1][0][1], cube[1][0][2]
            w1, w2, w3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
            b1, b2, b3 = cube[5][0][0], cube[5][1][0], cube[5][2][0]
            g1, g2, g3 = cube[4][0][2], cube[4][1][2], cube[4][2][2]
            cube[1][0][0], cube[1][0][1], cube[1][0][2] = g1, g2, g3
            cube[0][2][0], cube[0][2][1], cube[0][2][2] = b1, b2, b3
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = y3, y2, y1
            cube[4][0][2], cube[4][1][2], cube[4][2][2] = w3, w2, w1
        else:
            y1, y2, y3 = cube[1][0][0], cube[1][0][1], cube[1][0][2]
            w1, w2, w3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
            b1, b2, b3 = cube[5][0][0], cube[5][1][0], cube[5][2][0]
            g1, g2, g3 = cube[4][0][2], cube[4][1][2], cube[4][2][2]
            cube[1][0][0], cube[1][0][1], cube[1][0][2] = b3, b2, b1
            cube[0][2][0], cube[0][2][1], cube[0][2][2] = g3, g2, g1
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = w1, w2, w3
            cube[4][0][2], cube[4][1][2], cube[4][2][2] = y1, y2, y3
        cube[2] = spin_1(2, direction)
    elif space == 'B':
        if direction == '-':
            y1, y2, y3 = cube[1][2][0], cube[1][2][1], cube[1][2][2]
            w1, w2, w3 = cube[0][0][0], cube[0][0][1], cube[0][0][2]
            b1, b2, b3 = cube[5][0][2], cube[5][1][2], cube[5][2][2]
            g1, g2, g3 = cube[4][0][0], cube[4][1][0], cube[4][2][0]
            cube[1][2][0], cube[1][2][1], cube[1][2][2] = b3, b2, b1
            cube[0][0][0], cube[0][0][1], cube[0][0][2] = g3, g2, g1
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = w1, w2, w3
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = y1, y2, y3
        else:
            y1, y2, y3 = cube[1][2][0], cube[1][2][1], cube[1][2][2]
            w1, w2, w3 = cube[0][0][0], cube[0][0][1], cube[0][0][2]
            b1, b2, b3 = cube[5][0][2], cube[5][1][2], cube[5][2][2]
            g1, g2, g3 = cube[4][0][0], cube[4][1][0], cube[4][2][0]
            cube[1][2][0], cube[1][2][1], cube[1][2][2] = g1, g2, g3
            cube[0][0][0], cube[0][0][1], cube[0][0][2] = b1, b2, b3
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = y3, y2, y1
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = w3, w2, w1
        cube[3] = spin_1(3, direction)
    elif space == 'L':
        if direction == '-':
            w1, w2, w3 = cube[0][0][0], cube[0][1][0], cube[0][2][0]
            r1, r2, r3 = cube[2][0][0], cube[2][1][0], cube[2][2][0]
            y1, y2, y3 = cube[1][0][0], cube[1][1][0], cube[1][2][0]
            o1, o2, o3 = cube[3][0][2], cube[3][1][2], cube[3][2][2]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = r1, r2, r3
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = y1, y2, y3
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = o3, o2, o1
            cube[3][0][2], cube[3][1][2], cube[3][2][2] = w3, w2, w1
        else:
            w1, w2, w3 = cube[0][0][0], cube[0][1][0], cube[0][2][0]
            r1, r2, r3 = cube[2][0][0], cube[2][1][0], cube[2][2][0]
            y1, y2, y3 = cube[1][0][0], cube[1][1][0], cube[1][2][0]
            o1, o2, o3 = cube[3][0][2], cube[3][1][2], cube[3][2][2]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = o3, o2, o1
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = w1, w2, w3
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = r1, r2, r3
            cube[3][0][2], cube[3][1][2], cube[3][2][2] = y3, y2, y1
        cube[4] = spin_1(4, direction)
    else:
        if direction == '-':
            w1, w2, w3 = cube[0][0][2], cube[0][1][2], cube[0][2][2]
            r1, r2, r3 = cube[2][0][2], cube[2][1][2], cube[2][2][2]
            y1, y2, y3 = cube[1][0][2], cube[1][1][2], cube[1][2][2]
            o1, o2, o3 = cube[3][0][0], cube[3][1][0], cube[3][2][0]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = o3, o2, o1
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = w1, w2, w3
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = r1, r2, r3
            cube[3][0][0], cube[3][1][0], cube[3][2][0] = y3, y2, y1

        else:
            w1, w2, w3 = cube[0][0][2], cube[0][1][2], cube[0][2][2]
            r1, r2, r3 = cube[2][0][2], cube[2][1][2], cube[2][2][2]
            y1, y2, y3 = cube[1][0][2], cube[1][1][2], cube[1][2][2]
            o1, o2, o3 = cube[3][0][0], cube[3][1][0], cube[3][2][0]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = r1, r2, r3
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = y1, y2, y3
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = o3, o2, o1
            cube[3][0][0], cube[3][1][0], cube[3][2][0] = w3, w2, w1
        cube[5] = spin_1(5, direction)


t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    ways = input().rstrip().split()
    cube = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
            [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
            [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
            [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
            [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
            [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]]
    for way in ways:
        spin_2(way[0], way[1])
    for i in range(3):
        for j in range(3):
            print(cube[0][i][j], end='')
        print()
