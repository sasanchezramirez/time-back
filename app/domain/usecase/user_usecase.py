import logging


from datetime import datetime
from app.domain.model.user import User
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.gateway.persistence_gateway import PersistenceGateway
from app.domain.usecase.util.security import  hash_password

logger = logging.getLogger("User UseCase")


class UserUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway
        

    def create_user(self, user: User):
        logger.info("Init create user usecase")
        user.creation_date = datetime.now().isoformat()
        user.password = hash_password(user.password)
        try:
            created_user = self.persistence_gateway.create_user(user)
            return created_user
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

        
    def get_user(self, user_to_get: User):
        logger.info("Init get user usecase")
        if user_to_get.id and user_to_get.id != 0:
            try:
                user = self.persistence_gateway.get_user_by_id(user_to_get.id)
                return user
            except CustomException as e:
                logger.error(f"Custom exception: {e}")
                raise e
            except Exception as e:
                logger.error(f"Unhandled error: {e}")
                raise CustomException(ResponseCodeEnum.KOG01)
        else:
            try:
                user = self.persistence_gateway.get_user_by_email(user_to_get.email)
                return user
            except CustomException as e:
                logger.error(f"Custom exception: {e}")
                raise e
            except Exception as e:
                logger.error(f"Unhandled error: {e}")
                raise CustomException(ResponseCodeEnum.KOG01)
            
    def update_user(self, user: User):
        logger.info("Init update user usecase")
        user.password = hash_password(user.password) if user.password else user.password
        try:
            updated_user = self.persistence_gateway.update_user(user)
            return updated_user
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)




            

