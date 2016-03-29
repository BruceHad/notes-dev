class QuickFind:
    id = []
    def __init__(self, n):
        self.n = n
        for i in range(n):
            self.id.append(i)
    def connected(self, p, q):
        return self.id[p] == self.id[q]
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if(self.id[i] == pid): self.id[i] = qid


if __name__ == "__main__":
    x = QuickFind(10)
    x.union(3,5)
    x.union(1,8)
    x.union(1,9)
    x.union(1,5)
    x.union(9,0)
    x.union(7,2)
    print(x.id)