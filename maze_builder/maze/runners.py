from maze.helpers import Direction, START_POSITION

from queue import Queue
import copy
import pygame

def solve(maze):
    field = copy.deepcopy(maze.field)
    n, m = maze.shape
    dist = [[n * m + 1 for _ in range(m) ] for _ in range(n) ]
    dirs = [[Direction.UP for _ in range(m) ] for _ in range(n) ]
    queue = Queue()
    queue.put(START_POSITION)

    dist[START_POSITION[0]][START_POSITION[1]] = 0
    while not queue.empty():
        pos = queue.get()
        if field[pos[0]][pos[1]]:
            continue
        field[pos[0]][pos[1]] = True
        if pos == maze.exit:
            break
        for dir in Direction:
            idir = dir.value
            new_pos = (pos[0] + idir[0], pos[1] + idir[1])
            if new_pos[0] < 0 or new_pos[0] >= n or new_pos[1] < 0 or new_pos[1] >= m:
                continue
            if dist[new_pos[0]][new_pos[1]] > dist[pos[0]][pos[1]] + 1:
                dirs[new_pos[0]][new_pos[1]] = dir
                dist[new_pos[0]][new_pos[1]] = dist[pos[0]][pos[1]] + 1
                queue.put(new_pos)

    path = []
    position = maze.exit

    while position != START_POSITION:
        dir = dirs[position[0]][position[1]]
        path.append(dir)
        idir = dir.value
        position = (position[0] - idir[0], position[1] - idir[1])

    return path[::-1]


def get_solution(maze):
    path = solve(maze)
    solution = [START_POSITION]
    for dir in path:
        solution.append((solution[-1][0] + dir.value[0], solution[-1][1] + dir.value[1]))
    return solution


def solve_runner(maze):
    def runner():
        for dir in solve(maze):
            yield dir
    return runner



def user_yielder(key_yielder):
    while True:
        event = next(key_yielder())
        etype, key = event.type, event.key
        if etype == pygame.KEYDOWN:
            if key == pygame.K_LEFT:
                yield Direction.LEFT
            elif key == pygame.K_RIGHT:
                yield Direction.RIGHT
            elif key == pygame.K_UP:
                yield Direction.UP
            elif key == pygame.K_DOWN:
                yield Direction.DOWN
            elif key == pygame.K_ESCAPE:
                break

def user_runner(key_yielder):
    def runner():
        return user_yielder(key_yielder)
    return runner
