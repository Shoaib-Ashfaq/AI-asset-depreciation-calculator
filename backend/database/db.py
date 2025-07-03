import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# Load the .env file.
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Setup.
engine = create_engine(DATABASE_URL, echo=True, future=True)
sessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
Base = declarative_base()


class Database:
    def __get_session():
        db = sessionLocal()
        try:
            yield db
        finally:
            db.close()

    def get() -> Session:
        return next(Database.__get_session())
