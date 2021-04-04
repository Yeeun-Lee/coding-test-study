def solution(genres, plays):
    records = dict()
    for i, gen in enumerate(genres):
        records[gen] = records.get(gen, [])+[(plays[i], i)]
    # records = { gen1 : [(gen1-1's plays:gen1-1's id), ...], gen2 : [(..)]}
    for gen in records.keys():
        records[gen].sort(key = lambda x: (-x[0], x[1]))
        # plays 내림차순, id 오름차순 정렬
    records = sorted(list(records.items()), key = lambda x : sum(list(zip(*x[1]))[0]), reverse = True)
    # lambda ~ : plays의 합계 내림차순 정렬
    answer = []
    for rec in records:
        if len(rec[1])<2: # 속한 노래가 하나이면 하나만 출력
            answer.append(rec[1][0][1])
        else:
            answer+=list(zip(*rec[1]))[1][:2] # 앞에서 두개만 정답에 추가
    
    return answer

genres = eval(input())
plays = eval(input())
print(solution(genres, plays))
