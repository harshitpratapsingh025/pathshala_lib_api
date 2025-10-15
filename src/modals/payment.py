import enum
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, Numeric, String, func
from sqlalchemy.orm import relationship
from database.core import Base

class PaymentStatus(enum.Enum):
    pending = "pending"
    paid = "paid"
    partially_paid = "partially_paid"
    failed = "failed"

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    due_date = Column(DateTime, nullable=False)
    paid_at = Column(DateTime, nullable=True)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.pending, nullable=False)
    method = Column(String(64), nullable=True)  # "online", "cash", "cheque"
    reference = Column(String(256), nullable=True)  # transaction id or receipt
    created_at = Column(DateTime, default=func.now())
    user = relationship("User", back_populates="payments")