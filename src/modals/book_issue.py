import enum
from database.core import Base
from sqlalchemy import (
    Column, Integer, ForeignKey, DateTime, Enum, Numeric, Text, func
)
from sqlalchemy.orm import relationship

class IssueStatus(enum.Enum):
    issued = "issued"
    returned = "returned"
    overdue = "overdue"
    lost = "lost"

class BookIssue(Base):
    __tablename__ = "book_issues"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=False)
    copy_id = Column(Integer, ForeignKey("book_copies.id", ondelete="SET NULL"), nullable=False)
    issued_at = Column(DateTime, default=func.now(), nullable=False)
    due_at = Column(DateTime, nullable=False)
    returned_at = Column(DateTime, nullable=True)
    status: IssueStatus = Column(Enum(IssueStatus), default=IssueStatus.issued, nullable=False)
    fine_amount = Column(Numeric(10,2), default=0.0)
    notes = Column(Text, nullable=True)
    user = relationship("User", back_populates="issues")
    copy = relationship("BookCopy", back_populates="issues")