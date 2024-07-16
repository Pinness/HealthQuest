from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Foreignkey
from sqlalchemy.orm import relationship
from config.database import Base


class Quiz(Base):
    __tablename__ = 'quizzes'

    quiz_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = column(Text)
    category_id = Column(Integer, Foreignkey("categories.category_id"))
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", onupdate=CURRENT_TIMESTAMP)


    category = relationship("Category", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz")
    quiz_session = relationship("QuizSession", back_populates="quiz")
