class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    # 親を見つける
    def find(self, x):
        # 頂点の場合
        if self.parents[x] < 0:
            return x
        # 子頂点の場合、親の頂点をparentsに格納する
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
    def union(self, x, y):
        # x, yの頂点を探す
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0
        
        # xの頂点がyの頂点より大きい場合
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        # 頂点x, yを統合する
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -1 * self.parents[x]
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
N, Q = list(map(int, input().split()))
queries = [list((map(int, input().split()))) for _ in range(Q)]
uf = UnionFind(N)
for query in queries:
    typ, u, v = query
    u -= 1
    v -= 1
    if typ == 1:
        uf.union(u, v)
    if typ == 2:
        is_same = uf.same(u, v)
        if is_same:
            print("Yes")
        else:
            print("No")