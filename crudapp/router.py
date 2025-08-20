from fastapi import APIRouter, HTTPException
from model import UserCreate,UserUpdate,UserResponse
from db import db
from bson import ObjectId

users_collection = db["users"]
router = APIRouter()



@router.post("/users")
async def user_create(user: UserCreate):
    user_dict = user.model_dump()
    await users_collection.insert_one(user_dict)
    return {"message": "User Created!"}


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await users_collection.find_one({"_id":ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return  UserResponse(id=str(user["_id"]), **user)

@router.get("/users", response_model=list[UserResponse])
async def get_users():
    users = await users_collection.find().to_list(100)
    return [UserResponse(id=str(user["_id"]), **user)for user in users]

@router.put("/user/{user_id}")
async def update_user(user_id: str, user: UserUpdate):
    result = await  users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user.model_dump()}
    )
    if result.modified_count==0:
        raise HTTPException(status_code=404, detail="user not found")
    return {"message": "User Update !"}


@router.delete("/user/{user_id}")
async def delete_user(user_id: str):
    result = await users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User Not Found")
    return {"message": "user deleted"}

