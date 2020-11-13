n, m = map(int, input().split())
adjList = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    adjList[a].append(b)
    adjList[b].append(a)


def bfs(root):
    marks = [False] * n
    distances = [0] * n
    queue = list()
    queue.append(root)
    while len(queue) > 0:
        u = queue.pop(0)
        for v in adjList[u]:
            if not marks[v] and v != root:
                distances[v] = distances[u] + 1
                queue.append(v)
                marks[v] = True
    return max(distances)


maxi = 0
for i in range(n):
    temp = bfs(i)
    maxi = max(maxi, temp)
print(maxi)

