import sys
sys.setrecursionlimit(100000)
prime = 1251461
radix = 91
w = pow(10, 9) + 7


def power(base, exp, q):
    if exp == 1:
        return base
    if exp % 2 == 1:
        return ((power(base, exp // 2, q) ** 2) * base) % q
    else:
        return (power(base, exp // 2, q) ** 2) % q


def hashPrefix(i, j):
    return abs((prefixHash[j] - (prefixHash[i - 1] if i > 0 else 0) * pow(radix, j - i + 1, prime)) % prime)


# print(power(5, 907198))
prefixHash = list()
t = int(input())
for j in range(0, t):
    inp = input().split()
    n = int(inp[0])
    k = int(inp[1])
    inp = input().split()
    p = [int(i) for i in inp]
    pLen = len(p)
    inp = input().split()
    indices = [int(i) for i in inp]
    inp = None
    prefixHash = list()
    prefixHash.append(p[0])
    for i in range(1, pLen):
        prefixHash.append((prefixHash[i - 1] * radix + p[i]) % prime)
    P = None
    occupyedIndices = pLen
    isValid = True
    for i in range(len(indices) - 1):
        if indices[i] + pLen - 1 >= indices[i + 1]:
            if hashPrefix(indices[i + 1] - indices[i], pLen - 1) != hashPrefix(0, indices[i] + pLen - 1 - indices[i + 1]):
                isValid = False
                break
            occupyedIndices += indices[i + 1] - indices[i]
        else:
            occupyedIndices += pLen
    if isValid and indices[len(indices) - 1] + pLen - 1 > n:
        isValid = False
    num = 0
    if isValid:
        num = pow(k, n - occupyedIndices, w) % w
    print("Case " + str(j + 1) + ": " + str(num))

