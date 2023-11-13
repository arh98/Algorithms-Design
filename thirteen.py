from collections import deque

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(s)
    visited[s] = True
    
    while queue:
        u = queue.popleft()
        
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    
    return visited[t]

def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    
    while bfs(graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow
        
        v = sink
        
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    
    return max_flow

def h_connectivity():
    M, N = map(int, input().split())
    graph = [[0] * M for _ in range(M)]
    
    for i in range(N):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1
    
    min_cut = float('inf')
    
    for s in range(len(graph)):
        for t in range(s+1, len(graph)):
            residual_graph = [row[:] for row in graph]
            
            max_flow = ford_fulkerson(residual_graph, s, t)
            
            if max_flow < min_cut:
                min_cut = max_flow
                
    return min_cut
result = int(h_connectivity())
print(result)