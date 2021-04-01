# N과 사칙연산만으로 number를 표현할 수 있다.
# 이 중 최소값.
import sys

def solution(N, number):
    answer = -1
    dp = []
    for i in range(1, 9):
        temp = set()
        temp.add(int(str(N)*i))
        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    temp.add(x+y)
                    temp.add(x-y)
                    temp.add(x*y)
                    if y!=0:
                        temp.add(x//y)

        if number in temp:
            answer = i
            break
        dp.append(temp)
        
    return answer

if __name__=="__main__":
    N = int(input())
    number = int(input())
    print(solution(N, number))
    
