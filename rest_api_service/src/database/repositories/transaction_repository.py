from typing import Sequence

from sqlalchemy import select
from src.database.models.models import TransactionsModel
from src.database.repositories.absctract_repository import AbstractRepository


class TransactionRepository(AbstractRepository[TransactionsModel]):
    _model = TransactionsModel

    async def get_last_processed_block(self) -> int:
        query = select(TransactionsModel.block_number).order_by(
            TransactionsModel.block_number.desc()
        )
        result = await self._session.execute(query)
        return result.scalars().first()

    async def get_transactions_by_block(
        self, block_to_check: int
    ) -> Sequence[TransactionsModel]:
        query = select(TransactionsModel).filter(
            TransactionsModel.block_number > block_to_check
        )
        result = await self._session.execute(query)
        return result.scalars().all()
