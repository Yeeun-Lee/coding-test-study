from collections import deque
# python3는 시간초과 -> PyPy3로 제출

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split()) # x가 y를 신뢰한다 -> y를 해킹하면 x까지 해킹할 수 있다
    adj[y].append(x)

def bfs(v):
    q = deque([v])
    visited = [False]*(n+1)
    visited[v] = True
    count = 1
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e]=True
                count+=1
    return count

result = []
max_value = -1
# 모든 정점에 대해 bfs를 수행하여 count를 구하고, maximum value 와 비교한다.
for i in range(1, n+1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c
for e in result:
    print(e, end = " ")

