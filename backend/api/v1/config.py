from os import environ as env
from pydantic import Field, BaseModel

class PostgresConfig(BaseModel):
    host: str = Field(alias='POSTGRES_HOST', default='127.0.0.1')
    port: int = Field(alias='POSTGRES_PORT', default='5432')
    login: str = Field(alias='POSTGRES_USER', default='postgres')
    password: str = Field(alias='POSTGRES_PASSWORD', default='password')
    database: str = Field(alias='POSTGRES_DB', default='postgres')

class FastApiConfig(BaseModel):
    title: str = Field(default='projectname')
    version: str = Field(default='1.0')
    description: str = Field(default='projectname API')
    allow_origins: str = Field(default=['*'])
    allow_credentials: str = Field(default=True)
    allow_methods: str = Field(default=['*'])
    allow_headers: str = Field(default=['*'])

class JWTConfig(BaseModel):
    secret_key: str = Field(default='default')
    expiration_days: int = Field(default=30)

class Config(BaseModel):
    postgres: PostgresConfig = Field(default_factory=lambda: PostgresConfig(**env))
    fastapi: FastApiConfig = Field(default_factory=lambda: FastApiConfig(**env))
    jwt: JWTConfig = Field(default_factory=lambda: JWTConfig(**env))
