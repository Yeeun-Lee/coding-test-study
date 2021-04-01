def solution(n, t, m, timetable):
    timetable = [int(time[:2])*60+int(time[3:5]) for time in timetable] # h*60+min
    timetable.sort() # sort timetable

    for i in range(1, n+1):
        last = 540 + (n-1)*t
        if len(timetable) <  m:
            return "%02d:%02d"%(last//60, last%60)
        if i == n:
            if timetable[0]>last:
                return "%02d:%02d"%(last//60, last%60)
            else:
                return "%02d:%02d"%((timetable[-1]-1)//60, (timetable[-1]-1)%60)
        for j in range(m-1, -1, -1):
            bus_arrive = 540+i*t
            if timetable[j] <= bus_arrive:
                del timetable[j]
    answer = ''
    return answer

n = int(input())
t = int(input())
m = int(input())
timetable = eval(input())
print(solution(n, t, m, timetable))
