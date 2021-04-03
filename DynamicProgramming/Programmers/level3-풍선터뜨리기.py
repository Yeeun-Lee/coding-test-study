def solution(a):
    left, right = float('inf'), float('inf')
    answer = [False]*len(a)
    for i in range(len(a)):
        print(a[-1-i])
        if left > a[i]:
            left = a[i]
            answer[i] = True
        if right > a[-1-i]:
            right = a[-1-i]
            answer[-1-i] = True
    return sum(answer)

a = eval(input())
print(solution(a))
