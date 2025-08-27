from pydantic import BaseModel
from typing import Optional



# --- Pydantic Schemas ---
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
      name: str
      email: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


