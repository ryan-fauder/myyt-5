from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from environment import DATABASE_URL
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

