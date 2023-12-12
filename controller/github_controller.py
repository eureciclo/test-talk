from fastapi import APIRouter, Body, Path

from model import GithubRepo
from service import github_service

router = APIRouter(
    prefix="/github",
    responses={404: {"description": "Not found"}},
)


@router.get("/repos")
async def users():
    repos = await GithubRepo.find_all()
    return repos


@router.post("/repos")
async def create(
    body: dict = Body(
        default=...,
        title="Github user",
        description="",
        examples=[
            {
                "owner": "leonardoobaptistaa",
                "name": "new-repo",
                "likes": 0,
            }
        ],
    )
):
    body["id"] = None
    model = GithubRepo(**body)
    await model.save()
    return model


@router.get("/{user}")
async def user(
    user: str = Path(
        default=...,
        title="Github user",
        examples=["leonardoobaptistaa"],
    ),
):
    repos = await github_service.repositories_for(user)
    return repos


@router.get("/{user}/statistics")
async def statistics(
    user: str = Path(
        default=...,
        title="Github user",
        examples=["leonardoobaptistaa"],
    ),
):
    count_likes, avg_likes, count = await GithubRepo.statistics(user)
    return {"total_likes": count_likes, "avg_likes": avg_likes, "count": count}


@router.post("/{user}/import")
async def import_user(
    user: str = Path(
        default=...,
        title="Github user",
        examples=["leonardoobaptistaa"],
    ),
):
    repos = await github_service.repositories_for(user)
    for repo in repos:
        owner, name, likes = repo
        user_repo = GithubRepo(id=None, owner=owner, name=name, likes=likes)
        await user_repo.save()

    return {"message": f"Imported {len(repos)} repositories."}
