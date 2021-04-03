import sys
sys.setrecursionlimit(10000)

r, c = map(int, input().split())
board = [input() for _ in range(r)]
directions = [(1,0), (-1,0), (0, 1), (0, -1)]
result = 0

def promising(x, y, route):
    if x<0 or x>=r or y<0 or y>=c:
        return False
    if board[x][y] in route:
        return False
    return True

def dfs(x, y, step): # 시간초과
    global result
    result = max(result, len(step))
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if promising(nx, ny, step):
            dfs(nx, ny, step+board[nx][ny])
            
# 강의 bfs 사용
def bfs(x, y):
    global result
    q = set()
    q.add((x, y, board[x][y]))
    while q:
        x, y, step = q.pop()
        result = max(result, len(step))
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if promising(nx, ny, step):
                q.add((nx, ny, step+board[nx][ny]))
#dfs(0, 0, board[0][0])
bfs(0, 0)
print(result)
