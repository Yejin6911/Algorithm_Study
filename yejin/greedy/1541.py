import sys

data = sys.stdin.readline().rstrip()
operator = []
number = []

now = data[0]
# 숫자와 연산자 분리해서 각각 배열에 넣어주기
for i in range(1, len(data)):
    if data[i].isdigit():
        now += data[i]
    else:
        number.append(int(now))
        operator.append(data[i])
        now = ''
number.append(int(now))

result = 0
temp = number[-1]
# 마지막 숫자부터 시작
for i in range(len(operator)-1, -1, -1):
    # '-'인 경우 해당 숫자를 result에서 빼준 후 연산자 앞 숫자를 temp로 지정
    if operator[i] == '-':
        result -= temp
        temp = number[i]
    # '+'인 경우 해당 숫자를 temp에 더해준다.
    else:
        temp += number[i]
result += temp
print(result)

# 풀이법 2 - 입력값 값을 때 '-' 문자 기준으로 바로 쪼개기
data = sys.stdin.readline().rstrip().split('-')
number = []
for i in data:
    temp = 0
    s = i.split('+')
    for j in s:
        temp += int(j)
    number.append(temp)
result = number[0]
for i in range(1, len(number)):
    result -= number[i]

print(result)
