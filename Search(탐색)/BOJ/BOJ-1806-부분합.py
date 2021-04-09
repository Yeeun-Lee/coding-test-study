# 투포인터
n, s = map(int, input().split())
arr = list(map(int, input().split()))

answer = n+1 # initialize
left, right = 0, 0
_sum = arr[0]

while left <= right and right < n:
    if _sum < s:
        right+=1
        if right < n:
            _sum += arr[right]
    elif _sum == s:
        answer = min(right-left+1, answer)
        right+=1
        if right < n:
            _sum+=arr[right]
    elif _sum > s:
        answer = min(right-left+1, answer)
        _sum-=arr[left]
        left+=1
        if left > right and left < n:
            right = left
            _sum = arr[left]
            
if answer > n:
    answer = 0
    
print(answer)
