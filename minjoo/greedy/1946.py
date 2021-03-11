import sys

t = int(input())
for _ in range(t):
    n = int(input())
    new = [] # 신입사원
    cnt = 1
    for i in range(n):
        new.append(list(map(int, sys.stdin.readline().strip().split())))

    new = sorted(new, key=lambda x:x[0]) # 서류 성적이 좋은 순으로

    minscore = new[0][1] 
    for i in range(1, n): # 면접 성적 비교
        if(new[i][1] < minscore): # 면접 성적이 더 좋다면
            minscore = new[i][1]
            cnt += 1 # 선발
    print(cnt)
