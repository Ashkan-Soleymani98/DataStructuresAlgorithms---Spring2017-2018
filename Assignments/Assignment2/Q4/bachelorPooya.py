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

    def bubbleDown(self , index):
        while self.leftChildren(index) <= len(self.list) - 1:
            if self.rightChildren(index) <= len(self.list) - 1 and self.list[MinHeap.leftChildren(index)] >= self.list[MinHeap.rightChildren(index)]:
                tempIndex = self.rightChildren(index)
            else:
                tempIndex = self.leftChildren(index)
            if self.list[tempIndex] < self.list[index]:
                self.list[index] , self.list[tempIndex] = self.list[tempIndex] , self.list[index]
                index = tempIndex
            else:
                break

    def getMin(self):
        return self.list[1]

    def delMin(self):
        maxi = self.list[1]
        self.list[1] = self.list[-1]
        del(self.list[-1])
        self.bubbleDown(1)
        return maxi

    def size(self):
        return len(self.list) - 1

n = int(input())
if n != 1:
    array = input().split(" ")
    tempArray = [int(i) for i in array]
    array = tempArray
    amounts = input().split(" ")
    tempAmounts = [int(i) for i in amounts]
    amounts = tempAmounts

minHeap = MinHeap()
for i in range(n - 1):
    if array[i] == 0:
        minHeap.insert(amounts[i])
    else:
        while minHeap.size() >= amounts[i]:
            minHeap.delMin()

sum = 0
for i in minHeap.list:
    sum += i

print(sum)