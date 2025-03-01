from enum import Enum

class ResponseCodeEnum(Enum):
    KOU01 = (400, "User already exists")
    KOU02 = (404, "User not found")
    KOU03 = (400, "Invalid profile ID")
    KOU04 = (400, "Invalid status ID")
    KOU05 = (400, "Invalid ID")
    KOU06 = (400, "Invalid request")

    KOD01 = (400, "Invalid email")
    KOD02 = (400, "Invalid credentials")
    KOD03 = (401, "Token expired")
    KOD04 = (401, "Invalid token")



    KOG02 = (500, "A database error occurred")
    KOG01 = (500, "Internal Server Error")

    KO000 = (200, "Operation successful")

    def __init__(self, http_status, message):
        self.http_status = http_status
        self.message = message

class ResponseCode:
    def __init__(self, response_enum: ResponseCodeEnum):
        self.status = response_enum.http_status == 200
        self.http_status = response_enum.http_status
        self.code = response_enum.name
        self.message = response_enum.message

    def to_dict(self):
        return {
            "status": self.status,
            "code": self.code,
            "message": self.message
        }
