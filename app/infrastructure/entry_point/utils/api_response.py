from app.domain.model.util.response_codes import ResponseCodeEnum, ResponseCode
from app.domain.model.util.custom_exceptions import CustomException

class ApiResponse:
    @staticmethod
    def create_response(response_enum: ResponseCodeEnum, data=None):
        response_code = ResponseCode(response_enum)
        return {
            "apiCode": response_code.code,
            "data": data,
            "message": response_code.message,
            "status": response_code.http_status == 200
        }
    
    @staticmethod
    def create_error_response(exception: CustomException):
        return {
            "apiCode": exception.code,
            "data": None,
            "message": exception.message,
            "status": exception.http_status == 200
        }
