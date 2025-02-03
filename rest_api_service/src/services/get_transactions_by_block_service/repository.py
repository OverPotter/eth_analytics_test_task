from src.database.repositories.transaction_repository import (
    TransactionRepository,
)
from src.schemas.response.transactions.base import TransactionBaseResponse
from src.services.get_transactions_by_block_service.abc_service import (
    AbstractGetTransactionsByBlockService,
)


class RepositoryGetTransactionsByBlockService(
    AbstractGetTransactionsByBlockService
):
    def __init__(
        self,
        transaction_repository: TransactionRepository,
    ):
        self._transaction_repository = transaction_repository

    async def get_transactions_by_block(
        self, block_to_check: int
    ) -> list[TransactionBaseResponse]:
        transactions = (
            await self._transaction_repository.get_transactions_by_block(
                block_to_check=block_to_check
            )
        )
        return [
            TransactionBaseResponse.model_validate(tr) for tr in transactions
        ]
