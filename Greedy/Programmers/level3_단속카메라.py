def solution(routes):
    routes = sorted(routes)
    answer = 1
    _start, _end = routes.pop(0)
    while(routes):
        start, end = routes.pop(0)
        if end < _end:
            _end = end
        if start > _end:
            answer+=1
            _end = end
        _start = start
    return answer

routes = eval(input())
print(solution(routes))
            
