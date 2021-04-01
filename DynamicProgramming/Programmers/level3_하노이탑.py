def solution(n):
    def hanoi(n, f, t, sub):
        if n == 1:
            answer.append([f, t])
            return
        hanoi(n-1, f, sub, t)
        answer.append([f, t])
        hanoi(n-1, sub, t, f)
    answer = []
    hanoi(n, 1, 3, 2)
    return answer

n = int(input())
print(solution(n))
