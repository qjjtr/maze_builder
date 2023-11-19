from maze.helpers import *

class MazeVisitor:
    def __init__(self, maze):
        self.maze = maze
        self.position = START_POSITION
        self.visited = [[ False ] * maze.shape[1] for _ in range(maze.shape[0])]
        self.visited[START_POSITION[0]][START_POSITION[1]] = True


    def move(self, direction):
        new_position = (self.position[0] + direction.value[0], self.position[1] + direction.value[1])
        if self.is_blocked(new_position):
            return (self.__str__(), "can't move: path is blocked")
        else:
            self.position = new_position
            self.visited[new_position[0]][new_position[1]] = True
            return (self.__str__(), None)

    def is_blocked(self, position):
        return self.maze.field[position[0]][position[1]]

    def to_start(self):
        self.position = START_POSITION

    def is_exit(self):
        return self.position == self.maze.exit

    def run(self, yielder, listener = printer):
        listener((self.__str__(), None))
        for direction in yielder():
            listener(self.move(direction))
            if self.is_exit():
                listener((self.get_path(), "maze is solved!"))
                break

    def get_path(self):
        lines = list(map(lambda line : list(map(lambda value : ['#'] if value else [' '], line)), self.maze.field))
        for i in range(self.maze.shape[0]):
            for j in range(self.maze.shape[1]):
                if self.visited[i][j]:
                    lines[i][j] = '*'
        lines[self.position[0]][self.position[1]] = '@'
        return '\n'.join(map(lambda line : ''.join(map(lambda x : x[0], line)), lines))

    def __str__(self):
        lines = list(map(lambda line : list(map(lambda value : ['#'] if value else [' '], line)), self.maze.field))
        lines[self.position[0]][self.position[1]] = '@'

        return '\n'.join(map(lambda line : ''.join(map(lambda x : x[0], line)), lines))
