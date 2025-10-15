from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, func
)
from sqlalchemy.orm import relationship
from database.core import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(256), unique=True, nullable=False, index=True)
    full_name = Column(String(256), nullable=False)
    hashed_password = Column(String(512), nullable=False)
    phone = Column(String(32), nullable=True, index=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # relationships
    user_documents = relationship("UserDocument", back_populates="user", cascade="all, delete-orphan")
    roles = relationship("Role", back_populates="users", cascade="all")
    issues = relationship("BookIssue", back_populates="user")
    payments = relationship("Payment", back_populates="user")