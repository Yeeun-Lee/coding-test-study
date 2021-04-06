### 이분탐색(Binary Search)

탐색할 자료를 둘로 나누어 해당 데이터가 있을만한 곳을 탐색하는 방

#### 이분탐색에서의 Divide and Conquer process

- Divide : 리스트를 두 개의 서브 리스트로 나눈다(mid 값을 지정)
- Conquer 
  - 검색할 숫자(search) > mid 이면, 뒷 부분의 서브리스트에서 검색할 숫자를 찾는다
  - 검색할 숫자(search) < mid 이면, 뒷 부분의 서브리스트에서 검색할 숫자를 찾는다.



#### 구현

- 탐색의 범위를 지정한다 : start, end(혹은 left, right)
  - 탐색은 **while left(start) <= right(end)**
- 중간값을 생성한다 : mid = (start+end)//2
  - 이후 mid값을 변경해주면서 탐색한다.
- 조건에 따라 mid+1 혹은 mid-1로 start와 end값을 변경해준다
  - start = mid + 1 or end = mid-1

> value는 어떤 값을 사용 ? : 찾고자 하는 값!
>
> - 버스에 몇명이 탈 수 있을까 ? : 인원수의 최소값 - left, 최대값 - right

#### 시간복잡도

n개의 리스트를 매번 2로 나누어 1이 될 때까지 비교연산을 k회 진행하기 때문에

O(logn)이 된다 --> 입력 제한이 엄청나게 큰 문제가 나왔을 경우에는 이분탐색을 고려해보는 것이 좋다.





