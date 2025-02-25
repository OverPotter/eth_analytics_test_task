import httpx
from src._settings import Settings
from src.schemas.response.transactions.base import TransactionBaseResponse
from src.services.get_block_transactions_service.abc_service import (
    AbstractGetBlockTransactionsService,
)


class HTTPGetBlockTransactionsService(AbstractGetBlockTransactionsService):
    def __init__(self, settings: Settings):
        self._settings = settings

    async def get_block_transactions(
        self, block_number: int
    ) -> list[TransactionBaseResponse]:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={hex(block_number)}&boolean=true&apikey={self._settings.ETH_APT_TOKEN}"
            )
            raw_transactions = (
                response.json().get("result", {}).get("transactions", [])
            )

            return [
                TransactionBaseResponse(
                    block_number=block_number,
                    tx_from=tx["from"],
                    tx_to=tx["to"],
                    value=int(tx["value"], 16),
                )
                for tx in raw_transactions
            ]
