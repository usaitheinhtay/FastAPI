from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

from onlineclass.FastAPI.crudapp.router import users_collection

app = FastAPI()

client = AsyncIOMotorClient("mongodb+srv://theinhtay:285138thein@budget.f4mf9os.mongodb.net/?retryWrites=true&w=majority&appName=budget")
db = client["toedhana"]
user_collection = db["users"]

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


@app.post("/users")
def user_create(user: UserCreate):
    user_dict = user.model_dump()
    users_collection.insert_one()


@app.get("/users/{user_id}")
def get_user():
    pass

@app.get("/users")
def get_users():
    pass

@app.put("/users/{user_id")
def update_user():
    pass

@app.delete("/users/{user_id}")
def delete_user():
    pass




