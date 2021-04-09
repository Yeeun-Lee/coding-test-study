# 투포인터
n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
_sum = arr[0]
answer = 0

while left <= right and right < n:
    if _sum < m:
       right+=1
       if right < n:
           _sum+=arr[right]
    elif _sum == m:
        answer+=1
        right+=1
        if right < n:
            _sum+=arr[right]
    elif _sum > m:
        _sum-=arr[left]
        left+=1
        if left > right and left < n:
            right = left
            _sum = arr[left]
print(answer)
