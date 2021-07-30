import dotenv
from github import Github

licence_version = "1.0.0"
config = dotenv.dotenv_values(".env")
g_account = Github(config["GTOKEN"]).get_user("NutDevs-org")


def parse_licence(file: str):
    with open(file, "r", encoding="UTF-8") as f:
        return f.read()


def update_repo_licence(repo, licence):
    try:
        g_licence = repo.get_contents("LICENSE")
    except Exception:
        commit = repo.create_file(
            "LICENSE",
            "Adding LICENSE",
            licence,
            branch=repo.default_branch,
        )

    else:
        commit = repo.update_file(
            "LICENSE",
            "Updated LICENSE",
            licence,
            g_licence.sha,
            branch=repo.default_branch,
        )


def update_licence_repos(repo):
    for repo in g_account.get_repos():
        licence = parse_licence("LICENSE") \
            .replace("#PROJECT_NAME#", repo.name) \
            .replace("#LICENSE_VER_NUMBER#", licence_version)

        update_repo_licence(repo, licence)


def main():
    update_licence_repos(g_account)


if __name__ == '__main__':
    main()
