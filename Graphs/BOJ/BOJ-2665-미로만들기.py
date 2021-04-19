# 그래프 탐색+BFS+다익스트라
import heapq
import sys
input = sys.stdin.readline

n = int(input())
miro = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def dijkstra():
    heap = []
    heapq.heappush(heap, (0,0,0))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while heap:
        cnt, x, y = heapq.heappop(heap)
        if x == n-1 and y == n-1:
            return cnt
        if visited[y][x]:
            continue
        visited[y][x] = True

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[ny][nx]:
                if miro[ny][nx] == 1:
                    heapq.heappush(heap, (cnt, nx, ny))
                elif miro[ny][nx] == 0:
                    heapq.heappush(heap, (cnt+1, nx, ny))
print(dijkstra())