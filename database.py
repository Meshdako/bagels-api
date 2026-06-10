from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DB_PATH

# SQLite connection
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class
Base = declarative_base()

# Utility function (Dependency Injection) to FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
