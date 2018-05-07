from node_objects import Base


def create_all_tables(engine):
    Base.metadata.create_all(engine)
