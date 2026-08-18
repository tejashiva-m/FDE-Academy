import requests
from github_service import fetch_user
from utils import format_date


def display_user(username: str) -> None:
    try:
        data = fetch_user(username)
    except requests.HTTPError as exc:
        resp = getattr(exc, 'response', None)
        if resp is not None and resp.status_code == 404:
            print("GitHub user not found.")
        else:
            print(f"HTTP error: {exc}")
        return
    except requests.RequestException as exc:
        print(f"Network error: {exc}")
        return

    print(f"Name: {data.get('name') or 'No name provided'}")
    bio = data.get('bio') or 'Not provided'
    print(f"Bio: {bio}")
    print(f"Followers: {data.get('followers', 0)}")
    print(f"Following: {data.get('following', 0)}")
    print(f"Public Repositories: {data.get('public_repos', 0)}")
    print(f"Account Created: {format_date(data.get('created_at'))}")
    print(f"Profile URL: {data.get('html_url', 'Unknown')}")


def main() -> None:
    username = input("GitHub Username: ").strip()
    if not username:
        print("Please enter a GitHub username.")
        return
    display_user(username)


if __name__ == "__main__":
    main()
