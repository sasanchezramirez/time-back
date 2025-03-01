import logging


from datetime import datetime
from app.domain.model.user import User
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.gateway.persistence_gateway import PersistenceGateway
from app.domain.usecase.util.security import  verify_password
from app.domain.usecase.util.jwt import create_access_token


logger = logging.getLogger("Auth UseCase")


class AuthUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway

    def authenticate_user(self, user: User):
        user_validated = self.get_user(user)
        if user and verify_password(user.password, user_validated.password):
            return create_access_token({"sub": user.email})
        return None   

        
    def get_user(self, user_to_get: User):
        logger.info("Init get auth usecase")

        try:
            user = self.persistence_gateway.get_user_by_email(user_to_get.email)
            return user
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)



            

