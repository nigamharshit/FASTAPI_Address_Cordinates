# Create the SQLAlchemy parts

# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./address.db"

# Create the SQLAlchemy engine
# By default, check_same_thread is True and only the creating thread may use the connection. If set False,
# the returned connection may be shared across multiple threads
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a SessionLocal class¶
# Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base Class
# A simple constructor that allows initialization from kwargs.
Base = declarative_base()