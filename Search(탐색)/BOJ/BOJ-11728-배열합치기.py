# 투포인터
n, m = map(int, input().split())
# mapping 안해도 예시로 나온 테스트케이스는 돌아가는데 제출하면 틀림.
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i, j = 0, 0
answer = []
while i<n and j<m:

    if A[i]>B[j]:
        answer.append(B[j])
        j+=1
    else:
        answer.append(A[i])
        i+=1
while (i<n):
    answer.append(A[i])
    i+=1
while (j<m):
    answer.append(B[j])
    j+=1

for a in answer:
    print(a, end=' ')