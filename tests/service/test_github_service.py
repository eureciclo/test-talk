from httpx import AsyncClient

from service import github_service
from tests.utils import load_file_as_json


async def test_url_for_none():
    user = None
    url = github_service.url_for(user=user)
    assert url == None


async def test_url_for():
    user = "leonardoobaptistaa"
    url = github_service.url_for(user=user)
    assert url == "https://api.github.com/users/leonardoobaptistaa/repos"


async def test_repositories_for(httpx_mock):
    response_expected = await load_file_as_json("github_success.json")
    httpx_mock.add_response(
        method="GET",
        url="https://api.github.com/users/leonardoobaptistaa/repos",
        json=response_expected,
    )
    user = "leonardoobaptistaa"
    repos_infos = await github_service.repositories_for(user=user)

    assert len(repos_infos) == 20
    assert repos_infos[0] == (
        "leonardoobaptistaa",
        "avaliacao-desenvolvedor-aiml",
        1,
    )
