#def solution(number, k): # 런타임에러의 굴레..
#     for r in range(k):
#         for i in range(len(number)-1):
#             if number[i]=='9':
#                 continue
#             if number[i] < number[i+1]:
#                 number = number[:i]+number[i+1:]
#                 break
#     return number

def solution(number, k):
    # use stack, 시간 차이 매우 큼
    answer = [number[0]]
    for num in number[1:]:
        while len(answer) > 0 and answer[-1] < num and k > 0:
            k-=1
            answer.pop()
        answer.append(num)
    if k!=0:
        answer = answer[:-k]
    return ''.join(answer)

