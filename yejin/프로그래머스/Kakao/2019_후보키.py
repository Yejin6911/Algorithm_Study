from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    candidates = []
    for i in range(1, col+1):
        # i개를 선택하는 경우의 수
        for comb in combinations([x for x in range(col)], i):
            # 유일성
            keys = []
            for r in range(row):
                key = [relation[r][c] for c in comb]
                # 유일성 만족하지 않는 경우
                if key in keys:
                    break
                else:
                    keys.append(key)
            if len(keys) == row:
                # 최소성 확인
                check = True
                for candidate in candidates:
                    # 현재 선택한 속성집합의 부분집합이 후보키에 있으면 안됨
                    if set(candidate).issubset(set(comb)):
                        check = False
                        break
                if check:
                    candidates.append(comb)
    return len(candidates)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
      "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
