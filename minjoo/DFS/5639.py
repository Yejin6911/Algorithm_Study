import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def post_order(start, end):
    # 역전시 리턴
    if(start > end):
        return

    # 루트 노드
    root = pre_order[start]
    idx = start + 1

    # 루트보다 커지는 지점을 찾는 과정
    while(idx <= end):
        if(pre_order[idx] > root):
            break
        idx += 1

    # 왼쪽 서브트리
    post_order(start+1, idx-1)

    # 오른쪽 서브트리
    post_order(idx, end)

    # 후위순회이므로 제일 마지막에 찍으면 된다
    print(root)

pre_order = []
while(1):
    try:
        pre_order.append(int(input()))
    except:
        break

post_order(0, len(pre_order)-1)