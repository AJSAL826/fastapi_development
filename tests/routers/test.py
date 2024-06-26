from httpx import AsyncClient
import pytest


async def create_task(body: str, asnyc_client: AsyncClient) -> dict:
    response = await asnyc_client.post("/post", json={"body": body})
    return response


@pytest.fixture()
async def created_task(async_client: AsyncClient):
    return await create_task("message", async_client)


@pytest.fixture()
async def test_task(created_task):
    body = "/post"
    AsyncClient
