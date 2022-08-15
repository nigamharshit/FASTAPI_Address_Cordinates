# FASTAPI_Address_Cordinates
FastAPI CRUD Operations with Address Coordinates details using SQLite database and retrieve the address from the database that are within the given distance<br>

# Libraries which I installed and its command to install <br>

pip install fastapi<br>
pip install uvicorn<br>
pip install SQLAlchemy<br>
pip install geopy<br>
pip install pydantic<br>

# Libraries Version

fastapi==0.79.0<br>
uvicorn==0.18.2<br>
SQLAlchemy==1.4.40<br>
geopy==2.2.0<br>
pydantic==1.9.2<br>


----------------------------------------------------------------------------------------------------------------------------------------

# Command to run the program<br>
uvicorn applications:app --reload<br>

# Swagger API<br>
URL - http://127.0.0.1:8000/docs<br>

----------------------------------------------------------------------------------------------------------------------------------------

Database used - SQLite3<br>

Database name - address.db<br>

Table name - address<br>

Table Schema -<Br>
CREATE TABLE address (
        id INTEGER NOT NULL,
        address VARCHAR(255) NOT NULL,
        lattitude NUMERIC(18, 15),
        longitude NUMERIC(18, 15),
        PRIMARY KEY (id)
);
