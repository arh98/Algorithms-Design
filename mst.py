import math
# kruskal
class DSU():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1
        return True

def distance(p1, p2):
    res = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    return math.sqrt(res)

n = int(input())
vertices = []
for i in range(n):
    x, y = map(float, input().split())
    vertices.append((x, y))


edges = []
for i in range(n):
    for j in range(i+1, n):
        dist = distance(vertices[i], vertices[j])
        edges.append((dist, i, j))

edges.sort()
dsu = DSU(n)
total_len = 0

for edge in edges:
    length, u, v = edge
    if dsu.union(u, v):
        total_len += length

print(round(total_len , 2))