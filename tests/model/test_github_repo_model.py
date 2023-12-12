from model import GithubRepo


async def test_save_find_all():
    repo = GithubRepo(id=None, owner="leonardoobaptistaa", name="repo1", likes=100)
    await repo.save()

    all_repos = await GithubRepo.find_all()

    assert 1 == len(all_repos)
    repo = all_repos[0]
    assert "leonardoobaptistaa" == repo.owner
    assert "repo1" == repo.name
    assert 100 == repo.likes
    assert repo.id is not None


async def test_statistics(make_github_repo):
    await make_github_repo(owner="aaa", likes=1)
    await make_github_repo(owner="aaa", likes=2)
    await make_github_repo(owner="aaa", likes=2)
    await make_github_repo(owner="aaa", likes=2)
    await make_github_repo(owner="aaa", likes=3)

    statistics = await GithubRepo.statistics("aaa")

    assert statistics == (10, 2.0, 5)
