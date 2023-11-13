"""
A city contains n cities with numbers 1 to n, such that there is a one-way road between any two of these n cities. After receiving n and the condition of the roads, you should print a permutation of numbers 1 to n in the output. (p1, p2, p3, ..., pn), in such a way that: for every i in the interval [1, n-1] there is a road from city p(i) to p(i+1).
Entrance :
There will be n numbers in the first line and in the next n lines in each line, which represent the elements of the adjacency matrix of the problem graph.
Input example:
3
0 1 0
0 0 0
1 1 0
Expected output:
It contains n lines in such a way that the i-th element of the answer sequence is in the i-th line.
3
1
2
"""
# Solution:
# 1. Create a graph with the given number of vertices, and the edges are given by the adjacency matrix.
# 2. Find the topological sorting of the graph.
# 3. Print the topological sorting.
# 4. If the graph is not a DAG, then print "Sandro fails.".
# 5. If the graph is a DAG, then print the topological sorting.

# Code:
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)
    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        print(stack)


n = int(input())
g = Graph(n)
for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == '1':
            g.addEdge(i, j)
g.topologicalSort()
