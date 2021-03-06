n = int(input()) # 배달해야하는 설탕의 양

answer = 0
while(1):
    if(n < 0): # 0보다 작아지면 -1
        answer = -1
        break

    if(n%5==0):
        answer += n//5
        break
    else: # 5로 나눠지지 않으면 3키로 봉지로 한번 담기
        answer += 1
        n -= 3
    
print(answer)

