import enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, func
from sqlalchemy.orm import relationship
from database.core import Base


class CopyStatus(enum.Enum):
    available = "available"
    on_loan = "on_loan"
    reserved = "reserved"
    lost = "lost"
    maintenance = "maintenance"


class BookCopy(Base):
    __tablename__ = "book_copies"
    id = Column(Integer, primary_key=True)
    book_id = Column(
        Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False
    )
    accession_number = Column(String(128), nullable=True, unique=True)
    status = Column(Enum(CopyStatus), default=CopyStatus.available, nullable=False)
    location = Column(String(128), nullable=True)
    added_at = Column(DateTime, default=func.now())
    book = relationship("Book", back_populates="copies")
    issues = relationship("BookIssue", back_populates="copy")
