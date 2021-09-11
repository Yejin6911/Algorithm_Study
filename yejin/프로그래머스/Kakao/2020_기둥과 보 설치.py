def check(answer):
    for x, y, a in answer:
        # 기둥인 경우
        if a == 0:
            if not (y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer):
                return False
        # 보인 경우
        else:
            if not ([x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer)):
                return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # 설치
        if b == 1:
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
        # 삭제
        else:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
    return sorted(answer)
