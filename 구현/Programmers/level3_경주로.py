from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def road(cost, x, y, board):
    q = deque()
    q.append((0, x, y, 0)) # 0에서 갈 수 있는 경로에 대해 추가한다.
    q.append((0, x, y, 1))
    
    while q:
        _cost, x, y, d = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >=  n or board[ny][nx] == 1:
                continue
            if i == d:
                new_cost = 100
            else:
                new_cost = 600 # 직선 + 커브
            next_cost = new_cost + _cost

            if cost[ny][nx] == -1 or cost[ny][nx] >= next_cost:
                cost[ny][nx] = next_cost
                q.append((next_cost, nx, ny, i))
    return cost
                

def solution(board):
    global n
    n = len(board)
    cost = [[-1]*n for _ in range(n)]
    answer = road(cost, 0, 0, board)
    
    return answer[n-1][n-1]

board = eval(input())
print(solution(board))
