from typing import Optional

from ...helpers.http_helpers import HttpClient
from .... import settings

from ...helpers.loggers import get_logger

logger = get_logger()

class CoreService:
    CAREER_JET_API_URL = settings.CAREER_JET_API_URL

    def __init__(self):
        self.http_client = HttpClient(base_url=self.CAREER_JET_API_URL)

    async def fetch_jobs(
        self, endpoint: str, params: dict = None, base_url: Optional[str] = None,
        extra_headers: Optional[dict] = None
    ) -> dict:
        """Fetches data from an external service using the HttpClient."""
        if base_url:
            self.http_client.base_url = base_url
        params = params or {}
        params.update({"location": params.get("location", "United States")})
        response = await self.http_client.get(
            endpoint=endpoint, params=params, extra_headers=extra_headers
        )
        logger.debug(
            "response from job platform:::::: "
            f"{response}"
        )
        # TODO: save jobs in db; analyze with llm, then perform other necessary actions.
        return response.get("jobs", [])
