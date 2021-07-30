import os

from github import Github

licence_version = "1.0.0"
g_account = Github(os.environ["GTOKEN"]).get_user("NutDevs-org")


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
        licence_template = parse_licence("LICENSE_TEMPLATE") \
            .replace("#PROJECT_NAME#", repo.full_name) \
            .replace("#LICENSE_VER_NUMBER#", licence_version)

        update_repo_licence(repo, licence_template)


def main():
    update_licence_repos(g_account)


if __name__ == '__main__':
    main()
