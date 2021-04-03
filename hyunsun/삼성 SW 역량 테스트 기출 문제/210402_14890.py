n, l = map(int, input().split())
m=[]
for i in range(n):
    m.append(list(map(int, input().split())))

def check(line):
    not_empty = [False for i in range(n)]
    for i in range(n-1):
        if line[i] == line[i+1]:
            continue
        elif line[i] == line[i+1] + 1: #내려가기
            current = line[i+1] #주의
            for j in range(1,1+l):
                if 0 <= i+j < n: #범위 체크
                    if line[i+j] != current: return False #높이 불만족
                    if not_empty[i+j] == True: return False #이미 경사로 있음
                    not_empty[i+j] = True
                else:#범위 넘어가면 불가능한 것
                    return False
            #for j in range(1,1+l):
            #    not_empty[i+j] = True
        elif line[i] == line[i+1] - 1: #올라가기
            current = line[i]
            for j in range(l):
                if 0 <= i-j < n: #범위 체크
                    if line[i-j] != current: return False #높이 불만족
                    if not_empty[i-j] == True: return False #이미 경사로 있음
                    not_empty[i+j] = True
                else:#범위 넘어가면 불가능한 것
                    return False
            #for j in range(l):
            #    not_empty[i-j] = True
        else:#높이 2이상 차이
            return False
    return True

cnt = 0
for i in m: #가로 길 체크
    if check(i):
        cnt += 1
for i in range(n): # 세로 길 체크
    line = []
    for j in range(n):
        line.append(m[j][i])
    if check(line):
        cnt += 1
print(cnt)
