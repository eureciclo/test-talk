from dataclasses import dataclass

import aiosqlite

from config.db import connection_string as conn


@dataclass
class GithubRepoModel:
    id: int | None
    owner: str
    name: str
    likes: int

    @classmethod
    def from_row(cls, row):
        return GithubRepoModel(id=row[0], owner=row[1], name=row[2], likes=row[3])

    async def save(self):
        async with aiosqlite.connect(conn()) as db:
            await db.execute(
                "INSERT INTO github values (NULL, ?, ?, ?)",
                (self.owner, self.name, self.likes),
            )
            await db.commit()

    @classmethod
    async def find_all(cls):
        async with aiosqlite.connect(conn()) as db:
            results = await db.execute("SELECT * FROM github")
            objs = [GithubRepoModel.from_row(result) async for result in results]

        return objs

    @classmethod
    async def statistics(cls, user: str):
        async with aiosqlite.connect(conn()) as db:
            results = await db.execute(
                "SELECT sum(likes), avg(likes), count(id) FROM github WHERE owner like ?",
                (user,),
            )
            return await results.fetchone()
