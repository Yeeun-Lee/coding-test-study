# 구현 + 기하
import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
        continue
    _lim = math.sqrt(((x1-x2)**2+(y1-y2)**2))
    if _lim == r1+r2 or _lim == abs(r1-r2):
        print(1)
    if _lim < r1+r2 and _lim > abs(r1-r2):
        print(2)
    if _lim > r1+r2 or _lim < abs(r1- r2):
        print(0)
