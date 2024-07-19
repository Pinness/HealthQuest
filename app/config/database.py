from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import users, answers, quiz, question, user_response, quiz_session, category

username = "User"
password = "my_passsword"
database = "my_quiz"

#Create the connection string
Connection_string = 'mysql+mysqldb://{}:@localhost:{}'.format(username, password, database)

#Create the engine
engine = create_engine(connection_string, pool_pre_ping=True)

Base.metadata.create_all(engine)

#Test the connection
try:
    connection = engine.connect()
    print("Connection established")
    connection.close()
exept Exception as e:
    print(f"Connection failed: {e}")

Base = declarative_base()
Session = sessionmaker(bind=engine)