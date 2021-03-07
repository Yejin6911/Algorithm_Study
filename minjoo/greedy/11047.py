n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True) # 동전 크기가 큰 순서대로 정렬

answer = 0
for i in range(len(a)):
    q = k//a[i] # 동전으로 나눈 몫
    if(q > 0):
        answer += q
        k = k % a[i]

print(answer)