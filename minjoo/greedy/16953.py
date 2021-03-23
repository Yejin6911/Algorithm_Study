a, b = input().split()
# 큰수 -> 작은수를 만들 것임.

answer = 1
while(int(b) > int(a)):
    if(b[-1] == '1'): # 뒷자리가 1이면 제거
        b = b[:-1]
        answer += 1
    elif(int(b) % 2 == 0): # 2로 나눠지면 나누기
        b = str(int(b) // 2)
        answer += 1
    else: # 계산 불가능한 것
        break

if(a != b):
    print("-1")
else:
    print(answer)
    