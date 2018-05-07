from node_objects import *


def create_node(session, description, x_position, z_position):
    new_node = NodeObject(description=description, x_position=x_position, z_position=z_position)
    session.add(new_node)


def update_node():
    pass


def select_node_by_name(session, name):
    return session.query(NodeObject).filter(NodeObject.description == name).one()


def delete_node():
    pass
