"""
응용되어 많이 나오는 유형**
"""
import sys
sys.setrecursionlimit(100000) # 재귀 횟수에 대한 제한

def dfs(x, y):
    visited[x][y] = True
    # 상하좌우 방향벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy # new position with direction
        if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위내에서 움직이도록
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    array = [[0]*m for _ in range(n)]
    # 2차원 정의
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        array[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                result +=1
    print(result)

