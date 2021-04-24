import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))
B = [0 for _ in range(n*2)]

robot = 1
stage = 1
while True:
    # 벨트가 한 칸 회전한다.
    temp_A = A.pop()
    A = [temp_A] + A
    temp_B = B.pop()
    B = [temp_B] + B
    # 내려가는 위치에 로봇 있는 경우
    if B[n-1] > 0:
        B[n-1] = 0
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    for i in range(n-2, -1, -1):
        if B[i] != 0 and B[i+1] == 0 and A[i+1] >= 1:
            B[i], B[i+1] = 0, B[i]
            A[i+1] -= 1
    # 내려가는 위치에 로봇 있는 경우
    B[n-1] = 0
    # 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if B[0] == 0 and A[0] > 0:
        B[0] = robot
        A[0] -= 1
        robot += 1
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if A.count(0) >= k:
        break
    stage += 1

print(stage)
