from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
databaseurl= "postgresql://postgres:secret123@localhost:5432/kp"
engine=create_engine(databaseurl)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

# 🧱 Base class to define DB tables
Base = declarative_base()

# 🔁 Dependency used in FastAPI routes to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
