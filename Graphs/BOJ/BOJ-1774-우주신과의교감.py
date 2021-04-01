# mst
import math
import sys
input = sys.stdin.readlin

n, m = map(int, input().split())

def distance(a, b):
    # a : (x_1, y_1), b : (x_2, y_2) 유클리디안
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def get_parent(parent, n):
    # find역할, path compression
    if parent[n] == n:
        return n
    return get_parent(parent, parent[n])

def union_parent(parent, a, b):
    # union by rank
    a = get_parent(parent, a)
    b = get_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, a, b):
    # 같은 root를 가지는지 확인(사이클을 가지는지)
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a==b:
        return True
    else:
        return False

parent = {}
gods = []
edges = []

for _ in range(n): # 좌표
    x, y = map(int, input().split())
    gods.append((x, y))
    
for i in range(len(gods)-1):
    for j in range(i+1, len(gods)):
        edges.append((i+1, j+1, distance(gods[i], gods[j])))

for i in range(1, n+1): # initialize(아무것도 연결되어 있지 않은 상태, 자기 자신이 parent)
    parent[i] = i
    
for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b) # 노드 연결

edges.sort(key = lambda x: x[2])
result = 0

for a, b, cost in edges:
    if not find_parent(parent, a, b):  # 사이클을 이루지 않는다면
        union_parent(parent, a, b)
        result+=cost
        
print("%0.2f"%result)

