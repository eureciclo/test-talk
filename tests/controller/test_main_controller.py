from httpx import AsyncClient

from controller.main_controller import app


async def test_health():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/health")

    json_response = response.json()
    assert json_response == {"message": "ok"}
