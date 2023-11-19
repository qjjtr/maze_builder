class Maze:
    def __init__(self, arg1, n = None, m = None):
        if n != None and m != None:
            arg1 = arg1(n, m)
        self.restore_from_text(arg1)

    def restore_from_text(self, text):
        self.field = list(map(lambda line : list(map(lambda symbol : symbol == '#', line)), text.split('\n')))
        self.shape = (len(self.field), len(self.field[0]))
        self.exit = (self.shape[0] - 1, self.shape[1] - 2)


    def __str__(self):
        lines = list(map(lambda line : "".join(map(lambda value : '#' if value else ' ', line)), self.field))
        return "\n".join(lines)
