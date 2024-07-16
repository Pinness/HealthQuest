from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Boolean, Foreignkey
from sqlalchemy.orm import relationship
from config.database import Base

class Answer(Base):
    __tablename__ = 'answers'

    answer_id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, Foreignkey("question. question.id"))
    text = Column(Text, nullable=False)
    Is_correct = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")

    question = relationship('Question', back_populates='answer')
    user_responses = relationship('UserResponse', back_populates='answer')