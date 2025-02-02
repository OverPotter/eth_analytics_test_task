from src.services.get_block_transactions_service.abc_service import (
    AbstractGetBlockTransactionsService,
)
from src.services.get_last_processed_block_service.abc_service import (
    AbstractGetLastProcessedBlockService,
)
from src.services.get_latest_block_service.abc_service import (
    AbstractGetLatestBlockService,
)
from src.services.logging_service.logging_factory import Logger
from src.services.process_new_blocks_service.abc_service import (
    AbstractProcessNewBlocksService,
)
from src.services.save_transactions_service.abc_service import (
    AbstractSaveTransactionsService,
)


class FacadeProcessNewBlocksService(AbstractProcessNewBlocksService):
    def __init__(
        self,
        logger: Logger,
        get_block_transactions_service: AbstractGetBlockTransactionsService,
        get_latest_block_service: AbstractGetLatestBlockService,
        get_last_processed_block_service: AbstractGetLastProcessedBlockService,
        save_transactions_service: AbstractSaveTransactionsService,
    ):
        self._save_transactions_service = save_transactions_service
        self._get_last_processed_block_service = (
            get_last_processed_block_service
        )
        self._get_latest_block_service = get_latest_block_service
        self._get_block_transactions_service = get_block_transactions_service
        self._logger = logger

    async def process_new_blocks(self) -> None:
        latest_block = await self._get_latest_block_service.get_latest_block()
        start_block = max(
            19000000,
            await self._get_last_processed_block_service.get_last_processed_block(),
        )

        for block_number in range(start_block, latest_block + 1):
            transactions = await self._get_block_transactions_service.get_block_transactions(
                block_number
            )
            if transactions:
                await self._save_transactions_service.save_transactions(
                    transactions
                )
                self._logger.info(f"Processed block: {block_number}.")
