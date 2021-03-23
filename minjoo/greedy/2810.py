import sys

n = int(sys.stdin.readline()) # 좌석의 수
line = sys.stdin.readline() # 좌석 배치

direction = 0 # 왼쪽
skip = 0 # 커플석 패스
cnt = 0
for x in line:
    if(skip == 1):
        skip = 0
        direction = 1 # 오른쪽
        continue
    if(direction == 0 and x == 'L'):
        skip = 1
    elif(direction == 1 and x == 'L'):
        cnt += 1
        skip = 1
    else:
        pass

print(n - cnt)