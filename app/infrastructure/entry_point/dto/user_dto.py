from pydantic import BaseModel

class NewUserInput(BaseModel):
    email: str
    password: str
    profile_id: int
    status_id: int

class UserOutput(BaseModel):
    id: int
    email: str
    creation_date: str
    profile_id: int
    status_id: int

class GetUser(BaseModel):
    id: int
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginInput(BaseModel):
    email: str
    password: str

class UpdateUserInput(BaseModel):
    id: int
    email: str
    password: str
    profile_id: int
    status_id: int