from abc import ABC, abstractmethod


class AbstractGetLast100BlockService(ABC):
    @abstractmethod
    async def get_last_100_block(self) -> int: ...
