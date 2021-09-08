import copy
char_list = ['-', '_', '.']


def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    temp_id = new_id
    for x in new_id:
        if (not x.isalpha() and not x.isdigit()) and x not in char_list:
            temp_id = temp_id.replace(x, "")
    new_id = temp_id
    # 3단계
    idx = 0
    cnt = 0
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    # 4단계
    if len(new_id) and new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) and new_id[0] == '.':
        new_id = new_id[1:]
    # 5단계
    if not len(new_id):
        new_id += 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7단계
    if len(new_id) <= 2:
        new_id += new_id[-1]*(3-len(new_id))
    return new_id


# print(solution("abcdefghijklmn.p"))
