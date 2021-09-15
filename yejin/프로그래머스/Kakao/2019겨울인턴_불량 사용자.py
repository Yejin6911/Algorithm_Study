from itertools import permutations


def check(users, banned_id):
    for i in range(len(users)):
        user = users[i]
        ban_id = banned_id[i]
        if len(user) != len(ban_id):
            return False
        for n in range(len(user)):
            if ban_id[n] == '*':
                continue
            if user[n] != ban_id[n]:
                return False
    return True


def solution(user_id, banned_id):
    result = []
    candidates = permutations(user_id, len(banned_id))
    for candidate in candidates:
        # 하나의 튜플과 비교 시작
        if not check(candidate, banned_id):
            continue  # 다음 튜플 가져오기
        else:
            users = set(candidate)
            if users not in result:
                result.append(users)
    return len(result)


print(solution(["frodo", "fradi", "crodo", "abc123",
                "frodoc"], ["*rodo", "*rodo", "******"]))
