from sqlalchemy.orm import Session
import model
import schema

# importing geopy library
# Here we used the geopy library to determine the lattitude and longitude of the address
from geopy.geocoders import Nominatim
# Here we used geopy library to calculate the distance between two lattitude and longitude
from geopy.distance import geodesic

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# function to get address by ID
def get_address_by_id(db: Session, sl_id: int):
    return db.query(model.Address).filter(model.Address.id == sl_id).first()

# function to get the list of all address available in database
# skip means the number of address to skip from starting, by default 0
# limit means the maximum no. of records to display, by default 100
def get_address(db: Session, skip: int = 0, limit: int = 100):
    details = db.query(model.Address).offset(skip).limit(limit).all()
    return details


# function to add the address
# Now create utility functions to create data.
# The steps are:
# Create a SQLAlchemy model instance with your data.
# add - that instance object to your database session.
# commit - the changes to the database (so that they are saved).
# refresh - your instance (so that it contains any new data from the database, like the generated ID)

# Here we determine the lattitude and longitude of the address
# Here we have to used the Exception handling because if we gave invalid address then it will throw an error
# So in that case we will not update its lattitude and longitude
def add_address_details_to_db(db: Session, address: schema.Address):
    # entering the location name
    getLoc = loc.geocode(address.address)
    try:
        address_details = model.Address(
        id=address.id,
        address=address.address,
        lattitude = getLoc.latitude,
        longitude = getLoc.longitude)
        address.lattitude = getLoc.latitude
        address.longitude = getLoc.longitude
    except:
        address_details = model.Address(
        id=address.id,
        address=address.address)
    db.add(address_details)
    db.commit()
    db.refresh(address_details)
    return model.Address(**address.dict())

# function to update the address
# here once user updates the address then we will redetermine its lattitude and longitude and updates it
def update_address_details(db: Session, sl_id: int, details: schema.Address):
    getLoc = loc.geocode(details.address)
    try:
        details.lattitude = getLoc.latitude
        details.longitude = getLoc.longitude
        detail = db.query(model.Address).filter(model.Address.id == sl_id).update(vars(details))
        db.commit()
    except:
        db.query(model.Address).filter(model.Address.id == sl_id).update(vars(details))
        db.commit()
    return db.query(model.Address).filter(model.Address.id == sl_id).first()

# function to delete the address
def delete_address_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.Address).filter(model.Address.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)

# function to retrieve the addresses that are within a given distance given by user
def get_address_distance(db: Session, address: str, dist: int):
    
    # here we will extract the lattitude and longitude of input address
    getLoc1 = loc.geocode(address)

    # printing latitude and longitude
    # print("Latitude = ", getLoc1.latitude)
    # print("Longitude = ", getLoc1.longitude)
    # print()

    original_loc = tuple([getLoc1.latitude,getLoc1.longitude])

    # Extracting all data from database and calculate the distance between the original Location
    # and destination location. If its distance is less that the given distance then select it.
    details = db.query(model.Address).all()
    output = dict()
    i = 1
    for detail in details:

        # here we will extract the lattitude and longitude of input address
        getLoc2 = loc.geocode(detail.address)

        # print(getLoc2.latitude,getLoc2.longitude)
        destination_loc = tuple([getLoc2.latitude,getLoc2.longitude])

        # here calculate distance between original location and distination location in Kilometeres
        distance = geodesic(original_loc,destination_loc).kilometers
        # print(distance)

        # check if distance is in range or not and store it in a dictionary
        if distance <= dist:
            output[i] = [getLoc2.address, getLoc2.latitude, getLoc2.longitude, distance]
            i = i + 1

    return output