from fastapi import APIRouter, Depends
from src.database.repositories.manager import (
    OrmRepositoryManager,
    orm_repository_manager_factory,
)
from src.schemas.response.transactions.balance import BalanceChangeResponse
from src.services.get_address_with_largest_change_service.abc_service import (
    AbstractGetAddressWithLargestChangeService,
)
from src.services.get_address_with_largest_change_service.facade import (
    FacadeGetAddressWithLargestChangeService,
)
from src.services.get_last_100_block_service.repository import (
    RepositoryGetLast100BlockService,
)
from src.services.get_transactions_by_block_service.repository import (
    RepositoryGetTransactionsByBlockService,
)
from src.services.logging_service.logging_factory import Logger, logger_factory

router = APIRouter(prefix="/transactions")


@router.get("/top-balance-change", response_model=BalanceChangeResponse)
async def get_top_balance_changes(
    repository_manager: OrmRepositoryManager = Depends(
        orm_repository_manager_factory
    ),
    logger: Logger = Depends(logger_factory),
):
    async with repository_manager:
        service: AbstractGetAddressWithLargestChangeService = (
            FacadeGetAddressWithLargestChangeService(
                get_last_100_blocks_service=RepositoryGetLast100BlockService(
                    transaction_repository=repository_manager.get_transaction_repository()
                ),
                get_transactions_by_block_service=RepositoryGetTransactionsByBlockService(
                    transaction_repository=repository_manager.get_transaction_repository()
                ),
                logger=logger,
            )
        )
        return await service.get_address_with_largest_change()
