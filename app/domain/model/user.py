from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    email: str
    password: Optional[str] = None
    creation_date: Optional[str] = None
    profile_id: Optional[int] = None
    status_id: Optional[int] = None
