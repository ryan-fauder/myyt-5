from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from environment import DATABASE_URL

def create_session():
    engine = create_engine(DATABASE_URL, echo=True, pool_size=20, max_overflow=100)
    Session = sessionmaker(bind=engine)
    return scoped_session(Session)

global_session = create_session()