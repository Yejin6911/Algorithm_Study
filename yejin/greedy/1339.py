import sys

n = int(sys.stdin.readline().rstrip())
words = []
data = {}
for i in range(n):
    word = sys.stdin.readline().rstrip()
    words.append(word)
    length = len(word)-1
    for i in range(len(word)):
        if word[i] in data.keys():
            # data[word[i]] += pow(10,length-i) 이렇게 해도 같음
            data[word[i]] += 10**(length-i)
        else:
            data[word[i]] = 10**(length-i)

sorted_data = sorted(data.values(), reverse=True)
n = 9
result = 0
for i in sorted_data:
    result += i*n
    n -= 1

print(result)
