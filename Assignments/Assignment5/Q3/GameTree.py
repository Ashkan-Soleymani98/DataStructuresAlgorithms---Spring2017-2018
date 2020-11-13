n = int(input())
m = n - 1
adjList = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    adjList[a].append(b)
    adjList[b].append(a)

# print(adjList)

marks = [False] * n
subTreeNodes = [1] * n


def dfs(root):
    marks[root] = True
    for u in adjList[root]:
        if not marks[u]:
            dfs(u)
            subTreeNodes[root] += subTreeNodes[u]



dfs(0)
odds = 0
evens = 0
for i in subTreeNodes:
    if i % 2 == 0:
        evens += 1
    else:
        odds += 1

print(odds, evens)