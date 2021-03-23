import sys

N = int(sys.stdin.readline().rstrip())

# 풀이 1
S = list(sys.stdin.readline().rstrip())
cnt = 0
index = 0
couple = False
# 왼쪽 컵홀더 먼저 사용한다 가정
while index < len(S):
    if S[index] == "S":
        cnt += 1
        index += 1
    else:
        if couple:
            # 두번째 커플부터 오른쪽 컵홀더만 사용 가능
            cnt += 1
        else:
            # 처음 커블 좌석 사람만 2명 다 컵홀더 사용 가능
            cnt += 2
            couple = True
        index += 2

print(cnt)


# 풀이 2
S = sys.stdin.readline().rstrip()
couple = S.count('LL')
if couple <= 1:
    print(N)
else:
    print(N-(couple-1))
