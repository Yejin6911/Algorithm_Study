from itertools import permutations


def solution(n, weak, dist):
    # 길이를 2배로 늘려서 원형을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist) + 1

    # 시작점 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for choices in permutations(dist, len(dist)):
            # 선택한 친구 명수
            count = 1
            # 선택한 친구가 최대 갈 수 있는 거리
            position = weak[start] + choices[count-1]
            # 시작점 부터 모든 취약 지점을 확인
            for i in range(start, start+length):
                # 점검할 수 있는 취약점 위치를 벗어나는 경우
                if position < weak[i]:
                    count += 1  # 새로운 친구 투입
                    if count > len(dist):  # 더 투입 불가능한 경우 종료
                        break
                    position = weak[i]+choices[count-1]
            answer = min(answer, count)  # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer
