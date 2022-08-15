# Create the Pydantic models

from typing import Optional
from pydantic import BaseModel

# Create initial Pydantic models / schemas

class AddressBase(BaseModel):
    address: str

class AddressAdd(AddressBase):
    
    lattitude: Optional[float]
    longitude: Optional[float]

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    # This Config class is used to provide configurations to Pydantic
    class Config:
        orm_mode = True

# Create Pydantic models / schemas for reading / returning
class Address(AddressAdd):
    id: int

    class Config:
        orm_mode = True


class UpdateAddress(BaseModel):
    # Optional[int] is just a shorthand or alias for Union[int, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    address: str
    lattitude: Optional[int]
    longitude: Optional[int]

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class AddressDistance(BaseModel):
    # Optional[int] is just a shorthand or alias for Union[int, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    address: str
    # lattitude: Optional[int]
    # longitude: Optional[int]
    distance: int

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True
