def semiSort(n , A):
    for i in range(1, n - 1):
        if i % 2 == 0:
            maxSet(A , i - 1 , i , i + 1)
        else:
            minSet(A , i - 1 , i , i + 1)
    if (n - 1) % 2 == 0 and A[n - 1] < A[n - 2]:
        A[n - 1] , A[n - 2] = A[n - 2] , A[n - 1]
    if (n - 1) % 2 == 1 and A[n - 1] > A[n - 2]:
        A[n - 1], A[n - 2] = A[n - 2], A[n - 1]
    return A
def maxSet(A , a , b , c):
    if A[a] >= A[b] and A[a] >= A[c]:
        A[a] , A[b] = A[b] , A[a]
    elif A[b] <= A[c]:
        A[c] , A[b] = A[b] , A[c]
def minSet(A , a , b , c):
    if A[a] <= A[b] and A[a] <= A[c]:
        A[a], A[b] = A[b], A[a]
    elif A[c] <= A[b]:
        A[c], A[b] = A[b], A[c]

n = int(input())
A = input().split(' ')
for i in range(n):
    A[i] = int(A[i])
print(*semiSort(n , A))
