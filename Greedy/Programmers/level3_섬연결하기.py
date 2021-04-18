# def solution(n, costs):
#     costs.sort(key = lambda x:x[2])
#     visited = [False]*n
#     visited[0] = True
#     answer = 0
#     while not all(visited):
#         for c in costs:
#             if visited[c[0]] and visited[c[1]]:
#                 continue
#             if visited[c[0]] or visited[c[1]]:
#                 answer+=c[2]
#                 visited[c[0]], visited[c[1]] = True, True
#
#     return answer

def solution(n, costs):
    # kruskal algorithm
    answer = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    while len(routes)!=n:
        print(routes)
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                # routes.update([cost[0], cost[1]])
                routes|=set(cost[:2])
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return answer
