import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 방법 기억하기!!


def post_order(start, end):
    if start > end:
        return

    # 루트 노드
    root = pre_order[start]

    idx = start+1  # 나눠질 인덱스 탐색
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    # 왼쪽 서브트리
    post_order(start+1, idx-1)
    # 오른쪽 서브트리
    post_order(idx, end)
    # 루트
    print(root)


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

post_order(0, len(pre_order)-1)
