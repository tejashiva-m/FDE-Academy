import requests

response = requests.get(
    "https://api.github.com"
)

print(response.headers)

print()

print(response.headers["Content-Type"])