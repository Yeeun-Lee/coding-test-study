import sys
sys.setrecursionlimit(10000)

# dfs 사용 풀이 - 64ms
L, C = map(int, input().split())
letters = input().split()
letters.sort() # 오름차순으로 정렬

def promising(current):
    vowels = 'aeiou'
    v_cnt = 0
    for char in current:
        if char in vowels:
            v_cnt+=1
    if v_cnt<1:
        return False
    if L - v_cnt < 2:
        return False
    return True

def dfs(pwd, idx):
    if C-idx-1 < L-len(pwd): # 인덱스를 기준으로 남은 알파벳만으로 패스워드를 완성할 수 없을 때에는 종료한다.
        return
    if len(pwd) == L and promising(pwd):
        print(pwd) # password의 길이가 주어진 값이고, 조건을 만족할 때에만 출력
    else:
        for i in range(idx+1, C): # 현재 알파벳의 인덱스를 기준으로 뒤 알파벳만 탐색하도록 한다.
            dfs(pwd+letters[i], i)
            
for i in range(C):
    # 오름차순으로 정렬된 결과만 반환
    # 따라서 시작 글자보다 이전 순위의 알파벳은 사용될 수 없다.
    # 모든 알파벳에 대해 수행
    dfs(letters[i], i)

# 강의 - 조합 사용(combinations), 68ms
from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())

array = input().split()
array.sort()

for password in combinations(array, l):
    count = 0
    for i in password:
        if i in vowels:
            count+=1
    if count >=1 and count<=l-2:
        print(''.join(password))
