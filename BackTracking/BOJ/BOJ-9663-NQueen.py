# N-Queen(PyPy3)
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

def promising(x):
    for row in range(x):
        if rows[row]-rows[x] == 0: # or 로 연결해서 제출시 시간초과
            return False
        if abs(rows[row]-rows[x]) == x - row:
            return False
    return True

def dfs(x):
    global answer
    if x == N:
        answer+=1
    else:
        for i in range(N):
            rows[x] = i
            if promising(x):
                dfs(x+1) # 다음 행으로

rows = [0]*N
answer = 0
dfs(0) # cur_row
print(answer)
