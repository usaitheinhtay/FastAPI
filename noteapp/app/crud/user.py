from ..db import db_name
from ..models.user import UserRegister

user_collection = db_name["users"]


async  def register_user(user: UserRegister):
    user_data = user.model_dump()
    result = await user_collection.insert_one(user_data)
    return UserRegister(id=str(result.inserted_id), **user_data)


async def get_user_by_email(email: str):
    user = await user_collection.find_one({"email": email})
    if user :
        return UserRegister(id=str(user["_id"]), **user)
    return None


