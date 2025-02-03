from abc import ABC
from typing import Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models.base import Base

_MODEL_TYPE = TypeVar("_MODEL_TYPE", bound=Base)
_QUERY = TypeVar("_QUERY")


class AbstractRepository(ABC, Generic[_MODEL_TYPE]):
    _model: Type[_MODEL_TYPE] | None = None

    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, **kwargs) -> _MODEL_TYPE:
        entity = self._model(**kwargs)
        self._session.add(entity)
        await self._session.commit()
        return entity
