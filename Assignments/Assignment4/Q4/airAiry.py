class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.sets = [[i] for i in range(n)]
        self.foremans = [i for i in range(n)]

    def find(self, u):
        return self.foremans[u]

    def union(self, u, v):
        u_set = self.find(u)
        v_set = self.find(v)

        if u_set == v_set:
            return False

        if len(self.sets[v_set]) < len(self.sets[u_set]):
            v_set, u_set = u_set, v_set

        for i in self.sets[u_set]:
            self.sets[v_set].append(i)
            self.foremans[i] = v_set

        return True


prime = pow(10, 9) + 9
inp = input().split()
n = int(inp[0])
m = int(inp[1])
dsu = DisjointSet(n)
k = 0
for i in range(m):
    inp = input().split()
    a = int(inp[0]) - 1
    b = int(inp[1]) - 1
    if not dsu.union(a, b):
        k = (2 * k + 1) % prime
    print(k)
