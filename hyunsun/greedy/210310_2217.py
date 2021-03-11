#처음에 문제 잘 못 이해 
N = int(input())
rs = [int(input()) for i in range(N)]

#res = min(rs)*N #함수,정렬로 해도 됨

rs.sort(reverse=True) #reverse

for i in range(N):
    rs[i] = rs[i]*(i+1)

res = max(rs)

print(res)
