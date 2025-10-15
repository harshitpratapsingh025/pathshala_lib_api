import sqlalchemy as sa
from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from database.core import Base
import enum


class RoleEnum(enum.Enum):
    admin = "admin"
    librarian = "librarian"
    student = "student"
    guest = "guest"
    
user_roles = sa.Table(
    'user_roles', Base.metadata,
    Column('user_id', sa.Integer, sa.ForeignKey('users.id'), primary_key=True),
    Column('role_name', sa.String, sa.ForeignKey('roles.name'), primary_key=True)
)

class Role(Base):
    __tablename__ = "roles"
    name = Column(Enum(RoleEnum), primary_key=True)
    description = Column(String(256), nullable=True)
    users = relationship("User", secondary=user_roles, back_populates="roles")