import app.infrastructure.entry_point.validator.validator as validator
import app.infrastructure.entry_point.mapper.user_mapper as user_mapper
import logging

from fastapi import APIRouter, Depends 
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide
from app.infrastructure.entry_point.dto.user_dto import NewUserInput, GetUser, LoginInput, Token, UpdateUserInput
from app.domain.usecase.user_usecase import UserUseCase
from app.domain.usecase.auth_usecase import AuthUseCase

from app.application.container import Container
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.usecase.util.jwt import get_current_user
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.entry_point.dto.response_dto import ResponseDTO
from app.infrastructure.entry_point.utils.api_response import ApiResponse

logger = logging.getLogger("Auth Handler")

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/create-user', 
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
def create_user(
    user_dto: NewUserInput,
    user_usecase: UserUseCase = Depends(Provide[Container.user_usecase])
):
    """
    Creates a new user in the system.
    
    Args:
        user_dto (NewUserInput): The data transfer object containing the user's details.
        user_usecase (UserUseCase): The User UseCase.

    Returns:
        ResponseDTO: A response object containing the operation data.
    """
    
    logger.info("Init create-user handler")
    try:
        validator.validate_new_user(user_dto)
    except ValueError as e:
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOD01, str(e))
        return JSONResponse(status_code=400, content=response_code)

    user = user_mapper.map_user_dto_to_user(user_dto)

    try:
        user = user_usecase.create_user(user)
        response_data = user_mapper.map_user_to_user_output_dto(user)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, response_data)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)
    

@router.post(
    '/get-user',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        404: {"description": "User Not Found", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
def get_user(
    get_user_dto: GetUser,
    user_usecase: UserUseCase = Depends(Provide(Container.user_usecase)),
    current_user: str = Depends(get_current_user)
):
    """
    Retrieves the details of a user.

    Args:
        get_user_dto (GetUser): The data transfer object containing the necessary user details.
        user_usecase (UserUseCase): The User UseCase.

    Returns:
        ResponseDTO: A response object containing the user's data.
    """
    logger.info("Init get-user handler")
    try:
        validator.validate_get_user(get_user_dto)
    except ValueError as e:
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOD01, str(e))
        return JSONResponse(status_code=400, content=response_code)
    
    user = user_mapper.map_get_user_dto_to_user(get_user_dto)

    try:
        user =  user_usecase.get_user(user)
        response_data = user_mapper.map_user_to_user_output_dto(user)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, response_data)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post('/login', 
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
def login(
    login_dto: LoginInput,
    auth_usecase: AuthUseCase = Depends(Provide[Container.auth_usecase])
):
    """
    Logs in a user.
    
    Args:
        login_dto (LoginInput): The data transfer object containing the user's details.
        auth_usecase (AuthUseCase): The Auth UseCase.

    Returns:
        TokenDTO: A response object containing the token.
    """
    logger.info("Init login handler")
    try:
        validator.validate_login(login_dto)
    except ValueError as e:
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOD01, str(e))
        return JSONResponse(status_code=400, content=response_code)
    
    user = user_mapper.map_login_dto_to_user(login_dto)
    
    try:
        token =  auth_usecase.authenticate_user(user)
        if token:
            token = Token(access_token=token, token_type="bearer")
            return ApiResponse.create_response(ResponseCodeEnum.KO000, token)
        else:
            return ApiResponse.create_response(ResponseCodeEnum.KOD02)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post('/update-user',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)  
@inject
def update_user(
    update_user_dto: UpdateUserInput,
    user_usecase: UserUseCase = Depends(Provide(Container.user_usecase)),
    current_user: str = Depends(get_current_user)
):
    """
    Updates the details of a user.

    Args:
        update_user_dto (UpdateUserInput): The data transfer object containing the necessary user details. 
            If a parameter should not be updated, send it as an empty string or zero as appropriate.
            The `id` field is always mandatory.
        user_usecase (UserUseCase): The User UseCase.

    Returns:
        ResponseDTO: A response object containing the operation data.
    """
    logger.info("Init update-user handler")
    try:
        validator.validate_update_user(update_user_dto)
    except ValueError as e:
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOU06, str(e))
        return JSONResponse(status_code=400, content=response_code)
    
    user = user_mapper.map_update_user_dto_to_user(update_user_dto)

    try:
        user =  user_usecase.update_user(user)
        response_data = user_mapper.map_user_to_user_output_dto(user)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, response_data)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)
