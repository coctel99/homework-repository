from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_name = "main.db"
engine = create_engine(f"sqlite:///{db_name}")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
