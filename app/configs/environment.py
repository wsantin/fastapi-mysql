from pydantic import BaseSettings
from typing import Any
import json

class Settings(BaseSettings):
    DEBUG: bool = False
    TESTING: str = ''

    PROJECT_NAME: str = '2343'
    PROJECT_API_V1: str = '1.1'
    
    SQLALCHEMY_DATABASE_URI : str = 'postgresql://dbuser:dbpass@localhost:5432/agros-stage'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_ENGINE_OPTIONS_POOL_PRE_PING : bool = True
    SQLALCHEMY_ENGINE_OPTIONS_POOL_RECYCLE: int = 200
    SQLALCHEMY_ENGINE_OPTIONS_POOL_TIMEOUT: int = 110

    # HEADERS
    AWS_JWT_PREFIX:str = 'Bearer'

    #OTROS
    TIME_ZONE:str = 'America/Lima'

    #LOGS
    LOG_NAME_GROUP:str = ''

    class Config:
        env_file = ".env"
        
Config = Settings()