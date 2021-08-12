import sys
input = sys.stdin.readline

# 개념 참고
# https://claude-u.tistory.com/208

n, k = map(int, input().split())
data = []
for _ in range(n):
    w, v = map(int, input().split())
    data.append((w, v))

result = [0 for _ in range(k+1)]
for i in range(n):
    for j in range(k, 1, -1):
        # 현재 물건의 무개가 전체 무게 J보다 작거나 같을 때
        if data[i][0] <= j:
            # 해당 무게를 들때의 최대값 저장
            # j일때의 가치와  (j-현재배낭 무게 의 가치 + 현재배낭의 가치) 중 더 높은 값으로 Update
            result[j] = max(result[j], result[j-data[i][0]]+data[i][1])
print(result[k])
