import requests

payload = {
    "id": 1,
    "title": "Updated",
    "body": "Updated Body",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=payload
)

print(response.status_code)
print(response.json())

