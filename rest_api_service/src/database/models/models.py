from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from cron_service.src.database.models.base import BaseIDModel


class TransactionsModel(BaseIDModel):
    __tablename__ = "transactions"

    block_number: Mapped[BigInteger] = mapped_column(nullable=False)
    tx_from: Mapped[str] = mapped_column(nullable=False)
    tx_to: Mapped[str] = mapped_column(nullable=False)
    value: Mapped[BigInteger] = mapped_column(nullable=False)
