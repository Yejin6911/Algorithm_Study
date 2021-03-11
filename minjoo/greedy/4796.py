tc = 1
while(1):
    L, P, V = map(int, input().split())
    if(L==0 and P==0 and V==0):
            break

    result = V//P*L # 연속하는 P일이 횟수 * L일
    if(V%P >= L): # 나머지 휴가 계산
        result += L
    else:
        result += V%P
    print("Case {0}: {1}".format(tc, result))
    tc += 1
