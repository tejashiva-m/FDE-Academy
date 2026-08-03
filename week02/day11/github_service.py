import requests

BASE = "https://api.github.com/users"


def fetch_user(username: str) -> dict:
    """Fetch a GitHub user. Raises requests exceptions on network/HTTP errors."""
    url = f"{BASE}/{username}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()


def fetch_orgs(username: str) -> list:
    """Fetch organizations for a GitHub user."""
    url = f"{BASE}/{username}/orgs"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()
