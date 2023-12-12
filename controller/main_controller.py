from contextlib import asynccontextmanager

from fastapi import FastAPI

from config.db import init_db
from controller import github_controller


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="Talk Tests API",
    lifespan=lifespan,
)

app.include_router(github_controller.router)


@app.router.get("/health")
async def health():
    return {"message": "ok"}
