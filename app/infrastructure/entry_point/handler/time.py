import logging

from fastapi import APIRouter, Depends 
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide

from app.infrastructure.entry_point.dto.time_dto import NewTimeComparisionInputDto

from app.infrastructure.entry_point.mapper.time_mapper import TimeMapper

from app.domain.usecase.time_math_usecase import TimeMathUsecase

from app.application.container import Container
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.entry_point.dto.response_dto import ResponseDTO
from app.infrastructure.entry_point.utils.api_response import ApiResponse

logger = logging.getLogger("Time Handler")

router = APIRouter(
    prefix='/time',
    tags=['time']
)


@router.post('/time-comparision', 
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
def time_comparision(
    new_time_comparision_input: NewTimeComparisionInputDto,
    time_math_usecase: TimeMathUsecase = Depends(Provide[Container.time_math_usecase])
):
    """
    Comparates time of two bodies by their velocities.
    
    Args:
        new_time_comparision_input (NewTimeComparisionInput): The data transfer object containing the details.
        time_math_usecase (TimeMathUsecase): The UseCase.

    Returns:
        ResponseDTO: A response object containing the operation data.
    """
    
    logger.info("Init comparision handler")
   

    time_comparision = TimeMapper.map_new_time_comparision_input_to_time_comparision(new_time_comparision_input)

    try:
        time_comparision_result = time_math_usecase.time_comparision(time_comparision)
        response_data = TimeMapper.map_time_comparision_result_to_time_comparision_result_dto(time_comparision_result)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, response_data)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)
    