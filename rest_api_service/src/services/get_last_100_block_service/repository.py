from src.database.repositories.transaction_repository import (
    TransactionRepository,
)
from src.services.get_last_100_block_service.abc_service import (
    AbstractGetLast100BlockService,
)


class RepositoryGetLast100BlockService(AbstractGetLast100BlockService):
    def __init__(
        self,
        transaction_repository: TransactionRepository,
    ):
        self._transaction_repository = transaction_repository

    async def get_last_100_block(self) -> int:
        last_processed_block = (
            await self._transaction_repository.get_last_processed_block()
        )
        blocks_to_check = last_processed_block - 100
        return blocks_to_check
