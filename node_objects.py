class NodeObject:

    def __init__(self, name):
        self.name = name
        self.relationship_map = {}

    def add_relationships(self, *args):
        for arg in args:
            self.relationship_map[arg[0]] = arg[1]

    def get_cost_to_node(self, node):
        return self.relationship_map[node]
