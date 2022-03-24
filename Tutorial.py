from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from datetime import datetime
import os

Base_dir = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///" + os.path.join(Base_dir, 'site.db')


Base = declarative_base()

engine = create_engine(connection_string, echo=True)

Session = sessionmaker()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return f"<User username={self.username} email={self.email}>"


new_user = User(id=1, username="William", email="willpokerpro2016@gmail.com")
print(new_user)