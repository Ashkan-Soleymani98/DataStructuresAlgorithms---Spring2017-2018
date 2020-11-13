class binaryTrieNode:
    def __init__(self):
        self.number = 0
        self.leftChild = None
        self.rightChild = None


def insertInTrie(node, string, index):
    if index == len(string):
        node.number += 1
        return
    if string[index] == '0':
        if node.leftChild is not None:
            node.number += 1
            insertInTrie(node.leftChild, string, index + 1)
        else:
            node.leftChild = binaryTrieNode()
            node.number += 1
            insertInTrie(node.leftChild, string, index + 1)
    elif string[index] == '1':
        if node.rightChild is not None:
            node.number += 1
            insertInTrie(node.rightChild, string, index + 1)
        else:
            node.rightChild = binaryTrieNode()
            node.number += 1
            insertInTrie(node.rightChild, string, index + 1)
    return


def search(node, string, index):
    if index == len(string):
        return node
    if string[index] == '0':
        return search(node.leftChild, string, index + 1)
    elif string[index] == '1':
        return search(node.rightChild, string, index + 1)


def delete(node, string, index):
    if index == len(string):
        node.number -= 1
        return node
    if string[index] == '0':
        node.number -= 1
        return delete(node.leftChild, string, index + 1)
    elif string[index] == '1':
        node.number -= 1
        return delete(node.rightChild, string, index + 1)


def findMaxXor(node, string, index, outStr):
    if index == len(string):
        return outStr
    if node is None:
        return None
    if string[index] == '0':
        if node.rightChild is not None and node.rightChild.number != 0:
            outStr += '1'
            return findMaxXor(node.rightChild, string, index + 1, outStr)
        else:
            outStr += '0'
            return findMaxXor(node.leftChild, string, index + 1, outStr)
    elif string[index] == '1':
        if node.leftChild is not None and node.leftChild.number != 0:
            outStr += '1'
            return findMaxXor(node.leftChild, string, index + 1, outStr)
        else:
            outStr += '0'
            return findMaxXor(node.rightChild, string, index + 1, outStr)


def castTo32Bit(string):
    return string.zfill(32)


root = binaryTrieNode()
# insertInTrie(root, "0100", 0)
# insertInTrie(root, "001", 0)
# insertInTrie(root, "01", 0)
# delete(root, "0100", 0)
# print()
n = int(input())
# print(castTo32Bit("{0:b}".format(n)))
insertInTrie(root, castTo32Bit("{0:b}".format(0)), 0)
for i in range(n):
    str = input().split(" ")
    if str[0] == "add":
        insertInTrie(root, castTo32Bit("{0:b}".format(int(str[1]))), 0)
    elif str[0] == "rem":
        delete(root, castTo32Bit("{0:b}".format(int(str[1]))), 0)
    elif str[0] == "ans":
        output = findMaxXor(root, castTo32Bit("{0:b}".format(int(str[1]))), 0, "")
        # print(output)
        if output is not None:
            print(int(output, 2))