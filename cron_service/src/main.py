import asyncio

from src._settings import settings_factory
from src.database.repositories.manager import orm_repository_manager_factory
from src.services.get_block_transactions_service.https import (
    HTTPGetBlockTransactionsService,
)
from src.services.get_last_processed_block_service.repository import (
    RepositoryGetLastProcessedBlockService,
)
from src.services.get_latest_block_service.https import (
    HTTPGetLatestBlockService,
)
from src.services.logging_service.logging_factory import logger_factory
from src.services.process_new_blocks_service.abc_service import (
    AbstractProcessNewBlocksService,
)
from src.services.process_new_blocks_service.facade import (
    FacadeProcessNewBlocksService,
)
from src.services.save_transactions_service.repository import (
    RepositorySaveTransactionsService,
)

settings = settings_factory()
logger = logger_factory()
repository_manager = orm_repository_manager_factory()


async def main():
    async with repository_manager:
        facade: AbstractProcessNewBlocksService = FacadeProcessNewBlocksService(
            logger=logger,
            get_block_transactions_service=HTTPGetBlockTransactionsService(
                settings=settings, logger=logger
            ),
            get_latest_block_service=HTTPGetLatestBlockService(
                settings=settings, logger=logger
            ),
            save_transactions_service=RepositorySaveTransactionsService(
                logger=logger,
                transaction_repository=repository_manager.get_transaction_repository(),
            ),
            get_last_processed_block_service=RepositoryGetLastProcessedBlockService(
                settings=settings,
                logger=logger,
                transaction_repository=repository_manager.get_transaction_repository(),
            ),
        )
        await facade.process_new_blocks()


if __name__ == "__main__":
    asyncio.run(main())
