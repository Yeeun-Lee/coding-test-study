## MST(Minimum Spanning Tree)

### 01. Spanning Tree(신장트리)

- 그래프의 모든 노드가 연결되어 있으면서 트리의 속성을 만족하는 그래프
  - 그래프의 모든 노드 포함
  - 모든 노드가 서로 연결
  - 트리의 속성 만족(사이클이 존재하지 않는다)

### 02. MST(최소 신장 트리)

가능한 Spanning Tree 중, 간선의 가중치의 합이 최소인 Spanning Tree를 지칭

[ 대표적인 최소신장트리 알고리즘 ]

- Kruskal's algorithm(크루스칼 알고리즘)
- Prim's algorithm(프림 알고리즘)

### 03. Kruskal's algorithm(크루스칼 알고리즘)

1. 모든 정점을 **독립적인 집합**으로 만든다([Union-Find](#04.-union-find))

2. 모든 간선을 비용을 기준으로 <u>정렬</u>하고, **비용이 작은 간선**부터 양 끝의 두 정점을 비교한다.

3. 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다
   (사이클이 생기지 않도록한다)

   > 탐욕 알고리즘을 기초로 함(눈 앞의 최소비용 선택 -> 최적의 솔루션)

### 04. Union-Find 알고리즘

- Disjoint Set을 표현할 때 사용하는 알고리즘. 트리 구조를 활용함
- 노드들 중에 <u>연결된 노드를 찾거나</u>, <u>노드들을 서로 연결할 때</u> 사용한다.
- Disjoint Set
  - 서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조(공통 원소가 없는 상호 배타적 부분 집합들로 나눠진 원소들에 대한 자료구조)
  - == 서로소 집합 자료구조

> 1. **Initialize**
>    n개의 원소가 개별 집합으로 이뤄지도록 초기화
> 2. **Union**
>    두 개별 집합을 하나의 집합으로(두 트리를 하나의 트리로)
> 3. **Find**
>    여러 노드가 존재할 때, 두 개의 노드를 선택하여, 현재 <u>두 노드가 서로 같은 그래프에 속하는지 판별</u>하기 위해 각 그룹의 **루트노드**를 확인한다.

Union 순서에 따라서, 최악의 경우 링크드 리스트와 같은 형태가 될 수 있다.
이 때 Find/Union 시 계산량이 O(N)이 될 수 있다. 이 문제를 해결하기 위해 union-by-rank, path compression 기법을 사용한다.

<img src="https://www.fun-coding.org/00_Images/worst_findunion.png" alt="img" style="zoom: 50%;" />

#### 04-1 ) union-by-rank

- 각 트리에 대해 높이(rank)를 기억해두고 union시에 두 트리의 높이(rank)가 다르면, rank가 작은 트리를 rank가 큰 트리에 붙인다
  (즉, 높이가 큰 트리의 루트 노드가 합친 집합의 루트 노드가 되게 한다)

> - 높이가 h인 트리를 만들기 위해 높이가 h-1인 두 개의 트리를 합쳐야 함
> - 높이가 h-1인 트리를 만들기 위해 최소 n개의 원소가 필요하다 가정 -> 높이가 h인 트리가 만들어 지기 위해 최소 2n개의 원소 필요
> - 따라서 시간복잡도는 O(logN)이 된다

#### 04-2) path compression

- Find를 실행한 노드에서 거쳐간 노드를 루트에 다이렉트로 연결하는 기법
- Find를 실행한 노드는 이후부터는 <u>루트 노드를 한번에 알 수 있다.</u>

- union-by-rank 와 path compression 기법 사용시 시간 복잡도는 다음 계산식을 만족함이 증명되었음  
  - <img src="https://render.githubusercontent.com/render/math?math=O(M log^*{N})"> 
  - $ log^*{N} $ 은 다음 값을 가짐이 증명되었음
    - N이 $ 2^{65536} $ 값을 가지더라도, $$log^*{N}$$ 의 값이 5의 값을 가지므로, 거의 O(1), 즉 상수값에 가깝다고 볼 수 있음

<div style="text-align:left">
<table>
  <tr>
    <th style="text-align:center">N</th>
    <th style="text-align:center">$$log^*{N}$$</th>
  </tr>
  <tr>
    <td style="text-align:left">1</td>
    <td style="text-align:left">0</td>
  </tr>
  <tr>
    <td style="text-align:left">2</td>
    <td style="text-align:left">1</td>
  </tr>
  <tr>
    <td style="text-align:left">4</td>
    <td style="text-align:left">2</td>
  </tr>
  <tr>
    <td style="text-align:left">16</td>
    <td style="text-align:left">3</td>
  </tr>
  <tr>
    <td style="text-align:left">65536</td>
    <td style="text-align:left">4</td>
  </tr>
  <tr>
    <td style="text-align:left">$$2^{65536}$$</td>
    <td style="text-align:left">5</td>
  </tr>
</table>
</div>

### 05. Kruskal's algorithm의 구현

```python
parent = dict()
rank = dict()

def find(node):
    # path compression
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)
    
    # union by rank
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2]+=1
def  make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()
    # 1. initialize
    for node in graph['vertices']:
        make_set(node)
    # 2. sort by weights
    edges = graph['edges']
    edges.sort()
    # 3. connect edges without cycle
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u): # 같은 그래프에 속하지 않는다면(루트노드 비교)
            union(node_v, node_u)
            mst.append(edge)
    return mst
```

O(ElogE)