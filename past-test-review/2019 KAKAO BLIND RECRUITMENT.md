## 2019 KAKAO BLIND RECRUITMENT

진짜 코딩테스트처럼 다섯시간 잡고 전부 풀어보려고 했는데 아직은 부족한 실력이었다. level3 해당하는 문제까지만 시간 안에 잡고 풀어보았고, 못 푼 문제에 대해서는 구글링으로 정리하는 방향으로 진행했다. level 1-2에 해당하는 세문제는 굉장히 금방 풀었다. 확실히 이것저것 풀다보니 쉬운 문제의 구현 시간은 단축된듯 하다.

### 오픈채팅방

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/42888)

##### 입출력 예

| record                                                       | result                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]` | `["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]` |

#### solution

- Enter과 Leave에 대해서는 "님이 들어왔습니다" 혹은 "님이 나갔습니다"를 유저 아이디와 함께 리스트로 저장하였다. 
- 유저 아이디에 대한 닉네임을 Enter와 Change에서 업데이트 하였다.
- 최종 출력에 대해 유저 아이디로 닉네임에 접근하고, 구문과 join해 주었다.

```python
def solution(record):
    answer = []
    chats = []
    users = {}
    for rec in record:
        info = rec.split(" ")
        if info[0] == "Enter":
            users[info[1]] = info[2]
            chats.append([info[1], "님이 들어왔습니다."])
        elif info[0] == "Leave":
            chats.append([info[1], "님이 나갔습니다."])
        else:
            users[info[1]] = info[2]

    for c in chats:
        answer.append("".join([users[c[0]], c[1]]))
    return answer
```

### 실패율

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/42889)

##### 입출력 예

| N    | stages                   | result      |
| ---- | ------------------------ | ----------- |
| 5    | [2, 1, 2, 6, 2, 4, 3, 3] | [3,4,2,1,5] |
| 4    | [4,4,4,4,4]              | [4,1,2,3]   |

#### solution

- 각 스테이지에 멈춰 있는 유저의 수를 세준다.
- 스테이지별로 해당 스테이지 이상의 스테이지에 있는 유저들의 수의 합을 구해준다.
  - 0일 경우 실패율은 0
  - 아니라면 (해당 스테이지에 멈춰 있는 유저/유저의 합)을 실패율로 사용한다.
  - (스테이지, 실패율)을 rates에 저장한다.
- rates를 실패율 내림차순 -> 스테이지 오름차순(동일 실패율에 대해) 으로 정렬한다.

```python
def solution(N, stages):
    stage_info = {i:0 for i in range(1, N+2)}
    rates = []

    for s in stages:
        stage_info[s]+=1
    stage_info = list(stage_info.items())
    for i, stage in enumerate(stage_info):
        _sum = sum(list(zip(*stage_info[i:]))[1]) # i+1 stage를 도전한 사람의 수
        if _sum==0:
            rates.append((stage[0], 0))
        else:
            rates.append((stage[0], stage[1]/_sum))
    rates.sort(key = lambda x: (-x[1], x[0]))
    answer = [stage[0] for stage in rates if stage[0]<=N]
    
    return answer
```

### 후보키

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/42890)

##### 입출력 예

| relation                                                     | result |
| ------------------------------------------------------------ | ------ |
| `[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]` | 2      |

#### solution

- relation 테이블을 transpose해준다(column별로 접근할 수 있도록)
- cols에 0~columns의 수(즉, column index)를 저장한다
  - 하나씩 검사하면서 하나의 컬럼이 키로 사용될 수 있으면 cols에서 해당 index를 제외한다.
- 제외하고 남은 컬럼들에 대해 2~남은 컬럼의 수 까지 iteration을 돌면서 조합을 구하고, 컬럼의 조합으로 만들어진 열이 후보키의 속성을 가지는지 검사한다.
  - 최소성을 만족시켜야 하므로 이미 포함되어 있는 후보키가 신규로 들어오는 것의 부분집합인지 검사한다.

