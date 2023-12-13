from httpx import AsyncClient
from mock import patch

from controller.main_controller import app
from model import GithubRepo


@patch("model.GithubRepo.statistics", return_value=(10, 2.0, 5))
async def test_statistics(mock_statistics):
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/github/aaa/statistics")

    assert response.status_code == 200

    json_response = response.json()
    assert json_response["total_likes"] == 10
    assert json_response["avg_likes"] == 2.0
    assert json_response["count"] == 5

    mock_statistics.assert_awaited_with("aaa")


@patch("service.github_service.repositories_for")
async def test_import(mock_repositories):
    mock_repositories.return_value = [
        ("user", "repo-name01", 1),
        ("user", "repo-name02", 2),
        ("user", "repo-name03", 3),
        ("user", "repo-name04", 4),
    ]
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/github/user/import")

    assert response.status_code == 200

    json_response = response.json()
    assert json_response["message"] == "Imported 4 repositories."

    mock_repositories.assert_awaited_with("user")


@patch("service.github_service.repositories_for")
async def test_import_save_to_database(mock_repositories):
    mock_repositories.return_value = [
        ("user", "repo-name01", 1),
        ("user", "repo-name02", 2),
        ("user", "repo-name03", 3),
        ("user", "repo-name04", 4),
    ]
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        await client.post("/github/user/import")

    repos = await GithubRepo.find_all()
    assert len(repos) == 4
