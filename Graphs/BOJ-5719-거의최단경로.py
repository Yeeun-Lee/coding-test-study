# 다익스트라 + BFS/DFS
# 시간초과....

from collections import deque
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dijkstra():
    heap = []

    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, cur = heapq.heappop(heap)
        if distance[cur] < dist:
            continue
        for i in adj[cur]:
            cost = dist + i[1]
            if distance[i[0]] > cost and (cur, i[0]) not in dropped:
            # if distance[i[0]] > cost and not dropped[cur][i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    return distance

def bfs():  # 경로 확인을 위한 역추적(시간초과)
    q = deque()
    visited = [False]*n
    q.append(end)
    visited[end] = True
    while q:
        now = q.popleft()
        visited[now] = True
        if now == start:
            continue
        for prev, cost in reverse_adj[now]:
            if not visited[prev] and distance[now] == distance[prev] + cost:
                # dropped = [[False]*n for _ in n]일 때
                dropped[prev][now] = True
                q.append(prev)
def dfs(now): # 시간초과..
    if now == start:
        return
    for prev, cost in reverse_adj[now]:
        if distance[now] == distance[prev]+cost:
            dropped.add((prev, now))
            dfs(prev)
    for i in range(n):
        if distance[now]+adj[now][i] == distance[i]:
            dropped.add()

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    start, end = map(int, input().split())
    adj = [[] for _ in range(n)]
    reverse_adj = [[] for _ in range(n)]

    for _ in range(m):
        x, y, cost = map(int, input().split())
        adj[x].append((y, cost))
        reverse_adj[y].append((x, cost))

    dropped = set()
    distance = [1e9] * n
    dijkstra()
    # 다익스트라로 계산된 현재 distance와 reverse_adj를 사용하여 BFS로 역추적을 수행한다
    # bfs()  # dropped update(최단 경로 안에 포함되어 있는 노드 -> True)
    dfs(end)

    # 거의 최단경로 구하기
    distance = [1e9] * n
    dijkstra() # dropped == False인 노드들에 대해서만 다시 다익스트라 수행

    if distance[end] != 1e9:
        print(distance[end])
    else:
        print(-1)
