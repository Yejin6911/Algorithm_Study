def solution(play_time, adv_time, logs):
    # 모든 시간을 '초'단위로 환산
    play_time = str_to_int(play_time)        
    adv_time = str_to_int(adv_time)

    # 초로 환산된 play_time의 size만큼 모든 시간별 시청자수를 저장할 배열 생성           
    all_time = [0 for i in range(play_time + 1)]

    # logs내의 모든 시간 초로 환산 및 start, end 구분
    for l in logs:
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)

        all_time[start] += 1
        all_time[end] -= 1

    # 구간별 시청자수 기록
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    # 모든 구간 시청자 누적 기록
    for i in range(1, len(all_time)):
        # 0초부터 i초 까지의 누적 시청자 수
        all_time[i] = all_time[i] + all_time[i - 1]

    # 누적된 시청자수를 바탕으로 가장 시청자수가 많은 구간 탐색
    most_view = 0
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if(most_view < all_time[i] - all_time[i - adv_time]):
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)

# 초 단위로 환산
def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

# 다시 시, 분, 초 로 환산
def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

    
play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
solution(play_time, adv_time, logs)