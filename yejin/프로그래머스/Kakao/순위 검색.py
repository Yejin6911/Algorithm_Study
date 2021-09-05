from bisect import bisect_left
from itertools import combinations


def make_cases(info):
    cases = []
    # 4개 조건 중 n를 선택하는 경우
    for n in range(5):
        # n개의 조건 선택하는 조합
        for now in combinations([0, 1, 2, 3], n):
            case = ''
            for i in range(4):
                if i in now:
                    case += info[i]
                else:
                    case += '-'
            cases.append(case)
    return cases


def solution(info, query):
    answer = []
    all_candidates = {}
    for i in info:
        i = i.split()
        # 해당 정보로 만들 수 있는 모든 조건
        candidates = make_cases(i)
        for candidate in candidates:
            # 전체 경우의 수에 추가
            if candidate not in all_candidates.keys():
                all_candidates[candidate] = [int(i[4])]
            else:
                all_candidates[candidate].append(int(i[4]))
    # 각각 조건별로 점수 정렬
    for key in all_candidates.keys():
        all_candidates[key].sort()

    # 조건에 해당하는 사람 수 계산
    for q in query:
        q = q.split()
        target = q[0]+q[2]+q[4]+q[6]
        if target in all_candidates.keys():
            # 이진탐색으로 조건의 점수 이상인 사람들 시작점 앞 인덱스 찾기
            index = bisect_left(all_candidates[target], int(q[7]), lo=0, hi=len(all_candidates[target]))
            answer.append(len(all_candidates[target])-index)
        else:
            answer.append(0)
    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
