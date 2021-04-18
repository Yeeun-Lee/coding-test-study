from collections import deque

def bfs(graph, dist):
    q = deque([1])

    while q:
        cur = q.popleft()
        for e in graph[cur]:
            if not dist[e]:
                q.append(e)
                dist[e] = dist[cur]+1 # 1~현재점 까지의 거리에 1을 더한 값을 할당한다.

def solution(n, edge):
    edge.sort()
    graph = {}
    for e in edge: # 양방향 그래프 생성
        graph[e[0]] = graph.get(e[0], [])+[e[1]]
        graph[e[1]] = graph.get(e[1], [])+[e[0]]
    dist = [0]*(n+1) # 1에서부터의 거리 저장
    bfs(graph, dist)
    answer = 0
    for v in dist[2:]: # 1을 제외한 점들 중
        if v == max(dist):
            answer+=1
    return answer

