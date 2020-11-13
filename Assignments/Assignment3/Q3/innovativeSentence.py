def select2(t):
    return t * (t - 1) // 2


def pow2(t):
    return t * t


inp = input().split(" ")
n = int(inp[0])
x = int(inp[1])
k = int(inp[2])
numbers = list()
string = input().split(" ")
for i in range(n):
    numbers.append(int(string[i]))

numberSet = list(set(numbers))
numberSet.sort()
countNumbers = [numbers.count(i) for i in numberSet]

quotients1 = list()
quotients2 = list()
for i in numberSet:
    quotients1.append((i - 1) // x)
    quotients2.append(i // x)

num = 0
i = 0
j = 0
while i <= j < len(numberSet):
    if quotients2[j] - quotients1[i] == k:
        if k != 0:
            num += countNumbers[i] * countNumbers[j]
            if j + 1 >= len(numberSet):
                i += 1
            else:
                j += 1
        else:
            counter = countNumbers[i]
            if countNumbers[j] > 1:
                num += pow2(countNumbers[i]) - select2(countNumbers[i])
            else:
                num += 1
            while i <= j < len(numberSet) and quotients2[j] == quotients1[i]:
                if i != j:
                    counter += countNumbers[j]
                    if countNumbers[j] > 1:
                        num += pow2(countNumbers[j]) - select2(countNumbers[j])
                    else:
                        num += 1
                if j + 1 >= len(numberSet):
                    i += 1
                else:
                    j += 1
            num += select2(counter)

    elif quotients2[j] - quotients1[i] > k:
        i += 1
    elif quotients2[j] - quotients1[i] < k:
        j += 1

print(num)
