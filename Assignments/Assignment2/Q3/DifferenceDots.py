class MinHeap:
    def __init__(self):
        self.list = [0]

    @classmethod
    def parent(cls , i):
        return i // 2

    @classmethod
    def rightChildren(cls , i):
        return 2 * i + 1

    @classmethod
    def leftChildren(cls , i):
        return 2 * i

    def insert(self , value):
        self.list.append(value)
        self.bubbleUp(len(self.list) - 1)

    def bubbleUp(self , index):
        while index > 1:
            if not self.list[index] < self.list[MinHeap.parent(index)]:
                return
            self.list[index] , self.list[MinHeap.parent(index)] = self.list[MinHeap.parent(index)] , self.list[index]
            index = MinHeap.parent(index)


    def inOrder(self , index):
        orderedList = list()
        if index >= len(self.list):
            return orderedList
        orderedList.extend(self.inOrder(MinHeap.leftChildren(index)))
        orderedList.append(self.list[index])
        orderedList.extend(self.inOrder(MinHeap.rightChildren(index)))
        return orderedList

n = int(input())
minHeap = MinHeap()
ascendingList = list()
for i in range(n):
    inp = int(input())
    minHeap.insert(inp)
    ascendingList.append(inp)
ascendingList.sort()
minHeapList = minHeap.inOrder(1)
differences = 0
for i in range(len(ascendingList)):
    if ascendingList[i] != minHeapList[i]:
        differences += 1
print(differences)