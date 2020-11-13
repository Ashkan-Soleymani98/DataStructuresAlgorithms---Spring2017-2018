class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.sets = [[i] for i in range(n)]
        self.foremans = [i for i in range(n)]
        self.zarbaties = [i for i in range(n)]

    def find(self, u):
        return self.foremans[u]

    def union(self, u, v):
        u_set = self.find(u)
        v_set = self.find(v)

        if u_set == v_set:
            return

        if len(self.sets[v_set]) < len(self.sets[u_set]):
            v_set, u_set = u_set, v_set

        for i in self.sets[u_set]:
            self.sets[v_set].append(i)
            self.foremans[i] = v_set

    def ask(self, u, v):
        return self.find(u) == self.find(v)

    def normal(self, u, v):
        self.union(u, v)

    def zarbati(self, u, v):
        # u_set = self.find(u)
        # w = self.zarbaties[u_set]
        # if v <= w:
        #     return
        # for i in range(w, v):
        #     self.union(i, v)
        # u_set = self.find(u)
        # self.zarbaties[u_set] = v
        i = self.zarbaties[u]
        while i < v:
            self.union(i, v)
            if self.zarbaties[i] > i:
                i = self.zarbaties[i]
            else:
                self.zarbaties[i] = v
                i += 1
        self.zarbaties[u] = v



inp = input().split()
n = inp[0]
q = inp[1]
n = int(n)
q = int(q)
dsu = DisjointSet(n)
for i in range(q):
    inp = input().split()
    a = inp[1]
    b = inp[2]
    a = int(a) - 1
    b = int(b) - 1
    if inp[0] == "normal":
        dsu.normal(a, b)
    elif inp[0] == "zarbati":
        dsu.zarbati(a, b)
    elif inp[0] == "ask":
        print("Schafer" if not dsu.ask(a, b) else "Branko")
