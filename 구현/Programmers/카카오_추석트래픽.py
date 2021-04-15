time_table = dict()

def duplicated(second):
    if second not in time_table.keys():
        return second
    else:
        return dup(second - 0.000001)

def solution(lines):
    for index, line in enumerate(lines):
        date, time, duration = line.split() # 공백으로 분리
        h, m, n = time.split(':') # : 시, 분, 초 분리
        end = int(h) * 60 * 60 + int(m) * 60 + float(n) # 초로 계산
        duration = float(duration[:-1]) # 뒤에 s 제거
        start = end - duration + 0.001 - 0.9991
        
        time_table[duplicated(start)] = index
        time_table[duplicated(end)] = index
        
    history = []
    state = [0] * len(lines) # 트래픽이 동작 중인지 현재 상태 / 초기화 다 꺼져있다.
    
    for time in sorted(time_table.keys()):
        index = time_table[time]
        if state[index] == 0: # 트래픽이 시작이면 켠다.
            state[index] = 1
        elif state[index] == 1: # 트래픽이 종료시간이면 끈다.
            state[index] = 0
            
        history.append(state.count(1)) # 현재 동작 중인 트래픽 개수를 센다.
        #print(index, time, state, state.count(1))
        
    return max(history)

# 출처: https://jeongchul.tistory.com/660 [Jeongchul]
