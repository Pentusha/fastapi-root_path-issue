from typing import AsyncIterator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from app.main import app as asgi_app


@pytest.fixture
def app() -> FastAPI:
    return asgi_app


@pytest.fixture
async def client(app: FastAPI) -> AsyncIterator[AsyncClient]:
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client
