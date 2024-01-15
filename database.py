from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine





Base = declarative_base()

DB_URL = "sqlite:///./sql_app.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




def get_db():
    db = SessionLocal()
    try:
        return db
    finally: 
        db.close()