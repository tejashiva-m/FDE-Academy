import requests

payload = {
    "title": "My First API",
    "body": "Learning REST APIs",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload
)

print(response.status_code)
print(response.json())

