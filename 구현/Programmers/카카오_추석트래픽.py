from datetime import datetime, timedelta
from collections import deque
pat = "%H:%M:%S.%f"
sample  =  [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
    ]
def split_log(line):
    temp = line.split()
    time = datetime.strptime(temp[1], pat)
    return time-timedelta(seconds=float(temp[2][:-1])+0.001), time, float(temp[2][:-1])

sample = [split_log(s) for s in sample]
answer = [0]*(len(sample)+1)

_start = sample.pop(0)[0]
i = 1

while sample:
    start, end, time = sample.pop(0)
    print(_start)
    print(start)
    if start <= _start + timedelta(seconds = 1):
        print("passed")
        answer[i]+=1
    else:
        i+=1
        _start += timedelta(seconds = 1)

print(answer)



