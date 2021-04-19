# python3 시간초과 안나는 코드
# deque의 rotate 이용!!!

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*n)
res = 0

while 1:
    belt.rotate(1) # 시계방향으로 1칸 회전// -1일 경우 반시계 방향
    robot.rotate(1)
    robot[-1]=0 # 마지막 로봇 내리기
    if sum(robot): # 로봇이 있으면
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1:
                robot[i+1] = 1 
                robot[i] = 0 
                belt[i+1] -= 1
        robot[-1]=0
    if robot[0] == 0 and belt[0]>=1: # 로봇 올리기
        robot[0] = 1 
        belt[0] -= 1 
    res += 1 
    if belt.count(0) >= k: 
        break
        
print(res)




# pypy로 제출
# import sys
# from collections import deque
# input = sys.stdin.readline

# n, k = map(int, input().split()) # 벨트 길이, 내구도 0인 칸의 개수 제한
# belt = list(map(int, input().split())) # 벨트 내구도 (0 ~ 2n-1) 
# q = deque()
# for i in range(len(belt)):
#     q.append([belt[i], 0]) # [벨트 내구도, 로봇 유무]
# belt = q

# def four(belt):
#     zero = 0
#     for i in range(len(belt)):
#         if(belt[i][0] == 0):
#             zero += 1
#         if(zero >= k):
#             return True
#     return False

# cnt = 0
# while(1):
#     cnt += 1

#     belt.appendleft(belt[-1])
#     belt.pop()
#     if(belt[n-1][1] == 1):
#         belt[n-1][1] = 0 # 로봇 내리기
    
#     for i in range(n-2, -1, -1):
#         if(belt[i][1] == 1):
#             if(belt[i+1][1] == 0 and belt[i+1][0] >= 1): # 다음 칸이 비어있고 내구도 1 이상이면
#                 belt[i][1] = 0
#                 belt[i+1][1] = 1 # 로봇 이동
#                 belt[i+1][0] -= 1 # 내구도 감소
#     if(belt[n-1][1] == 1):
#         belt[n-1][1] = 0
    
#     if(belt[0][1] == 0 and belt[0][0] >= 1):
#         belt[0][1] = 1 # 로봇 올리기
#         belt[0][0] -= 1 # 내구도 감소

#     if(four(belt)):
#         print(cnt)
#         break