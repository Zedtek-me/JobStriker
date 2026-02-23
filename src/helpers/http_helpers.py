import requests

from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

from typing import Optional, Union

from .loggers import get_logger

logger = get_logger()

class ResponseHandler:

    @classmethod
    def handle_response(
        cls, data: Optional[Union[dict, list]] = None,
        error: Optional[str] = None, status_code: int = status.HTTP_200_OK
    ) -> dict:
        if error:
            raise HTTPException(status_code=status_code, detail=error)
        return JSONResponse(content=data, status_code=status_code)




class HttpClient:
    # client for external service requests
    async def __init__(self, base_url: str, headers: Optional[dict] = None):
        self.base_url = base_url
        self.headers = headers or {}

    async def get(
        self, endpoint: str, params: Optional[dict] = None,
        extra_headers: Optional[dict] = None
    ) -> dict:
        """fetches data from external service with url {self.base_url}"""
        url = f"{self.base_url}{'/' if '/' not in endpoint else ''}{endpoint}"
        if extra_headers:
            self.headers = {**self.headers, **extra_headers}
        response = requests.request(
            "GET", url, headers=self.headers, params=params,
            timeout=10
        )
        if response.status_code != 200:
            logger.exception(f"GET request to {url} failed with status {response.status_code}: {response.text}")
            raise HTTPException(
                status_code=response.status_code,
                detail=f"GET request failed: {response.text}"
            )
        return response.json()


    async def post(
        self, payload: dict, endpoint: str, extra_headers: Optional[dict] = None
    ) -> Optional[dict]:
        """posts data to external service with url {self.base_url}"""
        url = f"{self.base_url}{'/' if '/' not in endpoint else ''}{endpoint}"
        self.headers = {**self.headers, **extra_headers} if extra_headers else self.headers
        response = requests.request(
            "POST", url, headers=self.headers, json=payload, timeout=10
        )
        if response.status != 200:
            logger.exception(f"POST request to {url} failed with status {response.status_code}: {response.text}")
            raise HTTPException(
                status_code=response.status_code,
                detail=f"POST request failed: {response.text}"
            )
        return response.json() if response.content else None
