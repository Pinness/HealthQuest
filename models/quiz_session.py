from sqlalchemy import Column, Integer, TIMESTAMP, DECIMAL, Foreignkey
from sqlalchemy.orm import relationship
from config.database import Base

class QuizSession(Base):
    __tablename__ = 'quiz_sessions'

    session_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, Foreignkey("user.user_id"))
    quiz_id = Column(Integer, Foreignkey("quizzes.quiz_id"))
    start_time = Column(TIMESTAMP, nullable=False)
    end_time = Column(TIMESTAMP)
    score = Column(DECIMAL(5, 3))
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP",  onupdate="CURRENT_TIMESTAMP")

    user = relationship('User', back_populates='quiz_sessions')
    quiz = relationship('Quiz', back_populates='quiz_sessions')