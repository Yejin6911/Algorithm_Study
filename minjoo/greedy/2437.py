n = int(input()) # 저울추의 개수
w = list(map(int, input().split())) # 저울추의 무게
w.sort()
answer = 1
for i in range(n):
    if(w[i] <= answer):
        answer += w[i]
    else:
        break
print(answer)



######### 처음 시도했던 풀이 (조합) -> 메모리초과 ##########
# from itertools import combinations

# w.sort()
# candi = [i for i in w]

# def getcandidate(n):
#     com = list(combinations(w, n))
#     for i in range(len(com)):
#         candi.append(sum(com[i]))

# for i in range(2, n+1):
#     getcandidate(i)

# candi = list(set(candi))
# candi.sort()
# # print(candi)

# i = 1
# while(i in candi):
#     i += 1

# print(i)