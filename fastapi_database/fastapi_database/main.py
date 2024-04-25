# main.py
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
from fastapi_database import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlmodel import SQLModel, create_engine, Session, select
from typing import List

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)


# only needed for psycopg 3 - replace postgresql
# with postgresql+psycopg in settings.DATABASE_URL
connection_string = settings.DB_CONNECTION_STR

# recycle connections after 5 minutes
# to correspond with the compute scale down
engine = create_engine(
    connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()



# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("Creating tables..")
#     create_db_and_tables()  # Function to create database tables
#     yield



# app = FastAPI(
#     lifespan=lifespan,  # Use the defined context manager for app lifespan
#     title="Hello World API with DB",
#     version="0.0.1",
#     servers=[
#         {
#             "url": "http://127.0.0.1:8000",
#             "description": "Development Server"
#         }
#     ]
# )

# def get_session():
#     with Session(engine) as session:
#         yield session


# @app.get("/")
# def read_root():
#     return {"Hello":"World"}

# @app.post("/todos/",response_model=Todo)
# def create_todo(todo:Todo,session:Annotated[Session,Depends(get_session)]):
#     session.add(todo)
#     session.commit()
#     session.refresh(todo)
#     return todo


# @app.get("/todos/",response_model=list[Todo])
# def read_todos(session:Annotated[Session,Depends(get_session)]):
#     todos=session.exec(select(Todo)).all()
#     return todos



# Create a SQLModel engine
engine = create_engine(settings.DB_CONNECTION_STR)

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