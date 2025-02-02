from abc import ABC, abstractmethod


class AbstractGetLatestBlockService(ABC):
    @abstractmethod
    async def get_latest_block(self) -> int: ...
