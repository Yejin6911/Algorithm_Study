#좀 더 if else 구문 없이 짜보기

N = int(input())

num = 0
if N%5==0:
    num = N//5

else:
    N=N-3
    num += 1
    while(N%5!=0):
        if(N<0):
            break
        N=N-3
        num += 1

    if(N<0):
        num = -1
    else:
        num += (N//5)

print(num)
        

