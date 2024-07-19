from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Foreignkey
from sqlalchemy.orm import relationship
from config.database import Base

class Question(Base):
    __tablename__ = 'questions'

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    quiz_id = Column(Integer, Foreignkey('quizzes.quiz.id_id'))
    text = Column(Text, nullable=False)
    question_type = Column(Enum('multiple_choice', 'true/false'), nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")

    quiz = relationship('Quiz',back_populates='questions')
    answers = relationship('Answer',back_populates='questions')
    user_responses = relationship('User_Response', back_populates='question')