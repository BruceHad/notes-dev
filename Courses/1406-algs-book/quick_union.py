class QuickUnion:
    id = []
    def __init__(self, n):
        self.n = n
        for i in range(n):
            self.id.append(i)
    def root(self, i):
        while(i != self.id[i]): i = self.id[i]
        return i
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    def union(self, p, q):
        rootp = self.root(p)
        rootq = self.root(q)
        self.id[rootp] = rootq


if __name__ == "__main__":
    x = QuickUnion(5)
    print(x.id)
    print(x.connected(0, 4))
    x.union(0,4)
    print(x.connected(0, 4))
    x.union(1,2)
    x.union(2,4)
    print(x.connected(0,1))
    print(x.id)