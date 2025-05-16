from dishka import Provider, provide, Scope, from_context, AnyOf
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from config import Config, JWTConfig, MinioConfig
from infrastructure.db.database import new_session_maker
from typing import AsyncIterable
from application import common_interfaces

class FastApiApp(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    async def get_jwt_config(self, config: Config) -> JWTConfig:
        return config.jwt

    @provide(scope=Scope.APP)
    async def get_session_maker(self, config: Config) -> async_sessionmaker[AsyncSession]:
        async_session_maker = await new_session_maker(config.postgres)
        return async_session_maker
    
    @provide(scope=Scope.REQUEST)
    async def get_async_session(self, async_sessionmaker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AnyOf[AsyncSession, common_interfaces.DBSession]]:
        async with async_sessionmaker() as session:
            yield session
        