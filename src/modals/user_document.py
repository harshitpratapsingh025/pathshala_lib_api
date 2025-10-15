from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, func
from sqlalchemy.orm import relationship
from database.core import Base

class UserDocument(Base):
    __tablename__ = "user_documents"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    doc_type = Column(String(64), nullable=True)  
    file_url = Column(String(1024), nullable=False)
    uploaded_at = Column(DateTime, default=func.now())
    is_verified = Column(Boolean, default=False)
    user = relationship("User", back_populates="user_documents")