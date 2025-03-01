class CustomException(Exception):
    def __init__(self, response_code_enum):
        self.http_status = response_code_enum.http_status
        self.code = response_code_enum.name
        self.message = response_code_enum.message

    def to_dict(self):
        return {
            "apiCode": self.code,
            "data": None,
            "message": self.message,
            "status": self.http_status == 200
        }
