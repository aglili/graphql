from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


from .models import Base



DATABASE_URI = "sqlite:///./todo.db"


engine = create_engine(DATABASE_URI)


Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()