n, k = map(int, input().split()) # 구멍의 개수, 총 사용횟수
seq = list(map(int, input().split())) # 사용 순서

# 현재 탭에 꽂혀있는 전기용품 중,
# 남은 사용순서에서 가장 나중에 사용되는 전기용품을 반환
def latest(temp, tab):
    late = [-1, 0] # 인덱스, 전기용품
    for i in range(len(tab)):
        if(tab[i] in temp):
            idx = temp.index(tab[i]) 
            if(idx > late[0]):
                late = [idx, i]
        else:
            return i
    return late[1]

answer = 0
tab = [0 for i in range(n)] # 멀티탭
for i in range(k):
    if(seq[i] in tab): # 이미 꽂혀있으면
        pass
    elif(0 in tab): # 멀티탭에 빈 공간이 있으면
        idx = tab.index(0)
        tab[idx] = seq[i]
    else: # 빼야하는 경우
        temp = seq.copy()
        temp = temp[i+1:] # 남은 사용순서
        change = latest(temp, tab) # 가장 나중에 사용되는 것
        tab[change] = seq[i] # 바꿔끼움
        answer += 1

print(answer)

