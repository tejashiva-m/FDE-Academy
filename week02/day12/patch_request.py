import requests

payload = {
    "title": "Only Title Updated"
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=payload
)

print(response.status_code)
print(response.json())

