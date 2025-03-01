from pydantic import BaseModel
from typing import Optional

class NewTimeComparisionInputDto(BaseModel):
    user_id: Optional[str] = None
    is_logged: bool 
    v_1: int
    v_2: int
    t_ref: int

class TimeComparisionResultDto(BaseModel):
    t_1: float
    t_2: float
    delta_t: float