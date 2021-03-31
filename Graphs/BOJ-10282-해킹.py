# 다익스트라, 최단경로 문제 -> 우선순위 큐 사용
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start)) # initialize
    distance[start] = 0

    while heap:
        dist, cur = heapq.heappop(heap)
        if distance[cur] < dist: # 현재 distance보다 작을 경우만 업데이트
            continue
        for node, w in adj[cur]: # 노드 번호, 간선 가중치
            cost = dist + w
            if dist[node] > cost:
                dist[node] = cost
                heapq.heappush(heap, (cost, node))

for _ in range(int(input())):
    n, m, c = map(int, input().split())
    adj = [[] for i in range(n+1)]
    distance = [float('inf')]*(n+1)

    for _ in range(m):
        x, y, s = map(int, input().split())
        adj[y].append((x, s)) # x -> y 의존 == y감염 ->(s초후)-> x감염
    dijkstra(start = c)
    count = 0 # 감염된 컴퓨터의 수
    max_dist = 0
    for i in distance:
        if i!=float('inf'):
            count+=1
            if i > max_dist:
                max_dist = 1
    print(count, max_dist)