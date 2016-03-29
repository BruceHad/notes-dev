class QuickUnion:
    id = []
    sz = []
    def __init__(self, n):
        self.n = n
        for i in range(n):
            self.id.append(i)
            self.sz.append(1)
    def root(self, i):
        while(i != self.id[i]): i = self.id[i]
        return i
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    def union(self, p, q):
        rootp = self.root(p)
        rootq = self.root(q)
        if(rootp == rootq): return
        if(self.sz[rootp] < self.sz[rootq]):
            self.id[rootp] = rootq
            self.sz[rootq] += self.sz[rootp]
        else:
            self.id[rootq] = rootp
            self.sz[rootp] += self.sz[rootq]

if __name__ == "__main__":
    x = QuickUnion(10)
    x.union(8,5)
    x.union(4,0)
    x.union(1,7)
    x.union(6,1)
    x.union(6,3)
    x.union(3,9)
    x.union(6,2)
    x.union(0,8)
    x.union(6,8)
    print(x.id)