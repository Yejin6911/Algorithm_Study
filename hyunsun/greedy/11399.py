import sys    
N = int(input())
mins = list(map(int, input().split()))
#mins = input().split() 왜 런타임 에러?

if N == 1:
    print(mins[0])

else:
    mins.sort()

    prv_sum = 0
    min_sum = 0

    for i in range(N):
        min_sum += prv_sum + mins[i]
        prv_sum += mins[i]

    print(min_sum)
