n = int(input()) # 레벨의 수
score = [] # 점수
for _ in range(n):
    score.insert(0, int(input())) # 높은 레벨 순대로

answer = 0
for i in range(n-1):
    if(score[i] <= score[i+1]):
        temp = score[i+1]
        score[i+1] = score[i] - 1 # 이전 레벨의 점수에서 1 빼준 값을 대입
        answer += (temp - score[i+1]) # 차이만큼 정답에 더함

print(answer)