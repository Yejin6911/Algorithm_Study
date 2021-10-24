import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split())) # 내구도

belt = [0 for _ in range(2*n)]

def spin():
    global belt, a
    belt = belt[2*n-1:] + belt[:2*n-1] # 벨트 회전
    if(belt[n-1] != 0): # 로봇이 내리는 위치에 있으면
        belt[n-1] = 0 # 로봇 내리기
    a = a[2*n-1:] + a[:2*n-1] # 내구도 회전

def move_robot():
    global belt
    # 맨 마지막 칸 처리
    if(belt[-1] != 0 and belt[0] == 0 and a[0] >= 1):
        belt[-1] = 0
        belt[0] = 1
        a[0] -= 1

    # 2n-2 칸부터 0칸까지
    for i in range(2*n-2, -1, -1):
        if(belt[i] != 0):
            if(belt[i+1] == 0 and a[i+1] >= 1):
                belt[i] = 0
                belt[i+1] = 1
                a[i+1] -= 1
                if(i+1 == n-1): # 내리는 위치에 있으면
                    belt[i+1] = 0 # 로봇 내리기

def up():
    global belt
    if(a[0] != 0):
        belt[0] = 1 # 올리는 위치에 로봇 올리기
        a[0] -= 1

cnt = 0
while(1):
    cnt += 1
    spin()
    move_robot()
    up()
    count = a.count(0)
    if(count >= k):
        print(cnt)
        break
    
