from abc import ABC, abstractmethod


class AbstractProcessNewBlocksService(ABC):
    @abstractmethod
    async def process_new_blocks(self) -> None: ...
