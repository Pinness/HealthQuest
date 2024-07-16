from sqlalchemy import Column, Integer, TIMESTAMP, Foreignkey
from sqlalchemy.orm import relationship
from config.database import Base

class UserResponse(Base):
    __tablename__ = 'user_responses'

    user_response_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, Foreignkey('users.user_id'))
    question_id = Column(Integer, Foreignkey('questions.question_id'))
    selected_answer = Column(Integer, Foreignkey('answers.answer_id'))
    is_correct = Column(Boolean, nullable=False)
    response_time = Column(DECIMA(10, 2))
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    user = relationship('User', back_populates='user_response')
    question = relationship('Question', back_populates='user_response')
    answer = relationship('Answer', back_populates='user_response')