#푸는 중_에러
N = int(input())

for i in range(N):
    n = int(input())
    list = [list(map(int,input().split())) for i in range(n)]
    list.sort(reverse = True, key= lambda x: x[1])
    list.sort(key= lambda x: x[0])

    sum = 0
    for j in range(n-1):
        cnt = 0
        for k in range(n-(j+1)):
            if list[n][1] > list[n+k+1][1]:
                cnt = 1
                break
        if cnt == 0:
            sum += 1
    print(sum)
            
        
    
