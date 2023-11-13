from typing import List
from collections import deque

row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]

# Flood fill using BFS
def floodfillBFS(mat: List[List[str]], x: int, y: int, replacement: str) -> None:
    n, m = len(mat), len(mat[0])
    visited = set()
    queue = deque([(x, y)])
    original_color = mat[x][y]
    while queue:
        r, c = queue.popleft()
        if (r, c) in visited or mat[r][c] != original_color:
            continue
        mat[r][c] = replacement
        visited.add((r, c))
        for i in range(8):
            nr, nc = r + row[i], c + col[i]
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                queue.append((nr, nc))

# Flood fill using DFS
def floodfillDFS(mat: List[List[str]], x: int, y: int, replacement: str) -> None:
    n, m = len(mat), len(mat[0])
    visited = set()
    original_color = mat[x][y]
    def dfs(r, c):
        if (r, c) in visited or mat[r][c] != original_color:
            return
        mat[r][c] = replacement
        visited.add((r, c))
        for i in range(8):
            nr, nc = r + row[i], c + col[i]
            if 0 <= nr < n and 0 <= nc < m:
                dfs(nr, nc)
    dfs(x, y)


if __name__ == '__main__':
    DorB = int(input())
    a = int(input()) # dimension of matrix
    mat = [list(input().strip()) for _ in range(a)]
    x, y = map(int, input().split())
    replacement = input()[0]
    if DorB == 1:
        floodfillDFS(mat, x, y, replacement)
    else:
        floodfillBFS(mat, x, y, replacement)
    for row in mat:
        print(''.join(row))
