from itertools import combinations #팀 짤때 ->조합 함수

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

mem_index = [i for i in range(n)]
possible_team = []

#조합 사용 방법
for team in list(combinations(mem_index, n//2)):
    possible_team.append(team)

min_score = 10000 #최소값 구하기 위함
for i in range(len(possible_team)//2):
    #스타트 팀
    team_s = possible_team[i]
    score_s = 0
    for j in range(n//2):
        current_team_s = team_s[j] 
        for k in team_s:
            score_s += s[current_team_s][k] #멤버와 함께할 경우의 능력치들
            
    #링크 팀 - 나머지 팀
    #조합 사용 방법 : 첫 조합의 여집합은 마지막 조합
    team_l = possible_team[-i-1]
    score_l = 0
    for j in range(n//2):
        current_team_l = team_l[j]
        for k in team_l:
            score_l += s[current_team_l][k]
            
    min_score = min(min_score, abs(score_s - score_l)) #절댓값 함수
print(min_score)

#https://velog.io/@skyepodium/%EB%B0%B1%EC%A4%80-14889-%EC%8A%A4%ED%83%80%ED%8A%B8%EC%99%80-%EB%A7%81%ED%81%AC
#3) 비트마스킹,,
