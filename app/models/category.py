from sqlalchemy import Column, Integer, String, Enum, TIMEST
from sqlalchemy.orm import relationship
from config.database import Base

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default = "CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default = "CURRENT_TIMESTAMP")

    quizzes = relationship("Quizz", back_populates = 'category')