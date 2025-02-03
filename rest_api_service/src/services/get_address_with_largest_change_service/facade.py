from collections import defaultdict

from src.schemas.response.transactions.balance import BalanceChangeResponse
from src.schemas.response.transactions.base import TransactionBaseResponse
from src.services.get_address_with_largest_change_service.abc_service import (
    AbstractGetAddressWithLargestChangeService,
)
from src.services.get_last_100_block_service.abc_service import (
    AbstractGetLast100BlockService,
)
from src.services.get_transactions_by_block_service.abc_service import (
    AbstractGetTransactionsByBlockService,
)
from src.services.logging_service.logging_factory import Logger


class FacadeGetAddressWithLargestChangeService(
    AbstractGetAddressWithLargestChangeService
):
    def __init__(
        self,
        logger: Logger,
        get_last_100_blocks_service: AbstractGetLast100BlockService,
        get_transactions_by_block_service: AbstractGetTransactionsByBlockService,
    ):
        self._logger = logger
        self._get_last_100_blocks_service = get_last_100_blocks_service
        self._get_transactions_by_block_service = (
            get_transactions_by_block_service
        )

    async def get_address_with_largest_change(self) -> BalanceChangeResponse:
        blocks_to_check = (
            await self._get_last_100_blocks_service.get_last_100_block()
        )
        self._logger.debug(
            f"The first block has been received to check: № {blocks_to_check}."
        )

        transactions = await self._get_transactions_by_block_service.get_transactions_by_block(
            block_to_check=blocks_to_check
        )
        self._logger.debug(
            f"{len(transactions)} transactions have been received for further calculations."
        )

        balance_changes = self._calculate_balance_changes(
            transactions=transactions
        )
        self._logger.debug(
            "Calculations on changes in the balance in the blocks have been received."
        )

        address_with_largest_change = max(
            balance_changes, key=lambda addr: abs(balance_changes[addr])
        )
        balance_change_wei = balance_changes[address_with_largest_change]
        self._logger.info(
            f"The address with largest changes was received: {address_with_largest_change}."
        )

        return BalanceChangeResponse.from_wei(
            address=address_with_largest_change,
            balance_change=balance_change_wei,
        )

    @staticmethod
    def _calculate_balance_changes(
        transactions: list[TransactionBaseResponse],
    ) -> dict[str, float]:
        balance_changes: dict[str, float] = defaultdict(float)

        for tx in transactions:
            if tx.tx_from:
                balance_changes[tx.tx_from] -= float(tx.value)
            if tx.tx_to:
                balance_changes[tx.tx_to] += float(tx.value)

        return balance_changes
