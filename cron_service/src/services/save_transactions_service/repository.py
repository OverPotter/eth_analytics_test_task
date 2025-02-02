from src.database.repositories.transaction_repository import (
    TransactionRepository,
)
from src.schemas.response.transactions.base import TransactionBaseResponse
from src.services.logging_service.logging_factory import Logger
from src.services.save_transactions_service.abc_service import (
    AbstractSaveTransactionsService,
)


class RepositorySaveTransactionsService(AbstractSaveTransactionsService):
    def __init__(
        self, transaction_repository: TransactionRepository, logger: Logger
    ):
        self._transaction_repository = transaction_repository
        self._logger = logger

    async def save_transactions(
        self, transactions: list[TransactionBaseResponse]
    ) -> None:
        self._logger.info(
            f"Saving transactions {len(transactions)} to the database."
        )
        await self._transaction_repository.create_transactions(
            transactions=transactions
        )
