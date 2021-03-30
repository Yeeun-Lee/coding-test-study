"""
컴퓨터의 수 <= 100
수가 적기 때문에 DFS를 사용하는 것이 유리함(코드가 짧아서)
"""
from collections import deque

n = int(input())
p = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(p):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def bfs(now):
    q = deque([now])

    while q:
        cur = q.popleft()
        visited[cur] = True
        for conn in adj[cur]:
            if not visited[conn]:
                q.append(conn)

def dfs(now):
    visited[now] = True
    for conn in adj[now]:
        if not visited[conn]:
            dfs(conn)

visited = [False]*(n+1)
# bfs
bfs(1)
# dfs
dfs(1)
# 결과 출력(boolean array ==> 0, 1, 1, 0 --> sum)
print(sum(visited)-1)