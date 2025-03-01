from app.application.handler import Handlers
from app.domain.usecase.user_usecase import UserUseCase
from app.domain.usecase.auth_usecase import AuthUseCase
from app.infrastructure.driven_adapter.persistence.service.presistence import Persistence
from app.infrastructure.driven_adapter.persistence.config.database import SessionLocal
from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules= Handlers.modules())

    session = providers.Singleton(SessionLocal)

    persistence_gateway = providers.Factory(Persistence, session=session)

    user_usecase = providers.Factory(UserUseCase, persistence_gateway=persistence_gateway)
    auth_usecase = providers.Factory(AuthUseCase, persistence_gateway=persistence_gateway)

