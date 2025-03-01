from app.infrastructure.entry_point.dto.time_dto import NewTimeComparisionInputDto, TimeComparisionResultDto
from app.domain.model.time import TimeComparision, TimeComparisionResult


class TimeMapper():
    @staticmethod
    def map_new_time_comparision_input_to_time_comparision(new_time_comparision_input: NewTimeComparisionInputDto) -> TimeComparision:
        return TimeComparision(
            user_id=new_time_comparision_input.user_id if new_time_comparision_input.user_id else None,
            is_logged=new_time_comparision_input.is_logged,
            v_1=new_time_comparision_input.v_1,
            v_2=new_time_comparision_input.v_2
        )
    
    @staticmethod
    def map_time_comparision_result_to_time_comparision_result_dto(time_comparision_result: TimeComparisionResult) -> TimeComparisionResultDto:
        return TimeComparisionResultDto(
            t_1=time_comparision_result.t_1,
            t_2=time_comparision_result.t_2,
            delta_t=time_comparision_result.delta_t
        )