import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split()) # 컨베이어 벨트 길이, 내구도가 0인 칸의 개수 제한
a = deque(map(int, input().split())) # 내구도
belt = deque(0 for _ in range(2*n)) # 컨베이어 벨트

cnt = 0
while(a.count(0) < k):
    cnt += 1
    a.rotate(1)
    belt.rotate(1)

    if(belt[n-1] == 1):
        belt[n-1] = 0
    for i in range(n-2, -1, -1):
        if(belt[i] == 1 and belt[i+1] == 0 and a[i+1] > 0):
            belt[i] = 0
            belt[i+1] = 1
            a[i+1] -= 1 # 내구도 감소
            if(i+1 == n-1): # 내려가는 위치
                belt[i+1] = 0

    if(belt[0] == 0 and a[0] > 0):
        belt[0] = 1
        a[0] -= 1

print(cnt)