from node_objects import *


def create_relationship(session, parent, child, cost, accessible):
    parent_id = session.query(NodeObject.node_id).filter(NodeObject.description == parent).one()[0]
    child_id = session.query(NodeObject.node_id).filter(NodeObject.description == child).one()[0]
    session.add(NodePath(parent_node_id=parent_id, child_node_id=child_id, cost=cost, accessible=accessible))


def update_relationship():
    pass


def delete_relationship():
    pass
