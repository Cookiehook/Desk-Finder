class DeskObject:

    def __init__(self, name):
        self.name = name
        self.relationship_map = {}

    def add_relationships(self, *args):
        for arg in args:
            self.relationship_map[arg[0]] = arg[1]
