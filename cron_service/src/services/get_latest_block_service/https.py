import httpx
from src._settings import Settings
from src.services.get_latest_block_service.abc_service import (
    AbstractGetLatestBlockService,
)


class HTTPGetLatestBlockService(AbstractGetLatestBlockService):
    def __init__(self, settings: Settings):
        self._settings = settings

    async def get_latest_block(self) -> int:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey={self._settings.ETH_APT_TOKEN}"
            )
            latest_block_number = int(response.json().get("result", "0"), 16)

            return latest_block_number
