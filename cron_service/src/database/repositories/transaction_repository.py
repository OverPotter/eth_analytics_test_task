from sqlalchemy import select
from src.database.models.models import TransactionsModel
from src.database.repositories.absctract_repository import AbstractRepository
from src.schemas.response.transactions.base import TransactionBaseResponse


class TransactionRepository(AbstractRepository[TransactionsModel]):
    _model = TransactionsModel

    async def create_transactions(
        self, transactions: list[TransactionBaseResponse]
    ) -> None:
        for tx in transactions:
            await self.create(**tx.dict())

    async def get_last_processed_block(self) -> int:
        query = select(TransactionsModel.block_number).order_by(
            TransactionsModel.block_number.desc()
        )
        result = await self._session.execute(query)
        return result.scalars().first()
