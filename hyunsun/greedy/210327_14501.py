n = int(input())
t = []
p = []
max_pay = [] #DP 이용

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

max_pay = [0 for _ in range(n+1)]

for i in range(n-1,-1,-1): #n-1부터 0까지
     if t[i] + i > n:
         # max_pay[i] = 0 #X
         max_pay[i] = max_pay[i+1] #그냥 이번엔 못 하는 거
     else:
         max_pay[i] = max(max_pay[i+1], p[i] + max_pay[i+t[i]]) #그냥 이번에 안하는거 or 이번에 해서, 다시 계산해보는거
print(max_pay[0])
