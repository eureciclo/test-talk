from httpx import AsyncClient


def url_for(user: str | None) -> str | None:
    if not user:
        return None
    return f"https://api.github.com/users/{user}/repos"


async def repositories_for(user: str):
    url = url_for(user)
    async with AsyncClient() as client:
        response = await client.request(method="GET", url=str(url), json=None)

    json_response = response.json()
    return [
        (resp["owner"]["login"], resp.get("name"), resp.get("stargazers_count"))
        for resp in json_response
    ]
