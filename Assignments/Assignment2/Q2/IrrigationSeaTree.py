import sys
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self , label , parent , waterDemandingAmount):
        self.label = label
        self.parent = parent
        self.leftChild = None
        self.rightChild = None
        self.waterDemandingAmount = waterDemandingAmount

    @classmethod
    def insert(cls, node, label, waterDemandingAmount, updatingNotes):
        if label < node.label :
            updatingNotes.append(node)
            waterDemandingAmount += 1
            if node.leftChild is not None:
                Node.insert(node.leftChild, label , waterDemandingAmount , updatingNotes)
            else:
                node.leftChild = Node(label, node , waterDemandingAmount)
                for nod in updatingNotes:
                    nod.waterDemandingAmount += waterDemandingAmount
        elif label > node.label:
            updatingNotes.append(node)
            waterDemandingAmount += 1
            if node.rightChild is not None:
                Node.insert(node.rightChild, label , waterDemandingAmount , updatingNotes)
            else:
                node.rightChild = Node(label, node , waterDemandingAmount)
                for nod in updatingNotes:
                    nod.waterDemandingAmount += waterDemandingAmount
        else:
            print(node.waterDemandingAmount)


n = int(input())
root = Node(int(input()) , None , 1)
for i in range(n - 1):
    Node.insert(root , int(input()) , 1 , list())

    

import sys
sys.setrecursionlimit(1000000)


def binarySearch(i , j):
    tmpFinal = (i + j) / 2
    if comparePart(tmpFinal) == 0:
        return tmpFinal
    elif comparePart(tmpFinal) == 1:
        return binarySearch(i , tmpFinal)
    elif comparePart(tmpFinal) == -1:
        return binarySearch(tmpFinal , j)

def comparePart(finalAmount):
    semiSum = 0
    for i in range(n):
        semiSum += (k / 100) * max(resources[i] - finalAmount, 0)
    if sum - n * finalAmount - semiSum > 0.000001:
        return 1
    elif n * finalAmount + semiSum - sum > 0.000001:
        return -1
    else:
        return 0


inp = input().split(" ")
n = int(inp[0])
k = int(inp[1])
# print(n , k)
string = input().split(" ")
resources = list()
sum = 0
minSource = int(string[0])
for i in range(n):
    tmp = int(string[i])
    resources.append(tmp)
    minSource = min(minSource, tmp)
    sum += int(tmp)
# print(resources)
# print(sum , minSource)
avg = sum / n
print("%.6f" % (binarySearch(minSource, avg)))




