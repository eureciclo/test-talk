import aiosqlite
import pytest

from config.db import connection_string as conn
from model import GithubRepo


@pytest.fixture(autouse=True)
async def _clear_database():
    yield
    await clear_db()


async def clear_db():
    async with aiosqlite.connect(conn()) as db:
        # await db.execute("DELETE FROM github")
        # await db.commit()
        pass


@pytest.fixture
async def make_github_repo():
    async def _make_github_repo(**params):
        default_values = {
            "owner": "onwer_de_teste",
            "name": "repositorio de teste",
            "likes": 10,
        }
        params = default_values | params
        should_save = params.pop("should_save", True)
        github_repo = GithubRepo(**params)

        if should_save:
            await github_repo.save()
        return github_repo

    return _make_github_repo
