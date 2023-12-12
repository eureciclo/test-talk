import json

import aiofiles


async def load_file_as_json(filepath):
    fullpath = f"tests/resources/{filepath}"
    async with aiofiles.open(fullpath, "r") as f:
        json_string = await f.read()

    return json.loads(json_string)
