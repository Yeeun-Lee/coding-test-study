##2531 회전초밥
 
N, d, k, c = [int(x) for x in input().split()]
 
sushi = []
 
def findvariety(variety):
    temp = set(eaten) #list to set : 중복된 값 제거
    if (c not in temp):
        variety = max(variety, len(temp)+1)
    else:
        variety = max(variety, len(temp))
    return variety
 
for dish in range(N):
    sushi.append(int(input()))
 
eaten = sushi[-k+1:] + sushi[:1] #k개 만큼의 접시 초기값
variety = 0;
variety = findvariety(variety);
 
for x in range(N-1):
    eaten.pop(0) #가장 앞에 있는 접시 빼기
    eaten.append(sushi[x+1]) # 다음 접시 추가
    variety = findvariety(variety)
 
print (variety)


#출처: https://lazyren.tistory.com/28 [Lazy Ren's Blog]
