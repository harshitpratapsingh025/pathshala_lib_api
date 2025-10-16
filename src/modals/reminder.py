import enum
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, String, Text, func
from database.core import Base


class ReminderType(enum.Enum):
    payment_due = "payment_due"
    payment_overdue = "payment_overdue"
    issue_overdue = "issue_overdue"


class ReminderChannel(enum.Enum):
    email = "email"
    sms = "sms"
    in_app = "in_app"
    push = "push"
    whatsapp = "whatsapp"


class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    payment_id = Column(
        Integer, ForeignKey("payments.id", ondelete="SET NULL"), nullable=True
    )
    issue_id = Column(
        Integer, ForeignKey("book_issues.id", ondelete="SET NULL"), nullable=True
    )
    kind = Column(Enum(ReminderType), nullable=False)
    sent_at = Column(DateTime, default=func.now())
    channel = Column(Enum(ReminderChannel), nullable=False)
    message = Column(Text, nullable=True)
    status = Column(String(32), default="sent")
