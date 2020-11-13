class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def oneColumnsFinder(oneColumns , rowNum):
    n = len(oneColumns[0])
    for i in range(n):
        j = min(rowNum , oneColumns[1][i])
        if oneColumns[0][i] > 0:
            oneColumns[0][i] -= 1
        while plate[j][i] == 1 and j >= 0:
            oneColumns[0][i] += 1
            j -= 1
        oneColumns[1][i] = j;
    return oneColumns

def maxFinderInRow(bases):
    n = len(bases)
    mins = [0] * n
    maxs = [0] * n
    stack = Stack()
    for i in range(n):
        while not stack.isEmpty() and stack.top()[1] > bases[i]:
            temp = stack.pop()
            maxs[temp[0]] = i
        if not stack.isEmpty():
            mins[i] = stack.top()[0]
        else:
            mins[i] = -1
        temp = [i , bases[i]]
        stack.push(temp)

    while not stack.isEmpty():
        temp = stack.pop()
        maxs[temp[0]] = n

    maxi = 0
    for i in range(n):
        if maxi < (maxs[i] - mins[i] - 1) * bases[i]:
            maxi = (maxs[i] - mins[i] - 1) * bases[i]
    return maxi


m , n = input().split(" ")
m = int(m)
n = int(n)
plate = [[0 for i in range(n)] for i in range (m)]
for i in range(m):
    inp = list(input())
    # inp = input().split(" ")
    for j in range(n):
        if inp[j] == '.':
            plate[i][j] = 1
        elif inp[j] == '#':
            plate[i][j] = 0

oneColumns = [[0] * n , [m - 1] * n]

maximum = 0
for i in range(m - 1, -1 , -1):
    oneColumns = oneColumnsFinder(oneColumns , i)
    temp = maxFinderInRow(oneColumns[0])
    if temp > maximum:
        maximum = temp

print(maximum)
