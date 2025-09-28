from fastapi import APIRouter, HTTPException, status
from ..models.user import UserLogin, UserRegister
from ..crud.user import register_user, get_user_by_email
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED



router =APIRouter()

@router.post("/register")
async  def register(user: UserRegister):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User email already exits")
    await register_user(user)
    return {"message": "User registered!"}


@router.get("/login")
async def login(user: UserLogin):
    db_user = await  get_user_by_email(user.email)
    if not db_user or (user.password is not db_user.password):
        raise  HTTPException(status_code=HTTP_401_UNAUTHORIZED,detail=("Invalid credentials"))
    return {"message": "User Login success"}