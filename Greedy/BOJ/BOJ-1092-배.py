import sys
s = int(sys.stdin.readline().rstrip())
ship = list(map(int, sys.stdin.readline().rstrip().split()))
n = int(sys.stdin.readline().rstrip())
box = list(map(int, sys.stdin.readline().rstrip().split()))

box.sort(reverse = True)
ship.sort(reverse = True)
load = [0]*n
for b in box:
    if b > max(ship):
        print(-1)
        sys.exit(0)

    for i in range(s):
        if b < ship[i]:
            ship[i]-=b
            load[i]+=1
            break
print(max(load))


