import sys
data = sys.stdin.readline().rstrip()

cnt0 = 0
cnt1 = 0

if data[0]=='1':
    cnt0+=1
else:
    cnt1+=1
print(data)
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            cnt0+=1
        else:
            cnt1+=1
print(cnt0, cnt1)
print(min(cnt0, cnt1))
