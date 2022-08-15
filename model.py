# Create the database models

# Import Base from database (the file database.py)
# Create classes that inherit from it.
# These classes are the SQLAlchemy models
from sre_parse import State
from sqlalchemy import Column, Integer, String, Numeric
from db_handler import Base

# Here only one class used, so we don't use relationships between models

class Address(Base):
    """
    This is a model class. which is having the address table structure with all the constraint
    here tablename is address
    """
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    address = Column(String(255), index=True, nullable=False)
    lattitude = Column(Numeric(18,15))
    longitude = Column(Numeric(18,15))