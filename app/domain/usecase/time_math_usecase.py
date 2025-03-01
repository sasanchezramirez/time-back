import logging
import math

from app.domain.model.time import TimeComparision, TimeComparisionResult
from app.domain.gateway.persistence_gateway import PersistenceGateway

logger = logging.getLogger("User TimeMathUsecase")

C = 3.0e8  # Velocidad de la luz en m/s

class TimeMathUsecase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway

    def calculate_time_dilation(self, velocity: float) -> float:
        """Calcula el factor de dilatación del tiempo relativista para una velocidad dada."""
        beta = velocity / C
        if beta >= 1.0:
            raise ValueError("La velocidad no puede ser igual o mayor a la velocidad de la luz.")
        gamma = 1.0 / math.sqrt(1 - beta**2)
        return gamma

    def time_comparision(self, time_comparision: TimeComparision) -> TimeComparisionResult:
        """Compara el tiempo percibido por dos viajeros con diferentes velocidades."""
        logger.info(f"Calculando dilatación del tiempo para: {time_comparision}")

        # Convertir velocidades de km/h a m/s
        v_1_ms = time_comparision.v_1 * 1000.0 / 3600.0
        v_2_ms = time_comparision.v_2 * 1000.0 / 3600.0

        # Tiempo de referencia 
        t_ref = time_comparision.t_ref  # en segundos

        # Calcular tiempos propios
        gamma_1 = self.calculate_time_dilation(v_1_ms)
        gamma_2 = self.calculate_time_dilation(v_2_ms)

        t_1 = t_ref / gamma_1
        t_2 = t_ref / gamma_2
        delta_t = abs(t_1 - t_2)

        result = TimeComparisionResult(t_1=t_1 / 3600.0, t_2=t_2 / 3600.0, delta_t=delta_t / 3600.0)

        logger.info(f"Resultado: {result}")

        # Si el usuario está autenticado, guardar el resultado
        if time_comparision.is_logged and time_comparision.user_id:
            self.persistence_gateway.save_time_comparision(time_comparision.user_id, result)
            logger.info(f"Resultado guardado en la base de datos para el usuario {time_comparision.user_id}")

        return result
