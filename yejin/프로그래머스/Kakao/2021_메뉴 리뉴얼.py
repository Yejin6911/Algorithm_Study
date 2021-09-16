from itertools import combinations


def solution(orders, course):
    answer = []
    for n in course:
        course_cnt = {}
        for order in orders:
            courses = list(combinations(list(order), n))
            for c in courses:
                now = ''.join(sorted(c))
                if now not in course_cnt.keys():
                    # 처음 주문한 코스일 때
                    course_cnt[now] = 1
                else:
                    course_cnt[now] += 1
        # 가장 많이 주문한 코스부터, 알파벳 순으로
        course_cnt = sorted(course_cnt.items(), key=lambda x: (-x[1], x[0]))
        # 가장 많이 주문한 횟수가 2 이상일 때만 고려
        if len(course_cnt) and course_cnt[0][1] >= 2:
            Max = course_cnt[0][1]
        for menu, cnt in course_cnt:
            if cnt == Max:
                answer.append(menu)
    return sorted(answer)
