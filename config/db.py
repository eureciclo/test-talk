import os

import aiosqlite


def connection_string():
    env = os.getenv("ENV", "test")
    return f"test_talk_{env}.sqlite"


async def init_db():
    async with aiosqlite.connect(connection_string()) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS github(id INTEGER PRIMARY KEY,owner, name, likes)")
