from collections import deque

def dfs(v): # 깊이우선탐색
    print(v, end = ' ')
    visited[v] = True
    for e in adj[v]:
        if not visited([e]):
            dfs(e) # 재귀

def bfs(v): # 넓이우선탐색
    q = deque([v]) # queue 이용
    while q:
        v = q.popleft()
        if not visited([v]):
            visited[v] = True
            print(v, end = ' ')

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
for e in adj: # 작은 인덱스부터 확인할 수 있도록
    e.sort()

visited = [False]*(n+1)
dfs(v)
print()
visited = [False]*(n+1)
bfs(v)