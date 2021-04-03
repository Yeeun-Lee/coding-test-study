## Python 사용하기:snake:

### Container별 methods:star:

- Tuple : 위치(index)에 따른 의미

- Set : 포함여부(집합)

  - methods

  ```python
  sample1, sample2 = set(), set() # 몇개 원소가 들어 있다고 가정
  # 추가
  sample1.add(1)
  # 차집합
  z = sample1.difference(sample2) # in sample1 not in sample2
  # == sample1 - sample2
  # 교집합
  z = sample1.intersection(sample2)
  # 부분집합 boolean
  sample1.issubset(sample2)
  # 합집합
  z = sample1.union(sample2)
  # => sample1 |= sample2
  ```

  

- List : 위치(index)와 원소의 관계

  - methods

  ```python
  sample = list()
  # 역순
  sample[::-1]
  sample.reverse() #
  list(reversed(sample))
  # 정렬
  sorted(sample)
  sample.sort() #
  sample.sort(key = lambda x: x[1], reverse = True) # 세부설정
  ```

  - list comprehension

  ```python
  graph = [[] for _ in range(n)]
  # if else
  sample = [sp for i in range(n) if sp>1]
  sample = [sp if sp>1 else 0 for i in range(n)]
  ```

  - graph handling

  ```python
  sample = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
  # graph
  g = [list(s) for s in sample]
  # transpose
  g_t = list(map(list, zip(*sample)))
  # rotate
  g_r_90 = list(zip(*sample[::-1]))
  ```

- Dict : key와 value의 관계

  - methods

  ```python
  # dictionary 만들기
  d = dict()
  d = dict.fromkeys(somekeys, value) # key : value(specific)
  # get value with specified key
  d.get('a')
  # b라는 key가 없는 경우 -> 1000 return(리턴할 값을 지정) 
  d.get('b', 1000)
  # => input으로부터 사전을 만들때(ex, word counter)
  sample = 'word'
  word_counter = dict()
  for s in word_counter:
      word_counter[s] = word_counter.get(s, 0) + 1
  # (key, value)로 이루어진 리스트 반환
  d.items()
  #=> keys() : key반환
  ```

  

### 문제 유형별 대처

#### 방향벡터:arrow_right:

2/3차원 배열이나 BFS/DFS에서 많이 사용한다

- 탐색 방향에 따라 방향벡터를 생성해준다.

  ```python
  # 동서남북
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for dx, dy in directions:
      nx, ny = x+dx, y+ny
  ```

- 반시계방향
  dx = [0, -1, 0, 1]
  dy = [1, 0, -1, 0]
- 시계방향
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

#### 시간:clock10:

datetime같은 모듈에서 timedelta등으로 계산하는 것보다는, parsing으로 시, 분, 초 등의 단위로 쪼개준 다음 최소 단위의 시간으로 전부 변환해주는 것이 편리하다.

예를 들어 입력이 "10:30:20"# HH:MM:SS 라고 한다면

```python
inp = "10:30:20"
inp = inp.split(":")
time = int(inp[0])*(60**2) + int(inp[1])*60 + int(inp[2]) # 초 단위로 변경

# 차이를 구한 다음 다시 원래 단위로 변환하기
diff = time1 - time2
hour = diff//(60**2)
minute = diff//60
sec = diff%60
```