```python
from itertools import combinations

def check_unique(col):
    for value in col:
        if col.count(value)>1:
            return False
    return True

def solution(relation):
    answer = 0
    relation_t = list(zip(*relation))
    cols = [i for i in range(len(relation_t))]
    for i in range(len(cols)):
        if check_unique(relation_t[i]):
            answer+=1
            cols.remove(i)

    uniques = []
    for num in range(2, len(cols)+1):
        for comb in list(combinations(cols, num)):
            temp = []
            key = True
            for u in uniques:
                if len(set(u)-set(comb))==0:
                    key = False
                    break
            if not key:
                continue
            
            for c in comb:
                temp.append(relation_t[c])
            if check_unique(list(zip(*temp))) and key:
                answer+=1
                uniques.append(comb)
                
    return answer
```

---

여기까지는 꽤 빨리 풀었다.

### 길 찾기 게임

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/42892)

##### 입출력 예

| nodeinfo                                                  | result                                    |
| --------------------------------------------------------- | ----------------------------------------- |
| [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]] | [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]] |

#### solution

나는 이진트리 구현에서 꽉 막혀서 탐색으로 넘어갈수조차 없었다. 그동안 알고리즘 공부하면서 객체지향을 약간 등한시(?) 하고 트리같은걸 사전+리스트로 어거지로 짰는데, 막상 블로그를 참고해서 코드리뷰를 해보니 객체로 짜면 이렇게나 쉽구나 싶다.([참조블로그 링크(https://codedrive.tistory.com/329)](https://codedrive.tistory.com/329))

```python
import sys
sys.setrecursionlimit(1000000)

class Tree:
    def __init__(self, data, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right
preordered = []
postordered = []
def preorder(node, nodeinfo):
    preordered.append(nodeinfo.index(node.data)+1)
    
    if node.left:
        preorder(node.left, nodeinfo)
    if node.right:
        preorder(node.right, nodeinfo)
    
def postorder(node, nodeinfo):
    if node.left:
        postorder(node.left, nodeinfo)
    if node.right:
        postorder(node.right, nodeinfo)
    postordered.append(nodeinfo.index(node.data)+1)
    
def solution(nodeinfo):
    answer = []
    sorted_node = sorted(nodeinfo, key = lambda x: (-x[1], [0]))

    root = None
    for node in sorted_node:
        if not root:
            root = Tree(node)
        else:
            current = root
            while True:
                if node[0] < current.data[0]: # left
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(node)
                        break
                if node[0] > current.data[0]: # right
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(node)
                        break
                break
    preorder(root, nodeinfo)
    postorder(root, nodeinfo)
    answer.append(preordered)
    answer.append(postordered)
    
    return answer
```

### 매칭 점수

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/42893)

##### 입출력 예 #1

- word : blind

- pages :

  ```
  ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
  ```

#### solution

문자열 처리 공부를 해야하는 이유. 덕분에 정규식을 다시 공부했다. 데이터 사이언스용 코딩만 하다보니 문자열을 delim으로 split만 하면 되는 상태로 깔끔하게 만드는 것에 집착했었는데, 그냥 character 단위로 붙여서 counting하는 방법으로 하는게 가장 간단했다.

```python
import re

def page_link(html):
    pattern = '<meta\s.+?content=\"(https://.+)\"/>'
    return re.search(pattern, html).group(1)

def outer_link(html):
    pattern1 = '<a href=\"(\S*)\">'
    # page_link와 동일한 방식을 사용했을 때 space 이후에 다른 게 나오는 경우가 있어서
    # 테스트 케이스 통과를 못했다. 
    return re.findall(pattern1, html)

def body_content(html):
    pattern2 =  '<body>((.|\s)+)</body>'
    return re.search(pattern2, html).group(1)

def solution(word, pages):
    answer = 0
    page_index = {page_link(html):i for i, html in enumerate(pages)}
    base_scores = [0]*len(pages)
    link_scores = [0]*len(pages)

    for i in range(len(pages)):
        body = body_content(pages[i])
        count = 0
        temp = ""
        for idx, char in enumerate(body.lower()):
            if char.isalpha():
                temp+=char
                if not body[idx+1].isalpha():
                    if temp == word.lower():
                        count+=1
                        temp = ""
            else:
                temp = ""
        base_scores[i] = count
        links = outer_link(pages[i])
        for link in links:
            if link in page_index:
                link_scores[page_index[link]]+=(count/len(links))

    _max_value = 0
    for i in range(len(pages)):
        if base_scores[i]+link_scores[i] > _max_value:
            _max_value = base_scores[i]+link_scores[i]
            answer = i

    return answer
```

