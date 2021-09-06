from itertools import combinations

def solution(orders, course):
    answer = []
    dic = {}

    # 모든 주문 내역을 알파벳 순으로 정렬 
    for i in range(len(orders)):
        orders[i] = sorted(orders[i])

    # 가능한 조합의 경우와 그 조합이 나온 개수를 dic에 저장
    for i in range(len(orders)):
        for j in range(2, len(orders)+1):
            combis = list(combinations(orders[i], j))
            for c in range(len(combis)):
                if(combis[c] in dic.keys()):
                    dic[combis[c]] += 1
                else:
                    dic[combis[c]] = 1
    
    # dic을 1. 메뉴구성 개수 2. 몇번 나왔는지 를 순으로 정렬
    sdic = sorted(dic.items(), key = lambda item: (len(item[0]), item[1]), reverse = True)

    lengthdic = {}

    for i in range(len(sdic)):
        # 레스토랑 주인이 원하는 메뉴구성 개수일 때
        if(len(sdic[i][0]) in course):
            # 만약 최대 나온 개수가 저장되어 있다면
            if(len(sdic[i][0]) in lengthdic.keys()):
                if(sdic[i][1] == lengthdic[len(sdic[i][0])]):
                    answer.append(sdic[i][0])
            # 최대 나온 개수가 저장되어 있지 않다면
            else:
                # 두번 이상 나온 메뉴구성에 대해
                if(sdic[i][1] >= 2):
                    # 최대 나온 개수를 저장하고 answer에 append
                    lengthdic[len(sdic[i][0])] = sdic[i][1]
                    answer.append(sdic[i][0])

    answer.sort()

    ans = []
    for i in range(len(answer)):
        t = ''
        for j in range(len(answer[i])):
            t += answer[i][j]

        ans.append(t)
    return ans

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4] ))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5] ))
# print(solution(["XYZ", "XWY", "WXA"],[2,3,4] ))