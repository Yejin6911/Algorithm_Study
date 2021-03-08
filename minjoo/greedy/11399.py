n = int(input()) # 사람 수
p = list(map(int, input().split())) # 인출하는데 걸리는 시간

p.sort()

answer = 0
for i in range(n):
    answer += (n-i)*p[i]

print(answer)

