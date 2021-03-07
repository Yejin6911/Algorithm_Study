
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]#띄어쓰기된 입력 리스크로 받기

#for i in range(N):
#    coins = int(input())
    
coin_num = 0

for i in range(1,N+1):
    coin = coins[-i] #리스트에 -인덱스 공부

    if K >= coin:
        num = K//coin #정수 나누기 연산자
        K -= num*coin
        coin_num += num

print(coin_num)
        
        
 
