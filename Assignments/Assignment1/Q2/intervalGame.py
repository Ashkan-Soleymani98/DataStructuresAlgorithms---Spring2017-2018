n = int(input())
starts = [0] * 100002
ends = [0] * 100002
A = input().split(' ')
A[0] = int(A[0])
A[1] = int(A[1])
starts[A[0]] += 1
ends[A[1] + 1] += 1
itEnd = max(A) + 1
itStart = min(A)
for i in range(n - 1):
    A = input().split(' ')
    A[0] = int(A[0])
    A[1] = int(A[1])
    starts[A[0]] += 1
    ends[A[1] + 1] += 1
    itEnd = max(max(A) + 1 , itEnd)
    itStart = min(min(A) , itStart)
maxInterc = 0
temp = 0
for i in range(itStart , itEnd + 1):
    temp += starts[i]
    temp -= ends[i]
    if maxInterc < temp:
        maxInterc = temp
print(maxInterc)