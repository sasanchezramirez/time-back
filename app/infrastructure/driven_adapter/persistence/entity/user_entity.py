from sqlalchemy import Column, Integer, String
from app.infrastructure.driven_adapter.persistence.config.database import Base


class User_entity(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "relativistic_time_calculator"} 

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    creation_date = Column(String)
    profile_id = Column(Integer)
    status_id = Column(Integer)
    

    def __init__(self, user):
        self.email = user.email
        self.password = user.password
        self.creation_date = user.creation_date
        self.profile_id = user.profile_id
        self.status_id = user.status_id


