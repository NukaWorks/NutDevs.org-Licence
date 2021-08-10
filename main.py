"""A small python script to automatically update License files."""
import hashlib
import os
from typing import Optional

import dotenv
from github import Github
from github.AuthenticatedUser import AuthenticatedUser
from github.ContentFile import ContentFile
from github.GithubException import UnknownObjectException

ACCOUNT_NAME: str = "NutDevs-org"


def parse_licence(file: str, repo_name: str) -> str:
    """Load the license template and format it dynamically."""
    with open(file, "r", encoding="UTF-8") as f:
        content = f.read()

    return content.format(
        project_name=repo_name,
        license_version="1.0.0"
    )


def update_repo_licence(repo, licence) -> None:
    """Create/update license for a repository and commit the changes."""
    try:
        g_licence: ContentFile = repo.get_contents("LICENSE")

    except UnknownObjectException:
        if g_licence.sha == hashlib.sha1(parse_licence("LICENSE_TEMPLATE", repo.name)):
            repo.create_file(
                "LICENSE",
                "Adding LICENSE",
                licence,
                branch=repo.default_branch,
            )

    else:
        if g_licence.sha == hashlib.sha1(parse_licence("LICENSE_TEMPLATE", repo.name)):
            repo.update_file(
                "LICENSE",
                "Updated LICENSE",
                licence,
                g_licence.sha,
                branch=repo.default_branch,
            )


def update_licence_repos(account: AuthenticatedUser) -> None:
    """Update every license of the user repositories."""
    for repo in account.get_repos():
        if not repo.archived:
            licence_template = parse_licence("LICENSE_TEMPLATE", repo.name)
            update_repo_licence(repo, licence_template)


def main() -> None:
    """Main entry point of the license updater."""
    token: Optional[str] = (
            os.environ.get("G_TOKEN")
            or dotenv.dotenv_values('.env').get('G_TOKEN')
    )

    if token is None:
        print("No Token were provided.")
        return

    g_account: AuthenticatedUser = Github(token).get_user(ACCOUNT_NAME)
    update_licence_repos(g_account)


if __name__ == '__main__':
    main()
