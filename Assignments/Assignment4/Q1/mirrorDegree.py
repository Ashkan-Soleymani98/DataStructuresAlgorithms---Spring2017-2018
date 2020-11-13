prime = 907199
radix = 31
inp = input()
prefixHash = list()
suffixHash = [0] * len(inp)
prefixHash.append(ord(inp[0]) - ord('a'))
for i in range(1, len(inp)):
    prefixHash.append((prefixHash[i - 1] * radix + (ord(inp[i]) - ord('a'))) % prime)
suffixHash[-1] = ord(inp[-1]) - ord('a')
for i in range(len(inp) - 2, -1, -1):
    suffixHash[i] = ((suffixHash[i + 1] * radix + (ord(inp[i]) - ord('a'))) % prime)

powers = [1]
for i in range(len(inp) + 1):
    powers.append((powers[-1] * radix) % prime)


def hashPrefix(i, j):
    return abs((prefixHash[j] - prefixHash[i] * powers[j - i]) % prime)


def hashSuffix(i, j):
    return abs((suffixHash[i] - suffixHash[j] * powers[j - i]) % prime)


degrees = [1] + [0] * (len(inp) - 1)
for i in range(1, len(inp)):
    if hashPrefix(0, i) == hashSuffix(0, i):
        degrees[i] = degrees[(i + 1) // 2 - 1] + 1

sum = 0
for i in degrees:
    sum += i

print(sum)