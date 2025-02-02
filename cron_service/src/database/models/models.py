from sqlalchemy import BigInteger, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from src.database.models.base import BaseIDModel


class TransactionsModel(BaseIDModel):
    __tablename__ = "transactions"

    block_number: Mapped[int] = mapped_column(BigInteger, nullable=False)
    tx_from: Mapped[str] = mapped_column(nullable=False)
    tx_to: Mapped[str] = mapped_column(nullable=True)
    value: Mapped[float] = mapped_column(Numeric(precision=50), nullable=False)
