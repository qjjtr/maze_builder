from maze.helpers import Direction
from maze.maze import Maze
import random


def dfs_generator(n, m):
    n = 2 * n + 1
    m = 2 * m + 1

    visited = [ [ False ] * m for _ in range(n) ]
    field = [  [ '#' if j % 2 == 0 or i % 2 == 0 else ' ' for j in range(m) ] for i in range(n) ]

    def dfs(i, j):
        if visited[i][j]:
            return
        visited[i][j] = True

        free_neighbours = []
        for dir in Direction:
            x = i + dir.value[0] * 2
            y = j + dir.value[1] * 2
            if x > 0 and x < n and y > 0 and y < m and (not visited[x][y]):
                free_neighbours.append((x, y))

        random.shuffle(free_neighbours)
        for neighbour in free_neighbours:
            if not visited[neighbour[0]][neighbour[1]]:
                field[(i + neighbour[0]) // 2][(j + neighbour[1]) // 2] = ' '
            dfs(neighbour[0], neighbour[1])

    dfs(1, 1)
    field[0][1] = ' '
    field[-1][-2] = ' '

    return '\n'.join(map(lambda line : ''.join(map(lambda x : x[0], line)), field))

def kruskal_generator(n, m):
    n = 2 * n + 1
    m = 2 * m + 1

    field = [  [ '#' if j % 2 == 0 or i % 2 == 0 else ' ' for j in range(m) ] for i in range(n) ]
    parents = [ [ (i, j) for j in range(m) ] for i in range(n) ]
    union = [ [ (i, j) for j in range(m) ] for i in range(n) ]

    def get_parent(a):
        if parents[a[0]][a[1]] == a:
            return a
        else:
            parents[a[0]][a[1]] = get_parent(parents[a[0]][a[1]])
            return parents[a[0]][a[1]]

    def unite(a, b):
        a = get_parent(a)
        b = get_parent(b)
        if a == b:
            return False
        parents[a[0]][a[1]] = b
        return True

    edges = []
    for i in range(1, n, 2):
        for j in range(1, m, 2):
            for dir in Direction:
                if dir == Direction.UP or dir == Direction.LEFT:
                    continue
                x = i + dir.value[0] * 2
                y = j + dir.value[1] * 2
                if x >= 0 and x < n and y >= 0 and y < m:
                    edges.append( (random.randint(1, 10000), (i, j), (x, y)) )

    edges.sort()

    for edge in edges:
        a, b = edge[1], edge[2]
        if unite(a, b):
            field[(a[0] + b[0]) // 2][(a[1] + b[1]) // 2] = ' '

    field[0][1] = ' '
    field[-1][-2] = ' '

    return '\n'.join(map(lambda line : ''.join(map(lambda x : x[0], line)), field))

GENERATORS = {
    'dfs-generator': dfs_generator,
    'kruskal-generator': kruskal_generator
}
