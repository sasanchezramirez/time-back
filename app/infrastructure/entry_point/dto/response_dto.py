from pydantic import BaseModel
from typing import Any, Optional

class ResponseDTO(BaseModel):
    apiCode: str
    data: Optional[Any] = None
    message: Optional[str] = None
    status: Optional[bool] = None
