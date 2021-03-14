i = 1
while True:
    L, P, V = map(int, input().split())
    if L==0 and P==0 and V==0:
        break
    sum = ( V // P ) * L
    sum += min((V%P),L)#삼한연산자 대신 이거 가능 
    print('Case %d: %d' %(i,sum)) #출력형식 
    i += 1

