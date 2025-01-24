from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url_to_db = "postgresql://postgres:12345@localhost:5432/postgres"
engine = create_engine(url_to_db, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
