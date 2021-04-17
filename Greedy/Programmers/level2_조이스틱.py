def solution(name):
    name_arr = [min(ord(i)-ord("A"), ord("Z")-ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += name_arr[idx]
        name_arr[idx] = 0
        if sum(name_arr) == 0:
            break
        left, right = 1, 1
        while name_arr[idx-left]==0:
            left+=1
        while name_arr[idx+right]==0:
            right+=1
        answer+=left if left < right else right
        idx+=-left if left < right else right
    return answer
