#오른쪽 이동이 제약, 1,4만 최대한 쓰는 게 좋아서 1,4방법을 쓸 수 있는지 없는지로 나누기
N,M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2: #M:res 1~2:1 3~4:2 5~6:3
    print(min(4,(M+1)//2))#2,3번만 쓸 수 있음 : 따라서 4가지 방법 모두 쓸 수 없으니 최대가 4번 이동
else:
    if M<=6:
        #print(3*(M-1)+1)#문제이해x:지나간 칸 개수인 줄
        #print(M)#이동 횟수 다시 생각x
        print(min(4,M))#1,4 방법만이 이득
    else:
        print(M-2)#2,3 한번씩만 써서 -2
