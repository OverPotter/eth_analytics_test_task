from abc import ABC, abstractmethod


class AbstractGetLastProcessedBlockService(ABC):
    @abstractmethod
    async def get_last_processed_block(self) -> int: ...
