import copy


def solution(rows, columns, queries):
    matrix = [[0]*columns for _ in range(rows)]
    num = 1
    for r in range(rows):
        for c in range(columns):
            matrix[r][c] = num
            num += 1
    answer = []
    for r1, c1, r2, c2 in queries:
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1

        temp = []
        for c in range(c1, c2):
            temp.append(matrix[r1][c])
        for r in range(r1, r2):
            temp.append(matrix[r][c2])
        for c in range(c2, c1, -1):
            temp.append(matrix[r2][c])
        for r in range(r2, r1, -1):
            temp.append(matrix[r][c1])
        temp = [temp.pop()]+temp
        # 회전
        idx = 0
        for c in range(c1, c2):
            matrix[r1][c] = temp[idx]
            idx += 1
        for r in range(r1, r2):
            matrix[r][c2] = temp[idx]
            idx += 1
        for c in range(c2, c1, -1):
            matrix[r2][c] = temp[idx]
            idx += 1
        for r in range(r2, r1, -1):
            matrix[r][c1] = temp[idx]
            idx += 1
        # 최소값 저장
        answer.append(min(temp))
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
