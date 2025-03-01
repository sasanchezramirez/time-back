import logging
import app.infrastructure.driven_adapter.persistence.mapper.user_mapper as mapper
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.infrastructure.driven_adapter.persistence.entity.user_entity import User_entity
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.util.custom_exceptions import CustomException

logger = logging.getLogger("User Repository")

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user_entity: User_entity):
        logger.info(f"Creating user: {user_entity}")
        try:
            self.session.add(user_entity)
            self.session.commit()
            return user_entity
        except IntegrityError as e:
            logger.error(f"Operation failed: {e}")
            if "llave duplicada" or "duplicate key" in str(e.orig):
                raise CustomException(ResponseCodeEnum.KOU01)
            elif "viola la llave" or "key violation" in str(e.orig):
                if "profile_id" in str(e.orig):
                    raise CustomException(ResponseCodeEnum.KOU03)
                elif "status_id" in str(e.orig):
                    raise CustomException(ResponseCodeEnum.KOU04)
            raise CustomException(ResponseCodeEnum.KOG02)
        except SQLAlchemyError as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG02)
        except Exception as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
        
    def get_user_by_id(self, id: int):
        logger.info(f"Finding user for id {id}")
        try:
            user_entity = self.session.query(User_entity).filter_by(id=id).first()
            if user_entity is None:
                logger.error(f"User with id {id} not found")
                raise CustomException(ResponseCodeEnum.KOU02)
            return user_entity
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG02)
        except Exception as e:
            logger.error(f"Operation failed: {e}")  
            raise CustomException(ResponseCodeEnum.KOG01)
        
    def get_user_by_email(self, email: str):
        logger.info(f"Finding user for email {email}")
        try:
            user_entity = self.session.query(User_entity).filter_by(email=email).first()
            if user_entity is None:
                logger.error(f"User with email {email} not found")
                raise CustomException(ResponseCodeEnum.KOU02)
            return user_entity 
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG02)
        except Exception as e:
            logger.error(f"Operation failed: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
        
    def update_user(self, user_entity: User_entity):
            logger.info(f"Updating user: {user_entity}")
            try:
                existing_user = self.session.query(User_entity).filter_by(id=user_entity.id).first()
                if not existing_user:
                    raise CustomException(ResponseCodeEnum.KOD02)

                if user_entity.email:
                    existing_user.email = user_entity.email
                if user_entity.password:
                    existing_user.password = user_entity.password
                if user_entity.profile_id is not None and user_entity.profile_id != 0:
                    existing_user.profile_id = user_entity.profile_id
                if user_entity.status_id is not None and user_entity.status_id != 0:
                    existing_user.status_id = user_entity.status_id

                self.session.commit()
                return existing_user
            except IntegrityError as e:
                logger.error(f"Operation failed: {e}")
                if "llave duplicada" in str(e.orig) or "duplicate key" in str(e.orig):
                    raise CustomException(ResponseCodeEnum.KOU01)
                elif "viola la llave" in str(e.orig) or "key violation" in str(e.orig):
                    if "profile_id" in str(e.orig):
                        raise CustomException(ResponseCodeEnum.KOU03)
                    elif "status_id" in str(e.orig):
                        raise CustomException(ResponseCodeEnum.KOU04)
                raise CustomException(ResponseCodeEnum.KOG02)
            except SQLAlchemyError as e:
                logger.error(f"Operation failed: {e}")
                raise CustomException(ResponseCodeEnum.KOG02)
            except Exception as e:
                logger.error(f"Operation failed: {e}")
                raise CustomException(ResponseCodeEnum.KOG01)
