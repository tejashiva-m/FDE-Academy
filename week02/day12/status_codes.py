import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/999999"
)

print(response.status_code)

