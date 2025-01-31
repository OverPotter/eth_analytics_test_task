from sqlalchemy.orm import Mapped

from src.database.models.base import BaseIDModel


class WalletQueryModel(BaseIDModel):
    __tablename__ = "wallet_queries"

    address: Mapped[str]
    balance: Mapped[str]
    bandwidth: Mapped[str]
    energy: Mapped[str]
