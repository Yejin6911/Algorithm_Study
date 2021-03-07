N = int(input())
meeting = [list(map(int, input().split())) for i in range(N)]
meeting.sort(key= lambda x:(x[1],x[0])) #lambda 이해와 두번 정렬하는 방법도 해보기

num = 0
current_end = 0

for m in meeting: #for
    if current_end <= m[0]:
        num += 1
        current_end = m[1]

print(num)

#풀이 참고 했음 ㅠ

    
    
    
