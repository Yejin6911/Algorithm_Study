import sys

S = sys.stdin.readline().rstrip()
cnt_0 = 0
cnt_1 = 0

start = S[0]
temp = 1
index = 1
# 0이 연속되는 부분과 1이 연속되는 부분의 개수를 세준다.
while True:
    if index == len(S):
        if start == '0':
            cnt_0 += 1
        else:
            cnt_1 += 1
        break
    if S[index] == start:
        temp += 1
    else:
        if start == '0':
            cnt_0 += 1
        else:
            cnt_1 += 1
        start = S[index]
        temp = 1
    index += 1

# 최솟값 출력
result = min(cnt_0, cnt_1)
print(result)


# 간단 풀이 2
cnt = 0
for i in range(len(S)-1):
    # 숫자가 바뀌는 부분의 개수를 세준다.
    if S[i] != S[i+1]:
        cnt += 1
print((cnt+1)//2)
