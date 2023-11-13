def max_matching(seats):

    n = len(seats)
    m = len(seats[0])
    adj = [[] for _ in range(n + m)]
    for i in range(n):
        for j in range(m):
            if seats[i][j] == '.':
                adj[i].append(j + n)
                adj[j + n].append(i)

    # Find maximum matching using DFS
    match = [-1] * (n + m)
    visited = [False] * (n + m)
    for i in range(n):
        visited = [False] * (n + m)
        dfs(adj, match, visited, i)

    # Count number of matches
    count = 0
    for i in range(n):
        if match[i] != -1:
            count += 1

    # Return number of matches
    return count


def dfs(adj, match, visited, u):
    # print("dfs: u =", u)
    for v in adj[u]:
        # print("dfs: v =", v)
        if not visited[v]:
            visited[v] = True
            if match[v] == -1 or dfs(adj, match, visited, match[v]):
                match[v] = u
                match[u] = v
                return True
    return False


seats = ['#.##.#', '.####.', '#.##.#']
seats2 = ['.#', '##', '#.', '##', '.#']

rows, cols = map(int, input().split())
matrix = [[''] * cols for _ in range(rows)]

for i in range(rows):
    row_input = input().strip()
    for j in range(cols):
        matrix[i][j] = row_input[j]

# print matrix
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()


print(max_matching(seats) + 1)
