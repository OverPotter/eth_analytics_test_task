from src._settings import Settings
from src.database.repositories.transaction_repository import (
    TransactionRepository,
)
from src.services.get_last_processed_block_service.abc_service import (
    AbstractGetLastProcessedBlockService,
)


class RepositoryGetLastProcessedBlockService(
    AbstractGetLastProcessedBlockService
):
    def __init__(
        self,
        transaction_repository: TransactionRepository,
        settings: Settings,
    ):
        self._transaction_repository = transaction_repository
        self._settings = settings

    async def get_last_processed_block(self) -> int:
        last_processed_block = (
            await self._transaction_repository.get_last_processed_block()
        )

        return last_processed_block or self._settings.FIRST_BLOCK_NUMBER
