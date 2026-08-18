import requests
from github_service import fetch_orgs


def display_orgs(username: str) -> None:
    try:
        orgs = fetch_orgs(username)
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

    if not orgs:
        print("No organizations found.")
        return

    print("User's Organizations")
    for org in orgs:
        login = org.get("login") or org.get("name") or "Unknown organization"
        print(f"- {login}")


def main() -> None:
    username = input("GitHub Username: ").strip()
    if not username:
        print("Please enter a GitHub username.")
        return
    display_orgs(username)


if __name__ == "__main__":
    main()
