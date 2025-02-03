from abc import ABC, abstractmethod

from src.schemas.response.transactions.balance import BalanceChangeResponse


class AbstractGetAddressWithLargestChangeService(ABC):
    @abstractmethod
    async def get_address_with_largest_change(
        self,
    ) -> BalanceChangeResponse: ...
