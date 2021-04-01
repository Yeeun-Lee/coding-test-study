# 이분탐
def solution(n, times):
    answer = 0
    left, right = 1, max(times)*n

    while left <= right:
        # 한 심사관에게 주어진 시간
        mid = (left+right)//2
        people = 0

        for i in times:
            # 각 심사관마다, 주어진 시간동안 몇명의 사람을 심사할 수 있는가
            # mid 보다 작을 경우는 몫이 0
            people+=mid//i
            # 모든 사람을 심사할 수 있으면 반복문을 벗어난다.
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid -1
            # 모든 사람을 심사할 수 있을 때, 시간을 줄여본다(최소 시간을 찾는 것이 목표이기 때문에)
        elif people < n:
            left = mid +1
    return answer


n = int(input())
times = [7, 10]
print(solution(n, times))
