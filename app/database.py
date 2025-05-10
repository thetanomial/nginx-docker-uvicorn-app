from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./mysimpleapp.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={
    'check_same_thread' : False
})


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()