import sys
n = int(sys.stdin.readline().rstrip())

cnt = dict()
for _ in range(n):
    book = sys.stdin.readline().rstrip()
    if book in cnt.keys():
        cnt[book]+=1
    else:
        cnt[book]=1
result = sorted(cnt.items(), key = lambda x:(-x[1], x[0]))
print(result[0][0])
