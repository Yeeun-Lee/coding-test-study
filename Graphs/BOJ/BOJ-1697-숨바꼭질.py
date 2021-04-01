from collections import deque

n, k = map(int, input().split())
MAX = 100001 # 움직일 수 있는 최대 범위
arr = [0]*MAX # 시간 저장 --> 0 : not visited

def bfs():
    q = deque([n])
    while(q):
        cur = q.popleft()
        if cur == k:
            return arr[cur]
        for next_pos in (cur-1, cur+1, cur*2):
            if 0<=next_pos<MAX and not arr[next_pos]:
                arr[next_pos] = arr[cur]+1
                q.append(next_pos)
print(bfs())