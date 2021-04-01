import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

castle = []
for _ in range(n):
    castle.append(list(sys.stdin.readline().rstrip()))
print(castle)
new_n = n
idxs = []
for i in range(n):
    if 'X' in castle[i]:
        new_n -= 1
        for j in range(m):
            if castle[i][j] == 'X':
                idxs.append(j)
print(min(new_n, m-len(set(idxs)))+abs(new_n-(m-len(set(idxs)))))
           
