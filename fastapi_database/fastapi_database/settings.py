from starlette.config import Config
from starlette.datastructures import Secret
from sqlmodel import SQLModel, create_engine, Session, select
from typing import List
from fastapi_database.main import Todo

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

DB_CONNECTION_STR = config("DATABASE_URL")

TEST_DB_CONNECTION_STR = config("TEST_DATABASE_URL")





# Create a SQLModel engine
engine = create_engine(DB_CONNECTION_STR)

# Function to verify database connection and retrieve some data
def verify_database_connection():
    # Create a session
    with Session(engine) as session:
        try:
            # Execute a query to retrieve some data from the User table
            users: List[Todo] = session.exec(select(Todo)).all()

            # Print retrieved user data
            for user in users:
                print("User:", user)
        except Exception as e:
            print("Error:", e)

# Call the function to verify the database connection
verify_database_connection