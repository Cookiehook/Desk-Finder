from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class NodeObject(Base):

    __tablename__ = 'NODE'
    node_id = Column(Integer, primary_key=True)
    description = Column(String)
    x_position = Column(Integer)
    z_position = Column(Integer)

    parent_relationship = relationship("NodePath", foreign_keys="NodePath.parent_node_id")
    child_relationship = relationship("NodePath", foreign_keys="NodePath.child_node_id")

    def __repr__(self):
        return "<Node(Description='%s', x_position='%s', z_position='%s')>" % (
            self.description, self.x_position, self.z_position)


class NodePath(Base):

    __tablename__ = 'NODE_PATH'

    path_id = Column(Integer, primary_key=True)
    parent_node_id = Column(Integer, ForeignKey('NODE.node_id'))
    child_node_id = Column(Integer, ForeignKey('NODE.node_id'))
    cost = Column(Integer)
    accessible = Column(Boolean)

    def __repr__(self):
        return "<Relationship(Parent='%s', Child='%s', Cost='%s', Accessible='%s')>" % (
            self.parent_node, self.child_node, self.cost, self.accessible)
