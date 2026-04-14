class Agent:
    def __init__(self, start):
        self.position = start
        self.path = []
        self.step = 0

    def set_path(self, path):
        self.path = path
        self.step = 0

    def move(self):
        if self.step < len(self.path):
            self.position = self.path[self.step]
            self.step += 1
