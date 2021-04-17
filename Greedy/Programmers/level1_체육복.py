def solution(n, lost, reserve):
    _lost = set(lost)-set(reserve)
    _reserve = set(reserve)-set(lost)
    for st in _lost:
        if st+1 in _reserve:
            _reserve.remove(st+1)
        elif st-1 in _reserve:
            _reserve.remove(st-1)
        else:
            n-=1
    return n
# 조건을 잘 읽을것..
# 앞 뒤번호한테만 빌릴 수 있음..