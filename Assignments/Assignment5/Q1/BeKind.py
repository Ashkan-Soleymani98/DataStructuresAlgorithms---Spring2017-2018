n , m = map(int, input().split())
amount = [0] * n
for i in range(m):
    a, b, c = map(int, input().split())
    amount[a] += c
    amount[b] -= c
sum = 0
for i in amount:
    sum += abs(i)
sum = sum // 2
print(sum)