def str2sec(time):
    time = time.split(":")
    return 3600*int(time[0])+60*int(time[1])+int(time[2])


def sec2str(time):
    hour = time//3600
    time -= (3600*hour)
    min = time//60
    time -= (60*min)
    sec = time
    return ':'.join([str(hour).zfill(2), str(min).zfill(2), str(sec).zfill(2)])


def solution(play_time, adv_time, logs):
    # 모두 초로 변경
    play_time = str2sec(play_time)
    adv_time = str2sec(adv_time)

    # 매 초 보고있는 사람 수 저장
    viewers = [0 for _ in range(play_time+1)]
    for log in logs:
        s, e = map(str, log.split('-'))
        s = str2sec(s)
        e = str2sec(e)
        viewers[s] += 1
        viewers[e] -= 1

    # 현재 시청자수 저장
    for i in range(1, play_time+1):
        viewers[i] = viewers[i]+viewers[i-1]
    # 누적 시청자수 저장
    for i in range(1, play_time+1):
        viewers[i] = viewers[i]+viewers[i-1]

    max_cnt = viewers[adv_time-1]
    start = 0

    # i: 광고 종료 시간
    for i in range(adv_time, play_time):
        cnt = viewers[i]-viewers[i-adv_time]
        if cnt > max_cnt:
            max_cnt = cnt
            start = i-adv_time+1
    answer = sec2str(start)
    return answer


print(solution(	"02:03:55", "00:14:15", [
      "01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
