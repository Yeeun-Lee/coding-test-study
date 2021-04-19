# 다익스트라(PyPy3 제출)
import heapq

N, E = map(int, input().split())
INF = 1001


def dijkstra(init, N):
    heap = []
    distance = [INF] * (N + 1)
    distance[init] = 0  # intialize
    heapq.heappush(heap, (init, distance[init]))

    while heap:
        node, dist = heapq.heappop(heap)
        for n, c in graph[node]:
            if distance[n]>dist+c:
                distance[n]=dist+c
                heapq.heappush(heap, (n, dist+c))
    return distance

graph = {i:[] for i in range(N+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split()) # 반드시 거쳐야 하는 두 개의 정점 번호

dist = dijkstra(1, N)
dist_v1 = dijkstra(v1, N)
dist_v2 = dijkstra(v2, N)

ans1 = dist[v1]+dist_v1[v2]+dist_v2[N] # 1 -> v1 -> v2 -> N
ans2 = dist[v2]+dist_v2[v1]+dist_v1[N] # 1 -> v2 -> v1 -> N

if min(ans1, ans2)<INF:
    print(min(ans1, ans2))
else:
    print(-1)