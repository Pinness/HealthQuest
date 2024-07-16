from sqlalchemy import Column, Integer, String, Enum, TIMEST
from sqlalchemy.orm import relationship
from config.database import Base
import Enum


class Role(enum.Enum):
    admim = "admin"
    standard = "standard"

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(Role), default=Role.standard)
    created_at = Column(TIMESTAND, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAND, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")


    quiz_session = relationship("QuizSession", back_populates='users')
    user_responses = relationship("UserResponse", back_populates='users')