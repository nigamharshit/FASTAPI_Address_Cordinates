import crud
import model
import schema

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db_handler import SessionLocal, engine

# Create the database tables
model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Address Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)


# Create a Dependency
# Our dependency will create a new SQLAlchemy SessionLocal that will be used in a single request
# and then close it once the request is finished.
# And then, when using the dependency in a path operation function
# we declare it with the type Session we imported directly from SQLAlchemy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# To retrieve all address details from database
@app.get('/retrieve_all_address_details', response_model=List[schema.Address])
def retrieve_all_address_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    address = crud.get_address(db=db, skip=skip, limit=limit)
    return address

# To add new address to database
# Here from address given we find the lattitude and longitude of the address though library
# and update its lattitude and longitude, so please make sure to give valid address and also a unique id
@app.post('/add_new_address', response_model=schema.Address)
def add_new_address(address: schema.Address, db: Session = Depends(get_db)):
    id = crud.get_address_by_id(db=db, sl_id = address.id)
    if id:
        raise HTTPException(status_code=400, detail=f"Address id {address.id} already exist in database: {address.id}")
    return crud.add_address_details_to_db(db=db, address=address)

# To delete address on the basis of its id
@app.delete('/delete_address_by_id')
def delete_address_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_address_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")
    try:
        crud.delete_address_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}

# to update the address, once the address is updates then again we find its new lattitude and longitude and updates the same
@app.put('/update_address_details', response_model=schema.Address)
def update_address_details(sl_id: int, update_param: schema.UpdateAddress, db: Session = Depends(get_db)):
    details = crud.get_address_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_address_details(db=db, details=update_param, sl_id=sl_id)


@app.post('/address_within_distance')
def address_within_distance(address: schema.AddressDistance, db: Session = Depends(get_db)):
    try:
        output = crud.get_address_distance(db = db, address = address.address, dist= address.distance)
    except:
        output = { 'Error Message' : 'Please enter valid address'}

    # print(output)
    # print(type(output))

    # Output format
    # {
    # "1": [
    # Address => "Railway Station, Doddaballapur Road, Doddaballapura, Doddaballapura taluk, Bangalore Rural, Karnataka, 561203, India",
    # Lattitude => 13.280475,
    # Longitude => 77.5516397,
    # Distance between them => 473.09036380251774
    # ]
    # }

    return output