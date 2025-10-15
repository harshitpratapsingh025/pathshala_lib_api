from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from database.core import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(512), nullable=False, index=True)
    authors = Column(String(512), nullable=True)
    publisher = Column(String(256), nullable=True)
    publication_year = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    cover_url = Column(String(1024), nullable=True)
    total_copies = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    copies = relationship("BookCopy", back_populates="book", cascade="all, delete-orphan")