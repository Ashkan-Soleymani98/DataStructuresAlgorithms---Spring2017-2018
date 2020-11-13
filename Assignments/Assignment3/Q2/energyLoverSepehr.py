import sys
sys.setrecursionlimit(1000000)


def binarySearch(i , j):
    tmpFinal = (i + j) / 2
    if comparePart(tmpFinal) == 0:
        return tmpFinal
    elif comparePart(tmpFinal) == -1:
        return binarySearch(i , tmpFinal)
    elif comparePart(tmpFinal) == 1:
        return binarySearch(tmpFinal , j)

def comparePart(finalAmount):
    # print(finalAmount)
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
print("%.7f" % (binarySearch(minSource, avg)))




