from collections import deque
from copy import deepcopy

def bfs(graph, init, n):
    q = deque([init])
    visited = [False]*(n+1)
    visited[init] = True
    while q:
        cur = q.popleft()
        for e in graph[cur]:
            if not visited[e]:
                q.append(e)
                visited[e] = True

    return sum(visited)-1

def solution(n, results):
    answer = 0
    wins = {i:[] for i in range(1, n+1)}
    loses = deepcopy(wins)

    for r in results:
        wins[r[0]].append(r[1])
        loses[r[1]].append(r[0])

    for i in range(1, n+1): # 모든 선수들에 대해 이기고 지는 경우를 구한다.
        win = bfs(wins, i, n)
        lose = bfs(loses, i, n)
        if win+lose == n-1: # 순위가 결정되는 경우
            answer+=1
    return answer
