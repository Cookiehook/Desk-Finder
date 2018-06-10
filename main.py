import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_definitions import crud_node_objects as crud_node
from sql_definitions import crud_node_paths as crud_path
from sql_definitions import connection_operations as con
from node_objects import *
from path_logic.calculate_path import *

logging.basicConfig(level=logging.INFO)


def setup_db(engine, session):
    con.create_all_tables(engine)

    crud_node.create_node(session, "Door", 0, 0)
    crud_node.create_node(session, "Desk A", 0, 0)
    crud_node.create_node(session, "Desk B", 0, 0)
    crud_node.create_node(session, "Desk C", 0, 0)
    crud_node.create_node(session, "Desk D", 0, 0)
    crud_node.create_node(session, "Desk E", 0, 0)
    crud_node.create_node(session, "Desk F", 0, 0)
    crud_node.create_node(session, "Desk G", 0, 0)
    crud_node.create_node(session, "Desk H", 0, 0)
    crud_node.create_node(session, "Desk I", 0, 0)
    crud_node.create_node(session, "Desk J", 0, 0)

    crud_path.create_relationship(session, "Door", "Desk A", 4, True)
    crud_path.create_relationship(session, "Desk A", "Desk B", 1, True)
    crud_path.create_relationship(session, "Desk A", "Desk G", 2, True)
    crud_path.create_relationship(session, "Desk B", "Desk C", 1, True)
    crud_path.create_relationship(session, "Desk D", "Desk G", 5, True)
    crud_path.create_relationship(session, "Desk D", "Desk J", 1, True)
    crud_path.create_relationship(session, "Desk E", "Desk G", 2, True)
    crud_path.create_relationship(session, "Desk E", "Desk F", 1, True)
    crud_path.create_relationship(session, "Desk E", "Desk H", 1, True)
    crud_path.create_relationship(session, "Desk F", "Desk G", 15, True)
    crud_path.create_relationship(session, "Desk H", "Desk I", 2, True)
    crud_path.create_relationship(session, "Desk I", "Desk J", 3, True)

    session.commit()


def get_all_nodes():
    nodes = session.query(NodeObject).all()
    for node in nodes:
        print(node)


if __name__ == "__main__":

    engine = create_engine('sqlite:///data_files\\test_data.db', echo=False)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    # setup_db(engine, session)

    get_all_nodes()

    door = crud_node.select_node_by_name(session, "Door")
    desk_i = crud_node.select_node_by_name(session, "Desk I")
    nodes_lookup = session.query(NodeObject).all()
    relationship_lookup = session.query(NodePath).all()

    path = find_shortest_path(door, desk_i, nodes_lookup)
    for node in path:
        logging.info(node.description)

    cost = get_cost_of_route(path, relationship_lookup)
    logging.info("Total cost is: %s " % cost)
