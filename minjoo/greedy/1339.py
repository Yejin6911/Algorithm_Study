n = int(input())

value = {} # 알파벳 별 숫자 모음
words = [] # 단어의 모음

for _ in range(n):
    words.append(input())

for word in words:
    k = len(word)-1 # 자리수
    for x in word:
        if x in value:
            value[x] += pow(10, k) # 10의 거듭제곱으로 표현
        else:
            value[x] = pow(10, k)
        k -= 1

nums = [] # value딕셔너리의 value값만 담을 리스트
for v in value.values():
    nums.append(v)

nums.sort(reverse=True) # 큰 순으로 정렬

result = 0
x = 9

for i in range(len(nums)):
    result += nums[i]*x # 9부터 1씩 줄어들며 곱하기
    x -= 1

print(result)