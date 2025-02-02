from src._settings import Settings
from src.database.repositories.transaction_repository import (
    TransactionRepository,
)
from src.services.get_last_processed_block_service.abc_service import (
    AbstractGetLastProcessedBlockService,
)
from src.services.logging_service.logging_factory import Logger


class RepositoryGetLastProcessedBlockService(
    AbstractGetLastProcessedBlockService
):
    def __init__(
        self,
        transaction_repository: TransactionRepository,
        logger: Logger,
        settings: Settings,
    ):
        self._transaction_repository = transaction_repository
        self._logger = logger
        self._settings = settings

    async def get_last_processed_block(self) -> int:
        last_processed_block = (
            await self._transaction_repository.get_last_processed_block()
        )
        self._logger.info("Get last processed block.")
        return (
            last_processed_block
            if last_processed_block
            else self._settings.FIRST_BLOCK_NUMBER
        )
